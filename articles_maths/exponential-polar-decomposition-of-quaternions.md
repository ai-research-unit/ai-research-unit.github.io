# __Exponential Polar Decomposition of Quaternions__

## Introduction

The modulus–unit polar decomposition of *Modulus–Unit Polar Decomposition of Quaternions* writes every nonzero quaternion as $\tilde q=r\tilde u_{\mathrm r}$, with $r=\lvert\tilde q\rvert>0$ and $\tilde u_{\mathrm r}$ on the unit sphere. It names the modulus by a square root and the rotor by an equation. The exponential form names both by one exponent: it writes

$$
\tilde q = \exp(L), \qquad L = \ln r + v, \qquad v\in\operatorname{Im}\mathbb{H},
$$

with $\ln r$ the real logarithmic scale and $v$ the pure exponent. The unit factor is $\exp(v)$, and for $v\neq0$ it is $\cos\theta+n\sin\theta$ with $\theta=\lvert v\rvert$ and $n=v/\lvert v\rvert$ a unit pure quaternion. The pair $(r,\theta n)$ is the polar data of the quaternion in exponential coordinates.

The exponential is surjective onto $\mathbb{H}^{\times}$ but not injective: its kernel is a union of spheres and not a subgroup. Hence it is not a homomorphism, and $\mathbb{H}^{\times}$ is not the quotient $\mathbb{H}/\ker\exp$, in contrast with $\mathbb{C}^{\times}\cong\mathbb{C}/2\pi i\mathbb{Z}$. What survives is the amalgamation of the two factors into one exponential, and only because the logarithmic scale is central.

The plan is as follows: the closed form, the image and the kernel (§*The Image of the Exponential*, §*The Kernel*), the decomposition and its uniqueness (§*The Exponential Polar Decomposition*), the failure of the homomorphism, the critical set and the Jacobian, the matrix picture, the exponential coordinates, the comparison of the forms, and examples.

The conventions are those of *Quaternion Algebra*, *Norm and Invertibility in the Quaternion Algebra* and *Conventions in Mathematics*. The exponential is written $\exp(\cdot)$, with the letter $e$ reserved for the basis units. The symbols are collected in §*Summary of Notation*.

Every numerical value displayed below was recomputed in double precision.

## The Exponential Map

### The Series and the Closed Form

The exponential of a quaternion is defined by the absolutely convergent series

$$
\exp(\tilde q) = \sum_{k\ge0}\frac{\tilde q^k}{k!},
$$

the convergence following from $\lvert\tilde q^k\rvert=\lvert\tilde q\rvert^k$ and the convergence of the real exponential series.

**Proposition.** Write $\tilde q=q_t e_t+v$ with $v$ pure. If $v\neq0$ then

$$
\exp(\tilde q) = \exp(q_t)\left(\cos\lvert v\rvert+\frac{v}{\lvert v\rvert}\sin\lvert v\rvert\right),
$$

and if $v=0$ then $\exp(\tilde q)=\exp(q_t)e_t$.

**Proof.** The scalar $q_t$ commutes with $v$, so $\exp(q_t+v)=\exp(q_t)\exp(v)$. For pure $v$, the square is the scalar $v^2=-\lvert v\rvert^2$, hence $v^{2k}=(-1)^k\lvert v\rvert^{2k}$ and $v^{2k+1}=(-1)^k\lvert v\rvert^{2k}v$. The series therefore separates into

$$
\exp(v) = \sum_{k\ge0}\frac{(-1)^k\lvert v\rvert^{2k}}{(2k)!}
+ \frac{v}{\lvert v\rvert}\sum_{k\ge0}\frac{(-1)^k\lvert v\rvert^{2k+1}}{(2k+1)!}
= \cos\lvert v\rvert+\frac{v}{\lvert v\rvert}\sin\lvert v\rvert,
$$

and the two series are the cosine and the sine.

The formula is Euler's formula with the imaginary unit replaced by any unit pure quaternion. The unit pure quaternions form the axis sphere $S^2\subset\operatorname{Im}\mathbb{H}$, and every one of them squares to $-e_t$. There is no second row of the exponential trichotomy here: a unit pure quaternion squares to $-e_t$, never $+e_t$, and a pure quaternion with $v^2=0$ is zero, so there is no hyperbolic direction and no nilpotent direction on the pure subspace. The exponential is trigonometric on the pure subspace, real on the scalar line, and never parabolic.

Three values are worth recording:

