# __The Polar Element Representation of Biquaternions__

## Introduction

This article is about the **polar representation** of a biquaternion: the statement that every biquaternion with non-vanishing norm is the ordered product of a positive real scale, a central phase and two unit factors,

$$
\tilde{Q} = r\,\exp(i\alpha)\,\exp\Bigl(i\tfrac{\psi}{2}\hat u_{\mathrm b}\Bigr)\,\exp\Bigl(\tfrac{\theta}{2}\hat u_{\mathrm r}\Bigr) ,
$$

with the four factors, their exponents and their ranges collected in one table.

| # | factor | name | exponent | root | parameter and range | real dimension |
|---|---|---|---|---|---|---|
| 1 | $r$ | scale | — | — | $r \in \mathbb{R}$, $r>0$ | $1$ |
| 2 | $\exp(i\alpha)$ | central phase | $i\alpha$ | $i$ | $\alpha \in \left(-\frac{\pi}{2},\frac{\pi}{2}\right]$ | $1$ |
| 3 | $\exp\bigl(i\tfrac{\psi}{2}\hat u_{\mathrm b}\bigr)$ | boost | $i\tfrac{\psi}{2}\hat u_{\mathrm b}$ | $i\hat u_{\mathrm b}$ | $\psi \in \mathbb{R}$, $\psi\ge0$, $\hat u_{\mathrm b}\in\mathcal{A}$ | $3$ |
| 4 | $\exp\bigl(\tfrac{\theta}{2}\hat u_{\mathrm r}\bigr)$ | rotor | $\tfrac{\theta}{2}\hat u_{\mathrm r}$ | $\hat u_{\mathrm r}$ | $\theta \in [0,2\pi]$, $\hat u_{\mathrm r}\in\mathcal{A}$ | $3$ |

The scale is the one factor that is not an exponential. The three exponentials follow a single rule: the character of an exponential is trigonometric, hyperbolic or parabolic according to the square of the **root** of its exponent, a root of $-e_0$ giving the trigonometric case, a root of $+e_0$ the hyperbolic case, and a nilpotent root the parabolic case. The phase and the rotor stand on a root of $-e_0$, the boost on a root of $+e_0$, and the scale is the degenerate hyperbolic case whose root is the algebra unit $e_0$.

The four factors are unique, and their real dimensions $1+1+3+3$ sum to the eight real dimensions of the algebra. The word exists exactly on the complement of the null cone, and its failure there is the whole of its failure.

The body of the article is organised by the four factors: §*The Scale*, §*The Central Phase*, §*The Boost* and §*The Rotor* treat them one by one and gather their data — the exponent of each factor, its root, the subspace it lies in, the element it is built from and the cases in which it is trivial. §*Why Four Factors* states why the count is four, §*The Theorem* states and proves the representation and fixes its uniqueness, and the closing sections give the domain, the degenerate cases and the relation to the three pairings.

The conventions and the symbols are those of the corpus (*Conventions in Mathematics*, §*Symbols*, §*The Unitary Convention*); the symbols this article uses are collected in §*Summary of Notation*.

No physics is invoked.

## The Polar Word

The word is the ordered product of the four factors,

$$
\tilde{Q} = r\,\exp(i\alpha)\,\exp\Bigl(i\tfrac{\psi}{2}\hat u_{\mathrm b}\Bigr)\,\exp\Bigl(\tfrac{\theta}{2}\hat u_{\mathrm r}\Bigr) ,
$$

and the factors are read off the element one by one in the four sections that follow. Two objects are shared by them and are fixed here once.

**The root of the exponent.** Each of the three exponents is a real parameter times a **root** of $-e_0$, $0$ or $+e_0$ — the generator of a one-parameter group (*Conventions in Mathematics*, §*The Root Convention*) — and the character of its exponential is the square of that root.

| factor | exponent | root | square of the root | character |
|---|---|---|---|---|
| $r$ | — | $e_0$ | $+e_0$ | hyperbolic, degenerate |
| $\exp(i\alpha)$ | $i\alpha$ | $i$ | $-e_0$ | trigonometric, central |
| $\exp\bigl(i\tfrac{\psi}{2}\hat u_{\mathrm b}\bigr)$ | $i\tfrac{\psi}{2}\hat u_{\mathrm b}$ | $i\hat u_{\mathrm b}$ | $+e_0$ | hyperbolic |
| $\exp\bigl(\tfrac{\theta}{2}\hat u_{\mathrm r}\bigr)$ | $\tfrac{\theta}{2}\hat u_{\mathrm r}$ | $\hat u_{\mathrm r}$ | $-e_0$ | trigonometric |

A root of $-e_0$ gives the trigonometric case, a root of $+e_0$ the hyperbolic case, and a nilpotent root the parabolic case, where the series truncates to the unit plus the exponent. The parabolic case produces no factor of the representation but is not empty in $\mathbb{B}$: the element $e_1+ie_2$ has square zero, so its exponential is $e_0+(e_1+ie_2)$, of norm one and neither a rotor nor a boost. The rule is Lemma 1 of Sangwine & Hitzer, stated there for a hypercomplex root of $-1$, $0$ or $+1$.

**The two axes.** The boost axis $\hat u_{\mathrm b}$ is the direction of the motion; the rotor axis $\hat u_{\mathrm r}$ is the axis of the rotation. Each of them is one direction in space, given by three real numbers, its cosines on the basis vectors $e_1,e_2,e_3$, and the three numbers have squares that sum to one,

$$
\hat u = \hat u_1e_1+\hat u_2e_2+\hat u_3e_3 , \qquad \hat u_1,\hat u_2,\hat u_3\in\mathbb{R} , \qquad \hat u_1^2+\hat u_2^2+\hat u_3^2=1 .
$$

The **axis sphere** is the collection of all such directions. Three words describe one of its members.

- It is **real**: the three coordinates are real numbers and not complex ones, and the imaginary unit $i$ never multiplies them.
- It is **pure**: there is no $e_0$ term among the three, so its scalar part is zero. The word describes the missing coefficient, not the three present ones.
- It is **unit**: its length is one, which is the condition $\hat u_1^2+\hat u_2^2+\hat u_3^2=1$.

The three conditions have one algebraic consequence. Squaring the direction gives $\hat u^2=-e_0$, so the axis sphere is exactly the set of roots of $-e_0$ in $\mathbb{H}$: the quaternion roots of $-1$. The set is written $\mathcal{A}$ and not $S$, so that the symbol $S$ stays with the spin groups $\mathrm{Spin}(n)$ of the spinor context; the group of unit quaternions is written $\mathrm{Sp}(1)$.

The two axes are not the only unit elements of the algebra: the scale and the phase stand on the two central unit elements $e_0$ and $i$.

## The Scale

The first factor is the positive real

$$
r = \lvert\rho\rvert = \sqrt{\lvert\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\rvert} ,
$$

the absolute value of the **complex modulus** of the element.

### The Biquaternion Norm and Its Square Root

The number under the root is the **biquaternion norm**

$$
\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = \sum_{\mu=0}^{3}Q_\mu^2 ,
$$

the sum of the squares of the four complex coefficients: a complex number, central, multiplicative,

$$
\langle\tilde{P}\tilde{Q},\tilde{P}\tilde{Q}\rangle_{\natural} = \langle\tilde{P},\tilde{P}\rangle_{\natural}\langle\tilde{Q},\tilde{Q}\rangle_{\natural},
$$

and equal in the matrix model to the determinant, $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \det\mathsf{M}_2(\tilde{Q})$. The modulus is its square root; to make it single valued, fix the branch once and for all. Write the norm in polar form in $\mathbb{C}$,

$$
\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = |\langle\tilde{Q},\tilde{Q}\rangle_{\natural}|\,e^{i\varphi}, \qquad \varphi = \arg \langle\tilde{Q},\tilde{Q}\rangle_{\natural} \in (-\pi,\pi] ,
$$

and define

$$
\rho = \sqrt{|\langle\tilde{Q},\tilde{Q}\rangle_{\natural}|}\;e^{i\varphi/2} ,
$$

the principal square root. Its modulus and argument are

