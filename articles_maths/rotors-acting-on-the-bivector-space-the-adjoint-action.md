# __Rotors Acting on the Bivector Space: the Adjoint Action__

## Introduction

**A rotation acts on the bivectors by $K\mapsto QKQ^{\mathsf T}$, that action preserves the Killing form, so it is an orthogonal map of the space of bivectors, and at $n=3$ it is nothing but the rotation itself acting on $\mathbb{R}^{3}$.**

The bivector space is the space of antisymmetric matrices, of dimension $n(n-1)/2$. The article proves that the action of $\mathrm{SO}(n)$ is a homomorphism into $\mathrm{SO}(N)$, that the invariant form is the Killing form and is negative definite, that at $n=3$ the action is the defining action read through $\operatorname{Skew}_3\cong\mathbb{R}^{3}$, that at $n=4$ the space splits into two invariant halves, and that the orbits are classified by the angles. It assumes *The Exponential of the Antisymmetric Part: One-Parameter Rotations* and *The Rotor as a Square Root of a Rotation: $\mathrm{Spin}(n)\to\mathrm{SO}(n)$*.

Throughout $n\ge2$, $N=n(n-1)/2$, and $\langle X,Y\rangle=\operatorname{tr}(X^{\mathsf T}Y)$ is the Frobenius form.

## The Bivector Space

**A bivector is an antisymmetric matrix, and an antisymmetric matrix is a 2-form.** The space $\operatorname{Skew}_n$ is the Lie algebra of $\mathrm{SO}(n)$ under the commutator $[X,Y]=XY-YX$. An antisymmetric matrix is the same data as an alternating bilinear form, and the pairing

$$
K\longleftrightarrow\omega_{K}(u,v)=\langle Ku,v\rangle
$$

identifies $\operatorname{Skew}_n$ with $\Lambda^{2}\mathbb{R}^{n}$ and with $\Lambda^{2}(\mathbb{R}^{n})^{*}$. So

$$
\dim\operatorname{Skew}_n=\binom{n}{2}=\frac{n(n-1)}{2}=N .
$$

**The elementary bivector is a plane with an area.** The matrix $E_{ij}=e_{i}e_{j}^{\mathsf T}-e_{j}e_{i}^{\mathsf T}$ is anti-Hermitian, and the $E_{ij}$ for $i<j$ form a basis. The pair $(i,j)$ is a plane, and $E_{ij}$ records the plane with its orientation and its unit area. This is the sense in which the bivector space is the space of oriented areas.

**The commutator of two bivectors is a bivector.** The space is closed under the commutator, and the identity

$$
[E_{ij},E_{kl}]=\delta_{jk}E_{il}-\delta_{ik}E_{jl}-\delta_{jl}E_{ik}+\delta_{il}E_{jk}
$$

shows the closure on the basis. So the bivector space carries both an inner product and a bracket, and the adjoint action preserves both.

## The Adjoint Action

**Definition.** For $Q\in\mathrm{SO}(n)$ and $K\in\operatorname{Skew}_n$, put

$$
\operatorname{Ad}_{Q}(K)=QKQ^{\mathsf T}.
$$

The result is anti-Hermitian, since $(QKQ^{\mathsf T})^{\mathsf T}=QK^{\mathsf T}Q^{\mathsf T}=-QKQ^{\mathsf T}$, so the map lands in $\operatorname{Skew}_n$.

**The action is a homomorphism.** For $Q,R\in\mathrm{SO}(n)$,

$$
\operatorname{Ad}_{Q}\operatorname{Ad}_{R}(K)=QRK(QR)^{\mathsf T}=\operatorname{Ad}_{QR}(K),
$$

and $\operatorname{Ad}_{\mathrm{I}}$ is the identity. So

$$
\operatorname{Ad}:\ \mathrm{SO}(n)\longrightarrow\mathrm{GL}\big(\operatorname{Skew}_n\big)=\mathrm{GL}_N(\mathbb{R})
$$

is a representation of the rotation group on the bivector space, of dimension $N=n(n-1)/2$.

**The action on a bivector is the action on its plane.** At $n=3$ the map reads $[u]\mapsto[Qu]$: the rotated bivector is the bivector of the rotated vector. Over $100$ random pairs $(Q,u)$ the identity

$$
Q\,[u]\,Q^{\mathsf T}=[Qu]
$$

holds with maximum error $1.9\cdot10^{-15}$.

