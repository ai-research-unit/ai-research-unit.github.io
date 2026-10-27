# __The Polar Decomposition in Subspaces__

## Introduction

Each of the remarkable subspaces is a physical sector of the framework, and the polar decomposition behaves differently on each. The polar decomposition of a biquaternion,

$$
\tilde{Q} = r\,\exp(i\alpha)\,B\,\tilde q , \qquad r\in\mathbb{R}_{>0}, \quad \alpha\in\left(-\tfrac{\pi}{2},\tfrac{\pi}{2}\right], \quad B\in\mathbb{M}_+, \quad \tilde q\in\mathrm{Sp}(1) ,
$$

decomposes a general element of the algebra into a positive scale, a central phase, a Hermitian positive factor and a rotor. The companion article *The Polar Decomposition of Biquaternions* reads the four factors on the Lorentz group and on the four-vector. This article restricts the same representation to the **remarkable subspaces** of *The Biquaternion Space, the Group of Involutions and the Six Subspaces* and records what the restriction does to the four factors.

The restriction is not a cosmetic exercise, because each subspace is the fixed space of one of the algebra's involutions, and each involution constrains the factors in a different way. Two of the factors are always the modulus of the biquaternion norm, and the biquaternion norm on a subspace takes one of five forms — positive definite, negative definite, real indefinite, complex anisotropic, complex indefinite — and its argument is what the phase measures. The other two factors are the positive Hermitian square root of $\tilde{Q}\tilde{Q}^{*}$ and the unitary part of $\tilde{Q}/\rho$, and the subspaces are exactly the cases in which one of those two products degenerates. The restrictions therefore say which of the four factors a subspace is able to carry, and the answer is that no subspace carries all four freely:

| subspace | real dim | biquaternion norm | phase | boost | rotor |
|---|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ — centre | 2 | complex, anisotropic | free | $e_t$ | $\pm e_t$ |
| $\mathrm{Vect}(\mathbb{B})$ — vector subspace | 6 | complex, indefinite | free | boost about $\vec q\times\vec q'$ | unit vector in the plane of $\vec q$ and $\vec q'$ |
| $\mathbb{H}_{\mathbb{B}}$ — quaternions | 4 | positive definite | $0$ | $e_t$ | free in $\mathrm{Sp}(1)$ |
| $i\mathbb{H}_{\mathbb{B}}$ — antiquaternions | 4 | negative definite | $\pi/2$ | $e_t$ | free in $\mathrm{Sp}(1)$ |
| $\mathbb{M}_+$ — informational sector | 4 | real, indefinite | $0$ or $\pi/2$ | the boost, explicit | $\pm e_t$ or a direction |
| $\mathbb{M}_-$ — material sector | 4 | real, indefinite | $0$ or $\pi/2$ | the boost, explicit | $\pm e_t$ or a direction |

The conventions are those of *Conventions in the Biquaternion Universe*.

- **The basis.** $e_t = 1$ the algebra unit and $\vec e_x,\vec e_y,\vec e_z$ the quaternion units with $\vec e_k^2 = -e_t$ and $\vec e_x\vec e_y = \vec e_z$, so an element is written $\tilde{Q} = \sum_{\mu\in\{t,x,y,z\}} Q_\mu e_\mu$ with coefficients $Q_\mu \in \mathbb{C}$.
- **The scalar imaginary.** $i$, central, with $i^2 = -1$.
- **The norm.** $\langle\tilde{Q}\rangle_{\natural} = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = \sum_\mu Q_\mu^2 = \det\mathsf{M}_2(\tilde{Q})$ with $\mathsf{M}_2(e_t) = I$, $\mathsf{M}_2(\vec e_k) = -i\sigma_k$, $\mathsf{M}_2(i) = iI$; write $N=\langle\tilde Q\rangle_{\natural}$ for the norm.
- **The subspaces.**
    - $\mathbb{C}_{\mathbb{B}}$, the centre;
    - $\mathrm{Vect}(\mathbb{B})$, the kernel of the scalar part;
    - $\mathbb{H}_{\mathbb{B}}$, the fixed space of complex conjugation, the home of the rotations, whose unit sphere is $\mathrm{Sp}(1) = \{\tilde q \in \mathbb{H}_{\mathbb{B}} : \tilde q\tilde q^{\natural} = 1\}$, the group of unit real quaternions;
    - $i\mathbb{H}_{\mathbb{B}}$, the anti-fixed space of complex conjugation, its imaginary half;
    - $\mathbb{M}_+$, the fixed space of Hermitian conjugation, the home of the boosts;
    - $\mathbb{M}_-$, the anti-fixed space of Hermitian conjugation, with $Q_t = iq'_t$ and $Q_k$ real, the home of the four-vectors.

Every numerical value below was recomputed in double precision; the residuals of the identities quoted are below $2\times10^{-12}$. An element is **unitary** when it preserves the form, $\tilde{Q}\tilde{Q}^{*}=e_t$, and the unitary elements form the group $\mathrm{U}(\mathbb{B})\cong \mathrm{U}(2)$; the condition is narrower than norm one, the norm-one group being $\mathbb{B}^{\times}_1=\{N=e_t\}\cong SL(2,\mathbb{C})$ (*Conventions in the Biquaternion Universe*, §*The Unitary Convention*).

The restrictions are taken one at a time in the sections that follow, in the order in which the framework names the subspaces — centre, vector, quaternion, antiquaternion, informational, material — and each part is built the same way: it opens with the element and its biquaternion norm, states which of the four factors survive, gives the surviving factors explicitly, and closes with worked examples. Where a subspace's defining condition needs a computation of its own — the boost axis and the orthogonality of the rotor in the vector subspace, the two branches of each sector — that computation is a subsection of the part. Three further sections close the article, each a comparison across all six: the biquaternion norm as the single object that decides the phase, the count of the dimensions each factor accounts for, and the four coordinate blocks, on which the restrictions have to agree element by element.

## The Exponentials of the Four Factors

The word restricted in this article is the ordered product of four exponentials. In the physics normalisation of *The Polar Decomposition of Biquaternions*, with the rapidity $\psi \in \mathbb{R}$, $\psi \ge 0$, the boost direction $\vec u_{\mathrm b} \in \mathcal{A}$ (a unit pure real quaternion, $\vec u_{\mathrm b} = \vec v/|\vec v|$), and the rotation angle $\theta \in [0,2\pi]$ about the unit axis $\vec u_{\mathrm r} \in \mathcal{A}$ (the axis sphere, the unit vectors of $\mathbb{R}^3$),

$$
\tilde{Q} = \exp(\ln r)\,\exp(i\alpha)\,\exp(-i\psi\vec u_{\mathrm b})\,\exp\Bigl(\tfrac{\theta}{2}\vec u_{\mathrm r}\Bigr) .
$$

| # | factor | name | real dimension | exponential | case | closed form | parameter and range | unit axis |
|---|---|---|---|---|---|---|---|---|
| 1 | $r$ | scale | $1$ | $\exp(\ln r)$ | hyperbolic | $r$ | $\ln r \in \mathbb{R}$, $r > 0$ | $\mathbb{R}e_t$ |
| 2 | $\exp(i\alpha)$ | central phase | $1$ | $\exp(i\alpha)$ | trigonometric | $\cos\alpha\,e_t + i\sin\alpha$ | $\alpha \in \left(-\frac{\pi}{2},\frac{\pi}{2}\right]$ | $i\mathbb{R}$ |
| 3 | $B$ | boost factor | $3$ | $\exp(-i\psi\vec u_{\mathrm b})$ | hyperbolic | $\cosh\psi\,e_t - i\sinh\psi\,\vec u_{\mathrm b}$ | rapidity $\psi \in \mathbb{R}$, $\psi \ge 0$ | $\vec u_{\mathrm b} \in \mathcal{A}$ |
| 4 | $\tilde q$ | rotor | $3$ | $\exp\bigl(\tfrac{\theta}{2}\vec u_{\mathrm r}\bigr)$ | trigonometric | $\cos\tfrac{\theta}{2}\,e_t + \sin\tfrac{\theta}{2}\,\vec u_{\mathrm r}$ | rotation angle $\theta \in [0,2\pi]$ | $\vec u_{\mathrm r} \in \mathcal{A}$ |

