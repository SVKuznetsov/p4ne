- hosts: fs-ga
  tasks:
    - name: show the root directory
      command: ls -l /
      register: dir1

    - name: test
      set_fact:
        packets: "{{ interfaces['stdout'] | regex_findall('RX packets:([0-9]+)') }}"

    - name: show results
      debug:
        msg: "{{ packets }}"