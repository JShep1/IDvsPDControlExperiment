# IDvsPDControlExperiment
Data needed to replicate Inverse Dynamics controller vs. PD controller in simulation<br /><br />
The gains for the PID controller at timestep 0.001 are in the file gains.dat<br /><br />
The controller gains for the ID controller at its three timesteps are in IDgains.dat<br /><br />
Currently, the function for the ID controller is commented out in sinusoidal-controller.cpp, to run the ID controller, comment the current PID controller function and uncomment the ID controller function<br /><br />
The data for the plots at each time step is in the ControllerData folder<br /><br />
**NOTE** the dependencies on Positronics Lab code Moby and Ravelin found on Github<br /><br />
