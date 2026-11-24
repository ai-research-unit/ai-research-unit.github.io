# __The Anti-Hermitian Derivations of the Biquaternion Algebra as $\mathfrak{su}(2)$__

## Introduction

**Two conditions pick out the generators: anti-Hermitian and scalar-free. On the algebra they are the real vectors, of real dimension three. Each real vector $v$ gives the inner derivation $\mathrm{ad}_v=L_v-R_v$, which is anti-Hermitian for the Hermitian form, satisfies the Leibniz rule, and has $\mathrm{ad}_v(w)=2\,v\times w$ on the vector part. The three derivations $\mathrm{ad}_{\vec e_x},\mathrm{ad}_{\vec e_y},\mathrm{ad}_{\vec e_z}$ are the whole anti-Hermitian derivation set, and under the bracket they form $\mathfrak{su}(2)$.**

The article writes the generators in the corpus normalization $D_k=\tfrac12\mathrm{ad}_{\vec e_k}$, so that the structure constants come out as $\epsilon_{abc}$, as in *Automorphisms and Derivations of Algebras*. With the half, $D_v(w)=v\times w$ on the vector part and the arrays below carry the entries $\pm1$ instead of $\pm2$.

The exponential of each generator is a conjugation by a rotor: $e^{\theta D_v}=\mathrm{Ad}_{\rho}$ with $\rho=e^{\theta v/2}$. Each of the three generators does one thing. It fixes the scalar line, fixes its own axis, and turns the plane of the other two axes by the angle of the array, which is the angle of the rotor because the half of the normalization cancels the half of the double cover.

The article gives the three generators as explicit $4\times4$ arrays, the bracket table, the exponential of each generator written out entry by entry, and the action of each rotor on the four parts of the algebra. It also states the dimension ladder of the operator level, which is the part the element-level statement leaves out.

The article assumes the conventions of *Algebra and Element Conventions*, the adjoint rules of *Adjoint Pair of $L$ and $R$ Operators*, and the element-level closed form of *The Exponential of the Traceless Anti-Hermitian Part: Determinant One, Unitarity and the Rotation*. The coefficient basis is $e_t,\vec e_x,\vec e_y,\vec e_z$, with $\vec e_x\vec e_y=\vec e_z$, $\vec e_y\vec e_z=\vec e_x$, $\vec e_z\vec e_x=\vec e_y$ and $\vec e_k^{2}=-e_t$.

## The Two Conditions on the Element

### Anti-Hermitian and Scalar-Free

An element is $Q=Q_te_t+\vec Q$, with $\vec Q=q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$. The Hermitian conjugation reverses the vector coefficients and conjugates all four,

$$
Q^{*}=\bar Q_te_t-\bar q_x\vec e_x-\bar q_y\vec e_y-\bar q_z\vec e_z ,
$$

and the anti-Hermitian sign is its negative, $Q^{\flat}=-Q^{*}$.

**Proposition (the anti-Hermitian elements).** The condition $Q^{*}=-Q$ holds exactly when $Q_t$ is purely imaginary and $q_x,q_y,q_z$ are real. These elements form $\mathbb{B}_{\Phi}$, of real dimension four.

**Proof.** The scalar coefficient of $Q^{*}+Q$ is $\bar Q_t+Q_t$, so the condition is the vanishing of the real part of $Q_t$. The vector coefficient of $\vec e_k$ is $-\bar q_k+q_k$, so the condition is the vanishing of the imaginary part of each $q_k$. The four free real parameters are $\operatorname{Im}Q_t$ and the three $q_k$.

**Proposition (the scalar-free part).** Add $Q_t=0$. The two conditions then hold exactly for the real vectors

$$
v=q_x\vec e_x+q_y\vec e_y+q_z\vec e_z,\qquad q_x,q_y,q_z\in\mathbb{R},
$$

which form $\mathbb{B}_{\Phi}\cap\mathbb{B}_{V}$, of real dimension three.

**Proof.** With $Q_t=0$ the scalar condition holds, and the vector condition is the reality of the three coefficients.

