# __The Polar Element Representation of Biquaternions__

## Introduction

Every biquaternion of non-vanishing norm is the ordered product of a positive real scale, a central phase and two unit factors,

$$
\tilde{Q} = r\,\exp(i\alpha)\,\exp\Bigl(i\tfrac{\psi}{2}\vec u_{\mathrm b}\Bigr)\,\exp\Bigl(\tfrac{\theta}{2}\vec u_{\mathrm r}\Bigr) .
$$

| # | factor | name | exponent | root | range | real dimension |
|---|---|---|---|---|---|---|
| 1 | $r$ | scale | — | — | $r \in \mathbb{R}$, $r>0$ | $1$ |
| 2 | $\exp(i\alpha)$ | central phase | $i\alpha$ | $i$ | $\alpha \in \left(-\frac{\pi}{2},\frac{\pi}{2}\right]$ | $1$ |
| 3 | $\exp\bigl(i\tfrac{\psi}{2}\vec u_{\mathrm b}\bigr)$ | boost | $i\tfrac{\psi}{2}\vec u_{\mathrm b}$ | $i\vec u_{\mathrm b}$ | $\psi \ge0$, $\vec u_{\mathrm b}\in\mathcal{A}$ | $3$ |
| 4 | $\exp\bigl(\tfrac{\theta}{2}\vec u_{\mathrm r}\bigr)$ | rotor | $\tfrac{\theta}{2}\vec u_{\mathrm r}$ | $\vec u_{\mathrm r}$ | $\theta \in [0,2\pi]$, $\vec u_{\mathrm r}\in\mathcal{A}$ | $3$ |

The scale is the only factor that is not an exponential. Each exponent is a real parameter times a **root** of $-e_0$, $0$ or $+e_0$, and the character of the exponential is fixed by the square of its root: $-e_0$ trigonometric, $+e_0$ hyperbolic, $0$ parabolic, the series truncating to the unit plus the exponent. The phase and the rotor therefore stand on a root of $-e_0$, the boost on a root of $+e_0$, and the scale is the degenerate hyperbolic factor, whose root is $e_0$. The parabolic case carries no factor of this representation but is not empty in $\mathbb{B}$: the element $e_1+ie_2$ has square zero, so its exponential is $e_0+(e_1+ie_2)$, of norm one and neither a rotor nor a boost. The rule is Lemma 1 of Sangwine & Hitzer.

The two axes are directions in space, each a unit real pure quaternion,

$$
\vec u = \vec u_1e_1+\vec u_2e_2+\vec u_3e_3 , \qquad \vec u_1,\vec u_2,\vec u_3\in\mathbb{R} , \qquad \vec u_1^2+\vec u_2^2+\vec u_3^2=1 , \qquad \vec u^2=-e_0 .
$$

The set of them is the **axis sphere** $\mathcal{A}$, the quaternion roots of $-1$; the symbol $S$ is left to the spin groups $\mathrm{Spin}(n)$ of the spinor context, and the group of unit quaternions is written $\mathrm{Sp}(1)$. The scale and the phase stand on the two central unit elements $e_0$ and $i$.

The four factors are unique and their real dimensions $1+1+3+3$ sum to the eight of the algebra. The word exists exactly off the null cone, and it fails nowhere else. The body treats the four factors in turn — §*The Scale*, §*The Central Phase*, §*The Boost*, §*The Rotor* — the ordering is recorded in §*The Order of the Boost and the Rotor*, and §*The Theorem* proves the representation and its uniqueness. The conventions and symbols are the corpus's (*Conventions in Mathematics*, §*Symbols*, §*The Unitary Convention*). No physics is invoked.

## The Scale

The first factor is the positive real

$$
r = \lvert\rho\rvert = \sqrt{\lvert\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\rvert} .
$$

### The Norm and the Modulus

The number under the root is the **biquaternion norm**, the sum of the squares of the four complex coefficients, central and multiplicative,

$$
\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \sum_{\mu=0}^{3}Q_\mu^2 , \qquad \langle\tilde{P}\tilde{Q},\tilde{P}\tilde{Q}\rangle_{\natural} = \langle\tilde{P},\tilde{P}\rangle_{\natural}\langle\tilde{Q},\tilde{Q}\rangle_{\natural} .
$$

The modulus $\rho$ is its square root, and the root is two-valued. The branch is fixed once and for all: with $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \lvert\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\rvert\,\exp(i\varphi)$, $\varphi\in(-\pi,\pi]$, take the **principal** root