$$
\exp(\tfrac{\pi}{2}\vec e_x)=\vec e_x, \qquad \exp(\pi\vec e_x)=-e_t, \qquad \exp(2\pi\vec e_x)=e_t .
$$

The first is a quarter-turn rotor, the second is the central point $-1$, and the third is the first return to the identity.

### The Image of the Exponential

**Theorem.** The exponential maps $\mathbb{H}$ onto $\mathbb{H}^{\times}$.

**Proof.** The modulus of $\exp(\tilde q)$ is $\exp(q_t)$, which is strictly positive, so $0$ is not in the image. Conversely, let $\tilde q\neq0$, put $r=\lvert\tilde q\rvert$ and $\tilde u=\tilde q/r$. Then $\langle\tilde u\rangle_{\natural}=1$ and $\tilde u=\cos\theta+n\sin\theta$ with

$$
\theta=\arccos\bigl(\operatorname{Sc}\tilde u\bigr)\in[0,\pi],
$$

and with $n=\operatorname{Vec}\tilde u/\lvert\operatorname{Vec}\tilde u\rvert$ when $\operatorname{Vec}\tilde u\neq0$. Put $L=\ln r+\theta n$. If $\operatorname{Vec}\tilde u\neq0$ then $\sin\theta\neq0$ and

$$
\exp(L)=r\bigl(\cos\theta+n\sin\theta\bigr)=r\tilde u=\tilde q .
$$

If $\operatorname{Vec}\tilde u=0$ then $\tilde u=\pm e_t$. For $\tilde u=e_t$ take $L=\ln r$ and $\theta=0$; for $\tilde u=-e_t$ take $\theta=\pi$ and any unit pure $n$, so that $L=\ln r+\pi n$. In both cases $\exp(L)=\tilde q$. Hence every nonzero quaternion is an exponential.

The proof is constructive and gives a logarithm, but not a unique one: the choices at $\tilde u=\pm e_t$ are arbitrary, and the non-uniqueness for the other elements is computed in §*Uniqueness*.

### The Kernel

**Theorem.** Let $\tilde q=q_t e_t+v$ with $v$ pure. Then $\exp(\tilde q)=e_t$ if and only if $q_t=0$ and $\lvert v\rvert\in2\pi\mathbb{Z}$.

**Proof.** If $\exp(\tilde q)=e_t$ then taking moduli gives $\exp(q_t)=1$, hence $q_t=0$. If $v=0$ the condition is met. If $v\neq0$, the closed form gives

$$
\cos\lvert v\rvert+\frac{v}{\lvert v\rvert}\sin\lvert v\rvert=e_t .
$$

Comparing the pure parts gives $\sin\lvert v\rvert=0$, so $\lvert v\rvert\in\pi\mathbb{Z}$, and comparing the scalar parts gives $\cos\lvert v\rvert=1$, so $\lvert v\rvert\in2\pi\mathbb{Z}$. Conversely, if $q_t=0$ and $\lvert v\rvert=2\pi k$ with $k\ge1$, the closed form gives $\cos(2\pi k)+ (v/\lvert v\rvert)\sin(2\pi k)=e_t$; for $k=0$ one has $v=0$ and $\exp(0)=e_t$.

Hence

$$
\ker\exp = \{0\}\cup\bigcup_{k\ge1}2\pi k\,S^2,
$$

where $2\pi k\,S^2$ is the sphere of pure quaternions of norm $2\pi k$. The kernel is a union of spheres, one for each positive integer, together with the origin.

**Corollary.** The kernel is not a subgroup of $(\mathbb{H},+)$. The elements $2\pi\vec e_x$ and $2\pi\vec e_y$ both lie in the kernel, but their sum $2\pi(\vec e_x+\vec e_y)$ has norm $2\pi\sqrt{2}$, which is not a multiple of $2\pi$, so the sum is not in the kernel.

The kernel is closed under negation and under conjugation, but not under addition; it is a union of two-dimensional spheres together with the isolated origin, not a manifold of a single dimension.

## The Exponential Polar Decomposition

### Existence

**Theorem.** Every nonzero quaternion $\tilde q$ has an exponential polar decomposition

$$
\tilde q=\exp(\ln r+v), \qquad r=\lvert\tilde q\rvert>0, \quad v\in\operatorname{Im}\mathbb{H},
$$

with $\exp(v)=\tilde q/r$. The representation is principal when $\lvert v\rvert<\pi$.

