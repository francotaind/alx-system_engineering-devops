#1-install_flask.pp

#Ensure python3-pip is installed
package { 'python3-pip':
	ensure => installed,
}

#Install Flask using pip3
exec {'install_flask':
	command => '/usr/bin/pip3 install flask==2.1.0'
	unless => '/usr/bin/pip3 show flask | grep -q "Version: 2.1.0"',
}
# Notify for successful installation
notify {'Flask installed successfully':
	subscribe => Exec['install_flask'],
}