$$
r = |\rho| = \sqrt{|\langle\tilde{Q},\tilde{Q}\rangle_{\natural}|} \ \ge 0, \qquad \alpha = \arg\rho = \frac{\varphi}{2} \in \left(-\frac{\pi}{2},\frac{\pi}{2}\right] .
$$

The pair $(r,\alpha)$ is unique: the modulus is non-negative by construction and the angle lies in a half-open interval of length $\pi$, so no two pairs give the same $\rho$. The square root $\rho$ is one of the two solutions of $\tilde T^2 = \langle\tilde{Q},\tilde{Q}\rangle_{\natural}$, and the branch choice above selects one of them; the other, $-\rho$, has angle $\alpha\pm\pi$ and is outside the interval. **This branch is the only convention of the representation**; every other step is forced.

### The Scale as a Factor

The scale is a positive real number, the only factor that is both central and non-compact on the positive side, of real dimension $1$. It multiplies the element rigidly: replacing $\tilde{Q}$ by $\lambda\tilde{Q}$ with $\lambda>0$ multiplies $r$ by $\lambda$ and leaves the other three factors unchanged. It is the absolute value of the determinant of the matrix image, raised to the power $\tfrac12$, since $|\det\mathsf{M}_2(\tilde{Q})| = |\langle\tilde{Q},\tilde{Q}\rangle_{\natural}| = r^2$. It is the degenerate case of the hyperbolic row, and the one factor that is written without an exponential.

**Under the conjugations** the scale is unchanged, since the biquaternion norm is central and its modulus is invariant under each of them.

**The scale is trivial** exactly when the biquaternion norm has modulus one, $|\langle\tilde{Q},\tilde{Q}\rangle_{\natural}| = 1$; in particular it is one on the unit-norm elements, of which the Lorentz rotors of the physics articles are the case.

## The Central Phase

The second factor is the **central phase**

$$
e^{i\alpha}, \qquad \alpha = \tfrac12\arg\langle\tilde{Q},\tilde{Q}\rangle_{\natural} \in \left(-\tfrac{\pi}{2},\tfrac{\pi}{2}\right] ,
$$

the unit element of the centre given by the argument of the biquaternion norm.

### The Angle of the Norm

The phase is one half of the argument of the determinant of $\tilde{Q}$, the determinant being $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}$ in the matrix model, and it vanishes exactly when the biquaternion norm is a positive real. Its value is not a normalisation constant: it carries information, and in the physical interpretation of the companion articles it is the central phase that the corpus's Noether and gauge articles identify as the algebra's continuous symmetry. Its real dimension is $1$.

### Centrality, Exponent and Root

An element of the centre commutes with everything, so the phase may be moved through the other factors at no cost, and the central group $U(1)$ is a free one-parameter factor of any decomposition. It is the only factor that is both central and compact. Its exponent $i\alpha$ lies on the central imaginary line $i\mathbb{R}\subset\mathbb{C}_{\mathbb{B}}$, and it is the only exponent that commutes with the other three; its root is the central unit $i$, of square $-e_0$.

**Under the conjugations** the phase is reversed, $\alpha\mapsto-\alpha$, by the coefficientwise conjugation and by the Hermitian conjugation, and fixed by the quaternion conjugation.

**The phase is trivial** exactly when the biquaternion norm is a positive real, by $\alpha = \tfrac12\arg\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = 0$; and it takes its extremal value on the scalar imaginary, whose word is $i = 1\cdot e^{i\pi/2}\cdot e_0\cdot e_0$.

## The Boost

The third factor is the **boost**,

$$
\tilde U_{\mathrm b} = \exp\Bigl(i\tfrac{\psi}{2}\hat u_{\mathrm b}\Bigr) = \cosh\tfrac{\psi}{2}\,e_0 + i\sinh\tfrac{\psi}{2}\,\hat u_{\mathrm b} , \qquad \psi \ge 0, \qquad \hat u_{\mathrm b}\in\mathcal{A} ,
$$

the Hermitian positive unit element of the word. It is written $\tilde U_{\mathrm b}$ for short, and it is the factor the physics articles call the Lorentz boost rotor.

### The Exponent and the Root

The exponent $i\tfrac{\psi}{2}\hat u_{\mathrm b}$ lies in the Hermitian subspace $\mathbb{M}_+$, of real scalar part and purely imaginary vector part, and it is traceless, since its scalar part vanishes; its root is $i\hat u_{\mathrm b}$, Hermitian and of square $+e_0$. The exponent carries half of the rapidity: the conjugation by the boost produces a Lorentz transformation of rapidity $\psi$, so the stored half is counted twice, as §*What the Sandwich Sees* records. The boost is the only factor that is neither central nor compact, and its real dimension is $3$, the rapidity and the two angles of the axis.

### The Hermitian Positive Factor

The word **unit** is the corpus's, and it is relative to the norm: a **unit element** is an element of norm one, the norm being the one in view (*Conventions in Mathematics*, §*The Unitary Convention*). The norm in view here is the biquaternion norm $N = \langle\cdot,\cdot\rangle_{\natural}$, whose unit elements are the level set $\mathbb{B}^{\times}_1 = \{N = e_0\}$, the group of unit-norm elements, the special linear group $SL(2,\mathbb{C})$ in the matrix picture. A **unitary** element, by contrast, is one that preserves the sesquilinear form, and it is a narrower object.

Divide the biquaternion by its modulus,

$$
U = \frac{\tilde{Q}}{\rho} .
$$

Then $U$ has unit norm, $\langle U,U\rangle_{\natural} = 1$, and the whole content of the decomposition sits in the split of the unit-norm part into a boost and a rotor. Form the Hermitian element

$$
S = U U^{*} .
$$

It is Hermitian, since $S^{*} = (UU^{*})^{*} = UU^{*} = S$, and it is positive definite, because in the matrix model $\mathsf{M}_2(S) = \mathsf{M}_2(U)\mathsf{M}_2(U)^\dagger$ is a positive definite Hermitian matrix whenever $\mathsf{M}_2(U)$ is invertible. Its biquaternion norm is $\langle S,S\rangle_{\natural} = 1$.

The element $S$ is not itself the boost. The boost is its Hermitian positive square root,

$$
\tilde U_{\mathrm b} = \sqrt{S} , \qquad \tilde U_{\mathrm b}^2 = S ,
$$

which exists and is unique: a positive definite Hermitian matrix has exactly one positive definite Hermitian square root, and the condition $\langle S,S\rangle_{\natural} = 1$ is inherited as $\langle \tilde U_{\mathrm b},\tilde U_{\mathrm b}\rangle_{\natural}^2 = \langle S,S\rangle_{\natural} = 1$, so $\langle \tilde U_{\mathrm b},\tilde U_{\mathrm b}\rangle_{\natural} = 1$ for the positive root. The element $\tilde U_{\mathrm b}$ is not arbitrary in $\mathbb{M}_+$: the square root of a norm-one element has norm one, and that is the normalisation of the boost.

### The Closed Form, the Rapidity and the Axis

The matrix square root can be written out in the algebra, and this is what makes the decomposition an algorithm rather than an existence statement. Write the Hermitian element $S$ in its own parameters,

$$
S = \sigma\,e_0 + i\vec w, \qquad \sigma \in \mathbb{R}, \qquad \vec w \in \mathbb{R}^3 ,
$$

| symbol | meaning | range |
|---|---|---|
| $\sigma$ | the real scalar part of $S$ | $\sigma = \tfrac12\operatorname{tr}\mathsf{M}_2(S) \ge 1$ |
| $\vec w$ | the purely imaginary vector part of $S$ | $\lvert\vec w\rvert^2 = \sigma^2 - 1$ |

with real scalar part $\sigma$ and purely imaginary vector part $i\vec w$. The bound $\sigma \ge 1$ holds because the two eigenvalues of a positive definite matrix of determinant one and trace $2\sigma$ are positive and multiply to one; and

$$
\tilde U_{\mathrm b} = \sqrt{\frac{1+\sigma}{2}}\;e_0 + \frac{i\,\vec w}{\sqrt{2(1+\sigma)}} .
$$