Each exponent is a real parameter times a **root** of the algebra, and the square of that root decides the character of the exponential. For a root $\nu \in \mathbb{B}$ and a real $t \in \mathbb{R}$,

- the trigonometric case $\nu^2 = -e_t$ gives $\cos t\,e_t + \nu\sin t$;
- the parabolic case $\nu^2 = 0$ gives the truncation $e_t + \nu t$;
- the hyperbolic case $\nu^2 = +e_t$ gives $\cosh t\,e_t + \nu\sinh t$.

The four exponents are

- the scale exponent $\ln r$ ($r \in \mathbb{R}$, $r>0$), the real root $e_t$ of $+e_t$;
- the phase exponent $i\alpha$ ($\alpha \in (-\tfrac{\pi}{2},\tfrac{\pi}{2}]$), the central root $i$ of $-e_t$;
- the boost exponent $-i\psi\vec u_{\mathrm b}$, the Hermitian root $-i\vec u_{\mathrm b}$ of $+e_t$;
- the rotor exponent $\tfrac{\theta}{2}\vec u_{\mathrm r}$, the real pure root $\vec u_{\mathrm r}$ of $-e_t$.

The first two exponents are central, and the last two are not, so the word is ordered.

A remarkable subspace is a condition on the element, and the condition reads as a constraint on the four exponents: it forces one or two of the parameters to a value, or freezes one of the roots. The table of the Introduction records the result of each restriction, and the sections below compute it.

- **Centre.** The two non-central exponents are absent, the boost exponent being $0$ and the rotor exponent a discrete $\{0,\pi\}$.
- **Quaternion subspace.** The phase and the boost exponents vanish, leaving the free rotor exponent.
- **Antiquaternion subspace.** The phase exponent is frozen at $i\pi/2$.
- **Vector subspace.** The boost and the rotor exponents are tied to the same two directions.
- **The two sectors.** The phase exponent is frozen and the boost exponent is the explicit one of the element.

In every case the restriction is the statement that a subspace carries a subset of the four rows of the exponential rule, and the exponential rule is what the restriction acts on.

**The restriction does not repair the non-commutativity.** The boost exponent and the rotor exponent do not commute in general, so on a subspace that carries both non-trivially — the vector subspace above all — the order of the two exponents is part of the word and the two may not be fused into one. The restriction acts on the exponents, not on the commutation of the algebra, and the subspace whose defining condition makes the two axes parallel is exactly the subspace on which the two exponents do commute.

## The Four Factors and the Two Criteria

### The Factors in Terms of Two Products

The representation is constructed in two steps, and each step produces two factors. First the modulus is extracted, with

$$
\rho = r\exp(i\alpha) = \sqrt{\langle\tilde{Q}\rangle_{\natural}}, \qquad r = \left|\det\mathsf{M}_2(\tilde{Q})\right|^{1/2}, \qquad \alpha = \tfrac12\arg\det\mathsf{M}_2(\tilde{Q}) ,
$$

the principal branch of the square root fixing the pair $(r,\alpha)$ uniquely. The remaining element $U = \tilde{Q}/\rho$ has unit norm, and its polar decomposition is the Cartan decomposition

$$
U = B\,\tilde q , \qquad B = \sqrt{UU^{*}}, \qquad \tilde q = B^{-1}U ,
$$

with $B$ the unique Hermitian positive square root. In terms of the element itself,

$$
\boxed{\;B = \frac{\sqrt{\tilde{Q}\tilde{Q}^{*}}}{r} , \qquad \tilde q = B^{-1}\frac{\tilde{Q}}{\rho} , \qquad \tilde{Q}\tilde{Q}^{*} = r^2B^2\;}.
$$

The last identity is the one that decides the whole of what follows, because it shows that the boost factor is a scalar exactly when the product $\tilde{Q}\tilde{Q}^{*}$ is one.

### Criterion for the Boost Factor

**The boost factor is trivial, $B = e_t$, if and only if $\tilde{Q}\tilde{Q}^{*}$ is a positive real multiple of the unit.**

*Proof.* Let $\tilde{Q}\tilde{Q}^{*} = ce_t$ with $c > 0$. Then $B^2 = (c/r^2)e_t$, a positive real multiple of the unit; the unique Hermitian positive square root of such an element is the positive real multiple $\sqrt{c/r^2}\,e_t$ of the unit, and $\langle B\rangle_{\natural} = 1$ forces $\sqrt{c/r^2} = 1$ and $B = e_t$. Conversely $B = e_t$ gives $\tilde{Q}\tilde{Q}^{*} = r^2e_t$.

In the matrix picture the criterion reads $\mathsf{M}_2(\tilde{Q})\mathsf{M}_2(\tilde{Q})^\dagger = \lambda I$ with $\lambda > 0$: the boost factor is trivial exactly when the element is, up to a scale, a **unitary** matrix rather than a general invertible one. That is a condition on the element alone, and it is satisfied on three of the remarkable subspaces for every element — the centre and the two halves — on the vector subspace only for a parallel pair, and on the two sectors only in the two exceptional cases computed below.

### Criterion for the Rotor

**The rotor is a central sign, $\tilde q = \pm e_t$, if and only if $\tilde{Q}/\rho$ is Hermitian**, equivalently if and only if $\tilde{Q} = \pm\rho B$ for a Hermitian positive $B$ of unit norm.

*Proof.* If $\tilde q = \pm e_t$ then $\tilde{Q}/\rho = \pm B$ is Hermitian. Conversely let $\tilde{Q}/\rho = \tilde H$ be Hermitian of biquaternion norm one; then $\tilde H$ is either positive definite or negative definite, so $\tilde H = B$ or $\tilde H = -B$ with $B$ Hermitian positive of biquaternion norm one, and therefore $\tilde q = e_t$ or $\tilde q = -e_t$.

The rotor is thus the part of the element that obstructs its being a complex multiple of a Hermitian element, and the central sign $\pm e_t$ is the discrete residue of that obstruction, which is the kernel of the two-to-one cover of the Lorentz group.

### The Two Classes the Criteria Single Out

Each criterion is one condition, and each condition cuts a class out of the nonzero elements of the algebra: those whose product with their star is a positive real multiple of the unit, and those whose quotient by the modulus is Hermitian.

| class | defining condition | factorization | real dimension |
|---|---|---|---|
| $\mathcal{U}$, the boost-free elements | $B = e_t$ | $\tilde{Q} = r\,\exp(i\alpha)\tilde q$ | $1+1+3 = 5$ |
| $\mathcal{H}$, the rotor-free elements | $\tilde q = \pm e_t$ | $\tilde{Q} = \pm\rho B$ | $2+3 = 5$ |

The two counts are the ones the section *Where the Dimensions Go* distributes over the four factors, read the other way round: an element of $\mathcal{U}$ spends its real dimensions on a scale, a phase and a rotor, and an element of $\mathcal{H}$ on a complex modulus and a boost.

The two classes are not the same kind of object. $\mathcal{U}$ is closed under multiplication and under inversion, since a product of two positive multiples of unitary elements is again one, so it is a group — $\mathbb{R}_{>0}\times \mathrm{U}(2)$, with the central phase as its circle and the rotor group as its three-sphere. $\mathcal{H}$ is not closed: $\mathsf{M}_2(\tilde{Q}_1\tilde{Q}_2)$ is a product of two Hermitian positive definite matrices, and such a product is Hermitian exactly when the two factors commute, so two boosts about different axes leave the class as soon as they are composed, and only co-axial ones stay in it.

Read on the remarkable subspaces, the membership follows from the same two products. The centre lies in both classes. The quaternion and antiquaternion subspaces lie inside $\mathcal{U}$ and meet $\mathcal{H}$ only in the centre, since every element of those halves has a real biquaternion norm and hence a trivial boost factor, and a nontrivial rotor. The vector subspace lies inside $\mathcal{U}$ exactly on the parallel pairs $\vec q\parallel\vec q'$ and never inside $\mathcal{H}$ away from the centre. And a sector lies inside $\mathcal{H}$ exactly on its definite branch, the branch on which the rotor is the discrete sign, and inside $\mathcal{U}$ only on the centre and on the line $a = 0$, the line on which its Hermitian product degenerates to a scalar.