**Remark (the two conditions are independent over $\mathbb{C}$ and nested over $\mathbb{R}$).** The element $ie_t$ is anti-Hermitian and not scalar-free, so the second condition does not follow from the first over $\mathbb{C}$. Over $\mathbb{R}$ the scalar part of an anti-Hermitian element is real and purely imaginary at once, so it vanishes, and the second condition is automatic. The circle $i\mathbb{R}e_t$ is the direction that only the complex algebra adds.

**Remark (the names).** On an element the second condition is not a trace. *Algebra and Element Conventions* fixes the element-level name, *scalar-free*, and the trace symbol appears only on a named array. The operator that carries the condition is the inner derivation, and its condition is the Leibniz rule. The ladder of subspaces is

| object | condition one | condition two | real dimension |
|---|---|---|---|
| $\mathbb{B}$ | none | none | $8$ |
| $\mathbb{B}_{V}$, the vectors | none | $Q_t=0$, scalar-free | $6$ |
| $\mathbb{B}_{\Phi}$, the anti-Hermitian elements | $Q^{*}=-Q$ | none | $4$ |
| $\mathbb{B}_{\Phi}\cap\mathbb{B}_{V}$, the real vectors | $Q^{*}=-Q$ | $Q_t=0$ | $3$ |

The two middle rows are of different kinds. $\mathbb{B}_{V}$ is a complex subspace, of real dimension six; $\mathbb{B}_{\Phi}$ is a real subspace, of real dimension four. They meet in the real vectors, of real dimension three, so their sum has real dimension

$$
6+4-3=7 ,
$$

and it misses exactly one direction, the real scalar line $\mathbb{R}e_t$. So the algebra is the sum plus that line, $8=7+1$, and the five numbers $8,6,4,3,7$ are consistent with each other. A reader who adds the two middle rows without subtracting the intersection gets $10$ and must not: the two subspaces are not complementary, and their sum is not the whole algebra.

### The Element Exponential

**Proposition (the rotor).** For a real vector $v$ of norm $r$, with $\hat v=v/r$,

$$
e^{\theta v}=\cos(\theta r)\,e_t+\sin(\theta r)\,\hat v ,
$$

a unit element of the algebra.

**Proof.** $v^{2}=-r^{2}e_t$, so the series splits into the even part $\cos(\theta r)e_t$ and the odd part $\sin(\theta r)v/r$. The norm of the sum is $\cos^{2}+\sin^{2}=1$ because the scalar part and the vector part are orthogonal for the norm form.

**Corollary.** The element $\rho=e^{\theta v}$ is a rotor. Its $2\times2$ image is unitary of determinant one, and its conjugation action on the vector part is the rotation of angle $2\theta r$ about $\hat v$.

**Proof.** The image of a unit element is unitary and its determinant is the norm. The double angle is *The Rotor as a Square Root of a Rotation: the Two Signs and the Double Cover*.

## The Three Generators

**The normalization.** The corpus writes the basis of the derivation algebra as $D_\mu=\tfrac12\mathrm{ad}_{\vec e_\mu}$, so that the structure constants come out as $\epsilon_{\mu\nu\lambda}$; that is the convention of *Automorphisms and Derivations of Algebras*. The article follows it, and every array below is the array of $D_k$ rather than of $\mathrm{ad}_{\vec e_k}=2D_k$.

### The Arrays

**Definition.** The generator is

$$
D_k:=\tfrac12\bigl(L_{\mathrm{axf},\vec e_k}-R_{\mathrm{axf},\vec e_k}\bigr),
$$

the half-difference of the two axis-free matrices that *Matrix Representations and Conventions* prints. With the four coordinates read in the order $e_t,\vec e_x,\vec e_y,\vec e_z$,

$$
D_x=\begin{pmatrix}0&0&0&0\\0&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},\quad
D_y=\begin{pmatrix}0&0&0&0\\0&0&0&1\\0&0&0&0\\0&-1&0&0\end{pmatrix},\quad
D_z=\begin{pmatrix}0&0&0&0\\0&0&-1&0\\0&1&0&0\\0&0&0&0\end{pmatrix}.
$$

**Proposition (the three arrays are complete).** The three are linearly independent over $\mathbb{R}$, each is anti-Hermitian and of zero trace, and together they span every anti-Hermitian derivation of the algebra.

