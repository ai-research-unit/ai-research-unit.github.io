# __The Polar Element Representation of Biquaternions__

## Introduction

Every biquaternion of non-vanishing norm is the ordered product of a positive real scale, a central phase and two unit factors,

$$
\tilde{Q} = r\,\exp(i\alpha)\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r}
= r\,\exp(i\alpha)\,\exp\Bigl(i\tfrac{\psi}{2}\vec u_{\mathrm b}\Bigr)\,\exp\Bigl(\tfrac{\theta}{2}\vec u_{\mathrm r}\Bigr) .
$$

| # | factor | name | exponent | root | range | real dimension | action | stable subspaces |
|---|---|---|---|---|---|---|---|---|
| 1 | $r$ | scale | — | — | $r \in \mathbb{R}$, $r>0$ | $1$ | $\tilde Q\mapsto r^{2}\tilde Q$ | $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$, $\mathbb{M}_-$ |
| 2 | $\exp(i\alpha)$ | central phase | $i\alpha$ | $i$ | $\alpha \in \left(-\frac{\pi}{2},\frac{\pi}{2}\right]$ | $1$ | $\tilde Q\mapsto \exp(i\alpha)\tilde Q$ | $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$ |
| 3 | $\tilde U_{\mathrm b} = \exp\bigl(i\tfrac{\psi}{2}\vec u_{\mathrm b}\bigr)$ | boost | $i\tfrac{\psi}{2}\vec u_{\mathrm b}$ | $i\vec u_{\mathrm b}$ | $\psi \ge0$, $\vec u_{\mathrm b}\in\mathcal{A}$ | $3$ | $\tilde Q\mapsto \tilde U_{\mathrm b}\tilde Q\tilde U_{\mathrm b}^{*}$ | $\mathbb{M}_+$, $\mathbb{M}_-$ |
| 4 | $\tilde u_{\mathrm r} = \exp\bigl(\tfrac{\theta}{2}\vec u_{\mathrm r}\bigr)$ | rotor | $\tfrac{\theta}{2}\vec u_{\mathrm r}$ | $\vec u_{\mathrm r}$ | $\theta \in [0,2\pi]$, $\vec u_{\mathrm r}\in\mathcal{A}$ | $3$ | $\tilde Q\mapsto \tilde u_{\mathrm r}\tilde Q\tilde u_{\mathrm r}^{-1}$ | $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$, $\mathbb{M}_-$ |

The action column records the operation by which the factor acts on the algebra. For the scale, the boost and the rotor this is the sandwich by the factor in view, that is the dilation $\tilde Q\mapsto r^{2}\tilde Q$, the congruence $\tilde Q\mapsto\tilde U_{\mathrm b}\tilde Q\tilde U_{\mathrm b}^{*}$ and the conjugation $\tilde Q\mapsto\tilde u_{\mathrm r}\tilde Q\tilde u_{\mathrm r}^{-1}$. The phase is central and its sandwich is the identity, so its row records multiplication by the scalar, the only action under which it is not in the kernel; this is the one row that departs from the sandwich convention of *The Action of the Polar Element Representation on the Hermitian and Anti-Hermitian Subspaces*, where the phase would list every subspace because it acts trivially. The scale preserves $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$, $\mathbb{M}_-$. The phase preserves $\mathbb{C}_{\mathbb{B}}$ and $\mathrm{Vect}(\mathbb{B})$ and no other: on a real form the factor $\exp(i\alpha)$ turns a real part into an imaginary one. The boost preserves $\mathbb{M}_+$ and $\mathbb{M}_-$ and no other. The rotor preserves $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$, $\mathbb{M}_-$: conjugation by a real unit quaternion is an automorphism of $\mathbb{B}$ commuting with the three conjugations, so it carries each of the six into itself. Parameters are generic; at the identity value of a parameter the factor is $e_t$ and preserves every subspace. Two-sided multiplication by the rotor, $\tilde Q\mapsto\tilde u_{\mathrm r}\tilde Q\tilde u_{\mathrm r}$, is a different action and is not used: under it the rotor preserves only $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$, while under conjugation it preserves all six.

The scale is the only factor written without an exponential in the word. Each exponent is a real parameter times a **root** of $-e_t$, $0$ or $+e_t$, and the character of the exponential is fixed by the square of its root: $-e_t$ trigonometric, $+e_t$ hyperbolic, $0$ parabolic, the series truncating to the unit plus the exponent. The phase and the rotor therefore stand on a root of $-e_t$, the boost on a root of $+e_t$, and the scale is the degenerate hyperbolic factor, whose root is $e_t$. The parabolic case carries no factor of this representation but is not empty in $\mathbb{B}$: the element $\vec e_x+i\vec e_y$ has square zero, so its exponential is $e_t+(\vec e_x+i\vec e_y)$, of norm one and neither a rotor nor a boost. The rule is Lemma 1 of Sangwine & Hitzer.

The two axes are directions in space, each a unit real pure quaternion,

$$
\vec u = \vec u_x\vec e_x+\vec u_y\vec e_y+\vec u_z\vec e_z , \qquad \vec u_x,\vec u_y,\vec u_z\in\mathbb{R} , \qquad \vec u_x^2+\vec u_y^2+\vec u_z^2=1 , \qquad \vec u^2=-e_t .
$$

The set of them is the **axis sphere** $\mathcal{A}$, the quaternion roots of $-1$; the symbol $S$ is left to the spin groups $\mathrm{Spin}(n)$ of the spinor context, and the group of unit quaternions is written $\mathrm{Sp}(1)$. The scale and the phase stand on the two central unit elements $e_t$ and $i$.

The four factors are unique and their real dimensions $1+1+3+3$ sum to the eight of the algebra. The word exists exactly off the null cone, and it fails nowhere else. The body treats the four factors in turn — §*The Scale*, §*The Central Phase*, §*The Boost*, §*The Rotor* — the ordering is recorded in §*The Order of the Boost and the Rotor*, and §*The Theorem* proves the representation and its uniqueness; §*The Procedure in Practice* records the algorithm, the coordinate forms and three worked examples. The conventions and symbols are the corpus's (*Conventions in Mathematics*, §*Symbols*, §*The Unitary Convention*). No physics is invoked.

## The Scale

The first factor is the positive real

$$
r = \lvert\Rho\rvert = \sqrt{\lvert\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\rvert} .
$$

### The Norm and the Modulus

The number under the root is the **biquaternion norm**, the sum of the squares of the four complex coefficients, central and multiplicative,

$$
\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \sum_{\mu\in\{t,x,y,z\}}Q_\mu^2 , \qquad \langle\tilde Q_1\tilde Q_2,\tilde Q_1\tilde Q_2\rangle_{\natural} = \langle\tilde Q_1,\tilde Q_1\rangle_{\natural}\langle\tilde Q_2,\tilde Q_2\rangle_{\natural} .
$$

The modulus $\Rho$ is its square root, and the root is two-valued. The branch is fixed once and for all: with $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \lvert\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\rvert\,\exp(i\varphi)$, $\varphi\in(-\pi,\pi]$, take the **principal** root

$$
\Rho = \sqrt{\lvert\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\rvert}\;\exp(i\varphi/2) , \qquad r = \lvert\Rho\rvert , \qquad \alpha = \arg\Rho = \frac{\varphi}{2} \in \left(-\frac{\pi}{2},\frac{\pi}{2}\right] .
$$

The pair $(r,\alpha)$ is then unique, and the other root $-\Rho$ has angle $\alpha\pm\pi$, outside the interval. This branch is the only convention of the representation; every other step is forced.

### The Factor

The scale is central, of real dimension $1$. It scales the element rigidly: replacing $\tilde{Q}$ by $\lambda\tilde{Q}$ with $\lambda>0$ multiplies $r$ by $\lambda$ and leaves the other three factors unchanged. It is the one factor written without an exponential, and it is fixed by each of the four conjugations.

### The Unit-Norm Slice

The scale is one exactly when $\lvert\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\rvert = 1$; in particular it is one on the unit-norm elements. If $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = 1$ then also $\Rho = 1$ and $\alpha = 0$, and the word reduces to

$$
\tilde{Q} = \tilde U_{\mathrm b}\,\tilde u_{\mathrm r} , \qquad \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = 1 ,
$$

a boost times a rotation. This is the Cartan form of the physics articles, the only case their corpus uses.

### The Domain

The word exists if and only if $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\neq0$, that is, if and only if $\tilde{Q}$ is outside the null cone, equivalently invertible (*Norm and Invertibility in the General Quaternionic Algebra*). On the cone, and away from $\tilde{Q} = 0$, the element is a zero divisor and no factorisation exists, since the product of the four factors has norm $r^2\cdot1\cdot1\cdot1 = r^2 > 0$. The condition is one complex equation, hence two real equations, so the cone has real codimension two: $\dim_{\mathbb{R}}\{N = 0\} = 6$ in the eight-dimensional algebra, and deleting it leaves a domain of full dimension. The cone is the algebra's light cone (*The Zero Divisors of the Biquaternion Algebra*).

## The Central Phase

The second factor is the central phase

$$
\exp(i\alpha) , \qquad \alpha = \tfrac{1}{2}\arg\langle\tilde{Q},\tilde{Q}\rangle_{\natural} \in \left(-\tfrac{\pi}{2},\tfrac{\pi}{2}\right] ,
$$

the unit element of the centre given by the argument of the biquaternion norm.

### The Factor

Being central, the phase commutes with the other three factors and may be moved through them at no cost. It is the only factor that is both central and compact, of real dimension $1$; its exponent lies on the central imaginary line $i\mathbb{R}\subset\mathbb{C}_{\mathbb{B}}$, and its root is the central unit $i$, of square $-e_t$.

### The Two Sectors

The phase is zero on the quaternion half and $\pi/2$ on the anti-quaternion half, whose word, $i = 1\cdot \exp(i\pi/2)\cdot e_t\cdot e_t$, exhibits the extremal value. In the physical reading the vanishing of $\alpha$ selects the spacelike sector and its extremal value the timelike one.

