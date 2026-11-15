# __Simple and Non-Simple Rotations: One Angle at $n\le3$, $\lfloor n/2\rfloor$ Planes at $n\ge4$__

## Introduction

**A rotation is simple when it turns a single plane and fixes everything orthogonal to it, and the number of independent planes grows with the dimension: one at $n=2$ and $n=3$, and up to $\lfloor n/2\rfloor$ from $n=4$ on.**

The article defines simple rotations by their fixed subspace, proves that every rotation is simple at $n=2$ and $n=3$, gives the block form with $s=\lfloor n/2\rfloor$ angles, exhibits the first non-simple rotation at $n=4$, shows that every rotation is a product of simple ones, and treats the isoclinic case in which all angles are equal. It closes with the parameter count, $n(n-1)/2$ equal to the number of angles plus the number of plane parameters. It assumes *The Exponential of the Antisymmetric Part: One-Parameter Rotations*.

Throughout $n\ge2$, $R(\theta)$ is the rotation of a plane by the angle $\theta$, and $s=\lfloor n/2\rfloor$.

## The Definition of a Simple Rotation

**Definition.** A rotation $Q\in\mathrm{SO}(n)$ is simple when the subspace it fixes has codimension $2$:

$$
\dim\ker(Q-\mathrm{I})=n-2 .
$$

Equivalently, $Q$ acts as a rotation on one plane and as the identity on its orthogonal complement. The plane is the plane of the rotation, and the angle is the angle of the rotation on it.

**A simple rotation has one angle and no others.** In the block form of the spectral theorem, the angles are the arguments of the eigenvalues on the unit circle, counted in $[0,\pi]$. A simple rotation has one angle $\theta$, so its eigenvalues are $e^{\pm i\theta}$ and $1$ with multiplicity $n-2$. So

$$
Q=\text{rotation by }\theta\text{ in a plane }P,\qquad \text{and }Q=\mathrm{I}\text{ on }P^{\perp},
$$

and the pair $(\theta,P)$ determines $Q$; conversely $Q$ determines $P$ and $\theta$ up to the sign of the angle.

**The trace counts the angles.** For any rotation, $\operatorname{tr}Q=n-2s+2\sum_{j}\cos\theta_{j}$, and for a simple rotation this is $n-2+2\cos\theta$. At $n=3$ the trace of a rotation by $\theta$ is $1+2\cos\theta$, which is the formula of Rodrigues read on the diagonal.

**The fixed subspace is the invariant of simplicity.** A simple rotation fixes a subspace of dimension $n-2$; nothing smaller is possible, and nothing larger means an angle of $0$. So a rotation is simple exactly when its fixed subspace has the biggest dimension a rotation with a nonzero angle can have.

## Every Rotation at $n=2$ and $n=3$ Is Simple

**At $n=2$ every rotation is a rotation of the plane.** The dimension is $2$, the fixed subspace of a rotation by $\theta\ne0$ is $\{0\}$, of codimension $2$, so every rotation is simple. The angle is defined modulo $2\pi$.

**At $n=3$ every rotation is a rotation about an axis.** Every anti-Hermitian $3\times3$ matrix is $\theta[u]$, and the Rodrigues formula gives

$$
Q=\exp(\theta[u])=\cos\theta\,\mathrm{I}+\sin\theta\,[u]+(1-\cos\theta)\,uu^{\mathsf T},
$$

which fixes $u$ and rotates the plane orthogonal to $u$. So

$$
\dim\ker(Q-\mathrm{I})=1=n-2
$$

and every rotation is simple. The axis is the fixed line, and the angle is the rotation angle.

**The count of parameters matches at $n=3$.** A simple rotation is a line and an angle, which is $2+1=3$ parameters, and $\dim\mathrm{SO}(3)=3$. There is no room for a second angle, and none exists.

**Simplicity is not a property of the matrix alone.** The same matrix is simple at $n=3$ and not simple at $n=4$: the rotation by $\theta$ about a line in $\mathbb{R}^{3}$, read in $\mathbb{R}^{4}$ as a rotation of a plane with two fixed directions, fixes a plane of dimension $2=n-2$, so it is simple there as well. What changes at $n=4$ is that a rotation can turn two planes at once.

## The Block Form at $n\ge4$

**Every rotation is a block diagonal in a suitable orthonormal basis.** By the spectral theorem for orthogonal matrices, there are an orthonormal basis and angles $\theta_{1},\dots,\theta_{s}$ with $0\le\theta_{j}\le\pi$ such that

$$
Q=U\operatorname{diag}\big(R(\theta_{1}),\dots,R(\theta_{s}),1,\dots,1\big)U^{\mathsf T},\qquad s=\Big\lfloor\frac{n}{2}\Big\rfloor .
$$

The $s$ blocks act on mutually orthogonal planes, and the entries $1$ act on the orthogonal complement, of dimension $n-2s$, which is $0$ for even $n$ and $1$ for odd $n$.