**Proof.** Let $r=\lvert\tilde q\rvert$ and $\tilde u=\tilde q/r$. The proof of §*The Image of the Exponential* produces a pure $v$ with $\exp(v)=\tilde u$, either $v=0$ for $\tilde u=e_t$, or $v=\theta n$ with $\theta\in(0,\pi]$ for the other units. Then

$$
\exp(\ln r+v)=\exp(\ln r)\exp(v)=r\tilde u=\tilde q,
$$

the first equality because $\ln r$ is central and commutes with $v$. The principal choice takes $\theta\in[0,\pi)$ and $v=\theta n$, which is possible for every $\tilde u\neq-e_t$.

### Uniqueness

The pair $(r,v)$ is not unique in general, and the exact statement separates three cases.

**Theorem.** Let $\tilde q\neq0$.

- If $\tilde q\notin\mathbb{R}$, then $\tilde q$ has exactly one representation $\tilde q=\exp(\ln r+\theta n)$ with $r>0$, $\theta\in(0,\pi)$ and $n$ a unit pure quaternion. Every logarithm of $\tilde q$ is $\ln r+(\theta+2\pi k)n$ for some $k\in\mathbb{Z}$.
- If $\tilde q=r_0e_t$ with $r_0>0$, then $r=r_0$ and $\theta=0$, and the axis $n$ is arbitrary. The logarithms are $\ln r_0+w$ with $w$ pure and $\lvert w\rvert\in2\pi\mathbb{Z}_{\ge0}$.
- If $\tilde q=-r_0e_t$ with $r_0>0$, then $r=r_0$ and $\theta=\pi$, and the axis $n$ is arbitrary. The logarithms are $\ln r_0+w$ with $w$ pure and $\lvert w\rvert\in(2k+1)\pi$, $k\ge0$.

**Proof.** Let $L=\ln r+w$ be a logarithm with $w$ pure. Then $\exp(w)=\tilde u=\tilde q/r$. If $\tilde u\neq\pm e_t$, write $\tilde u=\cos\theta+n\sin\theta$ with $\theta\in(0,\pi)$ and $n$ unique. The closed form gives $\cos\lvert w\rvert=\cos\theta$ and $(w/\lvert w\rvert)\sin\lvert w\rvert=n\sin\theta$. Since $\sin\theta\neq0$, the second equation forces $w/\lvert w\rvert=\pm n$ and $\sin\lvert w\rvert=\pm\sin\theta$ with the same sign; in both cases $w=(\theta+2\pi k)n$. The two real cases follow from $\exp(w)=\pm e_t$, which is $\cos\lvert w\rvert=\pm1$ and $\sin\lvert w\rvert=0$, with the direction of $w$ free.

The pair $(r,\theta n)$ is therefore unique off the real axis. On the positive real axis the angle is zero and the axis is arbitrary; on the negative real axis the angle is $\pi$ and the axis is arbitrary. The principal representation, with $\lvert v\rvert<\pi$, exists for every element except the negative real axis, and it is unique there.

### The Single Exponential

The two factors of the modulus–unit form amalgamate into one exponential:

$$
\tilde q = \exp(\ln r)\,\exp(v)=\exp(\ln r+v).
$$

The first equality is the modulus–unit form; the second holds because $\ln r$ is a real scalar and therefore commutes with $v$. The amalgamation is a statement about two commuting exponents, not about the exponential being a homomorphism. For two general pure exponents the product $\exp(v_1)\exp(v_2)$ is not $\exp(v_1+v_2)$, as §*The Failure of the Homomorphism* shows.

The single exponential is therefore available for every nonzero quaternion, and its exponent is unique in the principal ball $\lvert v\rvert<\pi$. It is not a group coordinate: the map $L\mapsto\exp(L)$ is not a homomorphism.

## The Failure of the Homomorphism

### The Bracket and the Noncommutation

For pure quaternions $v_1,v_2$ the commutator is twice the cross product:

$$
[v_1,v_2]=v_1v_2-v_2v_1=2\,v_1\times v_2 .
$$

The Baker–Campbell–Hausdorff series begins

$$
\log\bigl(\exp(L_1)\exp(L_2)\bigr)=L_1+L_2+\tfrac12[L_1,L_2]+\cdots,
$$

so the exponential is a homomorphism only when the bracket and all higher commutators vanish. A direct counterexample is enough. Take $L_1=\tfrac{\pi}{2}\vec e_x$ and $L_2=\tfrac{\pi}{2}\vec e_y$. Then

$$
\exp(L_1)\exp(L_2)=\vec e_x\vec e_y=\vec e_z,
$$

while