$$
\rho = \sqrt{\lvert\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\rvert}\;\exp(i\varphi/2) , \qquad r = \lvert\rho\rvert , \qquad \alpha = \arg\rho = \frac{\varphi}{2} \in \left(-\frac{\pi}{2},\frac{\pi}{2}\right] .
$$

The pair $(r,\alpha)$ is then unique, and the other root $-\rho$ has angle $\alpha\pm\pi$, outside the interval. This branch is the only convention of the representation; every other step is forced.

### The Factor

The scale is central, of real dimension $1$. It scales the element rigidly: replacing $\tilde{Q}$ by $\lambda\tilde{Q}$ with $\lambda>0$ multiplies $r$ by $\lambda$ and leaves the other three factors unchanged. It is the one factor written without an exponential, and it is fixed by each of the four conjugations.

### The Unit-Norm Slice

The scale is one exactly when $\lvert\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\rvert = 1$; in particular it is one on the unit-norm elements. If $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = 1$ then also $\rho = 1$ and $\alpha = 0$, and the word reduces to

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

Being central, the phase commutes with the other three factors and may be moved through them at no cost. It is the only factor that is both central and compact, of real dimension $1$; its exponent lies on the central imaginary line $i\mathbb{R}\subset\mathbb{C}_{\mathbb{B}}$, and its root is the central unit $i$, of square $-e_0$.

### The Two Sectors

The phase is zero on the two halves of the algebra and extremal on the scalar imaginary, whose word, $i = 1\cdot \exp(i\pi/2)\cdot e_0\cdot e_0$, exhibits it at $\alpha = \pi/2$. In the physical reading the vanishing of $\alpha$ selects the spacelike sector and its extremal value the timelike one.

### The Conjugations and the Degenerate Cases

Under the conjugations the phase is reversed, $\alpha\mapsto-\alpha$, by the coefficientwise and the Hermitian conjugation, and fixed by the quaternion conjugation. It is trivial, $\exp(i\alpha) = e_0$, exactly when the biquaternion norm is a positive real.

## The Boost

The third factor is the boost

$$
\tilde U_{\mathrm b} = \exp\Bigl(i\tfrac{\psi}{2}\vec u_{\mathrm b}\Bigr) = \cosh\tfrac{\psi}{2}\,e_0 + i\sinh\tfrac{\psi}{2}\,\vec u_{\mathrm b} , \qquad \psi \ge 0, \qquad \vec u_{\mathrm b}\in\mathcal{A} ,
$$

the Hermitian positive unit element of the word.

### The Exponent and the Root

The exponent $i\tfrac{\psi}{2}\vec u_{\mathrm b}$ lies in the Hermitian subspace $\mathbb{M}_+$ and has vanishing scalar part; its root is $i\vec u_{\mathrm b}$, Hermitian and of square $+e_0$. The exponent carries half of the rapidity: the conjugation by the boost deposits the rapidity $\psi$ twice. The boost is the only factor that is neither central nor compact, of real dimension $3$ — the rapidity and the two angles of the axis.

### The Hermitian Positive Factor

Divide the element by its modulus, $U = \tilde{Q}/\rho$, so that $\langle U,U\rangle_{\natural} = 1$, and form the Hermitian element $UU^{*}$. It is Hermitian, $(UU^{*})^{*} = UU^{*}$, and positive definite, the product of an invertible element and its Hermitian conjugate; its biquaternion norm is $\langle UU^{*},UU^{*}\rangle_{\natural} = 1$. The boost is the unique Hermitian positive square root of $UU^{*}$,

$$
\tilde U_{\mathrm b} = \sqrt{UU^{*}} , \qquad \tilde U_{\mathrm b}^2 = UU^{*} , \qquad \langle \tilde U_{\mathrm b},\tilde U_{\mathrm b}\rangle_{\natural} = 1 ,
$$

the normalisation of the boost being that the square root of a norm-one element has norm one.

### The Closed Form

For an element with real scalar part, $X = \mathrm{Sc}(X)\,e_0 + i\,\mathrm{Vec}(X)$, the four coefficients are the scalar and $i$ times the three components of the vector part, so the biquaternion norm is the difference of the two squared lengths,

$$
\langle X,X\rangle_{\natural} = \mathrm{Sc}(X)^2 - \lvert \mathrm{Vec}(X)\rvert^2 .
$$

The Hermitian element is written through its scalar part and its vector part,