**The number of independent angles is at most $s$.** An angle can vanish, and a vanishing angle removes a plane; so $Q$ has at most $s$ independent angles, and a rotation of $\mathbb{R}^{n}$ with $n\ge4$ can have two or more of them. The rotation is simple exactly when at most one angle is nonzero.

**The smallest non-simple case is $n=4$.** There $s=2$, two planes fill the space, and no direction is fixed: a rotation with two nonzero angles fixes only $0$, of codimension $4$, so it is not simple.

## The Example at $n=4$

**A rotation by two different angles is not simple.** Put

$$
Q=\operatorname{diag}\big(R(\alpha),R(\beta)\big),\qquad \alpha\ne\beta,\quad \alpha,\beta\notin\pi\mathbb{Z}.
$$

Its eigenvalues are $e^{\pm i\alpha}$ and $e^{\pm i\beta}$, so its angles are $\alpha$ and $\beta$, and

$$
\ker(Q-\mathrm{I})=\{0\},\qquad \dim\ker(Q-\mathrm{I})=0\ne2 .
$$

So $Q$ is not simple. It turns two planes, and no vector is fixed.

**The numbers at $\alpha=0.3$ and $\beta=0.7$.** The eigenvalues of $Q$ are $e^{\pm0.3i}$ and $e^{\pm0.7i}$, the angles read from the arguments are $0.3$ and $0.7$, and the rank of $Q-\mathrm{I}$ is $4$, so the fixed subspace is $\{0\}$. A simple rotation of $\mathbb{R}^{4}$ by the same first angle, namely $\operatorname{diag}(R(0.4),1,1)$, has angles $\{0.4\}$ and fixed subspace of dimension $2$.

**A non-simple rotation is still a rotation.** It is orthogonal, of determinant $1$, and it is the exponential of an antisymmetric matrix; what it lacks is a fixed direction, not a property of the group.

## The Products of Simple Rotations

**Every rotation is a product of simple rotations in orthogonal planes.** The block form gives

$$
Q=\prod_{j=1}^{s}Q_{j},\qquad Q_{j}=\text{rotation by }\theta_{j}\text{ in the plane }P_{j},
$$

where the planes $P_{1},\dots,P_{s}$ are mutually orthogonal and the factors commute. Each factor is simple: it fixes the orthogonal complement of $P_{j}$, of dimension $n-2$. So

$$
\text{every rotation of }\mathbb{R}^{n}\text{ is a product of at most }s=\lfloor n/2\rfloor\text{ simple rotations,}
$$

and at $n=4$ it is a product of at most two.

**The product of two simple rotations need not be simple.** At $n=4$, the product of a rotation by $\alpha$ in a plane $P$ and a rotation by $\beta$ in $P^{\perp}$ is simple only when one of the angles is $0$ or when $\alpha=\beta$ and the planes are suitably paired. So the set of simple rotations is not closed under multiplication, and it is not a subgroup.

**The factors are not unique, and the planes matter.** The decomposition into planes is unique when the angles are distinct and nonzero, up to the order of the factors; when two angles coincide, the planes can be mixed by a rotation inside the two-plane spanned by them, and the decomposition ceases to be unique. This non-uniqueness is the same phenomenon as the repetition of eigenvalues in the adjoint action.

## The Isoclinic Case

**All angles equal is the isoclinic case.** A rotation with $\theta_{1}=\cdots=\theta_{s}=\theta$ is called isoclinic. At $n=4$ this is the case $\alpha=\beta$, and the matrix is

$$
Q=\operatorname{diag}\big(R(\theta),R(\theta)\big)=R(\theta)\oplus R(\theta),
$$

which acts on both planes by the same angle.

**An isoclinic rotation is not simple, except when the angle is $0$ or $\pi$.** For $\theta\notin\pi\mathbb{Z}$ the matrix $\mathrm{I}$ does not appear as a block, so $\ker(Q-\mathrm{I})=\{0\}$ and the rotation is not simple. The numerical check at $\theta=0.5$ confirms it: the angles are $0.5$ and $0.5$, and the fixed subspace is $\{0\}$. At $\theta=\pi$ the rotation is $-\mathrm{I}$, which also fixes only $0$.

**The angle does not determine the rotation at $n=4$, and the pair does.** The isoclinic rotations form a two-dimensional family inside the six-dimensional rotation group at $n=4$: the angle $\theta$ and the choice of the pair of orthogonal planes, up to the mixing that leaves the angles equal. So the level sets of the angle are not the orbits, and the angles plus the planes are the coordinates.

**Isoclinic rotations are the ones the two halves see alike.** Under the splitting of $\Lambda^{2}\mathbb{R}^{4}$ into self-dual and anti-self-dual halves, a rotation acts on each half by an $\mathfrak{so}(3)$ element. The two angles are the two half-angles seen by the two halves, so $\alpha=\beta$ exactly when the two actions have the same size. The splitting is treated in *Rotors Acting on the Bivector Space: the Adjoint Action*.