**Proof.** The independence is read off the three disjoint $2\times2$ blocks, one per generator. Each block is real and antisymmetric, so each array is minus its transpose and has zero diagonal. For completeness: $(\mathrm{ad}_a)^{*}=\mathrm{ad}_{a^{*}}$, so an anti-Hermitian derivation has an anti-Hermitian generator, and the anti-Hermitian generators modulo the centre $i\mathbb{R}e_t$ are the three real vector directions; the factor $\tfrac12$ changes none of this.

**Remark (the first row and column vanish).** Every entry in the first row and the first column is zero, because the derivation kills the scalar line, $\mathrm{ad}_v(e_t)=0$. The scalar line is fixed by all three generators.

**Remark (the arrays are three of the fifteen of the next level).** With $\ell_k=L_{\mathrm{axf},\vec e_k}$ and $r_k=R_{\mathrm{axf},\vec e_k}$, the array is $D_k=\tfrac12(\ell_k-r_k)$, and the six matrices $\ell_k,r_k$ are the six real generators of $\mathfrak{su}(4)$ in *The Anti-Hermitian Derivations of $M_4(\mathbb{C})$ as $\mathfrak{su}(4)$*. So the three generators of this article are the anti-diagonal combinations of that six, and the reader who wants to see them inside the fifteen has only to subtract.

### The Bracket

**Proposition (the structure constants).** The bracket of the three generators is

| bracket | value |
|---|---|
| $[D_x,D_y]$ | $D_z$ |
| $[D_y,D_z]$ | $D_x$ |
| $[D_z,D_x]$ | $D_y$ |

**Proof.** The map $a\mapsto\mathrm{ad}_a$ is a Lie algebra homomorphism, and $[\mathrm{ad}_{\vec e_x},\mathrm{ad}_{\vec e_y}]=\mathrm{ad}_{[\vec e_x,\vec e_y]}=\mathrm{ad}_{2\vec e_z}=2\mathrm{ad}_{\vec e_z}$, because the basis vectors anticommute. Halving all three gives $[D_x,D_y]=D_z$, and the other rows are cyclic.

**Remark (where the factor two went).** The factor $2$ is a property of $\mathrm{ad}$ and not of the algebra: $[\vec e_x,\vec e_y]=2\vec e_z$ carries it, and the normalization $D_\mu=\tfrac12\mathrm{ad}_{\vec e_\mu}$ puts it away. Written with $\mathrm{ad}$ the table reads $[\mathrm{ad}_{\vec e_x},\mathrm{ad}_{\vec e_y}]=2\mathrm{ad}_{\vec e_z}$, which is the same statement.

### Each Generator Turns One Plane

**Proposition (the action on the basis).** The three generators act on the four basis elements by

| generator | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
|---|---|---|---|---|
| $D_x$ | $0$ | $0$ | $\vec e_z$ | $-\vec e_y$ |
| $D_y$ | $0$ | $-\vec e_z$ | $0$ | $\vec e_x$ |
| $D_z$ | $0$ | $\vec e_y$ | $-\vec e_x$ | $0$ |

**Proof.** Evaluate $vX-Xv$ on the four basis elements and halve. For the first row, $\vec e_x\vec e_y=\vec e_z$ and $\vec e_y\vec e_x=-\vec e_z$, so the half-difference is $\vec e_z$; and $\vec e_x\vec e_z=-\vec e_y$, $\vec e_z\vec e_x=\vec e_y$, so the half-difference is $-\vec e_y$. The other rows are the same computation permuted cyclically.

**Corollary (one plane each, unit rate).** Each generator fixes its own axis and turns the plane of the other two axes, with the coefficient $1$. In cyclic order $x\to y\to z\to x$ the generator $D_a$ is the quarter-turn of the plane spanned by the two following vectors.

**Proof.** The table shows the axis of $D_a$ fixed and the other two exchanged with the coefficients $\pm1$, which are the entries of the quarter-turn $R$ of that plane in the cyclic orientation.