### The Conjugations and the Degenerate Cases

Under the conjugations the phase is reversed, $\alpha\mapsto-\alpha$, by the coefficientwise and the Hermitian conjugation, and fixed by the quaternion conjugation. It is trivial, $\exp(i\alpha) = e_t$, exactly when the biquaternion norm is a positive real.

## The Boost

The third factor is the boost

$$
\tilde U_{\mathrm b} = \exp\Bigl(i\tfrac{\psi}{2}\vec u_{\mathrm b}\Bigr) = \cosh\tfrac{\psi}{2}\,e_t + i\sinh\tfrac{\psi}{2}\,\vec u_{\mathrm b} , \qquad \psi \ge 0, \qquad \vec u_{\mathrm b}\in\mathcal{A} ,
$$

the Hermitian positive unit element of the word.

### The Exponent and the Root

The exponent $i\tfrac{\psi}{2}\vec u_{\mathrm b}$ lies in the Hermitian subspace $\mathbb{M}_+$ and has vanishing scalar part; its root is $i\vec u_{\mathrm b}$, Hermitian and of square $+e_t$. The exponent carries half of the rapidity: the conjugation by the boost deposits the rapidity $\psi$ twice. The boost is the only factor that is neither central nor compact, of real dimension $3$ — the rapidity and the two angles of the axis.

### The Hermitian Positive Factor

Divide the element by its modulus, $\tilde U = \tilde{Q}/\Rho$, so that $\langle \tilde U,\tilde U\rangle_{\natural} = 1$, and form the Hermitian element $\tilde U\tilde U^{*}$. It is Hermitian, $(\tilde U\tilde U^{*})^{*} = \tilde U\tilde U^{*}$, and positive definite, the product of an invertible element and its Hermitian conjugate; its biquaternion norm is $\langle \tilde U\tilde U^{*},\tilde U\tilde U^{*}\rangle_{\natural} = 1$. The boost is the unique Hermitian positive square root of $\tilde U\tilde U^{*}$,

$$
\tilde U_{\mathrm b} = \sqrt{\tilde U\tilde U^{*}} , \qquad \tilde U_{\mathrm b}^2 = \tilde U\tilde U^{*} , \qquad \langle \tilde U_{\mathrm b},\tilde U_{\mathrm b}\rangle_{\natural} = 1 ,
$$

the normalisation of the boost being that the square root of a norm-one element has norm one.

### The Closed Form

For an element with real scalar part, $\tilde Q = \mathrm{Sc}(\tilde Q)\,e_t + i\,\mathrm{Vec}(\tilde Q)$, the four coefficients are the scalar and $i$ times the three components of the vector part, so the biquaternion norm is the difference of the two squared lengths,

$$
\langle X,X\rangle_{\natural} = \mathrm{Sc}(X)^2 - \lvert \mathrm{Vec}(X)\rvert^2 .
$$

The Hermitian element is written through its scalar part and its vector part,

$$
\tilde U\tilde U^{*} = \mathrm{Sc}(\tilde U\tilde U^{*})\,e_t + i\,\mathrm{Vec}(\tilde U\tilde U^{*}) , \qquad \mathrm{Sc}(\tilde U\tilde U^{*}) \in \mathbb{R}, \qquad \mathrm{Vec}(\tilde U\tilde U^{*}) \in \mathbb{R}^3 ,
$$

so that its unit norm and its positivity read

$$
\mathrm{Sc}(\tilde U\tilde U^{*})^2 - \lvert \mathrm{Vec}(\tilde U\tilde U^{*})\rvert^2 = 1 , \qquad \mathrm{Sc}(\tilde U\tilde U^{*}) \ge 1 .
$$

The square root is Hermitian of the same shape. Write its scalar part $a = \mathrm{Sc}(\tilde U_{\mathrm b})$ and its vector part $\mathrm{Vec}(\tilde U_{\mathrm b})$, so that

$$
\tilde U_{\mathrm b} = a\,e_t + i\,\mathrm{Vec}(\tilde U_{\mathrm b}) , \qquad a \in \mathbb{R} , \qquad \mathrm{Vec}(\tilde U_{\mathrm b}) \in \mathbb{R}^3 , \qquad a^2 - \lvert \mathrm{Vec}(\tilde U_{\mathrm b})\rvert^2 = 1 ,
$$

the last relation being the unit norm of the square root, which holds because the norm of $\tilde U\tilde U^{*}$ is one and the norm is multiplicative. A real pure quaternion squares to minus its squared length, $\vec v^{\,2} = -\lvert\vec v\rvert^2 e_t$, so the squared imaginary vector part is $(i\,\mathrm{Vec}(\tilde U_{\mathrm b}))^2 = \lvert \mathrm{Vec}(\tilde U_{\mathrm b})\rvert^2 e_t$, and the square of the root is

$$
\tilde U_{\mathrm b}^{\,2} = \bigl(a^2 + \lvert \mathrm{Vec}(\tilde U_{\mathrm b})\rvert^2\bigr)e_t + 2a\,i\,\mathrm{Vec}(\tilde U_{\mathrm b}) .
$$

The equation $\tilde U_{\mathrm b}^{\,2} = \tilde U\tilde U^{*}$ splits into its scalar part and its vector part,

$$
a^2 + \lvert \mathrm{Vec}(\tilde U_{\mathrm b})\rvert^2 = \mathrm{Sc}(\tilde U\tilde U^{*}) , \qquad a\,\mathrm{Vec}(\tilde U_{\mathrm b}) = \tfrac12\,\mathrm{Vec}(\tilde U\tilde U^{*}) .
$$

Adding the scalar equation to the unit norm of $\tilde U_{\mathrm b}$ cancels the two squared lengths of the vector part and gives $2a^2 = \mathrm{Sc}(\tilde U\tilde U^{*}) + 1$, so the scalar part of the root is

$$
a = \sqrt{\frac{1+\mathrm{Sc}(\tilde U\tilde U^{*})}{2}} ,
$$

the positive root being taken because the square root is positive. The vector equation then gives the vector part of the root,

$$
\mathrm{Vec}(\tilde U_{\mathrm b}) = \frac{\mathrm{Vec}(\tilde U\tilde U^{*})}{2a} = \frac{\mathrm{Vec}(\tilde U\tilde U^{*})}{\sqrt{2\,\bigl(1+\mathrm{Sc}(\tilde U\tilde U^{*})\bigr)}} .
$$

Collecting the two parts, and using $\tilde U\tilde U^{*} = \mathrm{Sc}(\tilde U\tilde U^{*})e_t + i\,\mathrm{Vec}(\tilde U\tilde U^{*})$ for the last form,

$$
\tilde U_{\mathrm b} = \sqrt{\tilde U\tilde U^{*}} = \sqrt{\frac{1+\mathrm{Sc}(\tilde U\tilde U^{*})}{2}}\;e_t + \frac{i\,\mathrm{Vec}(\tilde U\tilde U^{*})}{\sqrt{2\,\bigl(1+\mathrm{Sc}(\tilde U\tilde U^{*})\bigr)}} = \frac{\tilde U\tilde U^{*}+e_t}{\sqrt{2\,\bigl(1+\mathrm{Sc}(\tilde U\tilde U^{*})\bigr)}} ,
$$

which squares back to $\tilde U\tilde U^{*}$. The comparison with the exponential writing gives the boost data

$$
\cosh\psi = \mathrm{Sc}(\tilde U\tilde U^{*}) , \qquad \sinh\psi = \lvert \mathrm{Vec}(\tilde U\tilde U^{*})\rvert , \qquad \vec u_{\mathrm b} = \frac{\mathrm{Vec}(\tilde U\tilde U^{*})}{\lvert \mathrm{Vec}(\tilde U\tilde U^{*})\rvert} .
$$

$\psi$ the **rapidity** and $\vec u_{\mathrm b}$ the **axis**. The boost carries three parameters and its set is the hyperbolic space $H^3$, the set of Lorentz boosts; in the notation of the physics articles it is the Lorentz boost rotor $\tilde U_{\mathrm b} = \cosh\tfrac{\psi}{2} + i\sinh\tfrac{\psi}{2}\vec u_{\mathrm b}$.

### The Order of the Boost and the Rotor

The two non-central factors do not commute, and the position of each in the word is part of the statement. The order is free for the central factors alone: $\exp(i\alpha)\tilde U_{\mathrm b}\tilde u_{\mathrm r} = \tilde U_{\mathrm b}\tilde u_{\mathrm r}\,\exp(i\alpha)$ exactly, and likewise for $r$. For the other two, $\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ differs from $\tilde u_{\mathrm r}\tilde U_{\mathrm b}$ as soon as the axes are not parallel, the two being related by the conjugation

$$
\tilde u_{\mathrm r}\tilde U_{\mathrm b} = \left(\tilde u_{\mathrm r}\tilde U_{\mathrm b}\tilde u_{\mathrm r}^{-1}\right)\tilde u_{\mathrm r} ,
$$

which keeps the rapidity, rotates the axis by the rotor, and leaves $r$ and $\alpha$ unchanged. The product of the two factors is not the exponential of the sum of their exponents, because their exponents do not commute, $[\log\tilde U_{\mathrm b},\log\tilde u_{\mathrm r}]\neq0$ in general:

$$
\exp\left(\log \tilde U_{\mathrm b} + \log\tilde u_{\mathrm r}\right) \neq \tilde U_{\mathrm b}\tilde u_{\mathrm r} .
$$

The rapidity of a product is therefore not the sum of the rapidities, nor the rotation angle the sum of the rotation angles, while the scale is multiplicative, $r = r_1r_2$, and the phase is additive modulo $\pi$, $\alpha\equiv\alpha_1+\alpha_2 \pmod{\pi}$, the sign being absorbed by the rotor when the sum leaves the branch. The word becomes order-free exactly when one of the two non-central factors is central or the two axes are parallel; in the last case the element is a single boost-rotation about the common axis, which is why two boosts along one line have no residual rotation.