$$
UU^{*} = \mathrm{Sc}(UU^{*})\,e_0 + i\,\mathrm{Vec}(UU^{*}) , \qquad \mathrm{Sc}(UU^{*}) \in \mathbb{R}, \qquad \mathrm{Vec}(UU^{*}) \in \mathbb{R}^3 ,
$$

so that its unit norm and its positivity read

$$
\mathrm{Sc}(UU^{*})^2 - \lvert \mathrm{Vec}(UU^{*})\rvert^2 = 1 , \qquad \mathrm{Sc}(UU^{*}) \ge 1 .
$$

The square root is Hermitian of the same shape. Write its scalar part $a = \mathrm{Sc}(\tilde U_{\mathrm b})$ and its vector part $\mathrm{Vec}(\tilde U_{\mathrm b})$, so that

$$
\tilde U_{\mathrm b} = a\,e_0 + i\,\mathrm{Vec}(\tilde U_{\mathrm b}) , \qquad a \in \mathbb{R} , \qquad \mathrm{Vec}(\tilde U_{\mathrm b}) \in \mathbb{R}^3 , \qquad a^2 - \lvert \mathrm{Vec}(\tilde U_{\mathrm b})\rvert^2 = 1 ,
$$

the last relation being the unit norm of the square root, which holds because the norm of $UU^{*}$ is one and the norm is multiplicative. A real pure quaternion squares to minus its squared length, $\vec v^{\,2} = -\lvert\vec v\rvert^2 e_0$, so the squared imaginary vector part is $(i\,\mathrm{Vec}(\tilde U_{\mathrm b}))^2 = \lvert \mathrm{Vec}(\tilde U_{\mathrm b})\rvert^2 e_0$, and the square of the root is

$$
\tilde U_{\mathrm b}^{\,2} = \bigl(a^2 + \lvert \mathrm{Vec}(\tilde U_{\mathrm b})\rvert^2\bigr)e_0 + 2a\,i\,\mathrm{Vec}(\tilde U_{\mathrm b}) .
$$

The equation $\tilde U_{\mathrm b}^{\,2} = UU^{*}$ splits into its scalar part and its vector part,

$$
a^2 + \lvert \mathrm{Vec}(\tilde U_{\mathrm b})\rvert^2 = \mathrm{Sc}(UU^{*}) , \qquad a\,\mathrm{Vec}(\tilde U_{\mathrm b}) = \tfrac12\,\mathrm{Vec}(UU^{*}) .
$$

Adding the scalar equation to the unit norm of $\tilde U_{\mathrm b}$ cancels the two squared lengths of the vector part and gives $2a^2 = \mathrm{Sc}(UU^{*}) + 1$, so the scalar part of the root is

$$
a = \sqrt{\frac{1+\mathrm{Sc}(UU^{*})}{2}} ,
$$

the positive root being taken because the square root is positive. The vector equation then gives the vector part of the root,

$$
\mathrm{Vec}(\tilde U_{\mathrm b}) = \frac{\mathrm{Vec}(UU^{*})}{2a} = \frac{\mathrm{Vec}(UU^{*})}{\sqrt{2\,\bigl(1+\mathrm{Sc}(UU^{*})\bigr)}} .
$$

Collecting the two parts, and using $UU^{*} = \mathrm{Sc}(UU^{*})e_0 + i\,\mathrm{Vec}(UU^{*})$ for the last form,

$$
\tilde U_{\mathrm b} = \sqrt{UU^{*}} = \sqrt{\frac{1+\mathrm{Sc}(UU^{*})}{2}}\;e_0 + \frac{i\,\mathrm{Vec}(UU^{*})}{\sqrt{2\,\bigl(1+\mathrm{Sc}(UU^{*})\bigr)}} = \frac{UU^{*}+e_0}{\sqrt{2\,\bigl(1+\mathrm{Sc}(UU^{*})\bigr)}} ,
$$

which squares back to $UU^{*}$. The comparison with the exponential writing gives the boost data

$$
\cosh\psi = \mathrm{Sc}(UU^{*}) , \qquad \sinh\psi = \lvert \mathrm{Vec}(UU^{*})\rvert , \qquad \vec u_{\mathrm b} = \frac{\mathrm{Vec}(UU^{*})}{\lvert \mathrm{Vec}(UU^{*})\rvert} .
$$

$\psi$ the **rapidity** and $\vec u_{\mathrm b}$ the **axis**. The boost carries three parameters and its set is the hyperbolic space $H^3$, the set of Lorentz boosts; in the notation of the physics articles it is the Lorentz boost rotor $\tilde\Lambda = \cosh\tfrac{\psi}{2} + i\sinh\tfrac{\psi}{2}\vec u_{\mathrm b}$.

