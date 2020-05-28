import numpy as np

import matplotlib.cm as cm

import matplotlib.pyplot as plt



__author__ = 'James Pang'

__name__ = '__main__'



class Simulation(object):

    rmax = 1

    lmax = 220.

    rs = rmax + 3.

    rd = rmax + 5.

    rkill = 100.*rmax

    xf = np.zeros([lmax, lmax])

    N = 3000.

    rx = 0.

    ry = 0.



    def jump(self):

    # add a docstring to this function

        '''It moves the particle to randomly adjacent site.'''

    

        choice = np.random.randint(0,4)

        if choice == 0:

            self.rx += 1

        elif choice == 1:

            self.rx += -1

        elif choice == 2:

            self.ry += 1

        elif choice == 3:

            self.ry += -1



    def aggregate(self):

        # add a docstring to this function

        '''The particle is added when it reaches a site adjacent to the aggregate. 

        If necessary, rmax is increased.'''

        

        self.xf[self.rx + self.lmax/2][self.ry + self.lmax/2] = 1

        self.rmax = max(self.rmax, np.sqrt((self.rx)**2 + (self.ry)**2))



    def occupy(self):

        # add a docstring to this function

        '''Start site of the particle is selected.'''

        

        phi = np.random.rand()*2*np.pi

        self.rx = self.rs*np.sin(phi)

        self.ry = self.rs*np.cos(phi)



    def circlejump(self):

        # add a docstring to this function

        '''A circle jump happens when the vector of length r-rs is added to the

        position of the particle.'''

        

        phi = np.random.rand()*2*np.pi

        r = np.sqrt(self.rx**2 + self.ry**2)

        self.rx += (r-self.rs)*np.sin(phi)

        self.ry += (r-self.rs)*np.cos(phi)



    def check(self):

        # add a docstring to this function

        '''Checks the status of the particle whether it 

        (1) is annihilated

        (2) has reached a site adjacent to the aggregate

        (3) do a short jump  if necessary

        (4) do a long circle jump if necessary.'''



        r = np.sqrt(self.rx**2 + self.ry**2)      

        if r > self.rkill:

            return 'k'

        elif r >= self.rd:

            return 'c'

        elif self.xf[self.rx + 1 + self.lmax/2][self.ry + self.lmax/2] + \
             self.xf[self.rx - 1 + self.lmax/2][self.ry + self.lmax/2] + \
             self.xf[self.rx + self.lmax/2][self.ry + 1 + self.lmax/2] + \
             self.xf[self.rx + self.lmax/2][self.ry - 1 + self.lmax/2] > 0.:

            return 'a'

        else:

            return 'j'



    def update(self):

        self.occupy()

        self.jump()



        while True:

            status = self.check()

            if status == 'k':

                self.occupy()

                self.jump()



            elif status == 'a':

                self.aggregate()



                # what will happen if the next three lines are removed

                # try it, explain why such pattern is produced

                '''If the next three lines will be remove, rs, rd, and rkill will 

                not change and the pattern will be enclose in a small circle 

                at the origin. Such pattern is produced since

                the particles cannot start and aggregate anywhere.'''

                

                self.rs = self.rmax + 3.

                self.rd = self.rmax + 5.

                self.rkill = 100.*self.rmax

                break



            elif status == 'j':

                self.jump()



            elif status == 'c':

                self.circlejump()



    def run(self):

    # what is the significance of the ff. line?

        '''An initial particle is added to the origin.'''

        

        self.xf[self.lmax/2][self.lmax/2] = 1



        for i in range(1, self.N):

            self.update()



if __name__ == '__main__':

    sim = Simulation()



    sim.N = 3000

    sim.run()

    # what happens when cmap=cm.gray

    '''When cmap=cm.gray,  the background is black while the aggregate is white.'''

    

    plt.imshow(sim.xf, cmap=cm.gray_r)

#    plt.axis('off')

    plt.show()

    plt.close()

    print('The fractal dimension is ', np.log(sim.N)/np.log(sim.rmax))



# Try changing the value of N and see the resulting patterns

"""When N is smaller, the pattern is smaller and runs shorter."""

# Note that the simulation speed is greatly affected by number of particles N

# Improve the code by adding a fractal dimension measurement



# OPTIONAL EXERCISE: Show as animation each time a particle joins the aggregate

# (Show updating of plt.matshow)