### The Conjugations

Under the conjugations the quaternion and the coefficientwise conjugation replace the boost by its inverse, the boost of the same rapidity about the reflected axis, and the Hermitian conjugation fixes it, $\tilde U_{\mathrm b}^{*} = \tilde U_{\mathrm b}$. The boost is trivial exactly when $\psi = 0$, that is, when $\tilde U\tilde U^{*} = e_t$, equivalently when the unit-norm part $\tilde U$ is unitary; this holds on the complex lines through a real quaternion, in particular on the centre, the quaternion subspace and the anti-quaternion subspace.

## The Rotor

The fourth factor is the rotor

$$
\tilde u_{\mathrm r} = \exp\Bigl(\tfrac{\theta}{2}\vec u_{\mathrm r}\Bigr) = \cos\tfrac{\theta}{2}\,e_t + \sin\tfrac{\theta}{2}\,\vec u_{\mathrm r} , \qquad \theta \in [0,2\pi], \qquad \vec u_{\mathrm r}\in\mathcal{A} ,
$$

the unit real quaternion of the word.

### The Exponent and the Root

The exponent $\tfrac{\theta}{2}\vec u_{\mathrm r}$ is a real pure quaternion, lying in the anti-Hermitian sector $\mathbb{M}_- \cap \mathrm{Vect}(\mathbb{B})$; it is the only exponent that is neither central nor Hermitian. Its root is the real pure unit quaternion $\vec u_{\mathrm r}$, of square $-e_t$, and it carries half of the rotation angle, the conjugation by the rotor producing a rotation by $\theta$. The rotor is compact, of real dimension $3$.

### The Definition

The rotor is the unitary factor of the right polar decomposition of the unit-norm part,

$$
\tilde U = \tilde u_{\mathrm r}\sqrt{\tilde U^{*}\tilde U} , \qquad \tilde u_{\mathrm r} = \tilde U\bigl(\sqrt{\tilde U^{*}\tilde U}\bigr)^{-1} .
$$

The element $\tilde U^{*}\tilde U$ is Hermitian positive definite, the product of an invertible element and its Hermitian conjugate, so $\sqrt{\tilde U^{*}\tilde U}$ is its unique Hermitian positive square root and the formula defines $\tilde u_{\mathrm r}$ from the unit-norm part alone; no other factor enters. Equivalently, $\tilde u_{\mathrm r}$ is the unique unit element for which $\tilde U\tilde u_{\mathrm r}^{-1}$ is Hermitian positive. If $\tilde U = \tilde u\,\tilde U_{\mathrm b}$ with $\tilde u$ a unit real quaternion and $\tilde U_{\mathrm b}$ Hermitian positive, then $\tilde U^{*}\tilde U = \tilde U_{\mathrm b}\tilde u^{*}\tilde u\,\tilde U_{\mathrm b} = \tilde U_{\mathrm b}^{2}$, since $\tilde u^{*} = \tilde u^{\natural} = \tilde u^{-1}$, so $\tilde U_{\mathrm b} = \sqrt{\tilde U^{*}\tilde U}$ by uniqueness of the square root and hence $\tilde u = \tilde u_{\mathrm r}$.

### The Reconstruction of the Unit-Norm Part

The rotor and the boost reconstitute the unit-norm part,

$$
\tilde U = \tilde U_{\mathrm b}\,\tilde u_{\mathrm r} .
$$

Indeed the same element commutes with itself, $\tilde U(\tilde U^{*}\tilde U) = (\tilde U\tilde U^{*})\tilde U$, so the relation holds between the two Hermitian positive square roots, $\tilde U\sqrt{\tilde U^{*}\tilde U} = \sqrt{\tilde U\tilde U^{*}}\,\tilde U$. Multiplying on the right by $(\sqrt{\tilde U^{*}\tilde U})^{-1}$ and using $\tilde U_{\mathrm b} = \sqrt{\tilde U\tilde U^{*}}$ and $\tilde u_{\mathrm r} = \tilde U(\sqrt{\tilde U^{*}\tilde U})^{-1}$ gives the statement. The left and the right polar decomposition of $\tilde U$ therefore carry the same unitary factor, and the reconstruction reads $\tilde u_{\mathrm r} = \tilde U_{\mathrm b}^{\natural}\tilde U$, since $\tilde U_{\mathrm b}^{-1} = \tilde U_{\mathrm b}^{\natural}$.

### Its Unitarity and Its Reality

It is unitary, preserving the sesquilinear form (*Conventions in Mathematics*, §*The Unitary Convention*),

$$
\tilde u_{\mathrm r}\,\tilde u_{\mathrm r}^{*} = \tilde U\bigl(\sqrt{\tilde U^{*}\tilde U}\bigr)^{-1}\bigl(\sqrt{\tilde U^{*}\tilde U}\bigr)^{-1}\tilde U^{*} = \tilde U(\tilde U^{*}\tilde U)^{-1}\tilde U^{*} = e_t ,
$$

and of unit norm by multiplicativity along the reconstruction, $\langle\tilde u_{\mathrm r},\tilde u_{\mathrm r}\rangle_{\natural} = \langle \tilde U,\tilde U\rangle_{\natural}/\langle \tilde U_{\mathrm b},\tilde U_{\mathrm b}\rangle_{\natural} = 1$. An element that is both unitary and of unit norm is a unit real quaternion: such an element is $\exp(i\beta)\tilde q_1$ with $\tilde q_1$ a unit real quaternion and has norm $\exp(2i\beta)$, so $N = 1$ forces $\exp(2i\beta) = 1$. Hence

$$
\tilde u_{\mathrm r} \in \mathrm{Sp}(1) = \{\tilde u \in \mathbb{H} : \tilde u\tilde u^{\natural} = 1\} ,
$$

the group of unit real quaternions. It is compact, and it is the unit factor of the quaternion polar representation of the companion article. By *The Lorentz Group in Biquaternionic Form*, it acts on the material sector as a spatial rotation; the central phase has been split off from it, which distinguishes it from the group of unitary elements $\mathrm{U}(\mathbb{B})$.

### The Closed Form

The rotor is a real quaternion of unit norm, so it is written through its scalar part and its vector part,

$$
\tilde u_{\mathrm r} = \mathrm{Sc}(\tilde u_{\mathrm r})\,e_t + \mathrm{Vec}(\tilde u_{\mathrm r}) , \qquad \mathrm{Sc}(\tilde u_{\mathrm r}) \in \mathbb{R} , \qquad \mathrm{Vec}(\tilde u_{\mathrm r}) \in \mathbb{R}^3 , \qquad \mathrm{Sc}(\tilde u_{\mathrm r})^2 + \lvert \mathrm{Vec}(\tilde u_{\mathrm r})\rvert^2 = 1 ,
$$

the vector part being real and pure, so that its square is minus its squared length and the unit norm is the **sum** of the two squared lengths, unlike the boost, whose unit norm is the difference. The exponential writing is the same element with scalar part $\cos\tfrac{\theta}{2}$ and vector part $\sin\tfrac{\theta}{2}\,\vec u_{\mathrm r}$, so the comparison reads

$$
\cos\frac{\theta}{2} = \mathrm{Sc}(\tilde u_{\mathrm r}) , \qquad \sin\frac{\theta}{2} = \lvert \mathrm{Vec}(\tilde u_{\mathrm r})\rvert , \qquad \vec u_{\mathrm r} = \frac{\mathrm{Vec}(\tilde u_{\mathrm r})}{\lvert \mathrm{Vec}(\tilde u_{\mathrm r})\rvert} .
$$

The stored half-angle lies in $[0,\pi]$, so the angle and the axis are read off the rotor by

$$
\theta = 2\arccos \mathrm{Sc}(\tilde u_{\mathrm r}) \in [0,2\pi] , \qquad \vec u_{\mathrm r} = \frac{\mathrm{Vec}(\tilde u_{\mathrm r})}{\lvert \mathrm{Vec}(\tilde u_{\mathrm r})\rvert} .
$$

The axis is defined whenever the vector part is nonzero, that is, away from $\theta = 0$ and $\theta = 2\pi$; at $\tilde u_{\mathrm r} = \pm e_t$ the vector part vanishes, the rotation is the identity or the full turn, and there is no axis. On the element the rotor is the unitary factor of the right polar decomposition,

$$
\tilde u_{\mathrm r} = \tilde U\bigl(\sqrt{\tilde U^{*}\tilde U}\bigr)^{-1} = \tilde U\bigl(\sqrt{\tilde U^{*}\tilde U}\bigr)^{\natural} = \tilde U_{\mathrm b}^{\natural}\tilde U ,
$$

the inverse being the quaternion conjugate because the root is Hermitian of unit norm, the root itself having the closed form $\sqrt{\tilde U^{*}\tilde U} = (\tilde U^{*}\tilde U+e_t)/\sqrt{2(1+\mathrm{Sc}(\tilde U^{*}\tilde U))}$, and the last form being the reconstructed one. So the two parts of the rotor, and with them $\theta$ and $\vec u_{\mathrm r}$, are read from the coefficients of $\tilde U$ alone, as $\psi$ and $\vec u_{\mathrm b}$ are read from those of $\tilde U\tilde U^{*}$.

### The Real Quaternions

If all four coefficients of $\tilde{Q}$ are real then $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \sum_\mu q_\mu^2$ is a positive real, so $\alpha = 0$ and $r = \lvert\tilde{Q}\rvert$ is the quaternion modulus. Then $\tilde U = \tilde{Q}/r$ is a unit real quaternion and $\tilde U\tilde U^{*} = \tilde U\tilde U^{\natural} = e_t$, so $\tilde U_{\mathrm b} = e_t$ and $\tilde u_{\mathrm r} = \tilde U$. The real quaternions have no boost, and their polar representation is the quaternion polar representation term by term.