### The Order of the Boost and the Rotor

The two non-central factors do not commute, and the position of each in the word is part of the statement. The order is free for the central factors alone: $\exp(i\alpha)\tilde U_{\mathrm b}\tilde u_{\mathrm r} = \tilde U_{\mathrm b}\tilde u_{\mathrm r}\,\exp(i\alpha)$ exactly, and likewise for $r$. For the other two, $\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ differs from $\tilde u_{\mathrm r}\tilde U_{\mathrm b}$ as soon as the axes are not parallel, the two being related by the conjugation

$$
\tilde u_{\mathrm r}\tilde U_{\mathrm b} = \left(\tilde u_{\mathrm r}\tilde U_{\mathrm b}\tilde u_{\mathrm r}^{-1}\right)\tilde u_{\mathrm r} ,
$$

which keeps the rapidity, rotates the axis by the rotor, and leaves $r$ and $\alpha$ unchanged. The product of the two factors is not the exponential of the sum of their exponents, because their exponents do not commute, $[\log\tilde U_{\mathrm b},\log\tilde u_{\mathrm r}]\neq0$ in general:

$$
\exp\left(\log \tilde U_{\mathrm b} + \log\tilde u_{\mathrm r}\right) \neq \tilde U_{\mathrm b}\tilde u_{\mathrm r} .
$$

The rapidity of a product is therefore not the sum of the rapidities, nor the rotation angle the sum of the rotation angles, while the modulus is exactly multiplicative, $r = r_1r_2$ and $\alpha = \alpha_1+\alpha_2$. The word becomes order-free exactly when one non-central factor is trivial or the two axes coincide; in the last case the element is a single boost-rotation about the common axis, which is why two boosts along one line have no residual rotation.

### The Conjugations

Under the conjugations the quaternion and the coefficientwise conjugation replace the boost by its inverse, the boost of the same rapidity about the reflected axis, and the Hermitian conjugation fixes it, $\tilde U_{\mathrm b}^{*} = \tilde U_{\mathrm b}$. The boost is trivial exactly when $\psi = 0$, that is, when $UU^{*} = e_0$, equivalently when the unit-norm part $U$ is unitary; this holds on the centre and on the real quaternions.

## The Rotor

The fourth factor is the rotor

$$
\tilde u_{\mathrm r} = \exp\Bigl(\tfrac{\theta}{2}\vec u_{\mathrm r}\Bigr) = \cos\tfrac{\theta}{2}\,e_0 + \sin\tfrac{\theta}{2}\,\vec u_{\mathrm r} , \qquad \theta \in [0,2\pi], \qquad \vec u_{\mathrm r}\in\mathcal{A} ,
$$

the unit real quaternion of the word.

### The Exponent and the Root

The exponent $\tfrac{\theta}{2}\vec u_{\mathrm r}$ is a real pure quaternion, lying in the anti-Hermitian sector $\mathbb{M}_- \cap \mathrm{Vect}(\mathbb{B})$; it is the only exponent that is neither central nor Hermitian. Its root is the real pure unit quaternion $\vec u_{\mathrm r}$, of square $-e_0$, and it carries half of the rotation angle, the conjugation by the rotor producing a rotation by $\theta$. The rotor is compact, of real dimension $3$.

### The Definition

The rotor is the unitary factor of the right polar decomposition of the unit-norm part,

$$
U = \tilde u_{\mathrm r}\sqrt{U^{*}U} , \qquad \tilde u_{\mathrm r} = U\bigl(\sqrt{U^{*}U}\bigr)^{-1} .
$$

The element $U^{*}U$ is Hermitian positive definite, the product of an invertible element and its Hermitian conjugate, so $\sqrt{U^{*}U}$ is its unique Hermitian positive square root and the formula defines $\tilde u_{\mathrm r}$ from the unit-norm part alone; no other factor enters. Equivalently, $\tilde u_{\mathrm r}$ is the unique unit element for which $U\tilde u_{\mathrm r}^{-1}$ is Hermitian positive. If $U = \tilde u P$ with $\tilde u$ a unit real quaternion and $P$ Hermitian positive, then $U^{*}U = P\tilde u^{*}\tilde u P = P^{2}$, since $\tilde u^{*} = \tilde u^{\natural} = \tilde u^{-1}$, so $P = \sqrt{U^{*}U}$ by uniqueness of the square root and hence $\tilde u = \tilde u_{\mathrm r}$.