### The Two Classes Meet in the Centre

An element of both classes has $B = e_t$ and $\tilde q = \pm e_t$, hence $\tilde{Q} = \pm\rho e_t = \pm r\exp(i\alpha)e_t$, so the intersection is the nonzero part of the centre,

$$
\boxed{\;\mathcal{U}\cap\mathcal{H} = \mathbb{C}_{\mathbb{B}}\setminus\{0\} , \qquad \dim_{\mathbb{R}}\left(\mathcal{U}\cap\mathcal{H}\right) = 2\;}.
$$

The count closes against the group of units, whose real dimension is $8$: $5+5-8 = 2$. The two conditions are therefore as independent as the ambient group allows, and the two five-dimensional families meet on the complex line and nowhere else. On the unit-norm slice the classes become the two factors of the Cartan decomposition — $\mathcal{U}\cap\{N = 1\}$ is the rotor group $\mathrm{Sp}(1)$ and $\mathcal{H}\cap\{N = 1\}$ is the boosts with a discrete sign — and their intersection there is the two-element group $\{\pm e_t\}$, the kernel of the double cover. The slice is thus the one place where the two criteria can be read against each other: the rotor and the boost factor are its two halves, and the only element of the slice on which both halves are trivial is the discrete unit $\pm e_t$.

### The Matrix Image of Each Subspace

The matrix representative makes the criteria computable at a glance. With $\mathsf{M}_2(\vec e_k) = -i\sigma_k$,

| subspace | $\mathsf{M}_2(\tilde{Q})$ | class of matrix |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $zI$ | scalar |
| $\mathrm{Vect}(\mathbb{B})$ | $\left(w_k - i v_k\right)\sigma_k$ | traceless |
| $\mathbb{H}_{\mathbb{B}}$ | $q_tI - i q_k\sigma_k = \begin{pmatrix} a & b \\ -\bar{b} & \bar{a}\end{pmatrix}$ | quaternionic |
| $i\mathbb{H}_{\mathbb{B}}$ | $i q_tI + q_k\sigma_k$ | $i$ times quaternionic |
| $\mathbb{M}_+$ | $aI + w_k\sigma_k$ | Hermitian |
| $\mathbb{M}_-$ | $i\left(aI - v_k\sigma_k\right)$ | $i$ times Hermitian |

All six classes are closed under the map $\tilde{Q}\mapsto\tilde{Q}\tilde{Q}^{*}$, and the resulting matrices are what the following sections compute.

## The Centre Subspace $\mathbb{C}_{\mathbb{B}}$: the Modulus and the Free Phase

### The Element and Its Biquaternion Norm

The centre is the set of complex scalars, $\tilde{Q} = ze_t$ with $z\in\mathbb{C}$, $z\neq0$. It is two-dimensional over the reals, and its biquaternion norm is the complex anisotropic form

$$
\langle\tilde{Q}\rangle_{\natural} = z^2 , \qquad r = |z| ,
$$

whose argument is $2\arg z$. The biquaternion norm vanishes only at $z = 0$: the centre carries no zero divisor other than the origin, and the representation is defined on $\mathbb{C}_{\mathbb{B}}\setminus\{0\}$.

### Which Factors Survive

Both criteria apply automatically. Since $\tilde{Q}\tilde{Q}^{*} = |z|^2e_t$ is a positive scalar, the first criterion gives the trivial boost $B = e_t$, and since $\tilde{Q}/\rho = (z/\rho)e_t$ is a real multiple of the unit, the second criterion gives a rotor that is a central sign, $\tilde q = \pm e_t$. The four factors therefore collapse to two numbers, the scale and the phase, which are the only factors with a continuous range:

$$
ze_t = \rho\,(\pm e_t) , \qquad \rho = \sqrt{z^2} , \qquad r = |z| , \qquad \alpha \equiv \arg z \ (\mathrm{mod}\ \pi)\ \text{taken in}\ \left(-\tfrac{\pi}{2},\tfrac{\pi}{2}\right] ,
$$

### The Explicit Factors

The rotor carries the sign of the element. With $\tilde q = z/\rho$, that is

$$
\tilde q = \frac{z}{\rho} = \begin{cases} +e_t , & \arg z\in\left(-\tfrac{\pi}{2},\tfrac{\pi}{2}\right] , \\ -e_t , & \arg z\in\left(\tfrac{\pi}{2},\pi\right]\cup\left(-{\pi},-\tfrac{\pi}{2}\right] ,\end{cases}
$$

the two lines being $\rho = z$ and $\rho = -z$. The polar decomposition of a biquaternion in the centre is therefore the polar form of the complex number $z$: the phase is **free**, and it is the argument of the element itself, taken modulo the branch of $\pi$. The two rotors have nothing to act on and reduce to the element $-e_t$ of the kernel of the two-to-one map, and the boundary case $\arg z = -\pi/2$ is the one on which the branch matters: for $\tilde{Q} = -2ie_t$ the phase is pulled from $-\pi/2$ to $+\pi/2$ and the sign is carried by the rotor.

The matrix statement is the same one: $\mathsf{M}_2(\tilde{Q}) = zI$ is a scalar matrix, its positive Hermitian polar factor is $|z|I$, and the unitary polar factor is the number $z/|z|$ read as $\pm I$ after the branch of the square root has absorbed the sign.

### Worked Examples

| example | $N = z^2$ | $r = |z|$ | $\alpha$ | $B$ | $\tilde q$ |
|---|---|---|---|---|---|
| $\tilde{Q} = (1+i)e_t$ | $2i$ | $1.414213562$ | $0.785398163$ | $e_t$ | $e_t$ |
| $\tilde{Q} = -e_t$ | $1$ | $1$ | $0$ | $e_t$ | $-e_t$ |
| $\tilde{Q} = 2ie_t$ | $-4$ | $2$ | $1.570796327$ | $e_t$ | $e_t$ |
| $\tilde{Q} = -2ie_t$ | $-4$ | $2$ | $1.570796327$ | $e_t$ | $-e_t$ |

In the first row $\rho = 1+i$, the principal square root of $2i$, and $\alpha = \pi/4$; in the second row $\rho = 1$ and the sign of $z$ is carried by $\tilde q$; in the third and fourth rows $\rho = 2i$ and the phase is the angle $\pi/2$ that turns the unit into the imaginary unit, the two rows differing by the sign of the rotor.

## The Vector Subspace $\mathrm{Vect}(\mathbb{B})$: the Rotor Relative to the Boost

### The Element and Its Biquaternion Norm

The vector subspace is the kernel of the scalar part, of real dimension six. Written with two real vectors, the element and its biquaternion norm are

$$
\tilde{Q} = \vec q + i\,\vec q' , \qquad \vec q,\vec q'\in\mathbb{R}^3 , \qquad \langle\tilde{Q}\rangle_{\natural} = |\vec q|^2 - |\vec q'|^2 + 2i\,\vec q\cdot\vec q' , \qquad \operatorname{Sc}(\tilde{Q}) = 0 .
$$

The biquaternion norm is complex and indefinite, so the phase is free here exactly as it is on the centre; the norm vanishes on the four-dimensional complex null cone $|\vec q| = |\vec q'|$, $\vec q\cdot\vec q' = 0$, and the representation is defined on the complement of that cone. In the matrix picture the subspace is the traceless class, $\mathsf{M}_2(\tilde{Q}) = \left(w_k - iv_k\right)\sigma_k$.

### Which Factors Survive

Neither criterion applies automatically, and both factors are genuinely present:

$$
\tilde{Q}\tilde{Q}^{*} = \left(|\vec q|^2 + |\vec q'|^2\right)e_t + 2i\left(\vec q\times\vec q'\right) ,
$$

