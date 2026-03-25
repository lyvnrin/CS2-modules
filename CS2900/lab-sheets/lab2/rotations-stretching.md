## Rotations & Stretching

A rotation in 2 dimensions over an angle $\theta$ is:
* $ \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end {pmatrix} $

**Extended to 3 dimensions**:
You want to do a rotation in 3 dimensional spaces, but only want a rotation in the x-y plane.

This means you want to rotate the $x$ and $y$ coords, but leave $z$ alone. You extend the above rotation without changing the $z$ coord. This is achieve with:
* $ \begin{pmatrix} \cos\theta & \sin\theta & 0 \\ -\sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{pmatrix}$