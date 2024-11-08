# nodejsapp

This role deploy a NodeJS application on a server. For now, it's aimed to be used on **Debian** based server. This role:

- Install NodeJS
- Deploy the application
- Create a systemd service to manage the app

## Info

This role offers 3 types of deployment:

- **deploy from git** (default behavior): Clone a public git repository.
- **deploy from local clone**: Locally clone the repo before deploy it (useful with private git server context).
- **deploy from ci**: When the role is called from a GitLab CI context.

## Role variables

| Name                                        | Description                                                                                                     | Type   | Required | Default value                                                                  |
|---------------------------------------------|-----------------------------------------------------------------------------------------------------------------|--------|----------|--------------------------------------------------------------------------------|
| nodejsapp_install_nodejs                    | Install NodeJS on server                                                                                        | bool   | false    | true                                                                           |
| nodejsapp_nodejs_install_from_distro_repo   | Install NodeJS from distribution packages (install latest). From node repository when 'false'                   | bool   | false    | true                                                                           |
| nodejsapp_nodejs_source_version             | NodeJS version package apt name to install (from Node repository)                                               | string | false    | 20.5.1-deb-1nodesource1                                                        |
| nodejsapp_nodejs_source_version_main        | NodeJS main version to install (must be same main version than nodejsapp_nodejs_source_version)                 | string | false    | "{{ nodejsapp_nodejs_version[:2] }}"                                           |
| nodejsapp_name                              | Give a name to the application to deploy                                                                        | string | true     |                                                                                |
| nodejsapp_repository_dest                   | Sources directory where the app is deployed on server                                                           | string | false    | "{{ nodejsapp_repository_dest }}"                                              |
| nodejsapp_packages_file_directory           | Directory containing the `package.json` node dependencies list to install                                       | string | false    | "{{ nodejsapp_repository_dest }}"                                              |
| nodejsapp_clone_locally                     | Clone the app locally before deploying on server (usefull for private git servers for instance)                 | bool   | false    | false                                                                          |
| nodejsapp_deploy_from_ci                    | Declare if the role is used in `GitLab CI` deployment context. Can not be `true` with `nodejsapp_clone_locally` | bool   | false    | false                                                                          |
| nodejsapp_repository_url                    | Repository URL of the NodeJS application to deploy                                                              | string | true     |                                                                                |
| nodejsapp_version                           | Select branch or tag from the git repository NodeJS app to deploy                                               | string | false    | master                                                                         |
| nodejsapp_src_path                          | Path to clone locally the repository before deploy. Only used when `nodejsapp_clone_locally` is true            | string | false    | "/tmp/{{ nodejsapp_name }}"                                                    |
| nodejsapp_service_command                   | Command executed by systemd service to start the NodeJS app                                                     | string | false    | "/usr/bin/node {{ nodejsapp_repository_dest }}/{{ nodejsapp_main_file_name }}" |
| nodejsapp_service_file_path                 | Path to the Ansible template deployed for the systemd service file                                              | string | false    | nodejsapp.service.j2                                                           |


## Example Playbook

```yml
- hosts: myserver.example.com
  become: yes
  roles:
    - role: nodejsapp
      nodejsapp_install_nodejs: true
      nodejsapp_node_version: 16.18.1-deb-1nodesource1
      nodejsapp_name: mynodejsapp
      nodejsapp_clone_locally: false
      nodejsapp_repository_url: https://github.com/johnpapa/node-hello.git
      nodejsapp_repository_dest: /opt/mynodejsapp
      nodejsapp_main_file_name: index.js
      nodejsapp_env_vars:
        - name: PORT
          value: 8000
```