which is a positive scalar only when $\vec q\times\vec q' = 0$. Hence the boost factor is trivial **exactly when the two vectors are parallel**, and in that case $\tilde{Q} = z\vec u_q$ with $z = |\vec q|\pm i|\vec q'|$ according to the relative sign, so the element is a complex multiple of a single real direction, $\langle\tilde{Q}\rangle_{\natural} = z^2$, and on the line $\mathbb{R}\{\vec q\}$ the representation is the representation of the centre. When the two vectors are not parallel the boost factor is

$$
B = \frac{\sqrt{\left(|\vec q|^2+|\vec q'|^2\right)e_t + 2i\left(\vec q\times\vec q'\right)}}{\sqrt{|\langle\tilde{Q}\rangle_{\natural}|}} = \cosh\varphi\,e_t + i\sinh\varphi\,\frac{\vec q\times\vec q'}{|\vec q\times\vec q'|} ,
$$

a boost about the axis $\vec q\times\vec q'$, with the rapidity fixed by

$$
\cosh 2\varphi = \frac{|\vec q|^2+|\vec q'|^2}{\left|\langle\tilde{Q}\rangle_{\natural}\right|} , \qquad \sinh 2\varphi = \frac{2\left|\vec q\times\vec q'\right|}{\left|\langle\tilde{Q}\rangle_{\natural}\right|} , \qquad \cosh^2 2\varphi - \sinh^2 2\varphi = 1 ,
$$

the last identity being the Lagrange identity $\left(|\vec q|^2+|\vec q'|^2\right)^2 - 4\left|\vec q\times\vec q'\right|^2 = |\langle\tilde{Q}\rangle_{\natural}|^2$, which is what makes the argument of the square root positive definite.

### The Rotor Is Orthogonal to the Boost Axis

The defining condition $\operatorname{Sc}(\tilde{Q}) = 0$ is a condition on the two factors. Write $\tilde{Q}^{\natural} = -\tilde{Q}$ and use the anti-automorphism property of quaternion conjugation, $\overline{AB} = \bar{B}\bar{A}$:

$$
\overline{\rho B\tilde q} = \bar{\tilde q}\,\bar{B}\,\rho = (-\tilde q)\left(\cosh\varphi\,e_t - i\sinh\varphi\,\vec u_{\mathrm b}\right)\rho = -\rho\,\tilde q\left(\cosh\varphi\,e_t - i\sinh\varphi\,\vec u_{\mathrm b}\right) ,
$$

and equating this to $-\rho\left(\cosh\varphi + i\sinh\varphi\,\vec u_{\mathrm b}\right)\tilde q$ gives

$$
\tilde q\,\vec u_{\mathrm b} = -\vec u_{\mathrm b}\,\tilde q \quad\Longleftrightarrow\quad -2\,\tilde q\cdot\vec u_{\mathrm b} = 0 \quad\Longleftrightarrow\quad \tilde q\perp\vec u_{\mathrm b} ,
$$

where $\vec u_{\mathrm b} = \vec q\times\vec q'/|\vec q\times\vec q'|$ is the boost axis. A pure unit vector orthogonal to $\vec u_{\mathrm b}$ lies in the plane orthogonal to $\vec u_{\mathrm b}$, and that plane is $\operatorname{span}(\vec q,\vec q')$, because $\vec q\cdot(\vec q\times\vec q') = 0$ and $\vec q'\cdot(\vec q\times\vec q') = 0$. The rotor is therefore a unit vector **in the plane spanned by $\vec q$ and $\vec q'$**, perpendicular to the boost axis. The two conditions are equivalent: the vanishing of the scalar part is the orthogonality of the rotor to the boost axis, and conversely. This is the exact sense in which the vector subspace exhibits the rotor relative to the boost rather than the rotor alone.

The count of the six dimensions of the subspace is then complete:

$$\boxed{\;\underbrace{2}_{r,\ \alpha} + \underbrace{3}_{B:\ \text{axis}\ (2) + \text{rapidity}\ (1)} + \underbrace{2}_{\tilde q} - \underbrace{1}_{\tilde q\perp\vec u_{\mathrm b}} = 6\;},$$

or, in the plane, $2$ for the modulus, $2$ for the axis, $1$ for the rapidity and $1$ for the angle of the rotor in the plane.

### Worked Examples

| example | $\langle\cdot\rangle_{\natural}$ | $r$ | $\alpha$ | $B$ | $\tilde q$ |
|---|---|---|---|---|---|
| $\tilde{Q} = \vec e_x+i\left(\vec e_y+\vec e_z\right)$ | $-1$ | $1$ | $1.570796327$ | $1.414213562\,e_t - 0.707106781\,i\vec e_y + 0.707106781\,i\vec e_z$ | $0.707106781\,\vec e_y + 0.707106781\,\vec e_z$ |
| $\tilde{Q} = \vec e_x+2i\vec e_x$ | $-3+4i$ | $2.236067977$ | $1.107148718$ | $e_t$ | $\vec e_x$ |

In the first row $\vec q\times\vec q' = \vec e_z-\vec e_y$, the boost axis is $(\vec e_z-\vec e_y)/\sqrt2$, the rapidity satisfies $\cosh 2\varphi = 3$, and the rotor is $(\vec e_y+\vec e_z)/\sqrt2$, which is orthogonal to the axis by construction. In the second row the two vectors are parallel, the boost factor is $e_t$, the element is $z \vec e_x$ with $z = 1+2i$, the modulus is $\rho = 1+2i$ and the phase is $\arg(1+2i) = 1.107148718$.

## The Quaternion Subspace $\mathbb{H}_{\mathbb{B}}$: the Rotor Alone

### The Element and Its Biquaternion Norm

Let $\tilde{Q}\in\mathbb{H}_{\mathbb{B}}$, that is $\bar{\tilde Q} = \tilde{Q}$, so that $\tilde{Q} = \sum_\mu q_\mu e_\mu$ with all four coefficients real. The subspace is the image of the real quaternion algebra inside $\mathbb{B}$, of real dimension four, and its biquaternion norm is the sum of four squares,

$$
\langle\tilde{Q}\rangle_{\natural} = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \sum_\mu q_\mu^2 > 0 \quad (\tilde{Q}\neq0), \qquad r = |\tilde{Q}| , \qquad \alpha = 0 ,
$$

positive definite, so its only zero is the origin and the representation is defined on the whole subspace except $0$. In the matrix picture it is the quaternionic class, $\mathsf{M}_2(\tilde{Q}) = q_tI - iq_k\sigma_k$.

### Which Factors Survive

On this subspace $\tilde{Q}^{*} = \tilde{Q}^{\natural}$, hence

$$
\tilde{Q}\tilde{Q}^{*} = \tilde{Q}\tilde{Q}^{\natural} = \langle\tilde{Q}\rangle_{\natural}e_t = |\tilde{Q}|^2e_t ,
$$

a positive scalar, so the first criterion gives $B = e_t$, and the rotor is the unit quaternion $\tilde q = \tilde{Q}/|\tilde{Q}|$. The four-factor representation reduces to

$$
\boxed{\;\tilde{Q} = r\,\tilde q , \qquad r = |\tilde{Q}| > 0 , \qquad \tilde q\in\mathrm{Sp}(1)\;},
$$

which is the classical polar form of a quaternion, with the boost factor absent: **the real quaternion subspace is the subspace on which the representation carries a rotor and no boost**. Writing $\tilde q = \cos\tfrac{\theta}{2} + \sin\tfrac{\theta}{2}\,\vec u_{\mathrm r}$ with $\vec u_{\mathrm r}$ a unit real vector, the rotor is a rotation of angle $\theta$ about the axis $\vec u_{\mathrm r}$, and the four real parameters of the subspace are $r$ and the three parameters of $\vec u_{\mathrm r}$ and $\theta$.

The matrix image explains the absence of the boost factor: a quaternionic matrix has the form $\begin{pmatrix} a & b \\ -\bar{b} & \bar{a}\end{pmatrix}$, and for every such matrix

$$
A A^\dagger = \left(|a|^2 + |b|^2\right) I ,
$$

a positive scalar, so the positive Hermitian polar factor of $A$ is the scalar $\sqrt{|a|^2+|b|^2}\,I$, which is the matrix image of a real multiple of $e_t$.

### Worked Examples