$$
\exp(L_1+L_2)=\cos\frac{\pi}{\sqrt2}+\frac{\vec e_x+\vec e_y}{\sqrt2}\sin\frac{\pi}{\sqrt2}
=-0.605700+0.562640\,(\vec e_x+\vec e_y),
$$

which is not $\vec e_z$. The bracket here is $2(\tfrac{\pi}{2}\vec e_x)\times(\tfrac{\pi}{2}\vec e_y)=\tfrac{\pi^2}{2}\vec e_z$, and it is the first obstruction to additivity.

The failure is not a small-angle effect: it persists for non-commuting exponents, however small. It is the exact quaternion analogue of the noncommutativity of the unit sphere. The modulus–unit form is a group isomorphism, $\mathbb{H}^{\times}\cong\mathbb{R}_{>0}\times S^3$; the exponential form is not.

### The Contrast with the Complex Case

In $\mathbb{C}$ the exponential is a homomorphism from $(\mathbb{C},+)$ onto $\mathbb{C}^{\times}$, with kernel $2\pi i\mathbb{Z}$, a discrete subgroup. The first isomorphism theorem gives

$$
\mathbb{C}^{\times}\cong\mathbb{C}/2\pi i\mathbb{Z},
$$

and the logarithm is a coset of the kernel: every logarithm of $Q$ is $\log Q+2\pi ik$.

In $\mathbb{H}$ none of this survives. The kernel $\{0\}\cup2\pi S^2\cup4\pi S^2\cup\cdots$ is not a subgroup, so $\mathbb{H}/\ker\exp$ is not a group; the exponential is not a homomorphism, so the first isomorphism theorem does not apply; and the fibres are not cosets of the kernel. For $\tilde q\notin\mathbb{R}$ the fibre is the discrete line

$$
\exp^{-1}(\tilde q)=\{\ln r+(\theta+2\pi k)n:k\in\mathbb{Z}\},
$$

whereas $\tilde q+\ker\exp$ would be a union of spheres through $\tilde q$. The two sets are different, and the difference is exactly the noncommutativity of the exponent. The modulus–unit splitting is the substitute for the missing quotient: it is a genuine group isomorphism, and it uses the sphere rather than the exponential to carry the non-central part.

## The Critical Set and the Jacobian

### The Critical Set

**Theorem.** The exponential is a local diffeomorphism at $\tilde q=q_t e_t+v$ exactly when $\lvert v\rvert\notin\pi\mathbb{Z}_{>0}$. The critical values are the nonzero real quaternions.

**Proof.** The differential of the exponential is

$$
\mathrm d\exp_{\tilde q} = L_{\exp(\tilde q)}\circ\frac{1-\exp(-\operatorname{ad}_{\tilde q})}{\operatorname{ad}_{\tilde q}},
$$

where $L$ denotes left multiplication and $\operatorname{ad}_{\tilde q}(X)=[\tilde q,X]$. The left factor is invertible, so the rank is that of

$$
A=\frac{1-\exp(-\operatorname{ad}_{\tilde q})}{\operatorname{ad}_{\tilde q}}.
$$

The operator $\operatorname{ad}_{\tilde q}$ is skew-symmetric for the Euclidean form. For $v\neq0$, its eigenvalues are $0$, on the two-dimensional span of $e_t$ and $v$, and $\pm2i\lvert v\rvert$, on the two-dimensional orthogonal complement of $v$ in the pure subspace. Hence the eigenvalues of $A$ are $1$ with multiplicity two and

$$
\frac{1-\exp(\mp2i\lvert v\rvert)}{\pm2i\lvert v\rvert}=\exp(\mp i\lvert v\rvert)\frac{\sin\lvert v\rvert}{\lvert v\rvert}
$$

with multiplicity one each for $v\neq0$; at $v=0$ all four are $1$. The differential is invertible exactly when $\lvert v\rvert\notin\pi\mathbb{Z}_{>0}$: at $\lvert v\rvert=0$ the operator $A$ is the identity, and for $\lvert v\rvert>0$ the condition is $\sin\lvert v\rvert\neq0$.

At a critical point $\lvert v\rvert=\pi k$ the two eigenvalues of $A$ on the orthogonal plane vanish, so the rank drops by two. The critical value is

$$
\exp(q_t)\bigl(\cos\pi k+n\sin\pi k\bigr)=(-1)^k\exp(q_t)e_t,
$$

and as $q_t$ ranges over $\mathbb{R}$ and $k\ge1$ varies, these are exactly the nonzero real quaternions, positive for even $k$ and negative for odd $k$.