## The Parameter Count

**The dimension of the rotation group is the sum of the angles and the planes.** A rotation is described by $s$ angles and by the choice of the $s$ orthogonal planes. The angles contribute $s$ parameters, and the planes contribute the rest:

$$
\dim\mathrm{SO}(n)=\frac{n(n-1)}{2}=s+\big(\text{parameters of the planes}\big).
$$

**The plane parameters are the differences.** The count gives

$$
\begin{array}{c|ccccc}
n & 3 & 4 & 5 & 6 & 7\\ \hline
s & 1 & 2 & 2 & 3 & 3\\
n(n-1)/2 & 3 & 6 & 10 & 15 & 21\\
\text{planes} & 2 & 4 & 8 & 12 & 18
\end{array}
$$

At $n=3$ the plane parameters are the $2$ of the axis; at $n=4$ they are the $4$ of a pair of orthogonal planes; at $n=5$ they are the $8$ of a pair of orthogonal planes plus the $1$ of the fixed direction, and so on. The plane count is the dimension of the homogeneous space of the orthogonal decompositions, $\mathrm{SO}(n)/(\mathrm{SO}(2)^{s}\times\mathrm{SO}(n-2s))$, plus $s$, the angles.

**The count explains why $n=4$ is the first interesting dimension.** At $n\le3$ the number of planes is at most one, so an angle and a plane exhaust the rotation; at $n=4$ there are two planes and $6=2+4$, and the extra $4$ parameters are exactly the room needed for the two angles to vary independently.

## The Numbers

**The checks at $n=4$.** The four numerical statements of the article are:

- the angles of $\operatorname{diag}(R(0.3),R(0.7))$ are $0.3$ and $0.7$, read as the absolute arguments of its eigenvalues;
- its fixed subspace is $\{0\}$, that is, $\operatorname{rank}(Q-\mathrm{I})=4$;
- the simple rotation $\operatorname{diag}(R(0.4),1,1)$ has angle $0.4$ and fixed subspace of dimension $2$;
- the isoclinic rotation $\operatorname{diag}(R(0.5),R(0.5))$ has two equal angles and fixed subspace $\{0\}$.

**The fixed subspace has the predicted dimension.** For a simple rotation of $\mathbb{R}^{n}$ the fixed subspace has dimension $n-2$, and the computation returns $1$ at $n=3$, $2$ at $n=4$ and $3$ at $n=5$. The pattern is the definition read numerically.

**The count is consistent with the group.** At $n=4$ the rotation group has dimension $6$, and the generic rotation has two distinct angles, so its orbit under conjugation is $6-2=4$-dimensional, which is the plane count. The coincidence is the statement that the angles are the invariants and the planes are the orbit coordinates.

## Summary

A rotation is simple when it fixes a subspace of codimension $2$, equivalently when it has one nonzero angle. Every rotation is simple at $n=2$ and at $n=3$, where a rotation is a rotation of the plane or a rotation about an axis. From $n=4$ on a rotation has up to $s=\lfloor n/2\rfloor$ independent angles, and the block form $\operatorname{diag}(R(\theta_{1}),\dots,R(\theta_{s}),1,\dots,1)$ displays them: the rotation by two different angles at $n=4$ fixes only $0$ and is not simple. Every rotation is a product of at most $s$ simple rotations in mutually orthogonal planes, and the isoclinic rotations, with all angles equal, are not simple but have equal angles. The parameters are the $s$ angles plus the choice of the planes, and their total is $n(n-1)/2$, which is $3=1+2$ at $n=3$ and $6=2+4$ at $n=4$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R(\theta)$ | the rotation of a plane by $\theta$ |
| $s=\lfloor n/2\rfloor$ | the maximal number of angles |
| $\theta_{j}$ | the angles, in $[0,\pi]$ |
| $P_{j}$ | the mutually orthogonal planes |
| $\ker(Q-\mathrm{I})$ | the fixed subspace |
| $\alpha,\beta$ | the two angles at $n=4$ |
| $n(n-1)/2$ | the dimension of the rotation group |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the canonical form of an orthogonal matrix.
- Percy A. M. Dirac, *The theory of spinors and the quantum mechanics of the electron*, for the isoclinic rotations of $\mathbb{R}^{4}$ and their role in the two halves.
- [The Exponential of the Antisymmetric Part: One-Parameter Rotations](the-exponential-of-the-antisymmetric-part-one-parameter-rotations.html), for the block form and the angles as exponentials.
- [Rotors Acting on the Bivector Space: the Adjoint Action](rotors-acting-on-the-bivector-space-the-adjoint-action.html), for the splitting of the bivectors at $n=4$.
- [The Rotor as a Square Root of a Rotation: $\mathrm{Spin}(n)\to\mathrm{SO}(n)$](the-rotor-as-a-square-root-of-a-rotation-spin-n-to-so-n.html), for the double cover of the rotation group.