### The Reconstruction of the Unit-Norm Part

The rotor and the boost reconstitute the unit-norm part,

$$
U = \tilde U_{\mathrm b}\,\tilde u_{\mathrm r} .
$$

Indeed the same element commutes with itself, $U(U^{*}U) = (UU^{*})U$, so the relation holds between the two Hermitian positive square roots, $U\sqrt{U^{*}U} = \sqrt{UU^{*}}\,U$. Multiplying on the right by $(\sqrt{U^{*}U})^{-1}$ and using $\tilde U_{\mathrm b} = \sqrt{UU^{*}}$ and $\tilde u_{\mathrm r} = U(\sqrt{U^{*}U})^{-1}$ gives the statement. The left and the right polar decomposition of $U$ therefore carry the same unitary factor, and the reconstruction reads $\tilde u_{\mathrm r} = \tilde U_{\mathrm b}^{\natural}U$, since $\tilde U_{\mathrm b}^{-1} = \tilde U_{\mathrm b}^{\natural}$.

### Its Unitarity and Its Reality

It is unitary, preserving the sesquilinear form (*Conventions in Mathematics*, §*The Unitary Convention*),

$$
\tilde u_{\mathrm r}\,\tilde u_{\mathrm r}^{*} = U\bigl(\sqrt{U^{*}U}\bigr)^{-1}\bigl(\sqrt{U^{*}U}\bigr)^{-1}U^{*} = U(U^{*}U)^{-1}U^{*} = e_0 ,
$$

and of unit norm by multiplicativity along the reconstruction, $\langle\tilde u_{\mathrm r},\tilde u_{\mathrm r}\rangle_{\natural} = \langle U,U\rangle_{\natural}/\langle \tilde U_{\mathrm b},\tilde U_{\mathrm b}\rangle_{\natural} = 1$. An element that is both unitary and of unit norm is a unit real quaternion: such an element is $\exp(i\beta)\tilde A$ with $\tilde A$ a unit real quaternion and has norm $\exp(2i\beta)$, so $N = 1$ forces $\exp(2i\beta) = 1$. Hence

$$
\tilde u_{\mathrm r} \in \mathrm{Sp}(1) = \{\tilde u \in \mathbb{H} : \tilde u\tilde u^{\natural} = 1\} ,
$$

the group of unit real quaternions. It is compact, and it is the unit factor of the quaternion polar representation of the companion article. By *The Lorentz Group in Biquaternionic Form*, it acts on the material sector as a spatial rotation; the central phase has been split off from it, which distinguishes it from the group of unitary elements $U(\mathbb{B})$.

### The Closed Form

The rotor is a real quaternion of unit norm, so it is written through its scalar part and its vector part,

$$
\tilde u_{\mathrm r} = \mathrm{Sc}(\tilde u_{\mathrm r})\,e_0 + \mathrm{Vec}(\tilde u_{\mathrm r}) , \qquad \mathrm{Sc}(\tilde u_{\mathrm r}) \in \mathbb{R} , \qquad \mathrm{Vec}(\tilde u_{\mathrm r}) \in \mathbb{R}^3 , \qquad \mathrm{Sc}(\tilde u_{\mathrm r})^2 + \lvert \mathrm{Vec}(\tilde u_{\mathrm r})\rvert^2 = 1 ,
$$

the vector part being real and pure, so that its square is minus its squared length and the unit norm is the **sum** of the two squared lengths, unlike the boost, whose unit norm is the difference. The exponential writing is the same element with scalar part $\cos\tfrac{\theta}{2}$ and vector part $\sin\tfrac{\theta}{2}\,\vec u_{\mathrm r}$, so the comparison reads

$$
\cos\frac{\theta}{2} = \mathrm{Sc}(\tilde u_{\mathrm r}) , \qquad \sin\frac{\theta}{2} = \lvert \mathrm{Vec}(\tilde u_{\mathrm r})\rvert , \qquad \vec u_{\mathrm r} = \frac{\mathrm{Vec}(\tilde u_{\mathrm r})}{\lvert \mathrm{Vec}(\tilde u_{\mathrm r})\rvert} .
$$

The stored half-angle lies in $[0,\pi]$, so the angle and the axis are read off the rotor by

$$
\theta = 2\arccos \mathrm{Sc}(\tilde u_{\mathrm r}) \in [0,2\pi] , \qquad \vec u_{\mathrm r} = \frac{\mathrm{Vec}(\tilde u_{\mathrm r})}{\lvert \mathrm{Vec}(\tilde u_{\mathrm r})\rvert} .
$$