The critical set is therefore the union of the spheres $\{\lvert v\rvert=\pi k\}$ over $k\ge1$, in every scalar height; its image is the real axis minus the origin. At the origin the differential is the identity.

### The Jacobian

The determinant of the differential is the product of the determinant of left multiplication by $\exp(\tilde q)$ and the determinant of $A$. Left multiplication by a quaternion of modulus $\exp(q_t)$ has determinant $\exp(4q_t)$, and $A$ has determinant $(\sin\lvert v\rvert/\lvert v\rvert)^2$, with the value $1$ at $v=0$. Hence

$$
\lvert\det \mathrm d\exp_{\tilde q}\rvert = \exp(4q_t)\left(\frac{\sin\lvert v\rvert}{\lvert v\rvert}\right)^2 .
$$

The singular values are also read from the same decomposition: the differential scales the plane spanned by $e_t$ and $v$ by $\exp(q_t)$, with multiplicity two, and the orthogonal pure plane by

$$
\exp(q_t)\frac{\lvert\sin\lvert v\rvert\rvert}{\lvert v\rvert},
$$

again with multiplicity two. The map is therefore a similarity on the first plane and a different similarity on the second. It is conformal only where the two factors agree, which is $\lvert\sin\lvert v\rvert\rvert=\lvert v\rvert$, that is, only at $v=0$. The quaternion exponential is not a conformal map of four-space.

The 4-volume element in the coordinates $(q_t,v_x,v_y,v_z)$ is

$$
\mathrm dV = \exp(4q_t)\left(\frac{\sin\lvert v\rvert}{\lvert v\rvert}\right)^2\mathrm dq_t\,\mathrm dv_x\,\mathrm dv_y\,\mathrm dv_z .
$$

In polar coordinates $v=\rho n$ on the pure subspace, with $\mathrm dv=\rho^2\mathrm d\rho\,\mathrm d\Omega$, the same element reads

$$
\mathrm dV = \exp(4q_t)\sin^2\rho\,\mathrm dq_t\,\mathrm d\rho\,\mathrm d\Omega .
$$

## The Matrix Picture

### The Exponential of a Conformal Matrix

Let $\iota$ be the embedding of *Modulus–Unit Polar Decomposition of Quaternions*, §*The Embedding in M_2(C)*. For a unit pure quaternion $n$, the matrix $N=\iota(n)$ satisfies

$$
N^{\dagger}=-N, \qquad N^2=-I, \qquad \operatorname{tr}N=0 .
$$

The exponential form of a quaternion reads, in matrices,

$$
M_{\tilde q}=\iota(\tilde q)=\exp\bigl(\ln r\,I+\theta N\bigr)
=r\bigl(\cos\theta\,I+\sin\theta\,N\bigr),
$$

with $\theta=\lvert v\rvert$ and $N=\iota(v/\lvert v\rvert)$. The determinant is

$$
\det M_{\tilde q}=r^2=\langle\tilde q\rangle_{\natural},
$$

as it must be, since the determinant of the exponential is the exponential of the trace.

### The Matrix Logarithm

The matrix logarithm of $M_{\tilde q}$ is the matrix of the quaternion logarithm:

$$
\log M_{\tilde q}=\ln r\,I+\theta N
$$

for the principal choice $\theta\in(0,\pi)$. The logarithm is not unique: adding $2\pi k N$ gives the same exponential, and at $M_{\tilde q}=-rI$ the matrix $\log(-I)=\pi N$ for any traceless skew-Hermitian $N$ with $N^2=-I$ is a logarithm. The matrix logarithm inherits exactly the ambiguity of §*Uniqueness*.

### The General Matrix Polar Decomposition

Every invertible matrix $B\in M_2(\mathbb{C})$ has the polar decomposition

$$
B=PU, \qquad P=(BB^{\dagger})^{1/2}, \qquad U=P^{-1}B,
$$

with $P$ positive definite Hermitian and $U$ unitary. For $B=M_{\tilde q}$ the conformal identity $BB^{\dagger}=r^2I$ gives $P=rI$ and $U=M_{\tilde u}\in SU(2)$. The general decomposition therefore specialises to the scalar positive factor and the special unitary factor of the quaternion case. The exponential enters through the logarithm: $P=\exp(\ln r\,I)$ and $U=\exp(\theta N)$, so the matrix polar decomposition and the matrix exponential are the same statement read in the two orders.

