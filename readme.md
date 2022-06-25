## put this in etc/datadog-agent/checks.d
enable logs and apm in the agent
in the etc/conf.d create a ddog_metric.d with a ddog_metric.yaml file inside
in the etc/conf.d create a python.d with a conf.yml file inside
make sure the log path in the python script and in the python.d/conf.yml file is the same
might have to sudo chmod 755 /etc/datadog-agent/checks.d to ensure the directory can be read for logs if the permissions doesnt work use a another directory from / like /tmp