The axis is defined whenever the vector part is nonzero, that is, away from $\theta = 0$ and $\theta = 2\pi$; at $\tilde u_{\mathrm r} = \pm e_0$ the vector part vanishes, the rotation is the identity or the full turn, and there is no axis. On the element the rotor is the unitary factor of the right polar decomposition,

$$
\tilde u_{\mathrm r} = U\bigl(\sqrt{U^{*}U}\bigr)^{-1} = U\bigl(\sqrt{U^{*}U}\bigr)^{\natural} = \tilde U_{\mathrm b}^{\natural}U ,
$$

the inverse being the quaternion conjugate because the root is Hermitian of unit norm, the root itself having the closed form $\sqrt{U^{*}U} = (U^{*}U+e_0)/\sqrt{2(1+\mathrm{Sc}(U^{*}U))}$, and the last form being the reconstructed one. So the two parts of the rotor, and with them $\theta$ and $\vec u_{\mathrm r}$, are read from the coefficients of $U$ alone, as $\psi$ and $\vec u_{\mathrm b}$ are read from those of $UU^{*}$.

### The Real Quaternions

If all four coefficients of $\tilde{Q}$ are real then $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \sum_\mu q_\mu^2$ is a positive real, so $\alpha = 0$ and $r = \lvert\tilde{Q}\rvert$ is the quaternion modulus. Then $U = \tilde{Q}/r$ is a unit real quaternion and $UU^{*} = UU^{\natural} = e_0$, so $\tilde U_{\mathrm b} = e_0$ and $\tilde u_{\mathrm r} = U$. The real quaternions have no boost, and their polar representation is the quaternion polar representation term by term.

### The Conjugations and the Degenerate Cases

Under the conjugations the rotor is fixed by the coefficientwise conjugation and inverted by the quaternion and the Hermitian conjugation,

$$
\bar{\tilde u_{\mathrm r}} = \tilde u_{\mathrm r} , \qquad \tilde u_{\mathrm r}^{\natural} = \tilde u_{\mathrm r}^{*} = \tilde u_{\mathrm r}^{-1} .
$$

The rotor is trivial exactly when the unit-norm part $U$ is Hermitian positive, that is, when $\tilde{Q} = \rho\,\tilde U_{\mathrm b}$.

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

Equivalently $\tilde{Q} = \rho\,\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ with $\rho = r\exp(i\alpha) = \sqrt{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}}$ the principal square root.

### Existence

The construction of §*The Boost* and §*The Rotor* gives the factors: $\rho$ from the branch of the square root of the norm, $U = \tilde{Q}/\rho$ of unit norm, $\tilde U_{\mathrm b} = \sqrt{UU^{*}}$ the unique Hermitian positive square root of $UU^{*}$, and $\tilde u_{\mathrm r} = U(\sqrt{U^{*}U})^{-1}$ the unitary factor of the right polar decomposition of $U$, unitary and of unit norm, hence a unit real quaternion. The reconstruction of §*The Rotor* is $U = \tilde U_{\mathrm b}\tilde u_{\mathrm r}$, so the product reproduces the element,

$$
r\,\exp(i\alpha)\tilde U_{\mathrm b}\tilde u_{\mathrm r} = \rho\,U = \tilde{Q} .
$$

### Uniqueness

Suppose $\tilde{Q} = r \exp(i\alpha)\tilde U_{\mathrm b}\tilde u_{\mathrm r} = r'\exp(i\alpha')\tilde U_{\mathrm b}'\tilde u_{\mathrm r}'$ with both quadruples admissible. Taking norms and using $\langle \tilde U_{\mathrm b}\tilde u_{\mathrm r},\tilde U_{\mathrm b}\tilde u_{\mathrm r}\rangle_{\natural} = 1$ gives $r^2\exp(2i\alpha) = (r')^2\exp(2i\alpha')$, so the two principal square roots of $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}$ agree, and since $r,r' > 0$ with $\alpha,\alpha'$ in the same half-open interval of length $\pi$, one has $r = r'$ and $\alpha = \alpha'$. Then $U = \tilde{Q}/\rho$ is the same in both, so $UU^{*}$ is the same, and its Hermitian positive square root is unique, so $\tilde U_{\mathrm b} = \tilde U_{\mathrm b}'$; then $\tilde u_{\mathrm r} = \tilde U_{\mathrm b}^{-1}U = \tilde u_{\mathrm r}'$.