Squaring this expression returns $S$, since

$$
\frac{1+\sigma}{2} - \frac{|\vec w|^2}{2(1+\sigma)} = \frac{(1+\sigma)^2 - |\vec w|^2}{2(1+\sigma)} = \frac{2\sigma(1+\sigma)}{2(1+\sigma)} = \sigma ,
$$

where $|\vec w|^2 = \sigma^2-1$ was used, which is the statement $\langle S,S\rangle_{\natural} = \sigma^2-|\vec w|^2 = 1$ for the Hermitian element $S$; the result is $\sigma + i\vec w = S$.

The closed form shows that the boost is determined by one positive number and one direction. Writing

$$
\tilde U_{\mathrm b} = \cosh\frac{\psi}{2}\,e_0 + i\sinh\frac{\psi}{2}\,\hat u_{\mathrm b} , \qquad \psi \ge 0, \qquad \hat u_{\mathrm b} \in \mathcal{A} ,
$$

with $\cosh\psi = \sigma$ and $\hat u_{\mathrm b} = \vec w/|\vec w|$, the number $\psi$ is the boost's **rapidity** and $\hat u_{\mathrm b}$ its axis. The comparison of the two writings gives the dictionary

$$
\cosh\frac{\psi}{2} = \sqrt{\frac{1+\sigma}{2}}, \qquad \sinh\frac{\psi}{2} = \frac{|\vec w|}{\sqrt{2(1+\sigma)}} ,
$$

which are the half-angle identities applied to $\sigma = \cosh\psi$ and $|\vec w| = \sinh\psi$.

| boost datum | symbol | definition | range |
|---|---|---|---|
| rapidity | $\psi$ | $\cosh\psi = \sigma$ | $\psi \ge 0$ |
| axis | $\hat u_{\mathrm b}$ | $\vec w/\lvert\vec w\rvert$ | the axis sphere $\mathcal{A}$, the unit vectors of $\mathbb{R}^3$ |

The boost carries three parameters, $\psi$ and the two angles of $\hat u_{\mathrm b}$, and the boost set is the three-dimensional hyperbolic space $H^3 = SL(2,\mathbb{C})/SU(2)$, the set of Lorentz boosts. The notation is the corpus's: $\tilde{\Lambda} = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\hat u_{\mathrm b}$ is the Lorentz boost biquaternion of the physics articles, Hermitian and of unit norm.

### The Conjugations and the Trivial Boost

**Under the conjugations** the quaternion conjugation and the coefficientwise conjugation replace the boost by its inverse, which is the boost of the same rapidity about the reflected axis, and the Hermitian conjugation fixes it, $\tilde U_{\mathrm b}^{*} = \tilde U_{\mathrm b}$.

**The boost is trivial** exactly when $\psi = 0$, that is, when $S = e_0$, equivalently when the unit-norm part $U$ is unitary; this holds on the centre and on the real quaternions.

## The Rotor

The fourth factor is the **rotor**,

$$
\tilde u_{\mathrm r} = \exp\Bigl(\tfrac{\theta}{2}\hat u_{\mathrm r}\Bigr) = \cos\tfrac{\theta}{2}\,e_0 + \sin\tfrac{\theta}{2}\,\hat u_{\mathrm r} , \qquad \theta \in [0,2\pi], \qquad \hat u_{\mathrm r}\in\mathcal{A} ,
$$

the unit real quaternion of the word, written $\tilde u_{\mathrm r}$ for short.

### The Exponent and the Root

The exponent $\tfrac{\theta}{2}\hat u_{\mathrm r}$ lies in $\mathbb{M}_- \cap \mathrm{Vect}(\mathbb{B})$, the real pure quaternions, the anti-Hermitian sector of the vector subspace; it is the only exponent that is neither central nor Hermitian. Its root is the real pure unit quaternion $\hat u_{\mathrm r}$, of square $-e_0$. The exponent carries half of the rotation angle: the conjugation by the rotor produces a rotation by the angle $\theta$. The rotor is compact and of real dimension $3$.

### The Residual and Its Unitarity

The rotor is the residual factor,

$$
\tilde u_{\mathrm r} = \tilde U_{\mathrm b}^{-1}U = \tilde U_{\mathrm b}^{\natural}\,U ,
$$

where $\tilde U_{\mathrm b}^{-1} = \tilde U_{\mathrm b}^{\natural}$ because $\langle \tilde U_{\mathrm b},\tilde U_{\mathrm b}\rangle_{\natural} = 1$ and $\tilde U_{\mathrm b}\tilde U_{\mathrm b}^{\natural} = \langle \tilde U_{\mathrm b},\tilde U_{\mathrm b}\rangle_{\natural}e_0 = e_0$. An element is **unitary** when it preserves the sesquilinear form, $\tilde U^{*}\tilde U = e_0$, and the unitary elements form the group $U(\mathbb{B})\cong U(2)$ (*Conventions in Mathematics*, §*The Unitary Convention*); the condition is narrower than norm one. The rotor is unitary,

$$
\tilde u_{\mathrm r}\,\tilde u_{\mathrm r}^{*} = \tilde U_{\mathrm b}^{-1}UU^{*}\tilde U_{\mathrm b}^{-1} = \tilde U_{\mathrm b}^{-1}S\,\tilde U_{\mathrm b}^{-1} = \tilde U_{\mathrm b}^{-1}\tilde U_{\mathrm b}^2\tilde U_{\mathrm b}^{-1} = e_0 ,
$$

using $S = \tilde U_{\mathrm b}^2$ and the Hermitian character of $\tilde U_{\mathrm b}$, which lets $\tilde U_{\mathrm b}^{-1}$ pass through the product. So $\tilde u_{\mathrm r}$ lies in the unitary group $U(\mathbb{B})\cong U(2)$.

### Why It Is a Real Quaternion

More is true: $\tilde u_{\mathrm r}$ is a real quaternion, that is, an element of the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, all four of whose coefficients are real. Two conditions are needed and both hold. First,

$$
\langle\tilde u_{\mathrm r},\tilde u_{\mathrm r}\rangle_{\natural} = \frac{\langle U,U\rangle_{\natural}}{\langle \tilde U_{\mathrm b},\tilde U_{\mathrm b}\rangle_{\natural}} = 1 ,
$$

by multiplicativity, so $\tilde u_{\mathrm r}$ is a unimodular unitary element, hence in $SU(2)$ in the matrix model. Second, the elements of $\mathbb{B}$ that are simultaneously unitary and of unit norm are exactly the unit real quaternions: an element of $U(2)$ is of the form $e^{i\beta}\tilde A$ with $\tilde A$ a unit real quaternion, and its biquaternion norm is $\langle e^{i\beta}\tilde A,e^{i\beta}\tilde A\rangle_{\natural} = e^{2i\beta}\langle\tilde A,\tilde A\rangle_{\natural} = e^{2i\beta}$, so the additional condition $N = 1$ forces $e^{2i\beta} = 1$, hence $\beta = 0$ modulo $\pi$, and leaves $\tilde A$ up to the sign that $N = 1$ fixes.

The rotor is therefore an element of

$$
\mathrm{Sp}(1) = \{\tilde u_{\mathrm r} \in \mathbb{H} : \tilde u_{\mathrm r}\tilde u_{\mathrm r}^{\natural} = 1\} = SU(2) ,
$$

the group of unit real quaternions, of dimension three. It is compact, and it is the same group that appears as the unit factor of the quaternion polar representation of the companion article. By the companion article on the Lorentz group, it acts on the material sector as a spatial rotation; the central phase $e^{i\alpha}$ has been split off from it, which is what distinguishes the present factor from the unitary factor of the matrix polar decomposition. Being non-central, the rotor does not commute with the boost, and that non-commutativity is the algebraic root of the Thomas-Wigner rotation of the physics articles: the product of two boosts is not a boost, and the discrepancy is a rotor.

### The Conjugations and the Trivial Rotor

**Under the conjugations** the rotor is fixed by the coefficientwise conjugation and inverted by the quaternion and the Hermitian conjugation,