### The Conjugations and the Degenerate Cases

Under the conjugations the rotor is fixed by the coefficientwise conjugation and inverted by the quaternion and the Hermitian conjugation,

$$
\bar{\tilde u_{\mathrm r}} = \tilde u_{\mathrm r} , \qquad \tilde u_{\mathrm r}^{\natural} = \tilde u_{\mathrm r}^{*} = \tilde u_{\mathrm r}^{-1} .
$$

The rotor is trivial exactly when the unit-norm part $\tilde U$ is Hermitian positive, that is, when $\tilde{Q} = \Rho\,\tilde U_{\mathrm b}$.

## The Theorem

### Statement

**Theorem (polar representation).** Let $\tilde{Q}\in\mathbb{B}$ with $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\neq0$. Then there are unique

$$
r \in \mathbb{R}, \quad r>0, \qquad \alpha \in \left(-\frac{\pi}{2},\frac{\pi}{2}\right], \qquad \tilde U_{\mathrm b} \in \mathbb{M}_+, \qquad \tilde u_{\mathrm r} \in \mathrm{Sp}(1),
$$

such that

$$
\tilde{Q} = r\,\exp(i\alpha)\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r} , \qquad \langle \tilde U_{\mathrm b},\tilde U_{\mathrm b}\rangle_{\natural} = \langle \tilde u_{\mathrm r},\tilde u_{\mathrm r}\rangle_{\natural} = 1 , \qquad \tilde U_{\mathrm b}^{*} = \tilde U_{\mathrm b} .
$$

Equivalently $\tilde{Q} = \Rho\,\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ with $\Rho = r\exp(i\alpha) = \sqrt{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}}$ the principal square root.

### Existence

The construction of §*The Boost* and §*The Rotor* gives the factors: $\Rho$ from the branch of the square root of the norm, $\tilde U = \tilde{Q}/\Rho$ of unit norm, $\tilde U_{\mathrm b} = \sqrt{\tilde U\tilde U^{*}}$ the unique Hermitian positive square root of $\tilde U\tilde U^{*}$, and $\tilde u_{\mathrm r} = \tilde U(\sqrt{\tilde U^{*}\tilde U})^{-1}$ the unitary factor of the right polar decomposition of $\tilde U$, unitary and of unit norm, hence a unit real quaternion. The reconstruction of §*The Rotor* is $\tilde U = \tilde U_{\mathrm b}\tilde u_{\mathrm r}$, so the product reproduces the element,

$$
r\,\exp(i\alpha)\tilde U_{\mathrm b}\tilde u_{\mathrm r} = \Rho\,\tilde U = \tilde{Q} .
$$

### Uniqueness

Suppose $\tilde{Q} = r \exp(i\alpha)\tilde U_{\mathrm b}\tilde u_{\mathrm r} = r'\exp(i\alpha')\tilde U_{\mathrm b}'\tilde u_{\mathrm r}'$ with both quadruples admissible. Taking norms and using $\langle \tilde U_{\mathrm b}\tilde u_{\mathrm r},\tilde U_{\mathrm b}\tilde u_{\mathrm r}\rangle_{\natural} = 1$ gives $r^2\exp(2i\alpha) = (r')^2\exp(2i\alpha')$, so the two principal square roots of $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}$ agree, and since $r,r' > 0$ with $\alpha,\alpha'$ in the same half-open interval of length $\pi$, one has $r = r'$ and $\alpha = \alpha'$. Then $\tilde U = \tilde{Q}/\Rho$ is the same in both, so $\tilde U\tilde U^{*}$ is the same, and its Hermitian positive square root is unique, so $\tilde U_{\mathrm b} = \tilde U_{\mathrm b}'$; then $\tilde u_{\mathrm r} = \tilde U_{\mathrm b}^{-1}\tilde U = \tilde u_{\mathrm r}'$.

## The Procedure in Practice

The representation of §*The Theorem* is an existence proof; the procedure below is the algorithm that proof contains. In the matrix picture it is the polar decomposition of $\mathrm{GL}(2,\mathbb{C})$, and it restricts to $\mathrm{SL}(2,\mathbb{C})$ on the unit-norm elements: the positive definite Hermitian factor of $\mathsf{M}_2(\tilde{Q})$ is $r\,\tilde U_{\mathrm b}$, its unitary factor is $\exp(i\alpha)\tilde u_{\mathrm r}$, and the scale and the phase are the split of the complex modulus $\Rho$ (*The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*). The section records the two invariants read off the element, the five steps in their forced order, the factors as closed expressions in the coordinates, the exponents collected with their half-angles, and three worked examples. The theoretical statements are those of §*The Scale* to §*The Rotor*; only the coordinate form and the examples are added. Every numerical value displayed below was recomputed in double precision.

### The Two Invariants

#### The Norm and the Euclidean Square

Two numbers are read off the four complex coordinates $Q_t,Q_x,Q_y,Q_z$, and the whole procedure turns on them:

$$
N = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = \sum_{\mu\in\{t,x,y,z\}}Q_\mu^{2}\in\mathbb{C} , \qquad E^{2} = \langle\tilde{Q},\tilde{Q}\rangle_{*} = \sum_{\mu\in\{t,x,y,z\}}\lvert Q_\mu\rvert^{2}\in\mathbb{R} .
$$

The first is the biquaternion norm of §*The Scale*; the second is the Hermitian form whose square root is the Euclidean norm $\lVert\tilde{Q}\rVert_{E}$. The two are two of the four forms of the algebra (*The 4 Forms over the Biquaternioid $\mathbb{C}$ Space*). The first is complex and central, the second is a sum of non-negative terms and is therefore real and non-negative. They are tied by

$$
E^{2}\ \ge\ \lvert N\rvert ,
$$

with equality exactly when the vector part of $\tilde{Q}\tilde{Q}^{*}$ vanishes, that is, when the boost is trivial: the inequality is the Cauchy–Schwarz inequality on the complex vector $(Q_t,Q_x,Q_y,Q_z)$.

**Comment.** The inequality is what makes the square roots of the procedure harmless. It gives $E^{2}+\lvert N\rvert > 0$ for every element of the domain, so no denominator below can vanish; it gives $\cosh\psi = E^{2}/\lvert N\rvert \ge 1$, so the rapidity read off the element is a real number; and it gives $\lvert\mathrm{Vec}(\tilde{Q}\tilde{Q}^{*})\rvert^{2} = E^{4}-\lvert N\rvert^{2} \ge 0$, so the boost axis is defined whenever the vector part is nonzero; the equality case is the trivial boost, where the axis is undefined, and it is the only degenerate case that the two numbers can detect.

#### The Hermitian Product and Its Vector Part

The vector part of the Hermitian product is where the relative phases of the coordinates first enter the procedure. Write $\vec Q = (Q_x,Q_y,Q_z)$ for the vector part of the four complex coordinates, so that $\overline{\vec Q} = (\overline{Q_x},\overline{Q_y},\overline{Q_z})$.

$$
\tilde{Q}\tilde{Q}^{*} = E^{2}\,e_t + i\,\mathrm{Vec}(\tilde{Q}\tilde{Q}^{*}) , \qquad \lvert\mathrm{Vec}(\tilde{Q}\tilde{Q}^{*})\rvert^{2} = E^{4}-\lvert N\rvert^{2} , \qquad
W_k = \operatorname{Im}\Bigl[\overline{Q_t}\,Q_k - Q_t\,\overline{Q_k} - (\vec Q\times\overline{\vec Q})_k\Bigr] , \quad k = 1,2,3 .
$$

Every bracket is purely imaginary, so each $W_k$ is real. The scalar part of the Hermitian product is the Euclidean square, the biquaternion norm of the Hermitian product is $N\overline N = \lvert N\rvert^{2}$, and the last identity is the multiplicativity of the norm read on that product.

**Comment.** The three sources of the vector part are the phase of $Q_t$ against the phases of the vector coordinates, in the first two terms of the bracket, and the phases of the vector coordinates against one another, in the cross product. The boost axis is $\vec u_{\mathrm b} = \mathrm{Vec}(\tilde{Q}\tilde{Q}^{*})/\lvert\mathrm{Vec}(\tilde{Q}\tilde{Q}^{*})\rvert$, so this is where the direction of the boost is decided.

#### What the Two Invariants Fix and What They Cannot

The pair $(N,E^{2})$ fixes the scale, the phase and the rapidity. The norm $\langle\cdot\rangle_{\natural}$ gives the modulus, hence the scale $r = \lvert N\rvert^{1/2}$ and the phase $\alpha = \tfrac12\arg N$; the ratio $E^{2}/\lvert N\rvert$ gives the rapidity through $\cosh\psi = E^{2}/\lvert N\rvert$.

The pair cannot give the two directions. Conjugating by a real unit quaternion $\tilde u$, so that $\vec Q\mapsto \tilde u\vec Q\tilde u^{-1}$ and $Q_t$ is unchanged, leaves both $\langle\cdot\rangle_{\natural}$ and $E^{2}$ unchanged, since a real rotation preserves $\sum_kQ_k^{2}$ and $\sum_k\lvert Q_k\rvert^{2}$, and carries $\mathrm{Vec}(\tilde{Q}\tilde{Q}^{*})$ to $\tilde u\mathrm{Vec}(\tilde{Q}\tilde{Q}^{*})\tilde u^{-1}$, so the axis turns while the pair stands still. Over $100$ random elements and random rotations the pair was invariant to $1.1\times10^{-14}$, the vector part reproduced the rotated vector to $4.4\times10^{-15}$, and the axis itself moved by more than $0.3$ in almost every draw.

The count is the same statement. The four complex coordinates carry eight real numbers. The pair $(N,E^{2})$ accounts for three of them, the scale, the phase and the rapidity, and the remaining five are the two numbers of the boost axis, the two numbers of the rotor axis, and the rotation angle. The two axes come from the phases of the coordinates, through $\mathrm{Vec}(\tilde{Q}\tilde{Q}^{*})$ and through the real parts of $Q_\mu \exp(-i\alpha)$.