| factor | matrix | logarithm | determinant |
|---|---|---|---|
| modulus | $rI$ | $\ln r\,I$ | $r^2$ |
| unit factor | $M_{\tilde u}\in SU(2)$ | $\theta N$ | $1$ |
| $\tilde q$ | $M_{\tilde q}$ | $\ln r\,I+\theta N$ | $r^2$ |

## The Exponential Coordinates

### The Coordinate Map

The **exponential coordinates** are the map

$$
E:\mathbb{R}\times\{\,v\in\operatorname{Im}\mathbb{H}:\lvert v\rvert<\pi\,\}\longrightarrow\mathbb{H}\setminus(-\infty,0], \qquad E(x,v)=\exp(x+v).
$$

**Theorem.** The map $E$ is a diffeomorphism onto its image.

**Proof.** The map is smooth. On the image, the inverse is $x=\ln\lvert\tilde q\rvert$ and $v$ the principal logarithm of §*Uniqueness*; it is smooth because $\arccos$ and the quotient $\theta\operatorname{Vec}\tilde u/\lvert\operatorname{Vec}\tilde u\rvert$ extend smoothly across $\operatorname{Vec}\tilde u=0$, and the remaining singular point $\tilde u=-1$ lies on the boundary $\lvert v\rvert=\pi$. The differential is invertible on $\lvert v\rvert<\pi$ by §*The Critical Set*, so the inverse function theorem makes the map a local diffeomorphism; the explicit inverse makes it bijective. Hence it is a diffeomorphism.

The image is the quaternion space cut along the closed negative real axis. The boundary sphere $\lvert v\rvert=\pi$ is mapped into that axis, and it is not part of the open coordinate domain.

### The Coordinate Lines

The coordinates $(x,v)$ give three families of curves and surfaces.

- **The scale lines.** At fixed $v$, the curve $x\mapsto\exp(x+v)$ is the ray of positive multiples of $\exp(v)$. It runs from the origin, which is not attained, through $\exp(v)$ and to infinity.
- **The angle lines.** At fixed unit $n$, the curve $\theta\mapsto\exp(x+\theta n)$ is the arc of the great circle in the plane spanned by $e_t$ and $n$. On the principal domain $\theta\in[0,\pi)$ it runs from $\exp(x)e_t$ to the point $\exp(x)(-e_t)$, which is excluded.
- **The latitude spheres.** At fixed $x$ and fixed $\rho=\lvert v\rvert$, the set of $\exp(x+\rho n)$ over unit $n$ is the two-sphere

$$
\{\,\tilde q:\lvert\tilde q\rvert=\exp(x),\ \operatorname{Sc}\tilde q=\exp(x)\cos\rho\,\},
$$

a latitude sphere in the three-sphere of radius $\exp(x)$. The exponential map reads these families as the scale, the angle and the axis.

### The Volume Element

The 4-volume element of §*The Jacobian* reads $\exp(4x)(\sin\rho/\rho)^2\,dx\,dv$ in Cartesian $v$, and $\exp(4x)\sin^2\rho\,dx\,d\rho\,d\Omega$ in polar $v=\rho n$. The factor $(\sin\rho/\rho)^2$ equals one at $\rho=0$ and vanishes on the boundary spheres $\rho=\pi k$.

## The Three Polar Decompositions

### The Three Forms

| form | word | domain | coordinate | regularity | cost |
|---|---|---|---|---|---|
| modulus–unit | $\tilde q=r\tilde u_{\mathrm r}$ | $\mathbb{H}^{\times}$ | none | algebraic | a square root |
| rational chart | $\tilde q=r\,u(v)$ | $\mathbb{H}\setminus(-\infty,0]$ | $v\in\operatorname{Im}\mathbb{H}$ | rational | a cut, and a noncommutative group law |
| exponential | $\tilde q=\exp(\ln r+v)$ | $\mathbb{H}^{\times}$ | $v\in\operatorname{Im}\mathbb{H}$ | transcendental | a non-subgroup kernel, and non-uniqueness on the real axis |

### The Comparison

The modulus–unit form is the most general and the least explicit: it exists on the whole group of units, uses only field operations and a square root, and names the rotor by the equation $\langle\tilde u_{\mathrm r}\rangle_{\natural}=1$. The rational chart is the most explicit and the most local: it gives the rotor by three rational functions of three real parameters, at the cost of the negative real axis, and its group law is a noncommutative sandwich. The exponential is global and analytic: it gives the rotor by three real parameters through a transcendental function, at the cost of a many-to-one parametrisation and a kernel that is not a subgroup.

### The Departures from the Complex Template