$$
\bar{\tilde u_{\mathrm r}} = \tilde u_{\mathrm r} , \qquad \tilde u_{\mathrm r}^{\natural} = \tilde u_{\mathrm r}^{*} = \tilde u_{\mathrm r}^{-1} .
$$

**The rotor is trivial** exactly when the unit-norm part $U$ is Hermitian positive, that is, when $\tilde{Q} = \rho\,\tilde U_{\mathrm b}$.

## Why Four Factors

### The Centre and the Phase

The centre of $\mathbb{B}$ is $\mathbb{C}_{\mathbb{B}} \cong \mathbb{C}$, the complex scalars. An element of the centre commutes with everything, so a central factor can be moved through the other factors without changing the product, and the central group $U(1)$ is therefore a free one-parameter factor of any decomposition. The phase $e^{i\alpha}$ of the representation is this factor (§*The Central Phase*), and the corpus's articles on Noether's theorem and the gauge principle rest on the same centrality.

### The Hermitian and the Anti-Hermitian Halves

The Hermitian conjugation ${}^{*}$ is an involution, so the algebra splits into its fixed space and its anti-fixed space,

$$
\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_- , \qquad \mathbb{M}_\pm = \{\tilde{Q} : \tilde{Q}^{*} = \pm\tilde{Q}\},
$$

| subspace | condition | scalar part | vector part | matrix model | role |
|---|---|---|---|---|---|
| $\mathbb{M}_+$ | $\tilde{Q}^{*} = \tilde{Q}$ | real | purely imaginary | Hermitian matrices | the boosts |
| $\mathbb{M}_-$ | $\tilde{Q}^{*} = -\tilde{Q}$ | purely imaginary | real | anti-Hermitian matrices | the four-vectors |

In the matrix model, $\mathbb{M}_+$ is the subspace of Hermitian matrices and $\mathbb{M}_-$ the subspace of anti-Hermitian ones, and this is the split that the matrix polar decomposition uses: the positive factor of a polar decomposition is a Hermitian matrix with positive eigenvalues, and the unitary factor is an element of the unitary group.

The Hermitian subspace is four-dimensional, and it contains the scalars. Removing the scalar direction leaves the three-dimensional space of traceless Hermitian elements, whose exponential is the hyperbolic space of boosts:

$$
\exp\left(\mathbb{M}_+ \cap \{\text{traceless}\}\right) = \text{the unit boosts} .
$$

This is the second of the two three-dimensional factor spaces, and it is the only part of the decomposition that is not compact.

### The Unit Group and Its Two Counts

The invertible elements of $\mathbb{B}$ form the group $GL(2,\mathbb{C})$ in the matrix model. As a manifold this group factors as

$$
GL(2,\mathbb{C}) \cong \mathbb{C}^* \times SL(2,\mathbb{C}) \cong \big(\mathbb{R}_{>0}\times U(1)\big)\times\big(SU(2)\times H^3\big),
$$

with $H^3 = SL(2,\mathbb{C})/SU(2)$ the three-dimensional hyperbolic space. The four factors of the product are exactly the four factors of the decomposition.

| manifold factor | algebra factor | real dimension | symbol |
|---|---|---|---|
| $\mathbb{R}_{>0}$ | scale | $1$ | $r$ |
| $U(1)$ | central phase | $1$ | $e^{i\alpha}$ |
| $SU(2)$ | rotor | $3$ | $\tilde u_{\mathrm r}$ |
| $H^3 = SL(2,\mathbb{C})/SU(2)$ | boost | $3$ | $\tilde U_{\mathrm b}$ |

The factorisation is the polar decomposition of a complex matrix, read as a statement about the algebra. It is a factorisation of manifolds and not a direct product of groups: the multiplication map $(A,M)\mapsto AM$ is two-to-one, since $(-A,-M)$ has the same image, and the two preimages are the two branches of the square root of the determinant. The two counts of the four factors are nevertheless the same, and the doubling is the same sign ambiguity that the branch $\alpha\in(-\pi/2,\pi/2]$ removes in the representation.

### The Counting

The real dimensions of the four factors are

$$
\dim r = 1, \qquad \dim e^{i\alpha} = 1, \qquad \dim \tilde U_{\mathrm b} = 3, \qquad \dim \tilde u_{\mathrm r} = 3 ,
$$

and their sum is the real dimension of the algebra,

$$
1+1+3+3 = 8 = \dim_{\mathbb{R}}\mathbb{B} .
$$

The additivity is the structural statement that the four factors are independent, and it is the reason the representation is the reference one: no named form can exhibit more than two of the four slots at a time. The companion articles obtain the following counts in the same four slots.

| algebra | scale | phase | boost | rotor | total |
|---|---|---|---|---|---|
| $\mathbb{H}$ | $1$ | $0$ | $0$ | $3$ | $4$ |
| $\mathbb{H}_{\mathrm{s}}$ | $1$ | $0$ | $2$ | $1$ | $4$ |
| $\mathbb{B}$ | $1$ | $1$ | $3$ | $3$ | $8$ |
| $\mathbb{H}_{\mathbb{D}}$ | $1$ | $1$ | $0$ | $6$ | $8$ |

## The Order of the Factors

**The order is part of the word, because the boost is not central.** The additivity $1+1+3+3 = 8$ counts the four factors as **parameters**, and it does not say that they may be written in any order. The four factors are unique as an ordered quadruple, in the word

$$
\tilde{Q} = r\,e^{i\alpha}\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r} ,
$$

and the position of each factor in it is part of the statement. Among the four exponents only the scale and the phase are central, so the exponents do not commute.

**The two central factors are free.** Since the centre $\mathbb{C}_{\mathbb{B}}$ is the whole of the central elements, the phase may be transposed at no cost, $e^{i\alpha}\tilde U_{\mathrm b}\tilde u_{\mathrm r} = \tilde U_{\mathrm b}\tilde u_{\mathrm r}\,e^{i\alpha}$ exactly, and the same holds for the scale. The other two factors may not. The product $\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ differs from $\tilde u_{\mathrm r}\tilde U_{\mathrm b}$ as soon as the two axes are not parallel, and the difference vanishes exactly when they are, and then the word is a single boost-rotation about the common axis. In general the two orders are related by a conjugation,

$$
\tilde u_{\mathrm r}\tilde U_{\mathrm b} = \left(\tilde u_{\mathrm r}\tilde U_{\mathrm b}\tilde u_{\mathrm r}^{-1}\right)\tilde u_{\mathrm r} ,
$$

so reversing the order replaces the boost by the conjugate boost: the rapidity is unchanged, the axis is rotated by the rotor, and the element is a different one. The modulus is not affected, since a conjugation preserves the biquaternion norm, so the reversed word has the same $r$ and the same $\alpha$: the non-commutativity lives in the last two factors alone.

**The product is not the exponential of the sum.** Both orders are single exponentials of the Hamilton form, and comparing their exponents shows what the order changes: the complex angle $\Theta$, whose imaginary part is the rapidity and whose real part is the rotation angle, is the same in both orders, and only the root of $-1$ changes. The exponent of a **product** is a different matter and is not the sum of the exponents of the factors,

$$
\exp\left(\log \tilde U_{\mathrm b} + \log\tilde u_{\mathrm r}\right)\neq \tilde U_{\mathrm b}\tilde u_{\mathrm r} ,
$$

because the two non-central exponents do not commute, their bracket $[\log \tilde U_{\mathrm b},\log\tilde u_{\mathrm r}]$ being non-zero in general. A non-zero bracket forbids two rewritings at once: the interchange of the two non-central exponents, and the replacement of their product by the exponential of their sum. So the rapidity of a product is not the sum of the rapidities, and its rotation angle is not the sum of the rotation angles; only the modulus is additive, $r = r_1r_2$ and $\alpha = \alpha_1 + \alpha_2$, and it is exactly so.

**The word is order-free in a short list of cases.** The word becomes order-free in exactly the cases in which one of the two non-central factors is trivial or the two axes coincide: on the two halves, where $\tilde U_{\mathrm b} = e_0$; on the branches of the two sectors on which the rotor is $\pm e_0$; on the centre, where both are trivial; and for a rotor about the axis of the boost. In the last case the element is a single boost-rotation, which is why two boosts along the same line have no residual rotation.