## Summary

Every biquaternion of non-vanishing norm has a unique polar representation

$$
\tilde{Q} = r\,\exp(i\alpha)\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r} = r\,\exp(i\alpha)\,\exp\Bigl(i\tfrac{\psi}{2}\vec u_{\mathrm b}\Bigr)\,\exp\Bigl(\tfrac{\theta}{2}\vec u_{\mathrm r}\Bigr) ,
$$

with $r = \sqrt{\lvert\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\rvert} > 0$, $\alpha = \tfrac{1}{2}\arg \langle\tilde{Q},\tilde{Q}\rangle_{\natural}$, $\tilde U_{\mathrm b}$ the Hermitian positive unit-norm boost and $\tilde u_{\mathrm r}$ the unit real quaternion rotor. The modulus is the complex number $\rho = r\exp(i\alpha) = \sqrt{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}}$, whose absolute value is the scale, so the phase is a factor in its own right rather than a correction. The four factors are unique, their real dimensions $1+1+3+3$ sum to the eight of the algebra, and the failure of the decomposition is exactly the null cone $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = 0$. The Cartan form of the physics articles is the unit-norm case, in which the scale and the phase are trivial.

## Summary of Notation

| symbol | set | meaning |
|---|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | — | the biquaternion algebra, $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ |
| $e_0 = 1$, $e_1,e_2,e_3$ | basis of $\mathbb{B}$ | the algebra unit and the quaternion units, $e_k^2 = -e_0$, $e_1e_2 = e_3$ |
| $Q_\mu$ | $\mathbb{C}$ | the four complex coefficients of $\tilde{Q}$ |
| $i$ | $\mathbb{C}_{\mathbb{B}}$, $i^2 = -1$ | the central scalar imaginary |
| $N = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = \sum_\mu Q_\mu^2$ | $\mathbb{C}$, central | the biquaternion norm |
| $\rho = \sqrt{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}}$ | $\mathbb{C}\setminus\{0\}$ | the complex modulus, the principal square root |
| $r = \sqrt{\lvert\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\rvert}$ | $\mathbb{R}$, $r > 0$ | the scale, a positive real |
| $\alpha = \tfrac{1}{2}\arg \langle\tilde{Q},\tilde{Q}\rangle_{\natural}$ | $\left(-\frac{\pi}{2},\frac{\pi}{2}\right]$ | the phase angle |
| $U = \tilde{Q}/\rho$ | $\mathbb{B}^{\times}_1$, $\langle U\rangle_{\natural}=e_0$ | the unit-norm part |
| $UU^{*}$ | $\mathbb{M}_+$, positive definite, $\langle UU^{*}\rangle_{\natural}=e_0$ | the Hermitian positive element, scalar part $\mathrm{Sc}(UU^{*})\in\mathbb{R}$, $\mathrm{Sc}(UU^{*})\ge1$, vector part $\mathrm{Vec}(UU^{*})\in\mathbb{R}^3$ |
| $\tilde U_{\mathrm b} = \sqrt{UU^{*}}$ | $\mathbb{M}_+$, positive definite, $\langle\tilde U_{\mathrm b}\rangle_{\natural}=e_0$ | the boost, a Hermitian positive unit element |
| $\psi$ | $\mathbb{R}$, $\psi\ge0$ | the rapidity of the boost |
| $\vec u_{\mathrm b}$ | $\mathcal{A}$, a unit vector of $\mathbb{R}^3$ | the axis of the boost |
| $i\frac{\psi}{2}\vec u_{\mathrm b}$ | $\mathbb{M}_+$, scalar part zero | the boost exponent |
| $\theta$ | $[0,2\pi]$ | the rotation angle of the rotor, whose stored half-angle is $\frac{\theta}{2}\in[0,\pi]$ |
| $\vec u_{\mathrm r}$ | $\mathcal{A}$, a unit vector of $\mathbb{R}^3$ | the axis of the rotor |
| $\frac{\theta}{2}\vec u_{\mathrm r}$ | real pure quaternion | the rotor exponent |
| $U = \tilde u_{\mathrm r}\sqrt{U^{*}U}$, $\tilde u_{\mathrm r} = U(\sqrt{U^{*}U})^{-1} = \tilde U_{\mathrm b}^{\natural}U$ | $\mathrm{Sp}(1)$ | the rotor, the unitary factor of the right polar decomposition, a unit real quaternion |
| $r\,\exp(i\alpha)\,\exp\bigl(i\frac{\psi}{2}\vec u_{\mathrm b}\bigr)\,\exp\bigl(\frac{\theta}{2}\vec u_{\mathrm r}\bigr)$ | — | the polar word, one positive real and three exponentials |
| $\mathbb{M}_+$ | subspace of $\mathbb{B}$ | the Hermitian subspace, real scalar part and imaginary vector part |
| $\mathbb{M}_-$ | subspace of $\mathbb{B}$ | the anti-Hermitian subspace, the material sector of the physics articles |
| $\mathbb{H}_{\mathbb{B}}$ | subspace of $\mathbb{B}$ | the real quaternion subspace, the fixed space of complex conjugation |
| $\mathrm{Sp}(1)$ | $\lvert\tilde u\rvert = 1$ in $\mathbb{H}$ | the group of unit real quaternions |