The complex exponential is a homomorphism with kernel $2\pi i\mathbb{Z}$; the quaternion exponential is not. Five consequences separate the two cases.

- **The kernel is not a subgroup.** It is a union of spheres, not a discrete lattice, so $\mathbb{H}/\ker\exp$ is not a group.
- **The fibres are not cosets.** For $\tilde q\notin\mathbb{R}$ the logarithms form the line $\ln r+(\theta+2\pi k)n$, not the translate $\tilde q+\ker\exp$.
- **The exponential has critical points.** The spheres $\lvert v\rvert=\pi k$ are critical, with the real axis as image; the complex exponential has none.
- **The principal domain is a ball, not a strip.** It is the open ball $\lvert v\rvert<\pi$, whose boundary sphere maps onto the negative real axis; the complex principal strip is half-open and contains that axis.
- **The axis is two-dimensional at the real points.** On the real axis the angle is fixed and the axis is an arbitrary point of $S^2$, whereas in $\mathbb{C}$ there is only one imaginary direction.

## Worked Examples

### Two Worked Elements

Take $\tilde q=3e_t+4\vec e_x$. Then $r=5$, $\operatorname{Sc}\tilde u=3/5$, and

$$
\theta=\arccos\frac{3}{5}=0.927295218, \qquad n=\vec e_x, \qquad L=\ln5+\theta\vec e_x=1.609437912+0.927295218\,\vec e_x .
$$

The reconstruction gives

$$
\exp(L)=5\left(\cos0.927295218+\vec e_x\sin0.927295218\right)=3e_t+4\vec e_x,
$$

with error $4.4\times10^{-16}$.

Take now

$$
\tilde q=e_t+2\vec e_x+3\vec e_y+4\vec e_z .
$$

The modulus is $r=\sqrt{30}=5.477225575$, the scalar part of the unit factor is $1/\sqrt{30}=0.182574186$, and

$$
\theta=\arccos\frac{1}{\sqrt{30}}=1.387192317, \qquad
n=0.371390676\,\vec e_x+0.557086015\,\vec e_y+0.742781353\,\vec e_z .
$$

The exponent is

$$
L=1.700598691+0.515190293\,\vec e_x+0.772785439\,\vec e_y+1.030380585\,\vec e_z,
$$

and $\exp(L)$ reproduces $\tilde q$ to $8.9\times10^{-16}$ in each coefficient.

### A Table of Examples

| $\tilde q$ | $r$ | $\theta$ | $n$ | $L$ |
|---|---|---|---|---|
| $2e_t$ | $2$ | $0$ | arbitrary | $\ln2$ |
| $-e_t$ | $1$ | $\pi$ | arbitrary | $\pi\vec e_x$ |
| $\vec e_x$ | $1$ | $\pi/2$ | $\vec e_x$ | $(\pi/2)\vec e_x$ |
| $3e_t+4\vec e_x$ | $5$ | $0.927295218$ | $\vec e_x$ | $1.609437912+0.927295218\,\vec e_x$ |
| $0.5e_t+0.1\vec e_x-0.2\vec e_y+0.3\vec e_z$ | $0.624499800$ | $0.642432399$ | $0.267261242\,\vec e_x-0.534522484\,\vec e_y+0.801783726\,\vec e_z$ | $-0.470804270+0.171697281\,\vec e_x-0.343394561\,\vec e_y+0.515091842\,\vec e_z$ |
| $e_t+2\vec e_x+3\vec e_y+4\vec e_z$ | $5.477225575$ | $1.387192317$ | the axis above | the exponent above |

The first line is the positive real axis: the angle is zero and the axis is undetermined. The second line is the negative real axis: the angle is $\pi$ and the axis is again undetermined; $\pi\vec e_x$ is one choice among a sphere of choices. The third line is a pure unit, whose angle is $\pi/2$ and whose axis is itself.

### The Kernel and the Non-Uniqueness

The elements $2\pi\vec e_x$, $2\pi\vec e_y$ and $2\pi(\vec e_x+\vec e_y)/\sqrt2$ all lie in the kernel. Their exponentials are $e_t$ to $2.4\times10^{-16}$. The sum $2\pi(\vec e_x+\vec e_y)$ does not lie in the kernel: its norm is $2\pi\sqrt2$, and

$$
\exp\bigl(2\pi(\vec e_x+\vec e_y)\bigr)
=\cos(2\pi\sqrt2)+\frac{\vec e_x+\vec e_y}{\sqrt2}\sin(2\pi\sqrt2)
=-0.858216186+0.362949706\,(\vec e_x+\vec e_y),
$$