**The three pairings are not reorderings.** All three keep the boost before the rotor; what a pairing moves is the single central factor, and where it needs the two non-central factors in the other order — as the complex form does, to stand its boost to the right of its modulus — it pays with a conjugation $\tilde u_{\mathrm r}^{-1}\tilde U_{\mathrm b}\tilde u_{\mathrm r}$, which is the boost about the rotated axis and not the original boost. The freedom of grouping and the lack of freedom of ordering are different freedoms, and the count $1+1+3+3$ is silent about both. The numerical illustration of the two orders is in *The Polar Decomposition of Biquaternions in Practice*.

## The Theorem

### Statement

**Theorem (polar representation).** Let $\tilde{Q}\in\mathbb{B}$ with $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\neq0$. Then there are unique

$$
r \in \mathbb{R}, \quad r>0, \qquad \alpha \in \left(-\frac{\pi}{2},\frac{\pi}{2}\right], \qquad \tilde U_{\mathrm b} = \cosh\frac{\psi}{2}\,e_0+i\sinh\frac{\psi}{2}\,\hat u_{\mathrm b} \in \mathbb{M}_+, \qquad \tilde u_{\mathrm r} \in \mathrm{Sp}(1),
$$

such that

$$
\tilde{Q} = r\,e^{i\alpha}\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r} .
$$

Equivalently, $\tilde{Q} = \rho \tilde U_{\mathrm b}\tilde u_{\mathrm r}$ with $\rho = re^{i\alpha} = \sqrt{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}}$ the principal square root.

### Existence

The construction of §*The Boost* and §*The Rotor* gives the factors: $\rho$ from the branch of the square root of the biquaternion norm, $U = \tilde{Q}/\rho$ of unit norm, $S = UU^{*}$ Hermitian positive definite of norm one, $\tilde U_{\mathrm b} = \sqrt{S}$ its unique Hermitian positive square root, and $\tilde u_{\mathrm r} = \tilde U_{\mathrm b}^{-1}U$, which is unitary and of norm one, hence a unit real quaternion. The product reproduces the element,

$$
r\,e^{i\alpha}\tilde U_{\mathrm b}\tilde u_{\mathrm r} = \rho\,\tilde U_{\mathrm b}\left(\tilde U_{\mathrm b}^{-1}U\right) = \rho U = \tilde{Q} .
$$

### Uniqueness

Suppose $\tilde{Q} = r e^{i\alpha}\tilde U_{\mathrm b}\tilde u_{\mathrm r} = r'e^{i\alpha'}\tilde U_{\mathrm b}'\tilde u_{\mathrm r}'$ with both quadruples admissible. Taking norms and using $\langle \tilde U_{\mathrm b}\tilde u_{\mathrm r},\tilde U_{\mathrm b}\tilde u_{\mathrm r}\rangle_{\natural} = \langle \tilde U_{\mathrm b},\tilde U_{\mathrm b}\rangle_{\natural}\langle\tilde u_{\mathrm r},\tilde u_{\mathrm r}\rangle_{\natural} = 1$ gives $r^2e^{2i\alpha} = (r')^2e^{2i\alpha'}$, so the two principal square roots of $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}$ agree, and since $r,r' > 0$ with $\alpha,\alpha'$ in the same half-open interval of length $\pi$, one has $r = r'$ and $\alpha = \alpha'$. Then $U = \tilde{Q}/\rho$ is the same element in both decompositions, so $UU^{*}$ is the same, and its Hermitian positive square root is unique, so $\tilde U_{\mathrm b} = \tilde U_{\mathrm b}'$; then $\tilde u_{\mathrm r} = \tilde U_{\mathrm b}^{-1}U = \tilde u_{\mathrm r}'$.

### The Domain and the Light Cone

The theorem is stated on the complement of the null cone, $\{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\neq0\}$, and that is exactly its domain: for $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = 0$ and $\tilde{Q}\neq0$ the element is a zero divisor, the matrix $\mathsf{M}_2(\tilde{Q})$ is singular, and no factorisation of the stated shape exists, since the product of the four factors has norm $r^2\cdot1\cdot1\cdot1 = r^2 > 0$ while $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = 0$. The null cone is the algebra's light cone, and it is treated in the companion article on biquaternion zero divisors. Among the decompositions of this series it is the mildest possible failure: a single cone, of real codimension two in the eight-dimensional algebra, whereas the partial forms of the companion articles fail on larger sets.

**The condition of existence, in one line.** The polar representation of $\tilde{Q}$ exists if and only if

$$
\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\neq0 ,
$$

that is, if and only if $\tilde{Q}$ lies outside the null cone; equivalently, by the determinant criterion of *Norm and Invertibility in the General Quaternionic Algebra*, if and only if $\tilde{Q}$ is invertible. The excluded elements are exactly the zero divisors, and no excluded element is reached as a limit of admissible ones: along a path to the cone the modulus $\rho = \sqrt{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}}$ tends to zero, while the norm-one part $\tilde{Q}/\rho$ has no limit in the algebra.

**The cone is thin in the algebra.** The condition $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = 0$ is one complex equation, hence two real equations, $\mathrm{Re}\,N = 0$ and $\mathrm{Im}\,N = 0$, and their gradients are independent away from the origin, so the cone has real codimension two. Counting real dimensions,

$$
\dim_{\mathbb{R}}\mathbb{B} = 8, \qquad
\dim_{\mathbb{R}}\{N = 0\} = 8 - 2 = 6, \qquad
\dim_{\mathbb{R}}\mathbb{B}^{\times} = 8 ,
$$

and deleting the cone does not lower the dimension of the algebra: the group of units $\mathbb{B}^{\times}$ and the algebra $\mathbb{B}$ are both eight-dimensional, and the domain of the polar representation is the algebra with a codimension-two set removed. The cone is stratified: away from the origin a generic point is a matrix of rank one, and at the single point $\tilde{Q} = 0$ the two gradients vanish together, so the cone is singular there, exactly as the classification of the zero divisors describes.

### The Boundary of the Family

The statement above says that on the null cone no factorisation of the four-factor shape exists; it does not say what the boundary of the family is. The limit of the boost family says it. Take the boost about the axis $-e_3$ and the real scale that collapses with it,

$$
r(\psi)\,\tilde U_{\mathrm b}(\psi) = e^{-\psi/2}\left(\cosh\tfrac{\psi}{2}\,e_0 - i\sinh\tfrac{\psi}{2}\,e_3\right) \longrightarrow \tfrac12\left(e_0 - ie_3\right), \qquad \psi \to \infty,
$$

the difference from the limit being exactly $\tfrac12e^{-\psi}$ in each of the two non-zero coefficients, as $e^{-\psi/2}\cosh(\psi/2)=(1+e^{-\psi})/2$ gives. The limit is the minimal idempotent $\tfrac12(e_0 + \hat\Xi i)$ with $\hat\Xi = -e_3$, the object classified in the companion article on biquaternion zero divisors: Hermitian, of norm zero, and idempotent. The word at the boundary therefore keeps a real scale and a trigonometric factor and fills the hyperbolic slot with a Hermitian idempotent of norm zero, one factor short of the four. Sangwine & Hitzer exhibit the same degeneration on a divisor of zero,

$$
\tilde P = \tfrac12\left(e_0 + e_1 + ie_2 - ie_3\right) = \sqrt2\cdot\frac{e_0+e_1}{\sqrt2}\cdot\tfrac12\left(e_0 - ie_3\right),
$$

whose last factor is that idempotent, and whose numerical factor $\sqrt2$ is not the modulus of $\tilde P$, which vanishes, but the modulus of the real part of $\tilde P$. The unbounded direction of the boost group and the null cone are thus a single cone, seen once as the boundary of the domain and once as the set of minimal idempotents, and the failure at that boundary is the collapse of the boost's positive factor rather than a discontinuity of the algebra.

## The Algorithm

