## LightLogo: A lightweight Logo-based agent-based simulation toolkit

LightLogo (LLogo) aims to provide a simple, lightweight, and powerful 3D agent-based simulation toolkit for educational and scientific research.

### Installation

```
    pip install LightLogo
```

### Features

- Redesigned turtle and more agent types that support 3D contexts;
  
- Easy integration with Python and its massive Python libraries to enhance experience;
  
- Following the basic principles of Logo language but with significant improvement. 

### Usage

Example 1: Playground

```python
from lightlogo.play3D import *

clearscreen()
reset()
setxyz(5,-5,0)
pendown()
repeat(8,[
    left(45),
    fd(5)
])
penup()
repeat_play()

```

Example 2: Full-scale agent-based simulation

```python
from lightlogo.world3D import *

if __name__=="__main__":
    # Step 1: Create a 3D world in LightLogo
    w3d=world3D(x_range=[-10,10],y_range=[-10,10],z_range=[-10,10],title="Demo 2",)
    w3d.create(style="seaborn-ticks")
    # Step 2: Define an initialization function
    def setup(world):
        # create turtles
        N=1
        list_turtles=[
            turtle3D(xyz=[0,0,0],color='red',shape='.',size=10) for _ in range(N)
        ]
        list_turtles[0].left(45)
        world.turtles(list_turtles)
    # Step 3: Define a step function for each frame to update
    def go(frame,world):
        list_turtles=world.turtles()
        print(f"Step {frame}\tTurtles Count: {len(list_turtles)}")
        # turtle 1
        turtle1=list_turtles[0]
        if frame==0:
            turtle1.pendown()

        turtle1.forward(3)
        # turtle1.setxrotate(45)
        # turtle1.right(60)
        # turtle1.up(45)
        # turtle1.rollback(30)
        # turtle1.setxrotate(45)
        # turtle1.setxrotate(90)

        if frame!=0 and frame % 1 == 0 and frame < 40:
            turtle1.left(30)
            t1=text3D(xyz=turtle1.pos(),color='green',text=f"p{frame}")
            world.texts().append(t1)

        if frame >=40:
            turtle1.penup()

        if frame>=10:
            turtle1.hide()

        if frame>=20:
            turtle1.show()

        list_turtles[0]=turtle1

        world.turtles(list_turtles)
        
    # Step 4 (final step): Run the simulation
    w3d.run(go=go,setup=setup,interval=500,frames=1000,repeat=True)
```

### Simulation screenshot

![](https://dhchenx.github.io/projects/LightLogo/images/screenshot1.png)

### License

The `LightLogo` project uses [BSD 3-Clause License](https://github.com/dhchenx/LightLogo/blob/main/LICENSE). 