### The Five Steps

Given $\tilde{Q}$ with $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\neq0$:

1. Compute the biquaternion norm $N = \sum_\mu Q_\mu^2 \in \mathbb{C}$.
2. Take its principal square root: write $N = \lvert N\rvert\exp(i\varphi)$ with $\varphi\in(-\pi,\pi]$, and put $\Rho = \sqrt{\lvert N\rvert}\exp(i\varphi/2)$, so that $r = \sqrt{\lvert N\rvert}$ and $\alpha = \varphi/2$.
3. Put $\tilde U = \tilde{Q}/\Rho$, of unit norm.
4. Compute the Hermitian element $\tilde U\tilde U^{*}$, and write it as $\mathrm{Sc}(\tilde U\tilde U^{*}) e_t + i\mathrm{Vec}(\tilde U\tilde U^{*})$ with $\mathrm{Sc}(\tilde U\tilde U^{*})\in\mathbb{R}$, $\mathrm{Vec}(\tilde U\tilde U^{*})\in\mathbb{R}^3$; then put
   $\tilde U_{\mathrm b} = \sqrt{\frac{1+\mathrm{Sc}(\tilde U\tilde U^{*})}{2}}\,e_t + \frac{i\mathrm{Vec}(\tilde U\tilde U^{*})}{\sqrt{2(1+\mathrm{Sc}(\tilde U\tilde U^{*}))}}$, and read the rapidity and axis off by $\cosh\psi = \mathrm{Sc}(\tilde U\tilde U^{*})$, $\vec u_{\mathrm b} = \mathrm{Vec}(\tilde U\tilde U^{*})/\lvert\mathrm{Vec}(\tilde U\tilde U^{*})\rvert$; when $\mathrm{Vec}(\tilde U\tilde U^{*})=0$ the boost is $\tilde U_{\mathrm b}=e_t$ and no axis is read.
5. Put $\tilde u_{\mathrm r} = \tilde U(\sqrt{\tilde U^{*}\tilde U})^{-1} = \tilde U_{\mathrm b}^{\natural}\tilde U$, the unitary factor of the right polar decomposition of $\tilde U$, and verify that its coefficients are real and that $\langle\tilde u_{\mathrm r},\tilde u_{\mathrm r}\rangle_{\natural} = 1$.

The factors so obtained satisfy $\tilde{Q} = r \exp(i\alpha)\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ identically.

**Comment on step 1.** Step 1 is a test before it is a computation. If $N = 0$ the element is zero or a zero divisor, no factor of the word exists, and the procedure stops. The domain of the representation is the complement of the null cone, and the test is the first thing to perform.

**Comment on step 2.** Step 2 is the only step that requires a convention, and it carries the whole of it: the branch of the square root is fixed once and for all by $\alpha\in(-\pi/2,\pi/2]$, the closed right half plane. The other root $-\Rho$ has angle $\alpha\pm\pi$ and is outside the interval. Every other step is forced.

**Comment on step 3.** Step 3 is a division by a complex number, that is, a multiplication by its inverse, and it costs nothing: $1/\Rho = \exp(-i\alpha)/r$. Its only role is to put the element on the unit-norm sphere, so that the remaining content of the decomposition is the split of a unit element into a boost and a rotor.

**Comment on step 4.** Step 4 is the only step that is not rational in the coordinates: it needs the positive square root of the Hermitian element $\tilde U\tilde U^{*}$, and the closed form above is that square root written in the algebra. The element $\tilde U\tilde U^{*}$ is Hermitian and positive definite, of unit norm, hence $\mathrm{Sc}(\tilde U\tilde U^{*})^{2}-\lvert\mathrm{Vec}(\tilde U\tilde U^{*})\rvert^{2} = 1$ and $\mathrm{Sc}(\tilde U\tilde U^{*})\ge1$, and the two Hermitian square roots of $\tilde U\tilde U^{*}$ are $\pm\tilde U_{\mathrm b}$; the positive one is taken. The rapidity and the axis are read off the two data of $\tilde U\tilde U^{*}$: $\cosh\psi = \mathrm{Sc}(\tilde U\tilde U^{*})$ and, when $\mathrm{Vec}(\tilde U\tilde U^{*})\neq0$, $\vec u_{\mathrm b} = \mathrm{Vec}(\tilde U\tilde U^{*})/\lvert\mathrm{Vec}(\tilde U\tilde U^{*})\rvert$; when the vector part vanishes the boost is $e_t$ and the axis is undefined.

**Comment on step 5.** Step 5 is a subtraction in disguise, and it needs no square root. The rotor is what is left of the unit element after the Hermitian positive part is divided out, and it is real because the division cancels the Hermitian part exactly: $\tilde U = \tilde U_{\mathrm b}\tilde u_{\mathrm r}$, and the rotor has as many real parameters as the boost has imaginary coefficients.

### The Order of the Steps

The procedure opens with a test and not with a computation: form the biquaternion norm $\langle\cdot\rangle_{\natural}$. If $N = 0$ the element is zero or a zero divisor, no factor of the word exists, and the whole of the above is empty; the domain of the representation is the complement of the null cone, which is the first thing to establish. If $N\neq0$ the order is forced and has no freedom left: the modulus $\Rho$ comes first, because it is the only step that needs the branch choice; the normalised element $\tilde U$ comes second, because every later step divides by $\Rho$ or by a function of it; the Hermitian element $\tilde U\tilde U^{*}$ comes third, because the boost is its root; and the rotor comes last, as the unitary factor of the right polar decomposition of $\tilde U$. No step can be moved, and no step needs a second convention. The order of the four **factors** in the word is a separate statement, recorded in §*The Order of the Boost and the Rotor*.

### Each Factor in a Sentence

| # | factor | what it is | where it lies |
|---|---|---|---|
| 1 | $r$ | the positive real absolute value of the modulus, central and non-compact | the positive real line, in the centre |
| 2 | $\exp(i\alpha)$ | the central phase, the only compact central factor | the unit circle of the centre |
| 3 | $\tilde U_{\mathrm b}$ | the Hermitian positive unit element, the Lorentz boost | $\mathbb{M}_+$ |
| 4 | $\tilde u_{\mathrm r}$ | the unit real quaternion, the spatial rotation | $\mathbb{H}_{\mathbb{B}}$ |

The dimensions are $1+1+3+3 = 8$, which is the real dimension of the algebra: the decomposition is a change of coordinates on the complement of the null cone, with as many real parameters as the ambient algebra has, and the same count as the real dimension of $\mathrm{GL}(2,\mathbb{C})$ in the matrix picture.

### The Factors in the Coordinates of $\tilde{Q}$

The five steps are formulas, and each factor is a closed expression in the four complex coordinates $Q_t,Q_x,Q_y,Q_z$. The expressions use **two numbers read off the coordinates**: the biquaternion norm $\langle\cdot\rangle_{\natural}$ and the Euclidean square $E^{2}$ of §*The Two Invariants*.

| factor | in the coordinates of $\tilde{Q}$, the norm $\langle\cdot\rangle_{\natural}$ and the Euclidean square $E^{2}$ |
|---|---|
| modulus | $\Rho = \sqrt{N} = r\,\exp(i\alpha)$, the principal square root |
| scale | $r = \lvert N\rvert^{1/2}$ |
| phase | $\alpha = \tfrac12\arg N$, with $\arg N \in (-\pi,\pi]$, so $\alpha \in \left(-\tfrac{\pi}{2},\tfrac{\pi}{2}\right]$ |
| normalised element | $U_\mu = \dfrac{Q_\mu}{\Rho} = \dfrac{Q_\mu\,\exp(-i\alpha)}{r}$ |
| boost, scalar part | $\cosh\dfrac{\psi}{2} = \sqrt{\dfrac{E^{2}+\lvert N\rvert}{2\,\lvert N\rvert}}$ |
| boost, vector part | $\sinh\dfrac{\psi}{2}\,\vec u_{\mathrm b} = \dfrac{\mathrm{Vec}(\tilde{Q}\tilde{Q}^{*})}{\sqrt{2\,\lvert N\rvert\,(E^{2}+\lvert N\rvert)}}$ |
| rapidity | $\cosh\psi = \dfrac{E^{2}}{\lvert N\rvert}$, and the speed $\tanh\dfrac{\psi}{2} = \sqrt{\dfrac{E^{2}-\lvert N\rvert}{E^{2}+\lvert N\rvert}}$ |
| rotor | $\tilde u_{\mathrm r,\mu} = \sqrt{\dfrac{2}{E^{2}+\lvert N\rvert}}\;\operatorname{Re}\!\bigl(Q_\mu\,\exp(-i\alpha)\bigr)$, $\mu\in\{t,x,y,z\}$ |

The vector part of the boost is read off the Hermitian product $\tilde{Q}\tilde{Q}^{*}$, which is the quantity $r^{2}\tilde U\tilde U^{*}$ of step 4,

$$
\tilde{Q}\tilde{Q}^{*} = E^{2}\,e_t + i\,\mathrm{Vec}(\tilde{Q}\tilde{Q}^{*}) , \qquad
\tilde U_{\mathrm b} = \sqrt{\frac{E^{2}+\lvert N\rvert}{2\,\lvert N\rvert}}\;e_t + \frac{i\,\mathrm{Vec}(\tilde{Q}\tilde{Q}^{*})}{\sqrt{2\,\lvert N\rvert\,(E^{2}+\lvert N\rvert)}} , \qquad
\lvert\mathrm{Vec}(\tilde{Q}\tilde{Q}^{*})\rvert^{2} = E^{4}-\lvert N\rvert^{2} .
$$