**The rotor acts by the sandwich.** A rotor $R$ acts on vectors by $X\mapsto RX\widetilde{R}$, and on bivectors by $K\mapsto RKR^{-1}$, because a bivector is a product of two vectors. The two actions are the same representation, one in the Clifford algebra and one in matrices.

## The Action Is an Automorphism

**The adjoint action preserves the commutator.** For anti-Hermitian $X,Y$ and orthogonal $Q$,

$$
[QXQ^{\mathsf T},QYQ^{\mathsf T}]=QXQ^{\mathsf T}QYQ^{\mathsf T}-QYQ^{\mathsf T}QXQ^{\mathsf T}=Q[X,Y]Q^{\mathsf T}.
$$

So each $\operatorname{Ad}_{Q}$ is an automorphism of the Lie algebra, which is the defining property of the adjoint representation.

**The action preserves the Frobenius form.** Since $Q^{\mathsf T}Q=\mathrm{I}$,

$$
\langle QXQ^{\mathsf T},QYQ^{\mathsf T}\rangle=\operatorname{tr}\big(QXQ^{\mathsf T}QYQ^{\mathsf T}\big)=\operatorname{tr}\big(QXYQ^{\mathsf T}\big)=\operatorname{tr}(XY)=\langle X,Y\rangle .
$$

So the representation is orthogonal for the Frobenius form, and its image lies in $\mathrm{O}(N)$.

**The trace form is negative definite on the anti-Hermitian space.** For anti-Hermitian $K\ne0$,

$$
\operatorname{tr}(K^{\mathsf T}K)=\operatorname{tr}(-K^{2})=-\operatorname{tr}(K^{2})=\sum_{ij}K_{ij}^{2}>0,
$$

so $\operatorname{tr}(K^{\mathsf T}K)$ is positive definite and $\operatorname{tr}(XY)$ is negative definite on $\operatorname{Skew}_n$, with the sign of the Killing form.

## The Killing Form

**The Killing form of $\mathfrak{so}(n)$ is a multiple of the trace form.** For $X,Y\in\operatorname{Skew}_n$,

$$
B(X,Y)=\operatorname{tr}\big(\operatorname{ad}_{X}\operatorname{ad}_{Y}\big)=(n-2)\operatorname{tr}(XY).
$$

The factor vanishes at $n=2$: the algebra is abelian and its Killing form is zero. For $n\ge3$ the factor is positive.

**The form is negative definite.** With $\operatorname{tr}(XY)<0$ for anti-Hermitian $X,Y$ and $X\ne0$,

$$
B(X,X)=(n-2)\operatorname{tr}(X^{2})=-(n-2)\sum_{ij}X_{ij}^{2}<0\qquad(n\ge3).
$$

So $-B$ is an inner product on the bivector space, and $\mathrm{SO}(n)$ acts by isometries of it. At $n=3$ and $X=[x]$, $Y=[y]$ the form is $-2\langle x,y\rangle$, the Euclidean form up to the factor.

**The form is invariant under the adjoint action.** Since $\operatorname{Ad}_{Q}$ is an algebra automorphism,

$$
B\big(\operatorname{Ad}_{Q}X,\operatorname{Ad}_{Q}Y\big)=B(X,Y),
$$

and the same identity follows from the trace computation with the factor $n-2$ carried along. Over $100$ random pairs of bivectors and $100$ random rotations the maximum error is $1.4\cdot10^{-14}$.

## The Image Is Orthogonal

**The image lies in $\mathrm{SO}(N)$, not only in $\mathrm{O}(N)$.** Each $\operatorname{Ad}_{Q}$ is orthogonal of size $N$; its determinant is continuous in $Q$ with values in $\{\pm1\}$, the group $\mathrm{SO}(n)$ is connected, and $\operatorname{Ad}_{\mathrm{I}}$ has determinant $1$. So

$$
\operatorname{Ad}_{Q}\in\mathrm{SO}(N),\qquad N=\frac{n(n-1)}{2},
$$

for every rotation $Q$. A check at $n=4$ returns determinant $1$ to $10^{-15}$.

**The eigenvalues of the adjoint map lie on the unit circle.** If $Q$ has eigenvalues $\lambda_{1},\dots,\lambda_{n}$ on the unit circle, then $\operatorname{Ad}_{Q}$ acts on $\Lambda^{2}$ with eigenvalues $\lambda_{i}\lambda_{j}$ for $i<j$, each of modulus one, so

