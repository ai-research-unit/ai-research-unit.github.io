# __The ADHM Construction and Instanton Moduli in Biquaternionic Form__

## Introduction

A topological sector is not one configuration but a family. The self-dual connections of charge $k$ form a manifold, the moduli space, and its dimension, its metric and its singularities are what the semiclassical expansion needs. The ADHM construction builds every such connection from a finite algebraic datum: two matrices and two vectors satisfying a pair of quadratic equations.

The construction in general form, with no sector attached. It states the self-duality equation as a quaternionic condition, the ADHM equations, the dimension of the moduli space, the reduction to the BPST solution at charge one, and the twistor reading. The construction is a statement about $SU(N)$ gauge theory in four Euclidean dimensions; it names no force.



- The strong sector. The application is [The ADHM Construction and Biquaternion Instanton Data](the-adhm-construction-and-biquaternion-instanton-data.html), which carries the construction in the framework's notation, fixes the minimal datum for the framework's compact factor and relates the quaternionic structure to the algebra's own.
- The electroweak sector, nowhere.

The moduli space is infinite-dimensional as a space of connections and finite-dimensional as a manifold. The ADHM datum is the finite description, and without it the measure on the moduli space could not be written.

## Self-Duality as a Quaternionic Equation

The identification. On $\mathbb{R}^4$ the coordinates combine into a quaternion, $x=x_0e_t+x_1\vec e_x+x_2\vec e_y+x_3\vec e_z$, and the field strength splits into a self-dual and an anti-self-dual part. Self-duality is the statement that one part vanishes.

The quaternionic form. A connection whose curvature is self-dual is equivalent to a connection whose curvature is a quaternionic-linear object: the three components of the anti-self-dual part vanish, and what remains is a triple of two-forms obeying the quaternionic relations. This is why the construction is algebraic rather than analytic — the differential equation becomes a linear condition on a finite set of matrices.

## The ADHM Equations

The datum. For gauge group $SU(N)$ and charge $k$:

$$
B_1,\ B_2 \in \mathrm{Hom}(\mathbb{C}^k,\mathbb{C}^k),
\qquad
I\in\mathrm{Hom}(\mathbb{C}^N,\mathbb{C}^k),
\qquad
J\in\mathrm{Hom}(\mathbb{C}^k,\mathbb{C}^N).
$$

The equations. Two conditions, one complex and one real:

$$
\boxed{\;\mu_{\mathbb C}=[B_1,B_2]+IJ=0\;}
$$

$$
\boxed{\;\mu_{\mathbb R}=[B_1,B_1^{\dagger}]+[B_2,B_2^{\dagger}]+II^{\dagger}-J^{\dagger}J=0\;}
$$

The first is holomorphic and the second is the moment map for the unitary action; together they are the self-duality equation in disguise.

**The gauge redundancy.** The datum carries a $\mathrm{U}(k)$ action, $B_i\mapsto gB_ig^{-1}$, $I\mapsto gI$, $J\mapsto Jg^{-1}$, which does not change the connection. The moduli space is the quotient of the solution set by that action, and taking the quotient is what makes it a manifold rather than a cone.

## The Dimension of the Moduli Space

The count. The datum has $4k^2+4kN$ real parameters; the two equations remove $3k^2$; the quotient removes $k^2$. The remainder is

$$
\boxed{\;\dim\mathcal{M}_{N,k}=4kN\;}
$$

the standard dimension of the charge-$k$ moduli space of $SU(N)$.

**The reading.** Every instanton carries four translational, four scale and three orientation parameters for each unit of charge, plus the parameters that come from the gauge orientation of the instanton in the group. The formula reproduces that count and fixes the measure.

The metric. The moduli space carries the metric induced by the field-space metric on the space of connections; the ADHM coordinates make it computable, and the hyper-Kähler structure of the manifold is visible in the quaternionic form of the equations.

## The Minimal Datum and the Charge-One Solution

**The reduction.** At $k=1$ the matrices $B_i$ are numbers and the equations reduce to algebraic relations among them. Solving them and inserting the datum into the reconstruction formula gives the BPST solution with its scale, its position and its gauge orientation.

The reconstruction. The connection is built from the null space of a linear operator constructed from the datum; the self-duality of the resulting connection is a consequence of the two equations, not an extra condition. This is the sense in which the construction is complete: every self-dual connection arises, and every datum gives one.

The twistor reading. The same equations are the statement that a certain holomorphic bundle over twistor space is trivial on each twistor line. The quaternionic and twistor pictures agree, and the agreement is what makes the moduli space hyper-Kähler.

## What the Framework Supplies

- **Supplied.** The quaternionic structure itself. The algebra is a quaternion algebra over $\mathbb{C}$, so the identification of $\mathbb{R}^4$ with the quaternions and the split of the field strength into self-dual parts are carried by the algebra and not imported.
- **Imported.** The moduli-space dimension, the quotient and the reconstruction formula. These are standard mathematics, transcribed.
- **Not supplied.** The gauge group of the sector. The construction is written for $SU(N)$; which $N$ applies is a sector question, and in this framework the compact factor fixes $N=2$.

Where the application is. [The ADHM Construction and Biquaternion Instanton Data](the-adhm-construction-and-biquaternion-instanton-data.html) works the construction for the framework's compact factor, states the dimension it gives, and relates the quaternionic structure of the datum to the algebra's own left multiplication.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $k$ | the instanton charge |
| $N$ | the rank of the gauge group |
| $B_1,B_2$ | the complex matrices of the datum |
| $I,J$ | the vectors of the datum |
| $\mu_{\mathbb C},\mu_{\mathbb R}$ | the complex and real equations |
| $\mathcal{M}_{N,k}$ | the moduli space |

## Further Reading

- M. F. Atiyah, N. J. Hitchin, V. G. Drinfeld and Yu. I. Manin, "Construction of Instantons," *Physics Letters A* **65** (1978) 185–187, the construction.
- M. F. Atiyah, *Geometry of Yang–Mills Fields*, the twistor reading.
- N. Dorey, T. J. Hollowood, V. V. Khoze and M. P. Mattis, "The Calculus of Many Instantons," *Physics Reports* **371** (2002) 231–459, the moduli-space measure.