## Further Reading

- *The Biquaternioid as a Vector Space over $\mathbb{C}$* (`articles_maths/the-biquaternioid-vector-space-over-c.md`), for the algebra, the four conjugations and the remarkable subspaces.
- *The Polar Decomposition of Biquaternions in Practice* (`articles_maths/the-polar-decomposition-of-biquaternions-in-practice.md`), for the procedure in full: the two invariants read off the coordinates, the five steps and their order, the factors in the coordinates of $\tilde{Q}$, the exponent of each factor with its position in the algebra, and the worked examples.
- *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/the-4-forms-over-the-biquaternioid-c-space.md`), for the two forms that the procedure reads off the element, the complex bilinear norm $\langle\cdot\rangle_{\natural}$ and the Hermitian form, and for the Euclidean norm $\lVert\cdot\rVert_{E}$.
- *The Polar Element Representation and Remarkable Subspaces* (`articles_maths/the-polar-element-representation-and-remarkable-subspaces.md`), for the four exponents read against the four coordinate blocks and the six remarkable subspaces, the incidence of the exponents with the subspaces, and the polar data each subspace carries.
- *Split-Biquaternion Polar Element Representation* (`articles_maths/split-biquaternion-polar-element-representation.md`), for the semisimple analogue, whose modulus is split complex and whose rotor is six-dimensional.
- *Quaternion Polar Element Representation* (`articles_maths/quaternion-polar-element-representation.md`), for the two-factor case that this decomposition restricts to on the real quaternions.
- *Complex Polar Element Representation* (`articles_maths/complex-polar-element-representation.md`) and *Split-Complex Polar Element Representation* (`articles_maths/split-complex-polar-element-representation.md`), for the two-dimensional members of the series, where the rule of the exponential is stated once and the slots are counted in the smallest cases.
- *The Lorentz Group in Biquaternionic Form — Structure and Representations* (`articles_physics/the-lorentz-group-in-biquaternionic-form-structure-and-representations.md`), for the boost and rotation rotors and the Thomas-Wigner rotation.
- S. J. Sangwine and E. Hitzer, "Polar decomposition of complexified quaternions and octonions", *Advances in Applied Clifford Algebras* (2020), DOI 10.1007/s00006-020-1048-y; technical report CES-535, University of Essex (2019), for the published two-exponential factorisation of the unit semi-norm elements and, in the general case, its Corollary 1 — whose trigonometric factor is the rotor $\tilde u_{\mathrm r}$ of this article and whose hyperbolic factor is the boost about the rotor-conjugated axis, $\tilde U_{\mathrm b} = \tilde u_{\mathrm r}^{-1}H\tilde u_{\mathrm r}$ with the same rapidity and norm — for Lemma 1, the trichotomy of the exponential of a hypercomplex root of $-1$, $0$ or $+1$, and for the degenerate word on the null cone. The order of the two non-central factors is reversed there, angle first, and the complex modulus is kept whole rather than split into a scale and a phase, which is the difference of count $2+3+3$ against $1+1+3+3$; the corpus fixes the branch and proves uniqueness, while the paper admits both orders.
- Soo-Chang Pei, Ja-Han Chang and Jian-Jiun Ding, "Commutative reduced biquaternions and their Fourier transform for signal and image processing applications", *IEEE Transactions on Signal Processing* **52** (2004) 2012–2022, for the reduced biquaternion algebra — the commutative four-dimensional algebra $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\oplus\mathbb{C}$, equivalently the double-complex, tessarine or commutative hypercomplex algebra — and for its polar form, its uniqueness under the phase-range convention, its De Moivre theorem and the simplified polar form for colour images.