**Remark (the vanishing planes).** The kernel of $D_x$ is the span of $e_t$ and $\vec e_x$, of complex dimension two. The other two generators have the analogous kernel. The intersection of the three kernels is the scalar line, and the sum of the three kernels is the whole algebra: a derivation sees only the part of an element that does not commute with the generator.

### The Derivation Algebra and Its Real Form

**Proposition (six and three).** The derivations of the algebra form a complex vector space of dimension three and a real Lie algebra of dimension six, isomorphic to $\mathfrak{sl}_2(\mathbb{C})$ as a real Lie algebra. The anti-Hermitian ones among them form the real form $\mathfrak{su}(2)$, of real dimension three.

**Proof.** The derivations of a full matrix algebra are the inner ones, and the inner ones are the algebra modulo its centre, of complex dimension $4-1=3$. Over $\mathbb{R}$ that is six. The anti-Hermitian condition selects the real vector directions by the corollary above, and the bracket of three real combinations closes with real constants by the bracket table.

## The Operator and Its Two Conditions

### The Derivation and the Leibniz Rule

**Proposition (Leibniz holds).** For all $X,Y$ in the algebra, $\mathrm{ad}_a(XY)=\mathrm{ad}_a(X)Y+X\,\mathrm{ad}_a(Y)$.

**Proof.** $aXY-XYa=(aX-Xa)Y+X(aY-Ya)$ after the two middle terms are inserted and cancelled. Associativity is the only input.

**Remark (the one-sided multipliers fail, exactly).** $L_v$ and $R_v$ are anti-Hermitian and have arrays of zero trace, and neither is a derivation. Take $v=\vec e_x$, $X=\vec e_y$, $Y=\vec e_z$. Then $XY=\vec e_x$ and $L_v(XY)=-e_t$, while $L_v(X)Y+XL_v(Y)=\vec e_z\vec e_z+\vec e_y(-\vec e_y)=-e_t+e_t=0$. The residual is $e_t$, of norm one. On the same triple $R_v$ fails by the same margin, and the commutator passes because the two failures are equal and opposite.

**Proposition (the adjoint rules).** For $\langle X,Y\rangle=\operatorname{Sc}(X^{*}Y)$ one has $(L_a)^{*}=L_{a^{*}}$, $(R_b)^{*}=R_{b^{*}}$ and $(\mathrm{ad}_a)^{*}=\mathrm{ad}_{a^{*}}$.

**Proof.** $\langle L_aX,Y\rangle=\operatorname{Sc}(X^{*}a^{*}Y)=\langle X,L_{a^{*}}Y\rangle$. On the right, $(Xb)^{*}=b^{*}X^{*}$, so $\langle Xb,Y\rangle=\operatorname{Sc}(b^{*}X^{*}Y)=\operatorname{Sc}(X^{*}Yb^{*})=\langle X,R_{b^{*}}Y\rangle$ by the cyclic invariance of the scalar part.

### The Dimension Ladder

| set | defining condition | real dimension |
|---|---|---|
| $\operatorname{End}(\mathbb{B})$, all operators | none | $32$ |
| anti-Hermitian operators | $F^{*}=-F$ | $16$ |
| derivations | Leibniz rule | $6$ |
| anti-Hermitian derivations | both | $3$ |
| the multipliers $L$ and $R$ | one side only | $14$ |

The last row counts the span of $L(\mathbb{B})$ and $R(\mathbb{B})$, which is $4+4-1=7$ complex dimensions because the two copies meet in the scalars, so $14$ real. The two sums in the table are not the same kind of count: the derivations are $6$ because the algebra has complex dimension four and loses its centre, and the real form is $3$ because the trace form is definite on the vector part.

**Remark (the ladder at a glance).** $32\to16\to3$ along the anti-Hermitian branch, $32\to6\to3$ along the derivation branch, and the two branches meet in the three. The anti-Hermitian branch is the larger one by far: unitarity of the exponential is a weak condition, and the Leibniz rule is the strong one.

## The Exponential of Each Generator

### The Closed Form

**Lemma (the square).** Let $v$ be a real vector of norm $r$, let $D_v=\tfrac12\mathrm{ad}_v$, and let $P$ be the orthogonal projection of the vector part onto the plane orthogonal to $v$. Then $D_v$ kills $\operatorname{span}\{e_t,v\}$ and $(D_v)^{2}=-r^{2}P$ on the plane.