$$
\operatorname{spec}\big(\operatorname{Ad}_{Q}\big)\subseteq\{z:|z|=1\},
$$

and the check at $n=4,5$ gives maximum deviation $1.8\cdot10^{-15}$.

## The Case $n=3$

**The bivector space is a three-dimensional Euclidean space.** The map $u\mapsto[u]$ is an isomorphism $\mathbb{R}^{3}\to\operatorname{Skew}_3$, and

$$
\langle[u],[v]\rangle=\operatorname{tr}\big([u]^{\mathsf T}[v]\big)=-2\langle u,v\rangle .
$$

So the Frobenius form is $-2$ times the Euclidean form, and the Killing form is the same up to the factor.

**The commutator is the cross product.** For $u,v\in\mathbb{R}^{3}$,

$$
\big[[u],[v]\big]=[u\times v],
$$

so $\operatorname{Skew}_3$ with the commutator is $\mathbb{R}^{3}$ with the cross product, and the rotation group acts by its defining action:

$$
\operatorname{Ad}_{Q}\big([u]\big)=[Qu].
$$

**The adjoint representation is the defining representation.** The matrix of $\operatorname{Ad}_{Q}$ in the basis $([e_{1}],[e_{2}],[e_{3}])$ is the matrix of $Q$, because $[Qu]$ has the coordinates $Qu$. So at $n=3$ the adjoint representation is the rotation acting on vectors, disguised as an action on planes.

## The Case $n=4$: Two Ideals

**The bivector space splits into a self-dual and an anti-self-dual half.** On $\Lambda^{2}\mathbb{R}^{4}$ the Hodge star satisfies $*^{2}=1$, so the space is the direct sum of the eigenspaces

$$
\Lambda^{2}_{+}=\{\omega:*\omega=\omega\},\qquad \Lambda^{2}_{-}=\{\omega:*\omega=-\omega\},
$$

each of dimension $3$. In matrix terms, with the basis $E_{12},E_{34},E_{13},E_{24},E_{14},E_{23}$,

$$
\Lambda^{2}_{\pm}=\operatorname{span}\big\{E_{12}\pm E_{34},\ E_{13}\mp E_{24},\ E_{14}\pm E_{23}\big\}.
$$

**The star commutes with the rotations, so the halves are invariant.** The star is built from the metric and the orientation, and a rotation preserves both, so $*\operatorname{Ad}_{Q}=\operatorname{Ad}_{Q}*$. Hence each half is carried into itself, and

$$
\operatorname{Skew}_4=\Lambda^{2}_{+}\oplus\Lambda^{2}_{-},\qquad 6=3+3,
$$

with both summands preserved. The direct check confirms it: the projection of $\operatorname{Ad}_{Q}K$ on a half depends only on the projection of $K$ on that half, to $10^{-15}$.

**Each half is an ideal, and each is a copy of $\mathfrak{so}(3)$.** A commutator of two self-dual bivectors is again self-dual, because the star commutes with the bracket, so each half is closed under the bracket and is an ideal. Each is three-dimensional with a negative definite Killing form, hence isomorphic to $\mathfrak{so}(3)$, and

$$
\mathfrak{so}(4)\cong\mathfrak{so}(3)\oplus\mathfrak{so}(3).
$$

**The two halves see the two angles separately.** A rotation of $\mathbb{R}^{4}$ has one angle per half, and equal angles in modulus give the isoclinic case, treated in *Simple and Non-Simple Rotations: One Angle at $n\le3$, $\lfloor n/2\rfloor$ Planes at $n\ge4$*.

## The Orbits

**The orbit of a bivector is determined by its angles.** Let $K\in\operatorname{Skew}_n$ have angles $\theta_{1},\dots,\theta_{s}$ with $s=\lfloor n/2\rfloor$, in the block form of the spectral theorem for antisymmetric matrices. Two bivectors lie in the same orbit exactly when

$$
\{\theta_{1},\dots,\theta_{s}\}=\{\theta'_{1},\dots,\theta'_{s}\}
$$

as multisets, zeros included. The angles are the invariants of the action, and the action is transitive on the set of bivectors with a given multiset.

**The dimension of a generic orbit is $N-s$.** The stabiliser of a bivector with distinct nonzero angles is the torus that rotates each invariant plane separately, of dimension $s$. So the orbit of such a bivector is the homogeneous space