The proof above is effective, and the procedure it yields is recorded, step by step, in the companion article *The Polar Decomposition of Biquaternions in Practice* (`articles_maths/the-polar-decomposition-of-biquaternions-in-practice.md`). That article gives the five steps in the order in which they are forced, the two invariants read off the four complex coordinates, the biquaternion norm and the Euclidean square, each of the four factors as a closed expression in those coordinates, the exponent of each factor with its position in the algebra, and three fully worked examples, one of them an element built from its factors and decomposed back. The word is the one stated above, and the branch of the square root of the modulus is its only convention.

## What the Sandwich Sees

The four factors are what an operator on the algebra detects, and the dagger sandwich $\mathrm{H}_{\tilde{Q}}(\tilde T)=\tilde{Q}\tilde T\tilde{Q}^{*}$ reads them as follows.

- The **scale** enters through the single dilation $\lvert \langle\tilde{Q},\tilde{Q}\rangle_{\natural}\rvert^{2}=r^{4}$ of the interval.
- The **central phase** enters through nothing at all, since the relation $\mathrm{H}_{A\tilde{Q}}=\lvert A\rvert^{2}\mathrm{H}_{\tilde{Q}}$ makes two elements differing by a unit-modulus central phase have the same operator.
- The remaining two factors, the **boost** and the **rotor**, are the boost part and the rotation part of the action, in the order of composition $\tilde U_{\mathrm b}\tilde u_{\mathrm r}$.

The kernel of the operator is the phase circle, so the phase is exactly the factor the action discards, while the scale survives only through its fourth power. The operator itself is in *Biquaternion Rotations and Lorentz Transformations*.

**The operator factorises through the boost and the rotor, and doubles their parameters.** With the polar word $\tilde{Q}=re^{i\alpha}\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ and $\tilde{\Lambda}=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ of unit norm,

$$
\mathrm{H}_{\tilde{Q}}=r^{2}\,\mathrm{H}_{\tilde{\Lambda}},
$$

because the Hermitian conjugates of the factors are $\tilde u_{\mathrm r}^{*}=\tilde u_{\mathrm r}^{-1}$, $\tilde U_{\mathrm b}^{*}=\tilde U_{\mathrm b}$, $r^{*}=r$ and $(e^{i\alpha})^{*}=e^{-i\alpha}$, so the two central factors cancel against their inverses. The pattern of the four factors as operators is then forced by the bilinearity:

| polar factor | range | as an operator on the algebra |
|---|---|---|
| scale $r$ | $(0,\infty)$ | dilatation by $r^{2}$, the factor counted twice |
| phase $e^{i\alpha}$ | $U(1)$ | none; it cancels and lies in the kernel |
| boost $\tilde U_{\mathrm b}$ | rapidity $\psi$, axis $\hat u_{\mathrm b}$ | boost of rapidity $\psi$, the exponent $\frac{\psi}{2}$ counted twice |
| rotor $\tilde u_{\mathrm r}$ | rotation angle $\theta$ | rotation by the angle $\theta$, the exponent $\frac{\theta}{2}$ counted twice |

A non-central factor occurs once on each side, so its parameter is deposited twice; a central factor occurs on both sides and cancels. The exact diagonal case is

$$
\mathsf{M}_2(\tilde U_{\mathrm b})=\operatorname{diag}\bigl(e^{\psi/2},e^{-\psi/2}\bigr)
\quad\Longrightarrow\quad
\mathsf{M}_2(\tilde U_{\mathrm b})\,\mathsf{M}_2(\tilde T)\,\mathsf{M}_2(\tilde U_{\mathrm b})=\operatorname{diag}\bigl(e^{\psi},e^{-\psi}\bigr)\mathsf{M}_2(\tilde T),
$$

in which the operator stores the half-rapidity and produces the rapidity. The same doubling holds for the rotation angle, and it is the geometric origin of the double cover $SL(2,\mathbb{C})\to SO^{+}(1,3)$ read in *Biquaternion Rotations and Lorentz Transformations* as the two-to-one rotor map.

## Degenerate Cases

### The Unit-Norm Elements

If $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = 1$ then $\rho = 1$, $r = 1$ and $\alpha = 0$, and the representation reduces to

$$
\tilde{Q} = \tilde U_{\mathrm b}\,\tilde u_{\mathrm r} , \qquad \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = 1 .
$$

This is the Cartan form of the physics articles, in which a Lorentz rotor is written as a **Lorentz boost** times a spatial rotation. It is the case of the decomposition in which two of the four factors are trivial, and it is the only case the physics corpus uses.

### The Central Elements

If $\tilde{Q} = Q_0e_0$ is a complex scalar then $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = Q_0^2$, and the construction returns $r = |Q_0|$, $\tilde U_{\mathrm b} = e_0$, and for the phase the representative of $\arg Q_0$ in $(-\pi/2,\pi/2]$, with the residual sign carried by $\tilde u_{\mathrm r} = \pm e_0$. The scalar imaginary itself has the decomposition

$$
i = 1\cdot e^{i\pi/2}\cdot e_0\cdot e_0 ,
$$

which exhibits the phase factor at its extremal value. This element is the sharpest illustration of the point of the four factors: two of the three named representations of the companion articles fail on it, since its vector part vanishes and its real quaternion part vanishes, while the representation is available and trivial.

### The Real Quaternions

If all four coefficients of $\tilde{Q}$ are real then $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \sum_\mu q_\mu^2$ is a positive real, so $\alpha = 0$ and $r = |\tilde{Q}|$ is the quaternion modulus of the companion article. The element $U = \tilde{Q}/r$ is a unit real quaternion, and $S = UU^{*} = UU^{\natural} = e_0$, so $\tilde U_{\mathrm b} = e_0$ and $\tilde u_{\mathrm r} = U$. The real quaternions therefore have no boost: their polar representation is the quaternion polar representation, and the two representations agree term by term.

### The Null Elements

If $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = 0$ and $\tilde{Q}\neq0$ the element is a zero divisor and no decomposition exists, as shown in the section on the domain. The failure is not uniform in the structure of the element: for $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = 0$ the matrix $\mathsf{M}_2(\tilde{Q})$ has rank one, its columns span a minimal left ideal, and the element is a multiple of an idempotent; the companion article on biquaternion zero divisors treats the classification. What is relevant here is only that no product of the four factors can reproduce it, because the biquaternion norm of such a product is a positive real.

### The Roots of One

The polar word is also read at a square root of one, and that reading — the two exponential forms the root set carries, the bridge between them, the Peirce decomposition that follows, and the Hamilton grouping of the same word — is developed in *The Hamilton Root Pairing of the Polar Element Representation of Biquaternions*.

## The Commutative Four-Dimensional Alternative

The four-factor representation above is the polar form of $\mathbb{B}$. The commutative four-dimensional algebra has its own, and it is the corpus's only polar form built for a commutative algebra of dimension four; it is recorded for the contrast, the two answering the same question differently.

The algebra is $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\oplus\mathbb{C}$, the reduced biquaternion algebra of *List of Algebras by Dimension*: an element is $q = A_1+A_2e$ with $e^2=+1$ and $A_1,A_2\in\mathbb{C}$. Pei, Chang and Ding construct its polar form (*IEEE Trans. Signal Processing* **52** (2004) 2012–2022, §III) and prove three things about it.

**Existence.** The form exists if and only if $\langle q,q\rangle_{\natural} = A_1^2-A_2^2\neq0$ — the domain condition of this article, and here it is also a factorisation statement, since $\langle q,q\rangle_{\natural} = \lambda_+\lambda_-$ in the idempotent coordinates $\lambda_\pm = A_1\pm A_2$. The excluded set is thus the union of the two ideals $\mathbb{C}e_+ \cup \mathbb{C}e_-$, with $e_\pm = \tfrac12(1\pm e)$, on which the element is a multiple of an idempotent; this is the commutative image of the null elements of the section above, and of the cone on which the four factors here fail.

**Uniqueness.** The form carries a scale and three phases, and it is unique once the ranges of the three phases are fixed; the uniqueness is proved by showing that the equations for the phases have exactly one solution in those ranges. The uniqueness here is therefore purchased by a range convention, whereas the uniqueness above is a theorem about the factorisation itself.

