# iwrr/load_balancer.py

from metrics_tracker import MetricsTracker

class LoadBalancer:
    def __init__(self, vms):
        self.vms = vms

    def get_LIF_metrics(self):
        L = sum(vm.current_load() for vm in self.vms)
        C = sum(vm.capacity for vm in self.vms)
        LPC = L / C if C != 0 else 0

        lif = {}
        for vm in self.vms:
            Ti = LPC * vm.capacity
            li = vm.current_load()
            if li < Ti:
                status = "underloaded"
            elif li > Ti:
                status = "overloaded"
            else:
                status = "balanced"
            lif[vm.id] = {
                "load": li,
                "Ti": Ti,
                "status": status,
                "capacity": vm.capacity
            }
        return lif

    def get_sorted_vms_by_queue(self):
        return sorted(self.vms, key=lambda vm: len(vm.waiting_list))

    def migrate_tasks(self):
        print("\n[Load Balancer] Starting migration loop...")
        lif = self.get_LIF_metrics()
        loop_counter = 0
        MAX_LOOPS = 1000

        while loop_counter < MAX_LOOPS:
            loop_counter += 1
            print(f"\n[Loop {loop_counter}] Sorting VMs by waiting queue size")
            sorted_vms = self.get_sorted_vms_by_queue()
            min_vm = sorted_vms[0]
            max_vm = sorted_vms[-1]

            print(f"Min Queue VM-{min_vm.id} has {len(min_vm.waiting_list)} tasks")
            print(f"Max Queue VM-{max_vm.id} has {len(max_vm.waiting_list)} tasks")

            if len(min_vm.waiting_list) >= 1:
                print("[Termination] First queue has ≥ 1 task → terminating LB loop.")
                break

            if len(max_vm.waiting_list) <= 1:
                print("[Termination] Last queue has ≤ 1 task → terminating LB loop.")
                break

            pending_vms = sorted(self.vms, key=lambda vm: vm.total_execution_time())
            print("[Step 11] VMs sorted by total pending execution time.")

            migration_done = False

            for vm in pending_vms[::-1]:
                if lif[vm.id]["status"] == "overloaded":
                    for i, task in enumerate(vm.waiting_list):
                        if not hasattr(task, 'was_migrated'):
                            task.was_migrated = False
                        if not task.was_migrated:
                            task = vm.waiting_list.pop(i)
                            task.was_migrated = True
                            print(f"[Step 12] Migrating Task-{task.id} from VM-{vm.id}")

                            for uvm in pending_vms:
                                if lif[uvm.id]["status"] == "underloaded":
                                    uvm.waiting_list.append(task)
                                    print(f" → Assigned to underloaded VM-{uvm.id}")
                                    migration_done = True

                                    # Log migration
                                    if hasattr(task, 'tracker'):
                                        task.tracker.log_task_migration()
                                    break
                            break
                if migration_done:
                    break

            if not migration_done:
                print("[Termination] No migration done this round. Exiting.")
                break

            lif = self.get_LIF_metrics()

    def schedule_task(self, task):
        # Static scheduling: assign based on load/capacity (weighted)
        target_vm = min(self.vms, key=lambda vm: vm.current_load() / vm.capacity)
        target_vm.waiting_list.append(task)
        return target_vm.id