**Proof.** $e_t$ is central and $v$ commutes with itself. On $w\perp v$ one has $\mathrm{ad}_v(w)=2v\times w$, so $D_v(w)=v\times w$, which stays in the plane; applying it twice gives $v\times(v\times w)=-r^{2}w$.

**Theorem (the exponential).** With $\hat v=v/r$ and $D_v=\tfrac12\mathrm{ad}_v$,

$$
e^{\theta D_v}=\mathrm{id}_{\,\operatorname{span}\{e_t,v\}}+\cos(\theta r)\,P+\sin(\theta r)\,(\hat v\times)P .
$$

**Proof.** The operator splits into its parts on two invariant subspaces, which commute; the first part is zero, and the second has square $-r^{2}$, so the series is the cosine and the sine of $\theta r$.

**Remark (the angle is the angle).** With the normalization $D_\mu=\tfrac12\mathrm{ad}_{\vec e_\mu}$ the parameter $\theta$ of the array is the angle through which the coordinate plane turns. With $\mathrm{ad}$ the same rotation reads $2\theta$, and with the element $\rho=e^{\theta v}$ it reads $2\theta r$. The three parameters differ by the two factors that the corpus puts into the normalization and into the double cover, and the array is the object whose angle is the plain one.

### The Three Rotors, Written Out

**Corollary (the three arrays, exponentiated).** With $c=\cos\theta$ and $s=\sin\theta$,

$$
e^{\theta D_x}=
\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&c&-s\\0&0&s&c\end{pmatrix},\quad
e^{\theta D_y}=
\begin{pmatrix}1&0&0&0\\0&c&0&s\\0&0&1&0\\0&-s&0&c\end{pmatrix},\quad
e^{\theta D_z}=
\begin{pmatrix}1&0&0&0\\0&c&-s&0\\0&s&c&0\\0&0&0&1\end{pmatrix}.
$$

**Proof.** Each generator is a block $R$ with $R$ the quarter-turn of a real plane, and $\exp(\theta R)=c\,\mathrm{I}_2+s\,R$ on that block, with the identity on the two fixed coordinates.

**Remark (read the three arrays against the table).** The $x$-generator leaves the $t$ and $x$ coordinates alone and moves the $(y,z)$ pair counterclockwise. The $y$-generator leaves $t$ and $y$ alone and moves the $(z,x)$ pair. The $z$-generator leaves $t$ and $z$ alone and moves the $(x,y)$ pair.

### What Each Generator Does

**Proposition (the rotor action, generator by generator).** Exponentiated, the three generators do the following.

| generator | fixed | turned | angle | rotor behind it |
|---|---|---|---|---|
| $D_x$ | $\mathbb{C}e_t$, $\mathbb{C}\vec e_x$ | plane of $\vec e_y,\vec e_z$ | $\theta$ | $e^{\tfrac{\theta}{2}\vec e_x}$ |
| $D_y$ | $\mathbb{C}e_t$, $\mathbb{C}\vec e_y$ | plane of $\vec e_z,\vec e_x$ | $\theta$ | $e^{\tfrac{\theta}{2}\vec e_y}$ |
| $D_z$ | $\mathbb{C}e_t$, $\mathbb{C}\vec e_z$ | plane of $\vec e_x,\vec e_y$ | $\theta$ | $e^{\tfrac{\theta}{2}\vec e_z}$ |

**Proof.** The fixed lines and the turned plane are the kernel and the non-trivial part of the lemma. The rotor is $e^{\theta v/2}$ with $v=\vec e_k$, which is the element whose derivation parameter is $\theta$, and whose angle on the vector plane is $\theta$ by the double cover.

**Corollary (the rotor is the conjugation).** $e^{\theta D_v}=\mathrm{Ad}_{\rho}$ with $\rho=e^{\theta v/2}$, and its array is the two-sided operator $T_{\rho,\rho^{-1}}=L_\rho R_{\rho^{-1}}$.