**Compatibility.** When the second component vanishes the form reduces to the ordinary complex polar form of *Complex Polar Element Representation*, which is the sense in which its authors select it as compatible with the complex case.

The form is useful for the two operations it is useful for here. Multiplication becomes trivial, moduli multiplying and phases adding, and the paper proves a **De Moivre theorem** for it; the inverse is read off directly; and the **geometric meaning** is stated — one scaling, four rotations in the coordinate planes $(1,2)$, $(3,4)$, $(1,4)$ and $(2,3)$, and two Lorentz transformations in the planes $(1,3)$ and $(2,4)$. That is the precise form of the claim recorded with this family of algebras in *The Three Two-Dimensional Algebras and the Three Kinds of Rotation*: the four-dimensional commutative algebra carries the elliptic rotations of its complex factor and the hyperbolic transformations of its split factor at the same time, and its authors attach the reading to the special theory of relativity.

One application is a use of a polar form the corpus does not otherwise have. The colour space is three-dimensional and the algebra four-dimensional, so the representation of a colour by an element of the algebra is not unique; the paper removes the redundancy by setting one of the three phases to zero, giving what it calls the **simplified polar form**, whose data are the brightness, hue and saturation of the colour and in which the norm and the conjugation of the element take their simplest forms. It is used for colour template matching and colour-sensitive edge detection, with the transforms of *Biquaternion Discrete Harmonic Analysis*.

## Relation to the Three Pairings

The relation of the present representation to the Hamilton, quaternion and Cartan pairings is the following. The Hamilton pairing, the first of the two **partial** regroupings, is stated here and developed in *The Hamilton Root Pairing of the Polar Element Representation of Biquaternions*; the quaternion pairing, the second, is developed in *The Quaternion Pairing of the Polar Element Representation of Biquaternions*; the Cartan pairing is the third grouping and is developed in *The Cartan Hermitian Pairing of the Polar Element Representation of Biquaternions*.

The **Hamilton form** writes $\tilde{Q} = R\exp(\hat\Xi\Theta)$ with $R$ a complex scalar and $\hat\Xi$ a non-central root of $-1$ parallel to the vector part; in the present notation its two factors are

$$
R = r\,e^{i\alpha}, \qquad \exp(\hat\Xi\Theta) = \tilde U_{\mathrm b}\,\tilde u_{\mathrm r} ,
$$

so that it groups the first two of the four factors into the modulus $R$ and the last two into the exponential. It is available whenever the vector part is non-null, which is a stronger condition than $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\neq0$.

The **quaternion form** writes $\tilde{Q} = Q\exp(i\Psi)$ with $Q$ a real quaternion; in the present notation its two factors are

$$
Q = r\,\tilde u_{\mathrm r} , \qquad \exp(i\Psi) = e^{i\alpha}\,\tilde u_{\mathrm r}^{\natural}\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r} ,
$$

so that it groups the scale with the rotor into the quaternion modulus and the phase with a conjugated boost into the exponential. Its construction in *The Quaternion Pairing of the Polar Element Representation of Biquaternions* proceeds from the real quaternion part of $\tilde{Q}$ and requires that part to be invertible, again a stronger condition than $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\neq0$.

Both partial forms are therefore regroupings of the same four factors, taken in pairs; there are exactly three ways to pair four objects into two pairs, and the third pairing, in which the scale is grouped with the boost and the phase with the rotor, is the Cartan pairing $\tilde{Q} = (r\tilde U_{\mathrm b})(e^{i\alpha}\tilde u_{\mathrm r})$, the matrix polar decomposition into a positive Hermitian factor and a unitary factor. The Hamilton form is treated in *The Hamilton Root Pairing of the Polar Element Representation of Biquaternions*, the quaternion form in *The Quaternion Pairing of the Polar Element Representation of Biquaternions*, and the Cartan pairing in *The Cartan Hermitian Pairing of the Polar Element Representation of Biquaternions*.

| representation | modulus | second factor | condition on $\tilde{Q}$ |
|---|---|---|---|
| Hamilton | $R = r\,e^{i\alpha}$ | $\exp(\hat\Xi\Theta) = \tilde U_{\mathrm b}\,\tilde u_{\mathrm r}$ | the vector part is non-null |
| quaternion pairing | $Q = r\,\tilde u_{\mathrm r}$ | $\exp(i\Psi) = e^{i\alpha}\,\tilde u_{\mathrm r}^{\natural}\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r}$ | the real quaternion part is invertible |
| Cartan | $r\,\tilde U_{\mathrm b}$ | $e^{i\alpha}\,\tilde u_{\mathrm r}$ | $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\neq0$ |

## Summary

Every biquaternion with non-vanishing norm has a unique polar representation

$$
\tilde{Q} = r\,e^{i\alpha}\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r} , \qquad r = \sqrt{\lvert\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\rvert} > 0, \quad \alpha = \tfrac{1}{2}\arg \langle\tilde{Q},\tilde{Q}\rangle_{\natural}, \quad \tilde U_{\mathrm b} \in \mathbb{M}_+, \quad \tilde u_{\mathrm r}\in\mathrm{Sp}(1) ,
$$

in which $\tilde U_{\mathrm b}$ is the Hermitian positive unit-norm boost and $\tilde u_{\mathrm r}$ the unit real quaternion rotor. The modulus of the decomposition is the complex number $\rho = re^{i\alpha} = \sqrt{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}}$, and the positive real factor $r$ is its absolute value, so a positive scale is always available and the phase is one of the four factors rather than a correction. The four factors have real dimensions $1+1+3+3 = 8$, they are unique, and the failure of the decomposition is exactly the null cone $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = 0$. The decomposition is the reference form of the series: the Hamilton form of *The Hamilton Root Pairing of the Polar Element Representation of Biquaternions* and the quaternion form of *The Quaternion Pairing of the Polar Element Representation of Biquaternions* are the two other pairings of the same four factors, and the Cartan form of the physics articles is the special case $N = 1$ in which the scale and the phase are trivial.

The word is a positive real times three exponentials of single elements of the algebra, read in one writing,

$$
\tilde{Q} = r\,\exp(i\alpha)\,\exp\Bigl(i\tfrac{\psi}{2}\hat u_{\mathrm b}\Bigr)\,\exp\Bigl(\tfrac{\theta}{2}\hat u_{\mathrm r}\Bigr) ,
$$

with the exponents

- $i\alpha$, central and of root $i$;
- $i\frac{\psi}{2}\hat u_{\mathrm b}$, traceless in $\mathbb{M}_+$, of root $i\hat u_{\mathrm b}$;
- $\tfrac{\theta}{2}\hat u_{\mathrm r}$, a real pure quaternion, of root $\hat u_{\mathrm r}$;

and the scale $r>0$ the degenerate hyperbolic factor, written without an exponential. The product is not the exponential of the sum of the exponents, because the two non-central exponents do not commute; the last two of them do collapse to a single exponential, $\exp\bigl(i\frac{\psi}{2}\hat u_{\mathrm b}\bigr)\exp\bigl(\frac{\theta}{2}\hat u_{\mathrm r}\bigr) = \exp(\hat\Xi\Theta)$, whenever the vector part is non-null, which is the Hamilton form $\tilde{Q} = R\exp(\hat\Xi\Theta)$ of *The Hamilton Root Pairing of the Polar Element Representation of Biquaternions*. The same word written at a root of one, $\langle\tilde\Xi,\tilde\Xi\rangle_{\natural} = \pm e_0$, is read in that article, together with the second, one-exponential form the root set carries on its halving idempotent and the chain that runs from the two pure factors to the idempotents and to the Peirce decomposition of the algebra.

## Summary of Notation