| example | $\langle\cdot\rangle_{\natural}$ | $r$ | $\alpha$ | $B$ | $\tilde q$ |
|---|---|---|---|---|---|
| $\tilde{Q} = e_t+2\vec e_x$ | $5$ | $2.236067977$ | $0$ | $e_t$ | $0.447213595\,e_t + 0.894427191\,\vec e_x$ |
| $\tilde{Q} = e_t+\vec e_x+\vec e_y+\vec e_z$ | $4$ | $2$ | $0$ | $e_t$ | $0.5\left(e_t+\vec e_x+\vec e_y+\vec e_z\right)$ |

Both rows have the trivial boost and the phase $0$, and the rotor is free: the first is a rotation by $2\arctan 2 = 2.214297436$ rad about $\vec e_x$, and the second is a rotation by $2\pi/3 = 2.094395102$ rad about $(\vec e_x+\vec e_y+\vec e_z)/\sqrt3$.

## The Antiquaternion Subspace $i\mathbb{H}_{\mathbb{B}}$: the Same Rotor with the Phase Frozen

### The Element and Its Biquaternion Norm

Let $\tilde{Q}\in i\mathbb{H}_{\mathbb{B}}$, that is $\bar{\tilde Q} = -\tilde{Q}$ and $\tilde{Q} = iq$ with $q$ a real quaternion. The subspace is the imaginary half of the coefficient split $\mathbb{B} = \mathbb{H}_{\mathbb{B}}\oplus i\mathbb{H}_{\mathbb{B}}$, of real dimension four, and its biquaternion norm is the negative of a sum of four squares,

$$
\langle\tilde{Q}\rangle_{\natural} = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = -\sum_\mu q_\mu^2 < 0 \quad (\tilde{Q}\neq0), \qquad r = |q| > 0 , \qquad \alpha = \frac{\pi}{2} ,
$$

negative definite, so again the only zero is the origin and the representation is defined on $i\mathbb{H}_{\mathbb{B}}\setminus\{0\}$. The principal square root of a negative real is positive imaginary, which is what freezes the phase at $\pi/2$.

### Which Factors Survive

The product $\tilde{Q}\tilde{Q}^{*} = |q|^2e_t$ is again a positive scalar, so the first criterion gives the trivial boost $B = e_t$, and the rotor is the unit quaternion $\tilde q = q/|q|$, free in $\mathrm{Sp}(1)$. The four factors are those of $\mathbb{H}_{\mathbb{B}}$ with the phase **frozen at $\pi/2$**:

$$
\tilde{Q} = r\exp(i\pi/2)\tilde q = i\,r\,\tilde q .
$$

The two halves therefore exhibit the same decomposition of the rotor, and differ by exactly the multiplication by the central phase $\exp(i\pi/2) = i$, which is the map $i\mathbb{H}_{\mathbb{B}} = i\cdot\mathbb{H}_{\mathbb{B}}$. In the corpus's notation the same fact is the sector exchange $\mathbb{M}_+ = i\mathbb{M}_-$; here it appears between the two halves, and it is the cleanest instance of the phase acting as a map rather than as a coordinate. In the matrix picture the half is carried by $i$ times the quaternionic class, $\mathsf{M}_2(\tilde{Q}) = i\mathsf{M}_2(q)$, and $\mathsf{M}_2(\tilde{Q})\mathsf{M}_2(\tilde{Q})^\dagger = \mathsf{M}_2(q)\mathsf{M}_2(q)^\dagger = (|a|^2+|b|^2)I$ is the same positive scalar as on $\mathbb{H}_{\mathbb{B}}$, so the boost factor is absent there for the same reason.

The two halves are the two definite subspaces — biquaternion norm of signature $(4,0)$ and $(0,4)$ — and on a definite subspace the phase cannot vary, because the biquaternion norm takes values on a ray of $\mathbb{C}$: the positive real axis on $\mathbb{H}_{\mathbb{B}}$ and the negative real axis on $i\mathbb{H}_{\mathbb{B}}$. This is the first instance of the rule proved in the section on the biquaternion norm below.

### Worked Examples

| example | $\langle\cdot\rangle_{\natural}$ | $r$ | $\alpha$ | $B$ | $\tilde q$ |
|---|---|---|---|---|---|
| $\tilde{Q} = i\left(e_t+2\vec e_x\right)$ | $-5$ | $2.236067977$ | $1.570796327$ | $e_t$ | $0.447213595\,e_t + 0.894427191\,\vec e_x$ |
| $\tilde{Q} = i\left(\vec e_x-\vec e_y\right)$ | $-2$ | $1.414213562$ | $1.570796327$ | $e_t$ | $0.707106781\,\vec e_x - 0.707106781\,\vec e_y$ |

Both rows have the trivial boost and the phase frozen at $\pi/2$: the first is the element $e_t+2\vec e_x$ carried into the antiquaternion subspace by the central $i$, with the same scale and the same rotor as in the quaternion table above, and the second is a rotation by $\pi$ about the direction $(\vec e_x-\vec e_y)/\sqrt2$.

## The Informational Sector $\mathbb{M}_+$: the Element Is Its Own Boost

### The Element and Its Biquaternion Norm

Let $\tilde{Q}\in\mathbb{M}_+$, written as

$$
\tilde{Q} = a\,e_t + i\,\vec q' , \qquad a\in\mathbb{R}, \quad \vec q'\in\mathbb{R}^3, \quad s = |\vec q'| , \qquad \langle\tilde{Q}\rangle_{\natural} = a^2 - s^2 \in\mathbb{R} .
$$

The sector is the fixed space of Hermitian conjugation, of real dimension four; its biquaternion norm is the real indefinite form $a^2-s^2$, vanishing on the cone $|a| = s$, and the representation is defined off that cone. The element is Hermitian, $\tilde{Q}^{*} = \tilde{Q}$, and in the matrix picture it is the Hermitian class, $\mathsf{M}_2(\tilde{Q}) = aI + w_k\sigma_k$.

### Why There Are Exactly Two Branches

Write the representation as $\tilde{Q} = \rho B\tilde q$ and impose Hermitian conjugation. With $\tilde q$ a real unit quaternion, $\tilde q^{*} = \tilde q^{\natural} = 2q_t - \tilde q$, while $B$ and the central factor $\rho$ are fixed by ${}^{*}$, so

$$
\tilde{Q}^{*} = \bar{\rho}\,B\,\tilde q^{\natural} = \tilde{Q} = \rho\,B\,\tilde q \quad\Longrightarrow\quad \tilde q^{\natural} = \exp(2i\alpha)\tilde q \quad\Longrightarrow\quad 2q_t = \left(1 + \exp(2i\alpha)\right)\tilde q .
$$

The left-hand side is a real multiple of the unit, so either $q_t = 0$, which forces $\exp(2i\alpha) = -1$, or $\tilde q = \pm e_t$, which forces $\exp(2i\alpha) = 1$ with the same sign in $q_t$ and in $\tilde q$. The two branches are therefore

$$
\alpha = 0 \ \text{with}\ \tilde q = \pm e_t \quad (\text{the case}\ N = a^2-s^2 > 0) , \qquad \alpha = \frac{\pi}{2}\ \text{with}\ \tilde q\ \text{a pure unit vector} \quad (\text{the case}\ N < 0) ,
$$

and no third possibility exists: the Hermitian condition permits exactly two branches, one for each sign of the biquaternion norm. The pairing is reversed with respect to the material sector of the next section, and the reason is the sign of the Hermitian condition — the element is a boost up to its modulus: on the branch $N > 0$ the element is definite, the rotor is the central sign, and $\tilde{Q} = \pm rB$ with the sign absorbed by the rotor; on the branch $N < 0$ the element is indefinite, the phase is $\pi/2$, and the rotor is the direction of the vector part.

### The Boost Factor

The boost factor is