**Proof.** $L_vR_v=R_vL_v$, so $e^{\theta(L_v-R_v)/2}=L_{\rho}R_{\rho^{-1}}$ with $\rho=e^{\theta v/2}$, and that operator sends $X$ to $\rho X\rho^{-1}$.

**Remark (the periods, one for each object).** The array has period $2\pi$ in $\theta$, because $e^{2\pi D}=\mathrm{I}_4$; at $\theta=\pi$ it is $\operatorname{diag}(1,1,-1,-1)$ up to the choice of axis. The derivation $\mathrm{ad}$ has period $\pi$ in its own parameter, and the element $\rho=e^{\theta v/2}$ has period $4\pi$ in $\theta$ and period $2\pi$ in the element parameter. Three objects, three periods, and the one that is a sign is the element.

**Remark (the invariants of the array).** The spectrum of each generator is $\{0,0,i,-i\}$; the trace is zero; the exponential is unitary of determinant one and lies in $\mathrm{SU}(4)$.

**Proof.** The block $R$ has the eigenvalues $\pm i$ and the two fixed directions give the two zeros. The trace of a commutator vanishes, and $\det e^{F}=e^{\operatorname{tr}F}=1$.

### The Rotor Acts on the Four Parts

| part of the algebra | real dimension | under $\mathrm{Ad}_\rho$ |
|---|---|---|
| the scalar line $\mathbb{C}e_t$ | $2$ | fixed |
| the vector subspace $\mathbb{B}_{V}$ | $6$ | preserved |
| the line $\mathbb{C}v$ | $2$ | fixed |
| the plane orthogonal to $v$ in $\mathbb{B}_{V}$ | $4$ | turned by $\theta r$, and by $2\theta r$ on its complex structure |
| $\mathbb{B}_{\Psi}$, $\mathbb{B}_{\Phi}$ | $4$, $4$ | preserved |
| the quaternion and antiquaternion subspaces | $4$, $4$ | mixed, unless $\rho$ is real |

**Remark (why the complexification doubles again).** The plane orthogonal to $v$ inside $\mathbb{B}_{V}$ is complex, so it carries two real planes: the real coefficients and the imaginary ones. The rotation on each of them is $\theta r$, and the element rotor acts on the complex structure at twice that rate in the sense that the two real planes are turned together. A reader who wants a single number should take the real plane.

**Remark (what is not preserved).** The quaternion and antiquaternion subspaces are exchanged only for a special rotor. A rotor with a complex coefficient moves a real element into a complex one, so the real subspace of the algebra is not invariant under the full group; it is invariant under the real one-parameter subgroups only.

## The Orbits

**Proposition (the orbit of a vector is a sphere).** The conjugation action of the rotor group sends a vector $v$ of norm $r$ to any other vector of the same norm, so the orbit is the sphere of radius $r$ in the three real dimensions of the vector part.

**Proof.** Every rotation of the vector part is the conjugation by some rotor, by the surjectivity of $\mathrm{SU}(2)\to\mathrm{SO}(3)$, and the norm is preserved. So the orbit is the set of vectors of norm $r$, which is a two-sphere.

**Corollary (the dimension count).** The orbit has real dimension $2$, the stabiliser of a non-zero vector is the circle about it, of real dimension $1$, and $3=2+1$ matches the dimension of the group.

**Proof.** The stabiliser is the set of rotors commuting with $v$, which is the circle $\{e^{\theta v}\}$. The orbit-stabiliser identity gives $3-1=2$.

**Remark (the operator level has a different orbit).** On the operator space, of complex dimension sixteen and real dimension thirty-two, the conjugation by $\mathrm{SU}(4)$ has orbits of real dimension $12$ for a generic element, with stabiliser the three-dimensional torus and group of real dimension fifteen. The sphere of the vector part is the orbit of the smallest representation, and the orbit of the algebra itself is the largest one that the three generators produce.

## The Two Conditions, Compared

| condition | set | real dimension | what it buys |
|---|---|---|---|
| anti-Hermitian | $\mathfrak{u}(4)$ of the array | $16$ | the exponential is unitary |
| derivation | the inner derivations | $6$ | the exponential is a conjugation |
| both | $\mathfrak{su}(2)$ of derivations | $3$ | the exponential is a conjugation by a norm-one element |