The rapidity datum $\mathrm{Sc}(\tilde U\tilde U^{*})$ of §*The Closed Form* under §*The Boost* is the ratio $\mathrm{Sc}(\tilde U\tilde U^{*}) = E^{2}/\lvert N\rvert$, and the boost datum $\mathrm{Vec}(\tilde U\tilde U^{*})$ of that section is $\mathrm{Vec}(\tilde{Q}\tilde{Q}^{*})/\lvert N\rvert$.

**Comment.** The table is the algorithm in one glance: two rows are read off $\langle\cdot\rangle_{\natural}$ alone, the two boost rows are read off $E^{2}$ against $\lvert N\rvert$ and off $\mathrm{Vec}(\tilde{Q}\tilde{Q}^{*})$, and the last row is the projection of the coordinates on the phase direction. Every entry is a closed expression, so no iteration, no search and no series occurs anywhere in the procedure except in the one square root of $\Rho$ that step 2 fixes by convention.

**Check on the first example below.** For $\tilde{Q} = (1+i)e_t+\vec e_x+2\vec e_y$ the pair is $N = 5+2i$ and $E^{2} = 7$, so the table gives $\lvert N\rvert = \sqrt{29} = 5.385164807$, $r = 2.320595787$, $\alpha = 0.190253189$, $\mathrm{Sc}(\tilde U\tilde U^{*}) = E^{2}/\lvert N\rvert = 1.299867367$, speed $\sqrt{(7-\sqrt{29})/(7+\sqrt{29})} = 0.361088126$ and boost scalar $\sqrt{(7+\sqrt{29})/(2\sqrt{29})} = 1.072349609$, all of them the values computed step by step; the Hermitian product is $\tilde{Q}\tilde{Q}^{*} = 7\,e_t - 2i\,\vec e_x - 4i\,\vec e_y$, of vector part $\mathrm{Vec}(\tilde{Q}\tilde{Q}^{*}) = (-2,-4,0)$, and the rotor coefficients $\sqrt{2/(7+\sqrt{29})}\,\operatorname{Re}(Q_\mu \exp(-i\alpha))$ are $0.470592172$, $0.394599292$, $0.789198585$ and $0$.

### The Exponents and the Half-Angles

Each factor is the exponential of a single element of the algebra, and the exponent is a real parameter times a root of $-e_t$, $0$ or $+e_t$; the character of the exponential is fixed by the square of its root, as recorded in the introduction. The positions of the exponents in the algebra are:

| factor | exponent | where the exponent lies |
|---|---|---|
| $r$ | $\ln r$ | the real line $\mathbb{R}e_t$ |
| $\exp(i\alpha)$ | $i\alpha$ | the imaginary line $i\mathbb{R}\subset\mathbb{C}_{\mathbb{B}}$ |
| $\tilde U_{\mathrm b}$ | $i\frac{\psi}{2}\vec u_{\mathrm b}$ | $\mathbb{M}_+$, traceless |
| $\tilde u_{\mathrm r}$ | $\frac{\theta}{2}\vec u_{\mathrm r}$ | $\mathbb{M}_- \cap \mathrm{Vect}(\mathbb{B})$, the real pure quaternions |

The two central exponents commute with everything and with each other; the two non-central exponents do not commute unless the two axes coincide or one of the factors is trivial. That is the content of §*The Order of the Boost and the Rotor*, and the third example below witnesses the size.

The exponents of the two non-central factors carry **half** of the parameter of the transformation they produce. The boost exponent is $i(\psi/2)\vec u_{\mathrm b}$ with $\psi$ the rapidity, and the conjugation by the boost produces a Lorentz transformation of rapidity $\psi$; the rotor exponent is $(\theta/2)\vec u_{\mathrm r}$ with $\theta$ the rotation angle, and the conjugation by the rotor produces a rotation by $\theta$. The doubling is the double cover of the two groups, and it is why the parameters of §*The Two Invariants* come back with a factor two: the dictionary of the half-angles is

$$
\cosh\frac{\psi}{2} = \sqrt{\frac{1+\mathrm{Sc}(\tilde U\tilde U^{*})}{2}} , \qquad \sinh\frac{\psi}{2} = \frac{\lvert\mathrm{Vec}(\tilde U\tilde U^{*})\rvert}{\sqrt{2(1+\mathrm{Sc}(\tilde U\tilde U^{*}))}} , \qquad \cos\frac{\theta}{2} = u_{\mathrm r,0} , \qquad \sin\frac{\theta}{2} = \lvert\mathrm{Vec}(\tilde u_{\mathrm r})\rvert ,
$$

with $\mathrm{Sc}(\tilde U\tilde U^{*}) = E^{2}/\lvert N\rvert$ and $\mathrm{Vec}(\tilde U\tilde U^{*}) = \mathrm{Vec}(\tilde{Q}\tilde{Q}^{*})/\lvert N\rvert$ the data of $\tilde U\tilde U^{*}$. The last two are read off the rotor itself: the scalar coefficient of a unit real quaternion is the cosine of the half-angle, and the length of its vector part the sine.

### Worked Example: an Element Given by Its Coordinates

Take

$$
\tilde{Q} = (1+i)e_t + \vec e_x + 2\vec e_y ,
$$

whose coefficients are $Q_t = 1+i$, $Q_x = 1$, $Q_y = 2$, $Q_z = 0$.

*Step 1.* The biquaternion norm is $N = (1+i)^2+1^2+2^2+0 = 2i+5 = 5+2i$, of modulus $\lvert N\rvert = \sqrt{29} = 5.385164807$ and argument $\arg N = 0.380506377$ rad.

*Step 2.* The modulus is $\Rho = \sqrt{5.385164807}\,\exp(0.190253189\,i) = 2.278723854 + 0.438842117 i$, hence

$$
r = 2.320595787 , \qquad \alpha = 0.190253189\ \text{rad} \approx 10.9007^\circ .
$$

*Step 3.* Dividing, $\tilde U = \tilde{Q}/\Rho$ has coefficients

$$
U_t = 0.504639332+0.341657461i, \quad U_x = 0.423148397-0.081490935i, \quad U_y = 0.846296793-0.162981871i, \quad U_z = 0 ,
$$

and $\langle \tilde U,\tilde U\rangle_{\natural} = 1$ as required.

*Step 4.* The Hermitian element $\tilde U\tilde U^{*}$ is

$$
\tilde U\tilde U^{*} = 1.299867367\,e_t - 0.371390676\,i\,\vec e_x - 0.742781353\,i\,\vec e_y ,
$$

so $\mathrm{Sc}(\tilde U\tilde U^{*}) = 1.299867367$, $\mathrm{Vec}(\tilde U\tilde U^{*}) = (-0.371390676, -0.742781353, 0)$ and $\lvert\mathrm{Vec}(\tilde U\tilde U^{*})\rvert = 0.830454799$; the identity $\mathrm{Sc}(\tilde U\tilde U^{*})^2-\lvert\mathrm{Vec}(\tilde U\tilde U^{*})\rvert^2 = 1$ holds to $7\times10^{-16}$. The boost is therefore

$$
\tilde U_{\mathrm b} = 1.072349609\,e_t - 0.173166789\,i\,\vec e_x - 0.346333577\,i\,\vec e_y ,
$$

with rapidity $\psi = 2\operatorname{arccosh}(1.072349609) = 0.756273220$, corresponding to the speed $\tanh(\psi/2) = 0.361088126$ in units $c = 1$, and axis $\vec u_{\mathrm b} = -(1,2,0)/\sqrt{5}$. The verification $\tilde U_{\mathrm b}^2 = \tilde U\tilde U^{*}$ was carried out to $2.2\times10^{-16}$ in the coefficients.

*Step 5.* The rotor is

$$
\tilde u_{\mathrm r} = \tilde U_{\mathrm b}^{\natural}\tilde U = 0.470592172\,e_t + 0.394599292\,\vec e_x + 0.789198585\,\vec e_y ,
$$

all of whose coefficients are real, with $\langle\tilde u_{\mathrm r},\tilde u_{\mathrm r}\rangle_{\natural} = 1$; its rotation angle is $\theta = 2.161669$ rad about the axis $(1,2,0)/\sqrt{5}$.

The reconstruction $\tilde{Q} = r \exp(i\alpha)\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ was verified in double precision and agrees with $\tilde{Q}$ to $1.6\times10^{-16}$ in each coefficient. Note that the boost axis and the rotation axis are opposite in this example, which is a coincidence of the element and not a structural relation: no relation between the two axes is imposed by the decomposition, and a random element generally has them unrelated.

*The four exponents of this example.* The four factors are exponentials, and their exponents to the nine decimals used above are

$$
\ln r = 0.841823957 , \qquad \alpha = 0.190253189 , \qquad \frac{\psi}{2} = 0.378136610 , \qquad \frac{\theta}{2} = 1.080834539 ,
$$

the boost about $\vec u_{\mathrm b} = -(1,2,0)/\sqrt5$ and the rotor about $\vec u_{\mathrm r} = (1,2,0)/\sqrt5$, so that the word is the ordered product of four exponentials

$$
\tilde{Q} = \exp(0.841823957)\,\exp(0.190253189\,i)\,\exp\bigl(i\,0.378136610\,\vec u_{\mathrm b}\bigr)\,\exp\bigl(1.080834539\,\vec u_{\mathrm r}\bigr) .
$$

Rebuilding $\tilde U_{\mathrm b}$ and $\tilde u_{\mathrm r}$ from the last two exponents reproduces the factors of Steps 4 and 5; the full parameters are the rapidity $\psi = 0.756273220$ and the rotation angle $\theta = 2.161669078$, each twice its stored half.

### Worked Example: an Element Already in the Polar Form

Take the Lorentz boost biquaternion of the physics articles with speed $0.6c$ along $\vec e_x$,

$$
\tilde Q = \cosh\frac{\psi}{2}\,e_t + i\sinh\frac{\psi}{2}\,\vec e_x , \qquad \psi = \operatorname{atanh}0.6 = 0.693147181 ,
$$