which is not $e_t$.

For $\tilde q=\vec e_x$ the principal exponent is $(\pi/2)\vec e_x$. The other logarithms are $(\pi/2+2\pi k)\vec e_x$, for example $(5\pi/2)\vec e_x$, and $\exp((5\pi/2)\vec e_x)=\vec e_x$ to $3.1\times10^{-16}$. Adding $2\pi\vec e_y$ does not give another logarithm: $\exp((\pi/2)\vec e_x+2\pi\vec e_y)$ is not $\vec e_x$, because the two exponents do not commute. The fibre of $\vec e_x$ is the line $(\pi/2+2\pi k)\vec e_x$, not the translate of the kernel.

## Summary

Every nonzero quaternion is $\exp(\ln r+v)$ with $r=\lvert\tilde q\rvert>0$ and $v$ pure; the unit factor is $\cos\theta+n\sin\theta$ with $\theta=\lvert v\rvert$ and $n$ a unit pure quaternion. The pair $(r,\theta n)$ is unique off the real axis; on the real axis the angle is fixed at $0$ or $\pi$ and the axis is arbitrary. The principal representation has $\lvert v\rvert<\pi$ and covers the quaternion space cut along the closed negative real axis.

The kernel is $\{0\}\cup2\pi S^2\cup4\pi S^2\cup\cdots$, a union of spheres and not a subgroup. The exponential is therefore not a homomorphism: the bracket of two pure exponents is twice their cross product, and $\exp(L_1+L_2)\neq\exp(L_1)\exp(L_2)$ for non-commuting exponents. The group of units is not $\mathbb{H}/\ker\exp$, and the fibres are lines, not cosets. The amalgamation into one exponential survives because the logarithmic scale is central.

The differential of the exponential is invertible exactly off the spheres $\lvert v\rvert=\pi k$, whose image is the nonzero real axis; its determinant is $\exp(4q_t)(\sin\lvert v\rvert/\lvert v\rvert)^2$. In the matrix picture the exponential is $\exp(\ln r\,I+\theta N)$ with $N$ skew-Hermitian and $N^2=-I$, and the matrix polar decomposition of the conformal matrix has positive factor $rI$ and special unitary factor.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{H}$ | the quaternion algebra, basis $e_t=1,\vec e_x,\vec e_y,\vec e_z$ |
| $\tilde q=q_t e_t+v$ | a quaternion, $q_t$ its scalar part, $v$ its pure part |
| $\tilde q^{\natural}=q_t e_t-v$ | the quaternion conjugate |
| $\langle\tilde q\rangle_{\natural}=\tilde q\tilde q^{\natural}$ | the quaternion norm, positive definite |
| $r=\lvert\tilde q\rvert=\sqrt{\langle\tilde q\rangle_{\natural}}$ | the modulus |
| $v=\theta n$ | the pure exponent, $\theta=\lvert v\rvert$, $n$ a unit pure quaternion |
| $\exp(\tilde q)=\exp(q_t)(\cos\lvert v\rvert+(v/\lvert v\rvert)\sin\lvert v\rvert)$ | the closed form |
| $\ker\exp=\{0\}\cup\bigcup_{k\ge1}2\pi kS^2$ | the kernel, not a subgroup |
| $[v_1,v_2]=2v_1\times v_2$ | the commutator of pure quaternions |
| $\mathrm d\exp_{\tilde q}$ | the differential, invertible off $\lvert v\rvert\in\pi\mathbb{Z}_{>0}$ |
| $\exp(4q_t)(\sin\lvert v\rvert/\lvert v\rvert)^2$ | the Jacobian determinant |
| $L=\ln r+v$ | the exponent, principal when $\lvert v\rvert<\pi$ |
| $N=\iota(n)$ | the skew-Hermitian matrix of the unit axis |
| $M_{\tilde q}=\exp(\ln r\,I+\theta N)$ | the matrix exponential |
| $\mathbb{H}\setminus(-\infty,0]$ | the image of the principal coordinates |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 1985), for the matrix exponential, the matrix logarithm and the polar decomposition.
- John Stillwell, *Naive Lie Theory* (Springer, 2008), for the exponential map of $SU(2)$ and the unit quaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd edition 2001), for the quaternion exponential and its relation to the rotation group.
- S. J. Sangwine and E. Hitzer, "Polar decomposition of complexified quaternions and octonions", *Advances in Applied Clifford Algebras* **30** (2020), for the exponential trichotomy and the polar forms of the hypercomplex algebras.