**Remark (the determinant is free on the derivation branch).** $\operatorname{tr}\mathrm{ad}_v=0$ for every $v$, so $\det e^{\mathrm{ad}_v}=1$ with no hypothesis. The determinant is not free one row up: the operator $i\,\mathrm{id}$ is anti-Hermitian, its array has trace $4i$, and the determinant of its exponential is $e^{4i}=-0.654-0.757i$. So the derivation condition is what makes the exponential special, and it is the only condition that does so.

## Summary

The anti-Hermitian scalar-free elements are the real vectors, of real dimension three, and their exponential is the rotor $\cos(\theta r)e_t+\sin(\theta r)\hat v$. Each vector gives the inner derivation $\mathrm{ad}_v=L_v-R_v$, which satisfies the Leibniz rule and is anti-Hermitian for the Hermitian form.

The three unit generators are the three real directions, written $D_k=\tfrac12\mathrm{ad}_{\vec e_k}$, and their arrays are the quarter-turn $R$ of one coordinate plane each, with the scalar line and the axis of the generator killed. Their bracket is $[D_x,D_y]=D_z$, and with real coefficients they form $\mathfrak{su}(2)$, of real dimension three inside the six of all derivations and the thirty-two of all operators.

Exponentiated, each generator fixes the scalar line and its own axis and turns the plane of the other two axes by the parameter. The exponential is the conjugation by the rotor $e^{\theta\vec e_k/2}$, of array $T_{\rho,\rho^{-1}}$, unitary of determinant one, of spectrum $\{0,0,\pm i\}$ and of period $2\pi$ in the parameter. The rotor moves a vector along its sphere, of real dimension two, and the stabiliser of a vector is the circle about it.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | the coefficient basis, with $\vec e_k^2=-e_t$ |
| $\mathbb{B}_{\Phi}$ | the anti-Hermitian elements, $Q^{*}=-Q$, real dimension $4$ |
| $\mathbb{B}_{V}$ | the vectors, $Q_t=0$, complex dimension $3$ |
| $L_a$, $R_b$ | left and right multiplication |
| $T_{a,b}$ | the two-sided operator $X\mapsto aXb$ |
| $\mathrm{ad}_a$ | the inner derivation $L_a-R_a$ |
| $\langle X,Y\rangle$ | the Hermitian form $\operatorname{Sc}(X^{*}Y)$ |
| $R$ | the quarter-turn $\begin{pmatrix}0&-1\\1&0\end{pmatrix}$ on a coordinate plane |
| $\rho$ | the rotor $e^{\theta v}$ |
| $\mathrm{Ad}_\rho$ | the conjugation $X\mapsto\rho X\rho^{-1}$ |
| $P$ | the projection onto the plane orthogonal to the generator |

## Further Reading

- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations* (Springer, 2015), for derivations, inner automorphisms and the exponential.
- John Stillwell, *Naive Lie Theory* (Springer, 2008), for the double cover and the unit quaternions.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge University Press, 2003), for the rotor and the double angle.
- [The Anti-Hermitian Derivations of $M_2(\mathbb{C})$ as $\mathfrak{su}(2)$](the-anti-hermitian-derivations-of-m2c-as-su2.html), for the same three generators in the matrix frame and the sign of the angle.
- [The Exponential of the Traceless Anti-Hermitian Part: Determinant One, Unitarity and the Rotation](the-exponential-of-the-traceless-anti-hermitian-part-determinant-one-unitarity-and-the-rotation.html), for the element-level theorem.
- [The Rotor as a Square Root of a Rotation: the Two Signs and the Double Cover](the-rotor-as-a-square-root-of-a-rotation-the-two-signs-and-the-double-cover.html), for the doubling of the angle.
- [Adjoint Pair of $L$ and $R$ Operators](adjoint-pair-of-l-and-r-operators.html), for the four adjoints.
- [The Anti-Hermitian Derivations of the Operators of the Biquaternion Algebra as $\mathfrak{su}(4)$](the-anti-hermitian-derivations-of-the-operators-of-the-biquaternion-algebra-as-su4.html), for the same construction one level up.
