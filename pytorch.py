import torch

def create_tensor():
    x1 = torch.empty(1,)
    print("Tensor:", x1)
    x2 = torch.empty(3)
    print("Tensor:", x2)
    x3 = torch.empty(2, 3)
    print("Tensor:", x3)
    x4 = torch.empty(2, 3, 4)
    print("Tensor:", x4)



def random_tensors():
    x1 = torch.rand((2,), requires_grad=True)
    # torch.rand generates random number between [0,1] uniformly.
    print("Random Tensor:", x1)
    x2 = torch.randn((2,2))
    print("Random Normal Tensor:", x2)
    print(x2.mean(), x2.std())
    # torch.randn generates radom number froma given normal distribution witha given mean and standard deviation value.
    x3 = torch.randint(0, 10, (2,2))
    print("Random Integer Tensor:", x3)
    # torch.randint() generates random integers betwen a given boundarys.


def autograd_example():
    x = torch.tensor([2.0, 3.0], requires_grad=True)
    y = x**2 + 3*x + 5
    print("y:", y)
    z = y.sum()
    print("z:", z)
    z.backward()
    print("Gradient of x:", x.grad)

autograd_example()