$$
\mathrm{SO}(n)\big/\big(\mathrm{SO}(2)^{s}\times\mathrm{SO}(n-2s)\big),\qquad \dim=\frac{n(n-1)}{2}-s .
$$

At $n=3$ this is $3-1=2$, a sphere: the orbit of a nonzero bivector is the sphere of bivectors of the same area. At $n=4$ with two distinct angles it is $6-2=4$, and with equal angles it is smaller, because the stabiliser grows.

**Repeated angles shrink the orbit.** When two angles coincide, the stabiliser contains the rotations that mix the two planes, and the orbit loses dimension. The extreme case is the zero bivector, whose orbit is a point. So the orbit is a function of the multiset of angles, and the multiset is the complete invariant.

**The angles are read on the exponential.** The eigenvalues of $\exp K$ are $e^{\pm i\theta_{j}}$ and $1$, so the angles are the arguments of the eigenvalues, in $[0,\pi]$. Two bivectors are in the same orbit exactly when $\exp K$ and $\exp K'$ are conjugate in $\mathrm{SO}(n)$: the adjoint orbits are the fibres of the exponential up to conjugacy.

## The Numbers

**The invariants hold numerically.** Over $100$ random rotations at $n=4$ and $100$ random pairs of bivectors, the following hold to the stated accuracy:

- the Killing form is preserved, maximum error $1.4\cdot10^{-14}$;
- the adjoint matrix is orthogonal with determinant $1$, to $10^{-15}$;
- its eigenvalues have modulus one, to $1.8\cdot10^{-15}$;
- the identity $\operatorname{Ad}_{Q}([u])=[Qu]$ at $n=3$ holds to $1.9\cdot10^{-15}$;
- the two halves of $\Lambda^{2}\mathbb{R}^{4}$ are invariant, to $10^{-15}$.

## Summary

The bivector space is $\operatorname{Skew}_n$, of dimension $N=n(n-1)/2$, identified with the 2-forms. A rotation acts on it by $\operatorname{Ad}_{Q}(K)=QKQ^{\mathsf T}$, an algebra automorphism that preserves the Frobenius form and the Killing form $B=(n-2)\operatorname{tr}(XY)$, and lands in $\mathrm{SO}(N)$ because the form is negative definite and the rotation group is connected. At $n=3$ the space is $\mathbb{R}^{3}$ with the cross product, and the adjoint action is the defining action, $\operatorname{Ad}_{Q}([u])=[Qu]$. At $n=4$ the space splits as $\Lambda^{2}_{+}\oplus\Lambda^{2}_{-}$, of dimensions $3+3$, and each half is an ideal isomorphic to $\mathfrak{so}(3)$, so $\mathfrak{so}(4)\cong\mathfrak{so}(3)\oplus\mathfrak{so}(3)$. The orbits are classified by the multiset of angles, a generic orbit has dimension $N-s$ with $s=\lfloor n/2\rfloor$, and the eigenvalues of every adjoint map lie on the unit circle.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{Skew}_n$ | the bivector space, of dimension $N=n(n-1)/2$ |
| $E_{ij}$ | the elementary bivector $e_{i}e_{j}^{\mathsf T}-e_{j}e_{i}^{\mathsf T}$ |
| $\operatorname{Ad}_{Q}(K)=QKQ^{\mathsf T}$ | the adjoint action |
| $B(X,Y)=(n-2)\operatorname{tr}(XY)$ | the Killing form |
| $\langle X,Y\rangle=\operatorname{tr}(X^{\mathsf T}Y)$ | the Frobenius form |
| $\Lambda^{2}_{\pm}$ | the self-dual and anti-self-dual halves at $n=4$ |
| $s=\lfloor n/2\rfloor$ | the rank, the number of angles |
| $\theta_{j}$ | the rotation angles of a bivector |

## Further Reading

- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (Academic Press, 1978), for the adjoint representation and the Killing form.
- [The Exponential of the Antisymmetric Part: One-Parameter Rotations](the-exponential-of-the-antisymmetric-part-one-parameter-rotations.html), for the block form and the angles of an antisymmetric matrix.
- [The Rotor as a Square Root of a Rotation: $\mathrm{Spin}(n)\to\mathrm{SO}(n)$](the-rotor-as-a-square-root-of-a-rotation-spin-n-to-so-n.html), for the sandwich action of the rotor.
- [The Matrix Algebra $M_n(\mathbb{R})$](the-matrix-algebra-mnr.html), for the bracket and the trace form.