| symbol | set | meaning |
|---|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | — | the biquaternion algebra, $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ |
| $e_0 = 1$, $e_1,e_2,e_3$ | basis of $\mathbb{B}$ | the algebra unit and the quaternion units, $e_k^2 = -e_0$, $e_1e_2 = e_3$ |
| $Q_\mu$ | $\mathbb{C}$ | the four complex coefficients of $\tilde{Q}$ |
| $i$ | $\mathbb{C}_{\mathbb{B}}$, $i^2 = -1$ | the central scalar imaginary |
| $N = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = \sum_\mu Q_\mu^2$ | $\mathbb{C}$, central | the biquaternion norm, equal to $\det\mathsf{M}_2(\tilde{Q})$ |
| $\rho = \sqrt{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}}$ | $\mathbb{C}\setminus\{0\}$ | the complex modulus, the principal square root |
| $r = \sqrt{\lvert\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\rvert}$ | $\mathbb{R}$, $r > 0$ | the scale, a positive real |
| $\alpha = \tfrac{1}{2}\arg \langle\tilde{Q},\tilde{Q}\rangle_{\natural}$ | $\left(-\frac{\pi}{2},\frac{\pi}{2}\right]$ | the phase angle |
| $U = \tilde{Q}/\rho$ | $\mathbb{B}^{\times}_1$, $N(U)=e_0$ | the unit-norm part |
| $S = UU^{*} = \sigma e_0 + i\vec w$ | $\mathbb{M}_+$, positive definite, $N(S)=e_0$ | the Hermitian positive element, $\sigma\in\mathbb{R}$, $\sigma\ge1$, $\vec w\in\mathbb{R}^3$ |
| $\tilde U_{\mathrm b} = \sqrt{S}$ | $\mathbb{M}_+$, positive definite, $N(\tilde U_{\mathrm b})=e_0$ | the boost, a Hermitian positive unit element |
| $\psi$ | $\mathbb{R}$, $\psi\ge0$ | the rapidity of the boost |
| $\hat u_{\mathrm b}$ | $\mathcal{A}$, a unit vector of $\mathbb{R}^3$ | the axis of the boost |
| $i\frac{\psi}{2}\hat u_{\mathrm b}$ | traceless in $\mathbb{M}_+$ | the boost exponent |
| $\theta$ | $[0,2\pi]$ | the rotation angle of the rotor, whose stored half-angle is $\frac{\theta}{2}\in[0,\pi]$ |
| $\hat u_{\mathrm r}$ | $\mathcal{A}$, a unit vector of $\mathbb{R}^3$ | the axis of the rotor |
| $\frac{\theta}{2}\hat u_{\mathrm r}$ | real pure quaternion | the rotor exponent |
| $\hat\Xi$ | $\mathbb{B}$, $\hat\Xi^2 = -e_0$ | the Hamilton axis, the pure root of $-1$ parallel to the vector part |
| $\tilde u_{\mathrm r} = \tilde U_{\mathrm b}^{\natural}U$ | $\mathrm{Sp}(1)$ | the rotor, a unit real quaternion |
| $r\,\exp(i\alpha)\,\exp\bigl(i\frac{\psi}{2}\hat u_{\mathrm b}\bigr)\,\exp\bigl(\frac{\theta}{2}\hat u_{\mathrm r}\bigr)$ | — | the polar word, one positive real and three exponentials |
| $\mathbb{M}_+$ | subspace of $\mathbb{B}$ | the Hermitian subspace, real scalar part and imaginary vector part |
| $\mathbb{M}_-$ | subspace of $\mathbb{B}$ | the anti-Hermitian subspace, the material sector of the physics articles |
| $\mathbb{H}_{\mathbb{B}}$ | subspace of $\mathbb{B}$ | the real quaternion subspace, the fixed space of complex conjugation |
| $\mathrm{Sp}(1)$ | $Sp(1) = SU(2)$ | the unit real quaternions |

## Further Reading

- *Biquaternions as a Vector Space over $\mathbb{C}$* (`articles_maths/biquaternions-as-a-vector-space-over-c.md`), for the algebra, the four conjugations and the remarkable subspaces.
- *The Polar Decomposition of Biquaternions in Practice* (`articles_maths/the-polar-decomposition-of-biquaternions-in-practice.md`), for the procedure in full: the two invariants read off the coordinates, the five steps and their order, the factors in the coordinates of $\tilde{Q}$, the exponent of each factor with its position in the algebra, and the worked examples.
- *The 4 Forms over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-4-forms-over-the-biquaternion-c-space.md`), for the two forms that the procedure reads off the element, the complex bilinear norm $N$ and the Hermitian form, and for the Euclidean norm $\lVert\cdot\rVert_{E}$.
- *The Quaternion Pairing of the Polar Element Representation of Biquaternions* (`articles_maths/the-quaternion-pairing-of-the-polar-element-representation-of-biquaternions.md`), for the quaternion pairing and the comparison of the two partial two-factor groupings of these four factors, with their domains.
- *The Hamilton Root Pairing of the Polar Element Representation of Biquaternions* (`articles_maths/the-hamilton-root-pairing-of-the-polar-element-representation-of-biquaternions.md`), for the Hamilton grouping, its non-central root of $-1$, and the reading of the same word at the roots of one in the two exponential forms.
- *The Cartan Hermitian Pairing of the Polar Element Representation of Biquaternions* (`articles_maths/the-cartan-hermitian-pairing-of-the-polar-element-representation-of-biquaternions.md`), for the third two-factor grouping, $\tilde{Q} = HU$ with $H$ Hermitian positive and $U$ unitary, its Hermitian and anti-Hermitian exponent split and its full domain.
- *The Polar Element Representation and Remarkable Subspaces* (`articles_maths/the-polar-element-representation-and-remarkable-subspaces.md`), for the four exponents read against the four coordinate blocks and the six remarkable subspaces, the incidence of the exponents with the subspaces, and the polar data each subspace carries.
- *Split-Biquaternion Polar Element Representation* (`articles_maths/split-biquaternion-polar-element-representation.md`), for the semisimple analogue, whose modulus is split complex and whose rotor is six-dimensional.
- *Quaternion Polar Element Representation* (`articles_maths/quaternion-polar-element-representation.md`), for the two-factor case that this decomposition restricts to on the real quaternions.
- *Complex Polar Element Representation* (`articles_maths/complex-polar-element-representation.md`) and *Split-Complex Polar Element Representation* (`articles_maths/split-complex-polar-element-representation.md`), for the two-dimensional members of the series, where the rule of the exponential is stated once and the slots are counted in the smallest cases.
- *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* (`articles_physics/the-2x2-matrix-element-representation-m2c-of-biquaternions.md`), for the isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$, the determinant, and the matrix polar decomposition.
- *The Lorentz Group in Biquaternionic Form — Structure and Representations* (`articles_physics/the-lorentz-group-in-biquaternionic-form-structure-and-representations.md`), for the boost and rotation rotors and the Thomas-Wigner rotation.
- S. J. Sangwine and E. Hitzer, "Polar decomposition of complexified quaternions and octonions", *Advances in Applied Clifford Algebras* (2020), DOI 10.1007/s00006-020-1048-y; technical report CES-535, University of Essex (2019), for the published two-exponential factorisation of the unit semi-norm elements and, in the general case, its Corollary 1 — whose trigonometric factor is the rotor $\tilde u_{\mathrm r}$ of this article and whose hyperbolic factor is the boost about the rotor-conjugated axis, $\tilde U_{\mathrm b} = \tilde u_{\mathrm r}^{-1}H\tilde u_{\mathrm r}$ with the same rapidity and norm — for Lemma 1, the trichotomy of the exponential of a hypercomplex root of $-1$, $0$ or $+1$, and for the degenerate word on the null cone of the boundary subsection above. The order of the two non-central factors is reversed there, angle first, and the complex modulus is kept whole rather than split into a scale and a phase, which is the difference of count $2+3+3$ against $1+1+3+3$; the corpus fixes the branch and proves uniqueness, while the paper admits both orders.
- Soo-Chang Pei, Ja-Han Chang and Jian-Jiun Ding, "Commutative reduced biquaternions and their Fourier transform for signal and image processing applications", *IEEE Transactions on Signal Processing* **52** (2004) 2012–2022, for the reduced biquaternion algebra — the commutative four-dimensional algebra $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\oplus\mathbb{C}$, equivalently the double-complex, tessarine or commutative hypercomplex algebra — and for its polar form, its uniqueness under the phase-range convention, its De Moivre theorem and the simplified polar form for colour images.