so that $\tilde Q = 1.060660172\,e_t + 0.353553391\,i\,\vec e_x$. Its biquaternion norm is $N = \cosh^2\frac{\psi}{2}-\sinh^2\frac{\psi}{2} = 1$, a positive real, so the modulus is $\Rho = 1$, the scale is $r = 1$ and the phase is $\alpha = 0$. The remaining construction returns $\tilde U = \tilde Q$, $\tilde U\tilde U^{*} = \tilde Q^{2}$, $\tilde U_{\mathrm b} = \tilde Q$ and $\tilde u_{\mathrm r} = e_t$, so that the four-factor form collapses to

$$
\tilde Q = 1\cdot \exp(i\cdot0)\cdot\tilde U_{\mathrm b}\cdot e_t .
$$

The example is the reason the representation is a strict refinement of the physics convention: a Lorentz rotor is already in polar form, with two of its four factors trivial. In the language of the two invariants, the norm is real positive, so the phase vanishes, and the Hermitian product is already its own square root in the sense of step 4.

### Worked Example: an Element Built from Its Four Factors

The last example runs the procedure in the other direction. The four factors are chosen first, with rational data, the element is multiplied out, and the algorithm is then asked to recover the factors it was given. Take

$$
r\,\exp(i\alpha) = 2+i , \qquad \tilde U_{\mathrm b} = \frac54\,e_t + \frac{9}{20}\,i\,\vec e_x + \frac35\,i\,\vec e_y , \qquad \tilde u_{\mathrm r} = \frac45\,e_t + \frac35\,\vec e_z .
$$

The data are those of the exponentials: $\Rho = 2+i$ has $r = \sqrt5 = 2.236067977$ and $\alpha = \operatorname{atan}\tfrac12 = 0.463647609$; the boost has $\cosh\frac{\psi}{2} = \frac54$ and $\sinh\frac{\psi}{2} = \frac34$ about the axis $\vec u_{\mathrm b} = (3,4,0)/5 = (0.6,0.8,0)$, so $\frac{\psi}{2} = \operatorname{arcosh}\frac54 = \ln 2$ and the rapidity is $\psi = 2\ln2 = 1.386294361$; the rotor has $\frac{\theta}{2} = \operatorname{atan}\frac34$, so $\theta = 1.287002218$ about $\vec u_{\mathrm r} = \vec e_z$. Both non-central factors are unit elements, and the two axes are perpendicular, the case in which the two non-central exponents commute least.

Multiplying the factors gives

$$
\tilde{Q} = (2+i)e_t + \left(-\tfrac{18}{25}+\tfrac{36}{25}i\right)\vec e_x + \left(-\tfrac{21}{100}+\tfrac{21}{50}i\right)\vec e_y + \left(\tfrac32+\tfrac34 i\right)\vec e_z ,
$$

that is $Q_t = 2+i$, $Q_x = -0.72+1.44i$, $Q_y = -0.21+0.42i$, $Q_z = 1.5+0.75i$. Now apply the algorithm to this element, forgetting how it was made.

*Step 1.* The norm is

$$
N = (2+i)^2 + \left(-\tfrac{18}{25}+\tfrac{36}{25}i\right)^2 + \left(-\tfrac{21}{100}+\tfrac{21}{50}i\right)^2 + \left(\tfrac32+\tfrac34 i\right)^2 = 3+4i ,
$$

of modulus $\lvert N\rvert = 5$ and argument $\arg N = \operatorname{atan}\tfrac43 = 0.927295218$. The imaginary part is not accidental: it is the phase of the central factor, and it returns in step 2.

*Step 2.* The modulus is $\Rho = \sqrt5\,\exp(0.463647609\,i) = 2+i$, exactly the central factor that was used to build the element, since $N = (2+i)^2$. Hence

$$
r = \sqrt5 = 2.236067977 , \qquad \alpha = \operatorname{atan}\tfrac12 = 0.463647609 .
$$

*Step 3.* Dividing, the unit element is

$$
\tilde U = \frac{\tilde{Q}}{\Rho} = e_t + \frac{18}{25}\,i\,\vec e_x + \frac{21}{100}\,i\,\vec e_y + \frac34\,\vec e_z ,
$$

that is $U_t = 1$, $U_x = 0.72i$, $U_y = 0.21i$, $U_z = 0.75$, and indeed $\tilde U = \tilde U_{\mathrm b}\tilde u_{\mathrm r}$.

*Step 4.* The Hermitian element is

$$
\tilde U\tilde U^{*} = \frac{17}{8}\,e_t + \frac98\,i\,\vec e_x + \frac32\,i\,\vec e_y = 2.125\,e_t + 1.125\,i\,\vec e_x + 1.5\,i\,\vec e_y ,
$$

so $\mathrm{Sc}(\tilde U\tilde U^{*}) = \frac{17}{8} = 2.125$, $\mathrm{Vec}(\tilde U\tilde U^{*}) = (\frac98,\frac32,0)$ and $\lvert\mathrm{Vec}(\tilde U\tilde U^{*})\rvert = \frac{15}{8} = 1.875$; the identity $\mathrm{Sc}(\tilde U\tilde U^{*})^2-\lvert\mathrm{Vec}(\tilde U\tilde U^{*})\rvert^2 = 1$ is exact, $\frac{289}{64}-\frac{225}{64} = 1$. The boost is

$$
\tilde U_{\mathrm b} = \sqrt{\frac{1+\mathrm{Sc}(\tilde U\tilde U^{*})}{2}}\,e_t + \frac{i\mathrm{Vec}(\tilde U\tilde U^{*})}{\sqrt{2(1+\mathrm{Sc}(\tilde U\tilde U^{*}))}} = \frac54\,e_t + \frac{9}{20}\,i\,\vec e_x + \frac35\,i\,\vec e_y ,
$$

since $\sqrt{(1+\mathrm{Sc}(\tilde U\tilde U^{*}))/2} = \sqrt{25/16} = \frac54$ and $\lvert\mathrm{Vec}(\tilde U\tilde U^{*})\rvert/\sqrt{2(1+\mathrm{Sc}(\tilde U\tilde U^{*}))} = \frac{15}{8}\cdot\frac25 = \frac34$. The rapidity is $\psi = 2\operatorname{arcosh}\frac54 = 2\ln 2 = 1.386294361$, the speed is $\tanh\frac{\psi}{2} = \frac34/\frac54 = 0.6$, and the axis is $\vec u_{\mathrm b} = \mathrm{Vec}(\tilde U\tilde U^{*})/\lvert\mathrm{Vec}(\tilde U\tilde U^{*})\rvert = (0.6,0.8,0)$.

*Step 5.* The rotor is

$$
\tilde u_{\mathrm r} = \tilde U_{\mathrm b}^{\natural}\tilde U = \frac45\,e_t + \frac35\,\vec e_z ,
$$

with real coefficients, of unit norm, and rotation angle $\theta = 2\operatorname{atan}\frac34 = 1.287002218$ about $\vec e_z$.

The procedure has returned the four factors that were used to build the element, with no residue: the boost matches to $0$ in every coefficient and the rotor to $1.7\times10^{-16}$, and the reconstruction $r\exp(i\alpha)\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ agrees with $\tilde{Q}$ to $5.0\times10^{-16}$ in the largest coefficient.

**Comment on the two orders.** The example shows why the word is ordered. With the two perpendicular axes the two non-central factors do not commute, the two orders differ by

$$
\tilde U_{\mathrm b}\tilde u_{\mathrm r} - \tilde u_{\mathrm r}\tilde U_{\mathrm b} = \frac{18}{25}\,i\,\vec e_x - \frac{27}{50}\,i\,\vec e_y ,
$$

of largest coefficient $0.72$, and the two non-central exponents, $\mathcal H = i\frac{\psi}{2}\vec u_{\mathrm b}$ and $\mathcal R = \frac{\theta}{2}\vec u_{\mathrm r}$, have the non-vanishing bracket

$$
[\mathcal H,\mathcal R] = \mathcal H\mathcal R-\mathcal R\mathcal H = i\,\ln 2\,\operatorname{atan}\tfrac34\left(\tfrac85\,\vec e_x - \tfrac65\,\vec e_y\right) = 0.713665567\,i\,\vec e_x - 0.535249175\,i\,\vec e_y .
$$

The shortcut of replacing the product of the two exponentials by the exponential of their sum fails accordingly: $\lVert\exp(X+Y)-\exp(X)\exp(Y)\rVert = 0.350671030$ in the largest coefficient, while $\exp(X)\exp(Y)$ is $\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ to $2.2\times10^{-16}$. The four exponents of this element are

$$
\ln r = 0.804718956 , \qquad \alpha = 0.463647609 , \qquad \frac{\psi}{2} = 0.693147181 , \qquad \frac{\theta}{2} = 0.643501109 ,
$$

and the word is

$$
\tilde{Q} = \exp(0.804718956)\,\exp(0.463647609\,i)\,\exp\bigl(i\,0.693147181\,\vec u_{\mathrm b}\bigr)\,\exp\bigl(0.643501109\,\vec u_{\mathrm r}\bigr) ,
$$

the product now taken in the order in which the four rows of the exponent table stand.

### The Procedure in One Sentence

The procedure is one test and four forced steps: test $N\neq0$; take the principal root $\Rho$; divide to the unit-norm part; take the Hermitian square root for the boost; multiply $\tilde U$ on the left by the quaternion conjugate of the boost for the rotor. The only convention is the branch of $\Rho$; every other step is a function of the element.

## Summary

Every biquaternion of non-vanishing norm has a unique polar representation

$$
\tilde{Q} = r\,\exp(i\alpha)\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r} = r\,\exp(i\alpha)\,\exp\Bigl(i\tfrac{\psi}{2}\vec u_{\mathrm b}\Bigr)\,\exp\Bigl(\tfrac{\theta}{2}\vec u_{\mathrm r}\Bigr) ,
$$