$$
B = \frac{1}{r}\left(M\,e_t + i\,\operatorname{sign}(a)\,m\,\vec u_{q'}\right) , \qquad M = \max(|a|,s), \quad m = \min(|a|,s) , \qquad \vec u_{q'} = \frac{\vec q'}{s} ,
$$

which squares to $\left((a^2+s^2)e_t + 2ia\vec q'\right)/r^2 = \tilde{Q}\tilde{Q}^{*}/r^2$ because $\tilde{Q}\tilde{Q}^{*} = (a^2+s^2)e_t + 2ia\vec q'$; the sign in front of the vector part is opposite to that of the material sector, and the two formulas are consistent under the map $\tilde{Q}\mapsto i\tilde{Q}$ from $\mathbb{M}_+$ to $\mathbb{M}_-$, which sends the pair $(a,\vec q')$ to $(a,-\vec q')$ and therefore flips the vector part: the material formula with $\vec q = -\vec q'$ returns the informational formula.

### Worked Examples

| example | $\langle\cdot\rangle_{\natural}$ | $r$ | $\alpha$ | $B$ | $\tilde q$ |
|---|---|---|---|---|---|
| $\tilde{Q} = 2e_t+i\vec e_x$ | $3$ | $1.732050808$ | $0$ | $1.154700538\,e_t + 0.577350269\,i\vec e_x$ | $e_t$ |
| $\tilde{Q} = -2e_t+i\vec e_x$ | $3$ | $1.732050808$ | $0$ | $1.154700538\,e_t - 0.577350269\,i\vec e_x$ | $-e_t$ |
| $\tilde{Q} = e_t+2i\vec e_x$ | $-3$ | $1.732050808$ | $1.570796327$ | $1.154700538\,e_t + 0.577350269\,i\vec e_x$ | $\vec e_x$ |

All three rows have the same scale, and the pattern of the two branches is complete. The first and second rows are the definite branch: the same boost factor in magnitude, the same phase $0$, and rotors of opposite sign, which is the sign of $a$ absorbed by the fourth factor. The first and third rows have the same boost factor and the same scale and differ in the phase and in the rotor, the definite branch against the indefinite one, and it is the third row that exhibits the direction $\vec u_{q'} = \vec e_x$. The third and fourth factors are therefore never both continuous here: either the rotor is the discrete sign $\pm e_t$ and the boost is a general boost of axis $\vec u_{q'}$ and rapidity $\operatorname{arctanh}(s/|a|)$, or the rotor is the direction $\vec u_{q'}$ itself and the boost is reduced to a rapidity about that same direction.

## The Material Sector $\mathbb{M}_-$: the Boost of a Four-Vector

### The Element and Its Biquaternion Norm

Let $\tilde{Q}\in\mathbb{M}_-$, written in the physics coordinates as

$$
\tilde{Q} = i\,a\,e_t + \vec q , \qquad a = ct'\in\mathbb{R}, \quad \vec q\in\mathbb{R}^3, \quad s = |\vec q| , \qquad \langle\tilde{Q}\rangle_{\natural} = s^2 - a^2 \in\mathbb{R} .
$$

The sector is the anti-fixed space of Hermitian conjugation, of real dimension four; its biquaternion norm is the real indefinite form $s^2-a^2$, vanishing on the light cone $s = |a|$, and the representation is defined off that cone. In the matrix picture it is $i$ times the Hermitian class, $\mathsf{M}_2(\tilde{Q}) = i\left(aI - v_k\sigma_k\right)$. The biquaternion norm is real, so the phase takes one of the two values compatible with a real biquaternion norm, and the element is anti-Hermitian, $\tilde{Q}^{*} = -\tilde{Q}$. That single condition fixes the shape of the representation.

### Why There Are Exactly Two Branches

Write the representation as $\tilde{Q} = \rho B\tilde q$ and apply the anti-Hermitian condition. With $\tilde q$ a real unit quaternion, $\tilde q^{*} = \tilde q^{\natural} = 2q_t - \tilde q$, so

$$
\tilde{Q}^{*} = \bar{\rho}\,B\,\tilde q^{\natural} = -\tilde{Q} = -\rho\,B\,\tilde q \quad\Longrightarrow\quad \tilde q^{\natural} = -\exp(2i\alpha)\tilde q \quad\Longrightarrow\quad 2q_t = \left(1 - \exp(2i\alpha)\right)\tilde q .
$$

The left-hand side is a real multiple of the unit, so either $q_t = 0$, which forces $\exp(2i\alpha) = 1$, or $\tilde q = \pm e_t$, which forces $\exp(2i\alpha) = -1$ with the same sign in $q_t$ and in $\tilde q$. The two solutions are therefore

$$
\alpha = 0 \ \text{with}\ \tilde q\ \text{a pure unit vector} , \qquad \text{or} \qquad \alpha = \frac{\pi}{2}\ \text{with}\ \tilde q = \pm e_t ,
$$

and no third possibility exists. Since $N = r^2\exp(2i\alpha)$, the first branch is the **spacelike** case $s > |a|$ and the second is the **timelike** case $|a| > s$. On the material sector the phase is thus a two-valued label of the causal character of the four-vector, and it is exactly the $ict'$ interpretation of the companion article: a timelike four-vector has interval $N < 0$, its square root is imaginary, and the phase is the angle $\pi/2$ that makes the time component imaginary.

### The Boost Factor

From $\tilde{Q}\tilde{Q}^{*} = (a^2+s^2)e_t - 2ia\vec q$ and $r^2 = |N|$ one gets the explicit factor

$$
B = \frac{1}{r}\left(M\,e_t - i\,\operatorname{sign}(a)\,m\,\vec u_q\right) , \qquad M = \max(|a|,s), \quad m = \min(|a|,s) , \qquad \vec u_q = \frac{\vec q}{s} ,
$$

which is a boost rotor $B = \cosh\varphi\,e_t - i\operatorname{sign}(a)\sinh\varphi\,\vec u_q$ of rapidity $2\varphi$ with $\tanh\varphi = m/M$. Squaring it uses $Mm = |a|s$ and gives $B^2 = \left((a^2+s^2)e_t - 2ia\vec q\right)/r^2 = \tilde{Q}\tilde{Q}^{*}/r^2$, so the closed form is verified by squaring. In the timelike case with $a = ct' > 0$ it is the four-velocity identity of the companion article,

$$
B = \frac{ct'\,e_t - i(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)}{c\tau} = \gamma\left(e_t - i\frac{\vec q}{c}\right) = -\frac{i}{c}\tilde{V} , \qquad \gamma = \frac{ct'}{c\tau} = \frac{1}{\sqrt{1-\beta^2}} ,
$$

with $\beta = s/(ct')$; the scale is the proper length $r = c\tau = ct'\sqrt{1-\beta^2}$ and the rotor is the central sign.

### The Two Branches of the Material Sector

| branch | $\langle\cdot\rangle_{\natural}$ | $r$ | $\alpha$ | $B$ | $\tilde q$ |
|---|---|---|---|---|---|
| timelike, $|a| > s$ | $< 0$ | $\sqrt{a^2-s^2}$ | $\pi/2$ | $\cosh\varphi\,e_t - i\operatorname{sign}(a)\sinh\varphi\,\vec u_q$ | $\operatorname{sign}(a)e_t$ |
| spacelike, $s > |a|$ | $> 0$ | $\sqrt{s^2-a^2}$ | $0$ | $\cosh\varphi\,e_t - i\operatorname{sign}(a)\sinh\varphi\,\vec u_q$ | $\vec u_q$ |
| pure time, $s = 0$ | $< 0$ | $|a|$ | $\pi/2$ | $e_t$ | $\operatorname{sign}(a)e_t$ |
| pure space, $a = 0$ | $> 0$ | $s$ | $0$ | $e_t$ | $\vec u_q$ |

On the **timelike** branch the rotor is a central sign, so the continuous data of the four-vector are the scale and the boost alone: $1 + 3 = 4$, the dimension of the sector. The boost factor is the four-velocity in the Hermitian normalisation, which is the identification of the companion article; the phase is the constant $\pi/2$; and the rotor is the discrete sign $\operatorname{sign}(a)$. This is the precise sense in which the physics of the corpus uses two of the four factors.

On the **spacelike** branch the rotor is the pure unit vector $\vec u_q$, a point of $\mathcal{A}$, and the boost is a boost about the same line: with $\tanh\varphi = m/M$ and $m/M = |a|/s < 1$, its axis is $-\operatorname{sign}(a)\vec u_q$, opposite to the direction the rotor carries when $a$ is positive. The four parameters of a spacelike displacement are therefore the scale $r$, the direction $\vec u_q$ carried by the rotor, and the remaining number $m/M$ carried by the rapidity of the boost. The direction of the displacement is a property of the rotor and not of the boost, and the boost measures how far the displacement is tilted out of the spatial slice: the boost is the identity, $m = 0$, exactly for a displacement in the spatial slice, $a = 0$.

### Worked Examples

| example | $\langle\cdot\rangle_{\natural}$ | $r$ | $\alpha$ | $B$ | $\tilde q$ |
|---|---|---|---|---|---|
| $\tilde{Q} = ie_t+0.6\,\vec e_x$ | $-0.64$ | $0.8$ | $1.570796327$ | $1.25\,e_t - 0.75\,i\vec e_x$ | $e_t$ |
| $\tilde{Q} = 0.5\,ie_t+\vec e_x$ | $0.75$ | $0.866025404$ | $0$ | $1.154700538\,e_t - 0.577350269\,i\vec e_x$ | $\vec e_x$ |

The first row is the four-position of the companion article at $ct' = 1$ and $0.6c$: $r = 0.8 = c\tau$, $\alpha = \pi/2$, $B = \gamma(e_t-i\beta)$ with $\gamma = 1.25$ and $\beta = 0.6$, and the rotor is $e_t$. The second row is spacelike: $r = \sqrt{3}/2 = 0.866025404$, the phase vanishes, the rotor is the direction $\vec e_x$, and the boost is a boost about the axis $-\vec e_x$ of rapidity $2\operatorname{arctanh}(0.5) = 1.098612289$.

## The Biquaternion Norm Decides the Phase

The phase is $\alpha = \tfrac12\arg \langle\tilde{Q}\rangle_{\natural}$, so the phase is constant on a subset exactly when the argument of the biquaternion norm is constant there, and the remarkable subspaces realise the five possible behaviours of the biquaternion norm:

| subspace | $\langle\tilde{Q}\rangle_{\natural}$ | argument of the biquaternion norm | phase |
|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $z^2$, complex anisotropic | $2\arg z$ | $\arg z$ mod $\pi$, free |
| $\mathrm{Vect}(\mathbb{B})$ | $|\vec q|^2-|\vec q'|^2+2i\,\vec q\cdot\vec q'$, complex indefinite | free | free |
| $\mathbb{H}_{\mathbb{B}}$ | $\sum q_\mu^2$, positive definite | $0$ | $0$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $-\sum q_\mu^2$, negative definite | $\pi$ | $\pi/2$ |
| $\mathbb{M}_+$ | $a^2-s^2$, real indefinite | $0$ or $\pi$ | $0$ or $\pi/2$ |
| $\mathbb{M}_-$ | $s^2-a^2$, real indefinite | $0$ or $\pi$ | $0$ or $\pi/2$ |

The rule is therefore: **the phase is frozen when the biquaternion norm is definite, two-valued when the biquaternion norm is real indefinite, and free when the biquaternion norm is complex.** The centre and the vector subspace are the two subspaces with a complex biquaternion norm, and they are the two on which the phase is a genuine coordinate. The two halves, whose biquaternion norms have signature $(4,0)$ and $(0,4)$, are the subspaces on which the phase is a constant — the two constants being the two angles $0$ and $\pi/2$ that distinguish a real from a purely imaginary real quaternion. The two sectors, on which the biquaternion norm is a real indefinite quadratic form, are the subspaces on which the phase is a two-valued label, and the label is the causal character of the element: on $\mathbb{M}_+$ the pattern is the reverse of that on $\mathbb{M}_-$, where $\alpha = 0$ for a spacelike and $\alpha = \pi/2$ for a timelike element.

The same table decides where the representation fails. The biquaternion norm vanishes only where the quadratic form is isotropic:

| subspace | zeros of $\langle\cdot\rangle_{\natural}$ | representation |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $z = 0$ (anisotropic) | defined on $\mathbb{C}_{\mathbb{B}}\setminus\{0\}$ |
| $\mathrm{Vect}(\mathbb{B})$ | $|\vec q| = |\vec q'|$ and $\vec q\cdot\vec q' = 0$ | fails on the complex null cone |
| $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$ | $\tilde{Q} = 0$ (definite) | defined on the whole subspace except $0$ |
| $\mathbb{M}_+$ | the cone $|a| = s$ | fails on the cone |
| $\mathbb{M}_-$ | the light cone $s = |a|$ | fails on the light cone |

The two halves and the centre carry no zero divisors other than the origin, which is the corpus's statement that the degeneracy of the algebra lies in the sectors and in the vector subspace. The null cones are the boundaries between the two branches of the phase in the sectors: crossing the light cone in $\mathbb{M}_-$ is crossing from $\alpha = 0$ to $\alpha = \pi/2$, and the representation fails exactly at the crossing because the two branches meet at $r = 0$. In the vector subspace the null cone is the four-dimensional cone $|\vec q| = |\vec q'|$, $\vec q\cdot\vec q' = 0$, on which the two vectors are the real and imaginary parts of a null complex vector; there the boost factor and the rotor both blow up, and the element is a zero divisor, as in the sectors.

## Where the Dimensions Go

Each row below is the count of the real dimensions of the subspace, distributed over the four factors. A factor that is trivial contributes nothing, a factor that is fixed contributes nothing, and a factor that is discrete contributes nothing continuous.

| subspace | dim | $r$ | $\exp(i\alpha)$ | $B$ | $\tilde q$ |
|---|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $2$ | $1$ | $1$ | $0$ | $0$ (discrete $\pm e_t$) |
| $\mathrm{Vect}(\mathbb{B})$ | $6$ | $1$ | $1$ | $3$ | $2$, less $1$ for $\tilde q\perp\vec u_{\mathrm b}$ |
| $\mathbb{H}_{\mathbb{B}}$ | $4$ | $1$ | $0$ (fixed $0$) | $0$ | $3$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $4$ | $1$ | $0$ (fixed $\pi/2$) | $0$ | $3$ |
| $\mathbb{M}_+$, $N>0$ | $4$ | $1$ | $0$ (fixed $0$) | $3$ | $0$ (discrete $\pm e_t$) |
| $\mathbb{M}_+$, $N<0$ | $4$ | $1$ | $0$ (fixed $\pi/2$) | $1$ (the rapidity) | $2$ (the direction) |
| $\mathbb{M}_-$, timelike | $4$ | $1$ | $0$ (fixed $\pi/2$) | $3$ | $0$ (discrete $\pm e_t$) |
| $\mathbb{M}_-$, spacelike | $4$ | $1$ | $0$ (fixed $0$) | $1$ (the rapidity) | $2$ (the direction) |

Only the vector subspace carries the phase as a dimension of its own together with a nontrivial boost and a nontrivial rotor, and this is why it is the largest of the remarkable subspaces. On the centre the scale and the phase survive, and the rotor is a discrete sign; on the two halves the boost is absent and the rotor absorbs everything but the scale; on the two sectors either the rotor or the boost is reduced to a single number or to a direction. No subspace carries the four factors independently, and the counting above is the exact statement of the dependencies.

## The Four Blocks

The four coordinate blocks

$$
T_{\mathrm{m}} = \mathbb{R}(ie_t) , \qquad T_{\mathrm{i}} = \mathbb{R}e_t , \qquad X_{\mathrm{m}} = \mathbb{R}(\vec e_x,\vec e_y,\vec e_z) , \qquad X_{\mathrm{i}} = \mathbb{R}(i\vec e_x,i\vec e_y,i\vec e_z)
$$

are the intersections of the remarkable subspaces, and each block lies in three of them. The restrictions must agree on the overlaps, and they do:

| block | subspaces containing it | element | $r$ | $\alpha$ | $B$ | $\tilde q$ |
|---|---|---|---|---|---|---|
| $T_{\mathrm{i}}$ | $\mathbb{C}_{\mathbb{B}}$, $\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$ | $t\,e_t$ | $|t|$ | $0$ | $e_t$ | $\operatorname{sign}(t)e_t$ |
| $T_{\mathrm{m}}$ | $\mathbb{C}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_-$ | $it'\,e_t$ | $|t'|$ | $\pi/2$ | $e_t$ | $\operatorname{sign}(t')e_t$ |
| $X_{\mathrm{m}}$ | $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_-$ | $x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ | $|x\,\vec e_x+y\,\vec e_y+z\,\vec e_z|$ | $0$ | $e_t$ | $\vec u_x$ |
| $X_{\mathrm{i}}$ | $\mathrm{Vect}(\mathbb{B})$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$ | $i\vec q'$ | $|\vec q'|$ | $\pi/2$ | $e_t$ | $\vec u_{q'}$ |

Every entry satisfies the restrictions of each subspace that contains it. On $T_{\mathrm{i}}$ the centre gives $\tilde q = \pm e_t$, the quaternion subspace gives $\tilde q = \tilde{Q}/|\tilde{Q}| = \pm e_t$, and the informational sector with $s = 0$ gives $m = 0$, hence $B = e_t$ and $\tilde q = \operatorname{sign}(a)e_t$; the three interpretations are the same. On $X_{\mathrm{m}}$ the vector subspace interpretation has $\vec q' = 0$, which is the degenerate case $\vec q\times\vec q' = 0$, hence $B = e_t$; the quaternion interpretation gives the rotor $\vec u_x$; and the material-sector interpretation with $a = 0$ gives the spacelike rotor $\vec u_q = \vec u_x$ with the trivial boost $B = e_t$; the three interpretations are the same. On $X_{\mathrm{i}}$ the vector, antiquaternion and informational interpretations agree the same way, with the phase $\pi/2$ and the rotor $\vec u_{q'}$ in all three. The blocks are therefore the elements on which all the applicable simplifications hold at once, and the table is a consistency check of the six sections above rather than a new computation.

## Physical Readings

The two criteria read as the framework's tests of positivity and of Hermiticity: the scalar factor is $e_t$ exactly when a product is a positive scalar, and the normalised element is Hermitian exactly when the central direction is $\pm e_t$. Read on the states, the criteria are the boundary between an element that can carry a state and one that cannot, which is the same boundary the indefinite metric meets; read on the clock, the two exceptional directions are the two orientations of the central axis, which is what the exchange rotates by a quarter turn at a time.

## Summary

Restricted to the remarkable subspaces, the polar decomposition $\tilde{Q} = r\exp(i\alpha)B\tilde q$ loses one or more of its factors, and the loss is computable from the involution that defines the subspace. The scale is always the square root of the absolute value of the determinant, and it never degenerates except on the null cones.

The phase is half the argument of the biquaternion norm: it is a free coordinate on the centre and on the vector subspace, where the biquaternion norm is complex; it is frozen at $0$ on the real quaternion subspace and at $\pi/2$ on the antiquaternion subspace, where the biquaternion norm is definite; and it is a two-valued label of the causal character of the element on the two sectors, where the biquaternion norm is real indefinite.

The boost factor is trivial exactly on the subspaces and on the elements for which $\tilde{Q}\tilde{Q}^{*}$ is a positive scalar: that is every element of the centre, every parallel pair $\vec q\parallel\vec q'$ in the vector subspace, and every element of the two halves; it is the exceptional case of a vanishing time coordinate, $a = 0$, or a vanishing vector part, in the sectors. The rotor is a central sign exactly when $\tilde{Q}/\rho$ is Hermitian: that is the centre, and one branch of each sector — the definite branch of the informational sector and the timelike branch of the material sector — while on the other branch it is a pure unit vector, the direction of the element. The vector subspace exhibits the rotor relative to the boost, with the scalar part vanishing exactly when the two axes are orthogonal; on the two halves the rotor is free and the boost is absent, so the halves exhibit the rotor alone; and the sectors exhibit the boost alone and reduce the rotor to a sign or to a direction.

The restrictions together exhaust the ways in which the four factors can depend on one another, and the biquaternion norm — positive definite, negative definite, real indefinite, complex anisotropic, complex indefinite — is what decides which way each subspace goes. Read over the whole algebra rather than on one subspace, the two criteria cut two classes out of the nonzero elements: the boost-free elements, which are the positive multiples of the unitary elements and form a group, and the rotor-free elements, which are the complex multiples of the Hermitian definite ones and do not. Each class has five real dimensions, and they meet exactly in the centre, the count $5+5-8 = 2$ closing against the eight real dimensions of the group of units; on the unit-norm slice they become the rotor group and the boosts with a discrete sign, the two halves of the Cartan decomposition.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ | a biquaternion, $Q_\mu\in\mathbb{C}$ |
| $\langle\tilde{Q}\rangle_{\natural} = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \sum_\mu Q_\mu^2 = \det\mathsf{M}_2(\tilde{Q})$ | the biquaternion norm and the determinant of the $2\times2$ representative |
| $\rho = r\exp(i\alpha) = \sqrt{\langle\tilde{Q}\rangle_{\natural}}$ | the complex modulus, in the principal branch $\alpha\in(-\pi/2,\pi/2]$ |
| $B = \sqrt{\tilde{Q}\tilde{Q}^{*}}/r$ | the boost factor, Hermitian positive of biquaternion norm one |
| $\tilde q = B^{-1}\tilde{Q}/\rho\in\mathrm{Sp}(1)$ | the rotor, a unit real quaternion |
| $\tilde q = \pm e_t \iff \tilde{Q}/\rho$ Hermitian | the criterion for a trivial rotor |
| $B = e_t \iff \tilde{Q}\tilde{Q}^{*}\in\mathbb{R}_{>0}e_t$ | the criterion for a trivial boost |
| $\mathcal{U}$, $\mathcal{H}$ | the boost-free and the rotor-free classes, $B=e_t$ and $\tilde q=\pm e_t$; five real dimensions each, meeting exactly in $\mathbb{C}_{\mathbb{B}}\setminus\{0\}$ |
| $\mathbb{C}_{\mathbb{B}}$ | the centre |
| $\mathrm{Vect}(\mathbb{B})$ | the vector subspace, $\operatorname{Sc}(\tilde{Q}) = 0$ |
| $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$ | real quaternion subspace, antiquaternion subspace |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | informational and material sectors |
| $\tilde{Q} = iae_t+\vec q$, $s = |\vec q|$ | element of the material sector; $a = ct'$ for a four-position |
| $\tilde{Q} = ae_t+i\vec q'$, $s = |\vec q'|$ | element of the informational sector |
| $\tilde{Q} = \vec q+i\vec q'$ | element of the vector subspace |
| $\varphi$ | the half-rapidity of $B$: $B = \cosh\varphi\,e_t + i\sinh\varphi\,\vec u_{\mathrm b}$, rapidity $2\varphi$ |
| $M = \max(|a|,s)$, $m = \min(|a|,s)$ | the two numbers that fix the rapidity of the sector boost |
| $T_{\mathrm{m}}, T_{\mathrm{i}}, X_{\mathrm{m}}, X_{\mathrm{i}}$ | the four coordinate blocks |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*})$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{*}=\sum_\mu\lvert Q_{2\mu}\rvert^{2}$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle$ | the general plain bilinear form, the scalar part of the general plain bilinear product, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2)$ |

## Further Reading

- [The Polar Decomposition of a N-Regular Biquaternion](../articles_maths/the-polar-decomposition-of-an-n-regular-biquaternion.html), for the theorem, the four factors, the algorithm and the uniqueness, the determinant, the interval and the light cone.
- [The Biquaternion Space, the Group of Involutions and the Six Subspaces](the-biquaternion-space-the-group-of-involutions-and-the-six-subspaces.html), for the remarkable subspaces, the involutions, the four blocks, the intersections and the biquaternion norm of each subspace.
- [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html), for the boosts and the information interpretation.
- [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html), for the four-vectors and the light cone.
- [Element and Operator Representations: The Three Actions](the-element-and-operator-representations.html), for the matrix classes of the remarkable subspaces and $\det\mathsf{M}_2(\tilde{Q}) = \langle\tilde{Q}\rangle_{\natural}$.