with $r = \sqrt{\lvert\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\rvert} > 0$, $\alpha = \tfrac{1}{2}\arg \langle\tilde{Q},\tilde{Q}\rangle_{\natural}$, $\tilde U_{\mathrm b}$ the Hermitian positive unit-norm boost and $\tilde u_{\mathrm r}$ the unit real quaternion rotor. The modulus is the complex number $\Rho = r\exp(i\alpha) = \sqrt{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}}$, whose absolute value is the scale, so the phase is a factor in its own right rather than a correction. The four factors are unique, their real dimensions $1+1+3+3$ sum to the eight of the algebra, and the failure of the decomposition is exactly the null cone $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = 0$. The Cartan form of the physics articles is the unit-norm case, in which the scale and the phase are trivial. The procedure of §*The Procedure in Practice* reads the four factors from the coordinates through two invariants: the norm gives the scale and the phase, the Euclidean square with the Hermitian product gives the rapidity and the boost axis, and the real parts of the normalised coordinates give the rotor.

## Summary of Notation

| symbol | set | meaning |
|---|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | — | the biquaternion algebra, $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ |
| $e_t = 1$, $\vec e_x,\vec e_y,\vec e_z$ | basis of $\mathbb{B}$ | the algebra unit and the quaternion units, $\vec e_k^2 = -e_t$, $\vec e_x\vec e_y = \vec e_z$ |
| $Q_\mu$ | $\mathbb{C}$ | the four complex coefficients of $\tilde{Q}$ |
| $i$ | $\mathbb{C}_{\mathbb{B}}$, $i^2 = -1$ | the central scalar imaginary |
| $N = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = \sum_\mu Q_\mu^2$ | $\mathbb{C}$, central | the biquaternion norm |
| $E^{2} = \langle\tilde{Q},\tilde{Q}\rangle_{*} = \sum_\mu \lvert Q_\mu\rvert^{2}$ | $\mathbb{R}$, $E^{2}\ge\lvert N\rvert$ | the Euclidean square, the second invariant of the procedure |
| $\Rho = \sqrt{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}}$ | $\mathbb{C}\setminus\{0\}$ | the complex modulus, the principal square root |
| $r = \sqrt{\lvert\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\rvert}$ | $\mathbb{R}$, $r > 0$ | the scale, a positive real |
| $\alpha = \tfrac{1}{2}\arg \langle\tilde{Q},\tilde{Q}\rangle_{\natural}$ | $\left(-\frac{\pi}{2},\frac{\pi}{2}\right]$ | the phase angle |
| $\tilde U = \tilde{Q}/\Rho$ | $\mathbb{B}^{\times}_1$, $\langle \tilde U\rangle_{\natural}=e_t$ | the unit-norm part |
| $\tilde{Q}\tilde{Q}^{*} = E^{2}e_t + i\,\mathrm{Vec}(\tilde{Q}\tilde{Q}^{*})$ | $\mathbb{M}_+$ | the Hermitian product, whose vector part carries the boost axis, $\lvert\mathrm{Vec}(\tilde{Q}\tilde{Q}^{*})\rvert^{2}=E^{4}-\lvert N\rvert^{2}$ |
| $\tilde U\tilde U^{*}$ | $\mathbb{M}_+$, positive definite, $\langle \tilde U\tilde U^{*}\rangle_{\natural}=e_t$ | the Hermitian positive element, scalar part $\mathrm{Sc}(\tilde U\tilde U^{*})\in\mathbb{R}$, $\mathrm{Sc}(\tilde U\tilde U^{*})\ge1$, vector part $\mathrm{Vec}(\tilde U\tilde U^{*})\in\mathbb{R}^3$ |
| $\tilde U_{\mathrm b} = \sqrt{\tilde U\tilde U^{*}}$ | $\mathbb{M}_+$, positive definite, $\langle\tilde U_{\mathrm b}\rangle_{\natural}=e_t$ | the boost, a Hermitian positive unit element |
| $\psi$ | $\mathbb{R}$, $\psi\ge0$ | the rapidity of the boost |
| $\vec u_{\mathrm b}$ | $\mathcal{A}$, a unit vector of $\mathbb{R}^3$ | the axis of the boost |
| $i\frac{\psi}{2}\vec u_{\mathrm b}$ | $\mathbb{M}_+$, scalar part zero | the boost exponent |
| $\theta$ | $[0,2\pi]$ | the rotation angle of the rotor, whose stored half-angle is $\frac{\theta}{2}\in[0,\pi]$ |
| $\vec u_{\mathrm r}$ | $\mathcal{A}$, a unit vector of $\mathbb{R}^3$ | the axis of the rotor |
| $\frac{\theta}{2}\vec u_{\mathrm r}$ | real pure quaternion | the rotor exponent |
| $\tilde U = \tilde u_{\mathrm r}\sqrt{\tilde U^{*}\tilde U}$, $\tilde u_{\mathrm r} = \tilde U(\sqrt{\tilde U^{*}\tilde U})^{-1} = \tilde U_{\mathrm b}^{\natural}\tilde U$ | $\mathrm{Sp}(1)$ | the rotor, the unitary factor of the right polar decomposition, a unit real quaternion |
| $r\,\exp(i\alpha)\,\exp\bigl(i\frac{\psi}{2}\vec u_{\mathrm b}\bigr)\,\exp\bigl(\frac{\theta}{2}\vec u_{\mathrm r}\bigr)$ | — | the polar word, one positive real and three exponentials |
| $\mathbb{M}_+$ | subspace of $\mathbb{B}$ | the Hermitian subspace, real scalar part and imaginary vector part |
| $\mathbb{M}_-$ | subspace of $\mathbb{B}$ | the anti-Hermitian subspace, the material sector of the physics articles |
| $\mathbb{H}_{\mathbb{B}}$ | subspace of $\mathbb{B}$ | the real quaternion subspace, the fixed space of complex conjugation |
| $\mathrm{Sp}(1)$ | $\lvert\tilde u\rvert = 1$ in $\mathbb{H}$ | the group of unit real quaternions |

## Further Reading

- *The Biquaternioid as a Vector Space over $\mathbb{C}$* (`articles_maths/the-biquaternioid-vector-space-over-c.md`), for the algebra, the four conjugations and the remarkable subspaces.
- *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* (`articles_physics/the-2x2-matrix-element-representation-m2c-of-biquaternions.md`), for the isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$, the determinant, and the matrix polar decomposition that §*The Procedure in Practice* performs.
- *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/the-4-forms-over-the-biquaternioid-c-space.md`), for the two forms that the procedure reads off the element, the complex bilinear norm $\langle\cdot\rangle_{\natural}$ and the Hermitian form, and for the Euclidean norm $\lVert\cdot\rVert_{E}$.
- *The 4 Algebraic Norms over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/the-4-algebraic-norms-over-the-biquaternioid-c-space.md`), for the definiteness of the algebraic norm of $\langle\cdot\rangle_{*}$ and the multiplicativity of $\langle\cdot\rangle_{\natural}$, on which the inequality $E^{2}\ge\lvert N\rvert$ and the identity $\lvert\mathrm{Vec}(\tilde{Q}\tilde{Q}^{*})\rvert^{2}=E^{4}-\lvert N\rvert^{2}$ rest.
- *The Polar Element Representation and Remarkable Subspaces* (`articles_maths/the-polar-element-representation-and-remarkable-subspaces.md`), for the four exponents read against the four coordinate blocks and the six remarkable subspaces, the incidence of the exponents with the subspaces, and the polar data each subspace carries.
- *Split-Biquaternion Polar Element Representation* (`articles_maths/split-biquaternion-polar-element-representation.md`), for the semisimple analogue, whose modulus is split complex and whose rotor is six-dimensional.
- *Quaternion Polar Element Representation* (`articles_maths/quaternion-polar-element-representation.md`), for the two-factor case that this decomposition restricts to on the real quaternions.
- *Complex Polar Element Representation* (`articles_maths/complex-polar-element-representation.md`) and *Split-Complex Polar Element Representation* (`articles_maths/split-complex-polar-element-representation.md`), for the two-dimensional members of the series, where the rule of the exponential is stated once and the slots are counted in the smallest cases.
- *The Lorentz Group in Biquaternionic Form — Structure and Representations* (`articles_physics/the-lorentz-group-in-biquaternionic-form-structure-and-representations.md`), for the boost and rotation rotors and the Thomas-Wigner rotation.
- S. J. Sangwine and E. Hitzer, "Polar decomposition of complexified quaternions and octonions", *Advances in Applied Clifford Algebras* (2020), DOI 10.1007/s00006-020-1048-y; technical report CES-535, University of Essex (2019), for the published two-exponential factorisation of the unit semi-norm elements and, in the general case, its Corollary 1 — whose trigonometric factor is the rotor $\tilde u_{\mathrm r}$ of this article and whose hyperbolic factor is the boost about the rotor-conjugated axis, $\tilde U_{\mathrm b} = \tilde u_{\mathrm r}^{-1}H\tilde u_{\mathrm r}$ with the same rapidity and norm — for Lemma 1, the trichotomy of the exponential of a hypercomplex root of $-1$, $0$ or $+1$, and for the degenerate word on the null cone. The order of the two non-central factors is reversed there, angle first, and the complex modulus is kept whole rather than split into a scale and a phase, which is the difference of count $2+3+3$ against $1+1+3+3$; the corpus fixes the branch and proves uniqueness, while the paper admits both orders.
- Soo-Chang Pei, Ja-Han Chang and Jian-Jiun Ding, "Commutative reduced biquaternions and their Fourier transform for signal and image processing applications", *IEEE Transactions on Signal Processing* **52** (2004) 2012–2022, for the reduced biquaternion algebra — the commutative four-dimensional algebra $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\oplus\mathbb{C}$, equivalently the double-complex, tessarine or commutative hypercomplex algebra — and for its polar form, its uniqueness under the phase-range convention, its De Moivre theorem and the simplified polar form for colour images.
