# __The Polar Element Representation of Biquaternions__

## Introduction

This article is about the **polar representation** of a biquaternion: the statement that every biquaternion with non-vanishing norm is the product of four factors,

$$
\tilde{Q} = r\,e^{i\alpha}\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r} ,
$$

where the four factors are the following.

| # | factor | name | real dimension | range or condition |
|---|---|---|---|---|
| 1 | $r$ | scale | $1$ | $r \in \mathbb{R}$, $r>0$ |
| 2 | $e^{i\alpha}$ | central phase | $1$ | $\alpha \in \left(-\frac{\pi}{2},\frac{\pi}{2}\right]$, defined modulo $2\pi$ before the branch is fixed |
| 3 | $\tilde U_{\mathrm b}$ | boost | $3$ | Hermitian positive definite, a unit element, $N(\tilde U_{\mathrm b})=e_0$ |
| 4 | $\tilde u_{\mathrm r}$ | rotor | $3$ | a unit real quaternion of $\mathbb{H}_{\mathbb{B}}$, $\mathrm{Sp}(1)$, $N(\tilde u_{\mathrm r})=e_0$ |

The norm in view is the biquaternion norm $N = \langle\cdot,\cdot\rangle_{\natural}$, so a **unit element** is an element with $N = e_0$ (*Conventions in Mathematics*, §*The Unitary Convention*); the boost and the rotor are the two unit elements of the word, and the scale and the phase are not.

The four factors are unique, and their real dimensions $1+1+3+3$ sum to the eight real dimensions of the algebra.

The modulus of the representation is the complex number $\rho = \sqrt{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}}$, developed in §*The Complex Modulus*.

The conventions and the symbols are those of the corpus (*Conventions in Mathematics*, §*Symbols*, §*The Unitary Convention*); the symbols this article uses are collected in §*Summary of Notation*.

No physics is invoked. Every numerical value displayed below was recomputed in double precision.

## The Exponentials of the Factors

Every one of the four factors is the exponential of a single element of the algebra, and the polar word is the ordered product of the four exponentials,

$$
\tilde{Q} = \exp(\ln r)\,\exp(i\alpha)\,\exp\Bigl(i\tfrac{\psi}{2}\hat u_{\mathrm b}\Bigr)\,\exp\Bigl(\tfrac{\theta}{2}\hat u_{\mathrm r}\Bigr) ,
$$

| # | factor | name | real dimension | exponential | case | closed form | parameter and range | unit axis |
|---|---|---|---|---|---|---|---|---|
| 1 | $r$ | scale | $1$ | $\exp(\ln r)$ | hyperbolic | $r$ | $\ln r \in \mathbb{R}$, $r > 0$ | — |
| 2 | $e^{i\alpha}$ | central phase | $1$ | $\exp(i\alpha)$ | trigonometric | $\cos\alpha\,e_0 + i\sin\alpha$ | $\alpha \in \left(-\frac{\pi}{2},\frac{\pi}{2}\right]$ | — |
| 3 | $\tilde U_{\mathrm b}$ | boost | $3$ | $\exp\bigl(i\frac{\psi}{2}\hat u_{\mathrm b}\bigr)$ | hyperbolic | $\cosh\frac{\psi}{2}\,e_0 + i\sinh\frac{\psi}{2}\,\hat u_{\mathrm b}$ | rapidity $\psi \in \mathbb{R}$, $\psi \ge 0$ | $\hat u_{\mathrm b}\in\mathcal{A}$, a unit vector of $\mathbb{R}^3$ |
| 4 | $\tilde u_{\mathrm r}$ | rotor | $3$ | $\exp\bigl(\tfrac{\theta}{2}\hat u_{\mathrm r}\bigr)$ | trigonometric | $\cos\tfrac{\theta}{2}\,e_0 + \sin\tfrac{\theta}{2}\,\hat u_{\mathrm r}$ | rotation angle $\theta \in [0,2\pi]$ | $\hat u_{\mathrm r}\in\mathcal{A}$, a unit vector of $\mathbb{R}^3$ |

**The two axes.** The boost axis $\hat u_{\mathrm b}$ is the direction of the motion; the rotor axis $\hat u_{\mathrm r}$ is the axis of the rotation. Each of them is one direction in space. A direction is given by three real numbers, its cosines on the basis vectors $e_1,e_2,e_3$, and the three numbers have squares that sum to one,

$$
\hat u = \hat u_1e_1+\hat u_2e_2+\hat u_3e_3 , \qquad \hat u_1,\hat u_2,\hat u_3\in\mathbb{R} , \qquad \hat u_1^2+\hat u_2^2+\hat u_3^2=1 .
$$

The **axis sphere** is the collection of all such directions. Three words describe one of its members.

- It is **real**: the three coordinates are real numbers and not complex ones, and the imaginary unit $i$ never multiplies them.
- It is **pure**: there is no $e_0$ term among the three, so its scalar part is zero. The word describes the missing coefficient, not the three present ones.
- It is **unit**: its length is one, which is the condition $\hat u_1^2+\hat u_2^2+\hat u_3^2=1$.

The three conditions have one algebraic consequence. Squaring the direction gives $\hat u^2=-e_0$, so the axis sphere is exactly the set of roots of $-e_0$ in $\mathbb{H}$: the quaternion roots of $-1$. The direction $e_1$ is one of them, the direction $(\tfrac{1}{\sqrt2},\tfrac{1}{\sqrt2},0)$ is another, and $e_0$ is not one of them, because it has a scalar part and its length is one only in the trivial sense of the scalar line.

The set is written $\mathcal{A}$ and not $S$, so that the symbol $S$ stays with the spin groups $\mathrm{Spin}(n)$ of the spinor context; the group of unit quaternions is written $\mathrm{Sp}(1)$.

The four exponentials are read off a single rule, which every algebra of the polar series follows: the character of the exponential is trigonometric, hyperbolic or parabolic according to the square of the root of the exponent, a root of $-e_0$ giving the trigonometric case, a root of $+e_0$ the hyperbolic case, and a nilpotent root the parabolic case, where the series truncates to the unit plus the exponent. The parabolic case produces no factor of the polar representation but is not empty in $\mathbb{B}$: the element $e_1+ie_2$ has square zero, so its exponential is $e_0+(e_1+ie_2)$, of norm one and neither a rotor nor a boost. The rule is Lemma 1 of Sangwine & Hitzer, stated there for a hypercomplex root of $-1$, $0$ or $+1$.

### The Exponent of Each Factor

Each exponent is a real parameter times a **root** of $-e_0$, $0$ or $+e_0$ — the generator of a one-parameter group (*Conventions in Mathematics*, §*The Root Convention*) — and the character of its exponential is the square of that root.

| factor | exponent | where the exponent lies |
|---|---|---|
| $r$ | $\ln r$ | the real line $\mathbb{R}e_0$ |
| $e^{i\alpha}$ | $i\alpha$ | the imaginary line $i\mathbb{R}\subset\mathbb{C}_{\mathbb{B}}$ |
| $\tilde U_{\mathrm b}$ | $i\frac{\psi}{2}\hat u_{\mathrm b}$ | $\mathbb{M}_+$, traceless |
| $\tilde u_{\mathrm r}$ | $\tfrac{\theta}{2}\hat u_{\mathrm r}$ | $\mathbb{M}_- \cap \mathrm{Vect}(\mathbb{B})$, the real pure quaternions |

| factor | parameter | root | its square |
|---|---|---|---|
| $r$ | $\ln r$ | $e_0$ | $+e_0$ |
| $e^{i\alpha}$ | $\alpha$ | $i$ | $-e_0$ |
| $\tilde U_{\mathrm b}$ | $\frac{\psi}{2}$ | $i\hat u_{\mathrm b}$ | $+e_0$ |
| $\tilde u_{\mathrm r}$ | $\tfrac{\theta}{2}$ | $\hat u_{\mathrm r}$ | $-e_0$ |

The scale is the degenerate case of the hyperbolic row: its exponent is the real scalar $\ln r$, its root is the algebra unit $e_0$, and the factor is positive by construction, since $r>0$. The phase and the rotor are the two roots of $-e_0$ of the trigonometric row, one central and one a real pure quaternion. The boost is the root of $+e_0$ of the hyperbolic row, the Hermitian $i\hat u_{\mathrm b}$. The positions of the four exponents in the algebra are the subject of the section on why there are four factors: the exponent of the boost lies in the Hermitian subspace $\mathbb{M}_+$, of real scalar part and purely imaginary vector part, and it is traceless because its scalar part vanishes; the exponent of the rotor lies in $\mathbb{M}_- \cap \mathrm{Vect}(\mathbb{B})$, the real pure quaternions, and a unit one squares to $-e_0$ because a real pure quaternion $x$ has $\langle x,x\rangle_{\natural} = -\,(x,x)$.

The exponents of the two non-central factors carry half of the parameter of the transformation they produce. The boost exponent is $\frac{\psi}{2}\hat u_{\mathrm b}$, with $\psi$ the rapidity, and the conjugation by the boost produces a boost of rapidity $\psi$; the rotor exponent is $\frac{\theta}{2}\hat u_{\mathrm r}$, with $\theta$ the rotation angle, and the conjugation by the rotor produces a rotation by the angle $\theta$. Each non-central exponent therefore carries half of the parameter it produces, and the stored half is counted twice, which is the reading of the double cover on the exponents, the same doubling that §*What the Sandwich Sees* records.

### The Two Cautions of the Exponential Reading

The product of the four exponentials is **not** the exponential of the sum of the four exponents, because the two non-central exponents do not commute. The size of the failure is measured in the section on the order of the factors, where the same pair of factors gives $\|\exp(\log \tilde U_{\mathrm b} + \log\tilde u_{\mathrm r}) - \tilde U_{\mathrm b}\tilde u_{\mathrm r}\| = 0.160024643$ against $\|[\log \tilde U_{\mathrm b},\log\tilde u_{\mathrm r}]\| = 0.308850825$, and where the product of the four exponentials is shown to be order-free exactly when one of the two non-central factors is trivial or the two axes coincide.

**The order cannot be changed, and the two non-central exponentials cannot be fused.** Both facts are the non-vanishing of the bracket $[\log \tilde U_{\mathrm b},\log\tilde u_{\mathrm r}]$, which measures how far the boost and the rotor are from commuting. Over $60$ random boosts and rotors the largest coefficient of that bracket is $3.58$ and the largest coefficient of the failure $\exp(\log \tilde U_{\mathrm b}+\log\tilde u_{\mathrm r})-\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ of the sum rule is $0.76$. A non-zero bracket forbids two rewritings at once: the interchange of the two non-central exponents, and the replacement of their product by the exponential of their sum. The phase is central and passes through both, so the order that matters is the relative order of the boost and the rotor; the word $re^{i\alpha}\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ fixes that relative order, and no rewriting of the four exponents changes it. The element still has a single exponential, but its exponent is read off the element and is **not** the sum $\log \tilde U_{\mathrm b} + \log\tilde u_{\mathrm r}$.

The last two exponentials collapse to a **single** one whenever the vector part of the element is non-null. Then $\tilde U_{\mathrm b}\tilde u_{\mathrm r} = \exp(\hat\Xi\Theta)$, with $\hat\Xi$ a root of $-1$ ($\hat\Xi\in\mathbb{B}$, $\hat\Xi^2 = -e_0$, the generator parallel to the vector part) and $\Theta\in\mathbb{C}$ the complex angle whose real part is the rotation angle and whose imaginary part is the rapidity, so that the element is the single exponential $\tilde{Q} = R\,\exp(\hat\Xi\Theta)$ with $R = re^{i\alpha}\in\mathbb{C}$ central. This is the Hamilton representation, the first of the three pairings of the companion article, and the condition on the vector part, the constancy of $\Theta$ across the two orders and the numerical values are those of the section on the order of the factors.

## Why Four Factors

### The Centre and the Phase

The centre of $\mathbb{B}$ is $\mathbb{C}_{\mathbb{B}} \cong \mathbb{C}$, the complex scalars. An element of the centre commutes with everything, so a central factor can be moved through the other factors without changing the product, and the central group $U(1)$ is therefore a free one-parameter factor of any decomposition. The phase $e^{i\alpha}$ of the representation is this factor, and the corpus's articles on Noether's theorem and the gauge principle rest on the same centrality.

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

### The Order of the Factors

**The order is part of the word, because $\tilde U_{\mathrm b}$ is not central.** The additivity $1+1+3+3 = 8$ counts the four factors as **parameters**, and it does not say that they may be written in any order. The four factors are unique as an ordered quadruple, in the word

$$
\tilde{Q} = r\,e^{i\alpha}\tilde U_{\mathrm b}\tilde u_{\mathrm r} ,
$$

and the position of each factor in it is part of the statement. All four are exponentials of a single element, as the section *The Exponentials of the Factors* above records in full; among the four exponents only the scale and the phase are central, so the exponents do not commute.

Since the centre $\mathbb{C}_{\mathbb{B}}$ is the whole of the central elements, the phase may be transposed at no cost, $e^{i\alpha}\tilde U_{\mathrm b}\tilde u_{\mathrm r} = \tilde U_{\mathrm b}\tilde u_{\mathrm r}\,e^{i\alpha}$ exactly, and the same holds for the scale. The other two factors may not be transposed. With $\tilde U_{\mathrm b}$ of rapidity $\psi = 0.7$ about $\hat u_{\mathrm b} = (1,0.3,0.2)/\|(1,0.3,0.2)\|$ and $\tilde u_{\mathrm r}$ of stored half-angle $\theta/2 = 0.6$ about $\hat u_{\mathrm r} = (\sin0.5,\ 0,\ \cos0.5)$,

$$
\left\|\tilde U_{\mathrm b}\tilde u_{\mathrm r} - \tilde u_{\mathrm r}\tilde U_{\mathrm b}\right\| = 0.296621057 ,
$$

where $\|\cdot\|$ denotes the largest modulus among the coefficient differences. The difference vanishes exactly when the two axes are parallel, and then the word is a single boost-rotation about the common axis. In general the two orders are related by a conjugation,

$$
\tilde u_{\mathrm r}\tilde U_{\mathrm b} = \left(\tilde u_{\mathrm r}\tilde U_{\mathrm b}\tilde u_{\mathrm r}^{-1}\right)\tilde u_{\mathrm r} ,
$$

so reversing the order replaces the boost by the conjugate boost: the rapidity is unchanged, the axis is rotated by the rotor, and the element is a different one. The modulus is not affected, since a conjugation preserves the biquaternion norm, so the reversed word has the same $r$ and the same $\alpha$: the non-commutativity lives in the last two factors alone.

Both orders are single exponentials of the Hamilton form, and comparing their exponents shows what the order does and does not change. For the same pair,

$$
\tilde U_{\mathrm b}\tilde u_{\mathrm r} = \exp(\xi_1\Theta) , \qquad \tilde u_{\mathrm r}\tilde U_{\mathrm b} = \exp(\xi_2\Theta) , \qquad \Theta = 0.549803506 + 0.235625491\,i , \qquad \left\|\xi_1 - \xi_2\right\| = 0.553422443 ,
$$

with $\xi_1,\xi_2$ roots of $-1$: the complex angle $\Theta$, whose imaginary part is the rapidity and whose real part is the rotation angle, is the same in both orders, and only the root changes. The exponent of a **product** is a different matter and is not the sum of the exponents of the factors,

$$
\exp\left(\log \tilde U_{\mathrm b} + \log\tilde u_{\mathrm r}\right)\neq \tilde U_{\mathrm b}\tilde u_{\mathrm r} , \qquad \left\|\exp\left(\log \tilde U_{\mathrm b} + \log\tilde u_{\mathrm r}\right) - \tilde U_{\mathrm b}\tilde u_{\mathrm r}\right\| = 0.160024643 , \qquad \left\|\left[\log \tilde U_{\mathrm b},\ \log\tilde u_{\mathrm r}\right]\right\| = 0.308850825 \neq 0 ,
$$

so the rapidity of a product is not the sum of the rapidities, and its rotation angle is not the sum of the rotation angles. Only the modulus is additive, $r = r_1r_2$ and $\alpha = \alpha_1 + \alpha_2$, and it is exactly so.

The non-commutativity is a property of the boost factor rather than of the representation. The boost $\tilde U_{\mathrm b}$ is Hermitian and positive definite of norm one, so it is a multiple of the unit only when $\tilde U_{\mathrm b} = e_0$; it is therefore non-central whenever it is nontrivial, and that non-centrality is what forbids the transposition. The word becomes order-free in exactly the cases in which one of the two non-central factors is trivial or the two axes coincide: on the two halves, where $\tilde U_{\mathrm b} = e_0$; on the branches of the two sectors on which the rotor is $\pm e_0$; on the centre, where both are trivial; and for a rotor about the axis of the boost. In the last case the element is a single boost-rotation, which is why two boosts along the same line have no residual rotation.

The three pairings of the companion article *Biquaternion Partial Polar Element Representations* are not reorderings of the word. All three keep $\tilde U_{\mathrm b}$ before $\tilde u_{\mathrm r}$; what a pairing moves is the single central factor, and where it needs the two non-central factors in the other order — as the complex form does, to stand its boost to the right of its modulus — it pays with a conjugation $\tilde u_{\mathrm r}^{-1}\tilde U_{\mathrm b}\tilde u_{\mathrm r}$, which is the boost about the rotated axis and not the original boost. The freedom of grouping and the lack of freedom of ordering are different freedoms, and the count $1+1+3+3$ is silent about both.

## The Complex Modulus

### The Biquaternion Norm

The biquaternion norm is

$$
\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = \sum_{\mu=0}^{3}Q_\mu^2 ,
$$

the sum of the squares of the four complex coefficients. It is a complex number, it is central, and it is multiplicative,

$$
\langle\tilde{P}\tilde{Q},\tilde{P}\tilde{Q}\rangle_{\natural} = \langle\tilde{P},\tilde{P}\rangle_{\natural}\langle\tilde{Q},\tilde{Q}\rangle_{\natural}.
$$

In the matrix model it is the determinant, $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \det\mathsf{M}_2(\tilde{Q})$, so $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = 0$ is exactly the condition that $\tilde{Q}$ be a zero divisor, and the set $\{N = 0\}$ is the algebra's null cone.

### The Square Root and the Branch

The modulus is the square root of the biquaternion norm. To make it single valued, fix the branch once and for all. Write the biquaternion norm in polar form in $\mathbb{C}$,

$$
\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = |\langle\tilde{Q},\tilde{Q}\rangle_{\natural}|\,e^{i\varphi}, \qquad \varphi = \arg \langle\tilde{Q},\tilde{Q}\rangle_{\natural} \in (-\pi,\pi] ,
$$

and define

$$
\rho = \sqrt{|\langle\tilde{Q},\tilde{Q}\rangle_{\natural}|}\;e^{i\varphi/2} ,
$$

which is the principal square root of $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}$. Its modulus and argument are

$$
r = |\rho| = \sqrt{|\langle\tilde{Q},\tilde{Q}\rangle_{\natural}|} \ \ge 0, \qquad \alpha = \arg\rho = \frac{\varphi}{2} \in \left(-\frac{\pi}{2},\frac{\pi}{2}\right] .
$$

The pair $(r,\alpha)$ is unique: the modulus is non-negative by construction and the angle lies in a half-open interval of length $\pi$, so no two pairs give the same $\rho$. The square root $\rho$ is one of the two solutions of $\tilde T^2 = \langle\tilde{Q},\tilde{Q}\rangle_{\natural}$, and the branch choice above selects one of them; the other, $-\rho$, has angle $\alpha\pm\pi$ and is outside the interval.

### The Positive Real Part and the Phase

The modulus is the first two factors of the decomposition written as one,

$$
\rho = r\,e^{i\alpha},
$$

with $r$ a positive real and $e^{i\alpha}$ central. This is the sense in which the representation always supplies a positive real factor: the positive real part of the complex square root of the biquaternion norm exists whenever the biquaternion norm is nonzero, and it is the absolute value $|\langle\tilde{Q},\tilde{Q}\rangle_{\natural}|^{1/2}$.

The phase is not a normalisation constant, and its value carries information: it is one half of the argument of the determinant of $\tilde{Q}$, and it is nonzero exactly when $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}$ is not a positive real. In the physical reading of the companion articles, $e^{i\alpha}$ is the central phase that the corpus's Noether and gauge articles identify as the algebra's continuous symmetry.

## The Hermitian Positive Factor

### The Element of Unit Norm

The word **unit** is the corpus's, and it is relative to the norm: a **unit element** is an element of norm one, the norm being the one in view (*Conventions in Mathematics*, §*The Unitary Convention*). The norm in view here is the biquaternion norm $N = \langle\cdot,\cdot\rangle_{\natural}$, whose unit elements are the level set $\mathbb{B}^{\times}_1 = \{N = e_0\}$, the group of unit-norm elements, the special linear group $SL(2,\mathbb{C})$ in the matrix picture. A **unitary** element, by contrast, is one that preserves the sesquilinear form, and it is a narrower object, defined in the next section.

Divide the biquaternion by its modulus:

$$
U = \frac{\tilde{Q}}{\rho} .
$$

Then $U$ has unit norm,

$$
\langle U,U\rangle_{\natural} = \frac{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}}{\rho^2} = \frac{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}}{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}} = 1 ,
$$

so $U$ lies in the algebra's analogue of the special linear group, and the whole content of the decomposition now sits in the split $U = \tilde U_{\mathrm b}\tilde u_{\mathrm r}$.

### The Square Root of $UU^{*}$

Form the Hermitian element

$$
S = U U^{*} .
$$

It is Hermitian, since $S^{*} = (UU^{*})^{*} = UU^{*} = S$, and it is positive definite, because in the matrix model $\mathsf{M}_2(S) = \mathsf{M}_2(U)\mathsf{M}_2(U)^\dagger$ is a positive definite Hermitian matrix whenever $\mathsf{M}_2(U)$ is invertible. Its biquaternion norm is

$$
\langle S,S\rangle_{\natural} = \langle U,U\rangle_{\natural}\,\langle U^{*},U^{*}\rangle_{\natural} = \langle U,U\rangle_{\natural}\,\langle U,U\rangle_{\natural}^{*} = 1 ,
$$

using multiplicativity, the reality of $\langle U,U\rangle_{\natural} = 1$, and $\langle U^{*},U^{*}\rangle_{\natural} = \langle U,U\rangle_{\natural}^*$.

The element $S$ is not itself the boost. The boost is its Hermitian positive square root,

$$
\tilde U_{\mathrm b} = \sqrt{S} , \qquad \tilde U_{\mathrm b}^2 = S ,
$$

which exists and is unique: a positive definite Hermitian matrix has exactly one positive definite Hermitian square root, and the condition $\langle S,S\rangle_{\natural} = 1$ is inherited as $\langle \tilde U_{\mathrm b},\tilde U_{\mathrm b}\rangle_{\natural}^2 = \langle S,S\rangle_{\natural} = 1$, so $\langle \tilde U_{\mathrm b},\tilde U_{\mathrm b}\rangle_{\natural} = 1$ for the positive root. The element $\tilde U_{\mathrm b}$ is not arbitrary in $\mathbb{M}_+$: the square root of a norm-one element has norm one, and that is the normalisation of the boost.

### The Closed Form of the Boost

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


$$
\frac{1+\sigma}{2} - \frac{|\vec w|^2}{2(1+\sigma)} = \frac{(1+\sigma)^2 - |\vec w|^2}{2(1+\sigma)} = \frac{2\sigma(1+\sigma)}{2(1+\sigma)} = \sigma ,
$$

where $|\vec w|^2 = \sigma^2-1$ was used, which is the statement $\langle S,S\rangle_{\natural} = \sigma^2-|\vec w|^2 = 1$ for the Hermitian element $S$. The result is $\sigma + i\vec w = S$.

### The Rapidity and the Axis

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

The boost therefore carries three parameters, $\psi$ and the two angles of $\hat u_{\mathrm b}$, and the boost set is the three-dimensional hyperbolic space $H^3$ of the previous section, the set of Lorentz boosts. The notation is the corpus's: $\tilde{\Lambda} = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\hat u_{\mathrm b}$ is the Lorentz boost biquaternion of the physics articles, Hermitian and of unit norm.

## The Unitary Factor

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

the group of unit real quaternions, of dimension three. It is compact, and it is the same group that appears as the unit factor of the quaternion polar representation of the companion article. By the companion article on the Lorentz group, it acts on the material sector as a spatial rotation; the central phase $e^{i\alpha}$ has been split off from it, which is what distinguishes the present factor from the unitary factor of the matrix polar decomposition.

## The Theorem

### Statement

**Theorem (polar representation).** Let $\tilde{Q}\in\mathbb{B}$ with $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\neq0$. Then there are unique

$$
r \in \mathbb{R}, \quad r>0, \qquad \alpha \in \left(-\frac{\pi}{2},\frac{\pi}{2}\right], \qquad \tilde U_{\mathrm b} = \cosh\frac{\psi}{2}+i\sinh\frac{\psi}{2}\hat u_{\mathrm b} \in \mathbb{M}_+, \qquad \tilde u_{\mathrm r} \in \mathrm{Sp}(1),
$$

such that

$$
\tilde{Q} = r\,e^{i\alpha}\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r} .
$$

Equivalently, $\tilde{Q} = \rho \tilde U_{\mathrm b}\tilde u_{\mathrm r}$ with $\rho = re^{i\alpha} = \sqrt{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}}$ the principal square root.

### Existence

The construction of the three preceding sections gives the factors: $\rho$ from the branch of the square root of the biquaternion norm, $U = \tilde{Q}/\rho$ of unit norm, $S = UU^{*}$ Hermitian positive definite of norm one, $\tilde U_{\mathrm b} = \sqrt{S}$ its unique Hermitian positive square root, and $\tilde u_{\mathrm r} = \tilde U_{\mathrm b}^{-1}U$, which is unitary and of norm one, hence a unit real quaternion. The product reproduces the element,

$$
r\,e^{i\alpha}\tilde U_{\mathrm b}\tilde u_{\mathrm r} = \rho\,\tilde U_{\mathrm b}\left(\tilde U_{\mathrm b}^{-1}U\right) = \rho U = \tilde{Q} .
$$

### Uniqueness

Suppose $\tilde{Q} = r e^{i\alpha}\tilde U_{\mathrm b}\tilde u_{\mathrm r} = r'e^{i\alpha'}\tilde U_{\mathrm b}'\tilde u_{\mathrm r}'$ with both quadruples admissible. Taking norms and using $\langle \tilde U_{\mathrm b}\tilde u_{\mathrm r},\tilde U_{\mathrm b}\tilde u_{\mathrm r}\rangle_{\natural} = \langle \tilde U_{\mathrm b},\tilde U_{\mathrm b}\rangle_{\natural}\langle\tilde u_{\mathrm r},\tilde u_{\mathrm r}\rangle_{\natural} = 1$ gives $r^2e^{2i\alpha} = (r')^2e^{2i\alpha'}$, so the two principal square roots of $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}$ agree, and since $r,r' > 0$ with $\alpha,\alpha'$ in the same half-open interval of length $\pi$, one has $r = r'$ and $\alpha = \alpha'$. Then $U = \tilde{Q}/\rho$ is the same element in both decompositions, so $UU^{*}$ is the same, and its Hermitian positive square root is unique, so $\tilde U_{\mathrm b} = \tilde U_{\mathrm b}'$; then $\tilde u_{\mathrm r} = \tilde U_{\mathrm b}^{-1}U = \tilde u_{\mathrm r}'$.

### The Domain and the Light Cone

The theorem is stated on the complement of the null cone, $\{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\neq0\}$, and that is exactly its domain: for $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = 0$ and $\tilde{Q}\neq0$ the element is a zero divisor, the matrix $\mathsf{M}_2(\tilde{Q})$ is singular, and no factorisation of the stated shape exists, since the product of the four factors has norm $r^2\cdot1\cdot1\cdot1 = r^2 > 0$ while $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = 0$. The null cone is the algebra's light cone, and it is treated in the companion article on biquaternion zero divisors. Among the decompositions of this series it is the mildest possible failure: a single cone, of real codimension two in the eight-dimensional algebra, whereas the partial forms of the companion article fail on larger sets.

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

verified at $\psi = 20, 40, 80$, the difference from the limit being exactly $\tfrac12e^{-\psi}$ in each of the two non-zero coefficients. The limit is the minimal idempotent $\tfrac12(e_0 + \hat\Xi i)$ with $\hat\Xi = -e_3$, the object classified in the companion article on biquaternion zero divisors: Hermitian, of norm zero, and idempotent. The word at the boundary therefore keeps a real scale and a trigonometric factor and fills the hyperbolic slot with a Hermitian idempotent of norm zero, one factor short of the four. Sangwine & Hitzer exhibit the same degeneration on a divisor of zero,

$$
\tilde P = \tfrac12\left(e_0 + e_1 + ie_2 - ie_3\right) = \sqrt2\cdot\frac{e_0+e_1}{\sqrt2}\cdot\tfrac12\left(e_0 - ie_3\right),
$$

whose last factor is that idempotent, and whose numerical factor $\sqrt2$ is not the modulus of $\tilde P$, which vanishes, but the modulus of the real part of $\tilde P$. The unbounded direction of the boost group and the null cone are thus a single cone, seen once as the boundary of the domain and once as the set of minimal idempotents, and the failure at that boundary is the collapse of the boost's positive factor rather than a discontinuity of the algebra.

## The Algorithm

### The Five Steps

The proof above is effective, and it is worth recording as a procedure. Given $\tilde{Q}$ with $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\neq0$:

1. Compute the biquaternion norm $N = \sum_\mu Q_\mu^2 \in \mathbb{C}$.
2. Take its principal square root: write $N = |N|e^{i\varphi}$ with $\varphi\in(-\pi,\pi]$, and put $\rho = \sqrt{|N|}e^{i\varphi/2}$, so that $r = \sqrt{|N|}$ and $\alpha = \varphi/2$.
3. Put $U = \tilde{Q}/\rho$, of unit norm.
4. Compute $S = UU^{*}$, and write it as $\sigma e_0 + i\vec w$ with $\sigma\in\mathbb{R}$, $\vec w\in\mathbb{R}^3$; then put
$\tilde U_{\mathrm b} = \sqrt{\frac{1+\sigma}{2}}\,e_0 + \frac{i\vec w}{\sqrt{2(1+\sigma)}}$, and read the rapidity and axis off by $\cosh\psi = \sigma$, $\hat u_{\mathrm b} = \vec w/|\vec w|$.
5. Put $\tilde u_{\mathrm r} = \tilde U_{\mathrm b}^{\natural}U$, and verify that its coefficients are real and that $\langle\tilde u_{\mathrm r},\tilde u_{\mathrm r}\rangle_{\natural} = 1$.

The factors so obtained satisfy $\tilde{Q} = r e^{i\alpha}\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ identically. The only step that requires a convention rather than a formula is step 2, where the branch of the square root is fixed by $\alpha \in (-\pi/2,\pi/2]$; the other four steps are forced.

### A Worked Example, Step by Step

Take

$$
\tilde{Q} = (1+i)e_0 + e_1 + 2e_2 ,
$$

whose coefficients are $Q_0 = 1+i$, $Q_1 = 1$, $Q_2 = 2$, $Q_3 = 0$.

*Step 1.* The biquaternion norm is $N = (1+i)^2+1^2+2^2+0 = 2i+5 = 5+2i$, of modulus $|N| = \sqrt{29} = 5.385164807$ and argument $\arg N = 0.380506377$ rad.

*Step 2.* The modulus is $\rho = \sqrt{5.385164807}\,e^{0.190253189\,i} = 2.278723854 + 0.438842117 i$, hence

$$
r = 2.320595787 , \qquad \alpha = 0.190253189\ \text{rad} \approx 10.9007^\circ .
$$

*Step 3.* Dividing, $U = \tilde{Q}/\rho$ has coefficients

$$
U_0 = 0.504639332+0.341657461i, \quad U_1 = 0.423148397-0.081490935i, \quad U_2 = 0.846296793-0.162981871i, \quad U_3 = 0 ,
$$

and $\langle U,U\rangle_{\natural} = 1$ as required.

*Step 4.* The Hermitian element $S = UU^{*}$ is

$$
S = 1.299867367\,e_0 - 0.371390676\,i\,e_1 - 0.742781353\,i\,e_2 ,
$$

so $\sigma = 1.299867367$, $\vec w = (-0.371390676, -0.742781353, 0)$ and $|\vec w| = 0.830454799$; the identity $\sigma^2-|\vec w|^2 = 1$ holds to $7\times10^{-16}$. The boost is therefore

$$
\tilde U_{\mathrm b} = 1.072349609\,e_0 - 0.173166789\,i\,e_1 - 0.346333577\,i\,e_2 ,
$$

with rapidity $\psi = 2\operatorname{arccosh}(1.072349609) = 0.756273220$, corresponding to the speed $\tanh(\psi/2) = 0.361088126$ in units $c = 1$, and axis $\hat u_{\mathrm b} = -(1,2,0)/\sqrt{5}$. The verification $\tilde U_{\mathrm b}^2 = S$ was carried out to $2.2\times10^{-16}$ in the coefficients.

*Step 5.* The rotor is

$$
\tilde u_{\mathrm r} = \tilde U_{\mathrm b}^{\natural}U = 0.470592172\,e_0 + 0.394599292\,e_1 + 0.789198585\,e_2 ,
$$

all of whose coefficients are real, with $\langle\tilde u_{\mathrm r},\tilde u_{\mathrm r}\rangle_{\natural} = 1$; its rotation angle is $\theta = 2.161669$ rad about the axis $(1,2,0)/\sqrt{5}$.

The reconstruction $\tilde{Q} = r e^{i\alpha}\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ was verified in double precision and agrees with $\tilde{Q}$ to $1.6\times10^{-16}$ in each coefficient. Note that the boost axis and the rotation axis are opposite in this example, which is a coincidence of the element and not a structural relation: no relation between the two axes is imposed by the decomposition, and a random element generally has them unrelated.

*The four exponents of this example.* The four factors are exponentials, and their exponents to the nine decimals used above are

$$
\ln r = 0.841823957 , \qquad \alpha = 0.190253189 , \qquad \frac{\psi}{2} = 0.378136610 , \qquad \frac{\theta}{2} = 1.080834539 ,
$$

the boost about $\hat u_{\mathrm b} = -(1,2,0)/\sqrt5$ and the rotor about $\hat u_{\mathrm r} = (1,2,0)/\sqrt5$, so that the word is the ordered product of four exponentials

$$
\tilde{Q} = \exp(0.841823957)\,\exp(0.190253189\,i)\,\exp\bigl(i\,0.378136610\,\hat u_{\mathrm b}\bigr)\,\exp\bigl(1.080834539\,\hat u_{\mathrm r}\bigr) .
$$

Rebuilding $\tilde U_{\mathrm b}$ and $\tilde u_{\mathrm r}$ from the last two exponents reproduces the factors of Steps 4 and 5; the full parameters are the rapidity $\psi = 0.756273220$ and the rotation angle $\theta = 2.161669078$, each twice its stored half.

### A Second Example: an Element Already in Polar Form

Take the Lorentz boost biquaternion of the physics articles with speed $0.6c$ along $e_1$,

$$
\tilde{\Lambda} = \cosh\frac{\psi}{2}\,e_0 + i\sinh\frac{\psi}{2}\,e_1 , \qquad \psi = \operatorname{atanh}0.6 = 0.693147181 ,
$$

so that $\tilde{\Lambda} = 1.060660172\,e_0 + 0.353553391\,i\,e_1$. Its biquaternion norm is $N = \cosh^2\frac{\psi}{2}-\sinh^2\frac{\psi}{2} = 1$, a positive real, so the modulus is $\rho = 1$, the scale is $r = 1$ and the phase is $\alpha = 0$. The remaining construction returns $U = \tilde{\Lambda}$, $S = \tilde{\Lambda}^2$, $\tilde U_{\mathrm b} = \tilde{\Lambda}$ and $\tilde u_{\mathrm r} = e_0$, so that the four-factor form collapses to

$$
\tilde{\Lambda} = 1\cdot e^{i\cdot0}\cdot\tilde{\Lambda}\cdot e_0 .
$$

The example is the reason the representation is a strict refinement of the physics convention: a Lorentz rotor is already in polar form, with two of its four factors trivial.

## The Four Factors and Their Meanings

### The Table of the Factors

| factor | symbol | range | real dimension | what it is |
|---|---|---|---|---|
| scale | $r$ | $(0,\infty)$ | $1$ | the absolute value of the complex modulus |
| phase | $e^{i\alpha}$ | $U(1)$, $\alpha\in(-\pi/2,\pi/2]$ | $1$ | the central phase, half the argument of the biquaternion norm |
| boost | $\tilde U_{\mathrm b}$ | $\cosh\frac{\psi}{2}+i\sinh\frac{\psi}{2}\hat u_{\mathrm b}$, $\psi\ge0$ | $3$ | the Hermitian positive unit element, $N(\tilde U_{\mathrm b})=e_0$, in $\mathbb{M}_+$ |
| rotor | $\tilde u_{\mathrm r}$ | $\mathrm{Sp}(1) = SU(2)$ | $3$ | the unit real quaternion, $N(\tilde u_{\mathrm r})=e_0$, in $\mathbb{H}_{\mathbb{B}}$ |

### The Scale

The scale is a positive real number, the only factor that is both central and non-compact on the positive side. It multiplies the element rigidly: replacing $\tilde{Q}$ by $\lambda\tilde{Q}$ with $\lambda>0$ multiplies $r$ by $\lambda$ and leaves the other three factors unchanged. It is the absolute value of the determinant of the matrix image, raised to the power $\tfrac12$, since $|\det\mathsf{M}_2(\tilde{Q})| = |\langle\tilde{Q},\tilde{Q}\rangle_{\natural}| = r^2$. As an exponential it is the degenerate case, $r = \exp(\ln r)$ of the real exponent $\ln r$, and its root is the algebra unit $e_0$.

### The Central Phase

The phase is an element of the centre lying on the unit circle, and it is the only factor that is central and compact. It is determined by the argument of the biquaternion norm, $\alpha = \tfrac{1}{2}\arg \langle\tilde{Q},\tilde{Q}\rangle_{\natural}$, and it vanishes exactly when the biquaternion norm is a positive real. It commutes with everything, so it may be written on either side of the other factors; in the physical reading it is the algebra's continuous internal symmetry. As an exponential it is $\exp(i\alpha)$, the central imaginary exponent, and its root is the central $i$, of square $-e_0$.

### The Boost

The boost is the only factor that is neither central nor compact. It lies in the Hermitian subspace $\mathbb{M}_+$, is positive definite in the matrix picture, has unit norm, and is the exponential of a traceless Hermitian element,

$$
\tilde U_{\mathrm b} = \exp\Bigl(i\tfrac{\psi}{2}\hat u_{\mathrm b}\Bigr), \qquad i\tfrac{\psi}{2}\hat u_{\mathrm b} \in \mathbb{M}_+ \cap \{\text{traceless}\} ,
$$

the exponent being traceless and Hermitian, since its scalar part vanishes and its vector part is purely imaginary. The three parameters are the rapidity and the two angles of the axis, and the boost set is the hyperbolic space $H^3$. In the physics articles this factor is the Lorentz boost rotor, and its action on the material sector $\mathbb{M}_-$ is the boost of the frame.

### The Rotor

The rotor is a unit real quaternion: compact, three-dimensional, an element of the same group that the quaternion polar representation of the companion article produces as its unit factor. It is the factor that carries the spatial rotation, and it is the only factor that lies in the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ on the unit sphere. It is the exponential of a real pure quaternion,

$$
\tilde u_{\mathrm r} = \exp\Bigl(\tfrac{\theta}{2}\hat u_{\mathrm r}\Bigr) = \cos\tfrac{\theta}{2}\,e_0 + \sin\tfrac{\theta}{2}\,\hat u_{\mathrm r} , \qquad \hat u_{\mathrm r}\in\mathbb{R}^3, \quad (\hat u_{\mathrm r},\hat u_{\mathrm r}) = 1 ,
$$

with the rotation angle $\theta$ and the unit axis $\hat u_{\mathrm r}$: the exponent lies in $\mathbb{M}_- \cap \mathrm{Vect}(\mathbb{B})$, the real pure quaternions, the anti-Hermitian sector of the vector subspace. The rotation it performs is by the angle $\theta$, and the exponent $\tfrac{\theta}{2}\hat u_{\mathrm r}$ is the only one of the four that is neither central nor Hermitian. Being non-central, it does not commute with the boost, and that non-commutativity is the algebraic root of the Thomas-Wigner rotation of the physics articles: the product of two boosts is not a boost, and the discrepancy is a rotor.

### What the Sandwich Sees

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

which exhibits the phase factor at its extremal value. This element is the sharpest illustration of the point of the four factors: two of the three named representations of the companion article fail on it, since its vector part vanishes and its real quaternion part vanishes, while the representation is available and trivial.

### The Real Quaternions

If all four coefficients of $\tilde{Q}$ are real then $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \sum_\mu q_\mu^2$ is a positive real, so $\alpha = 0$ and $r = |\tilde{Q}|$ is the quaternion modulus of the companion article. The element $U = \tilde{Q}/r$ is a unit real quaternion, and $S = UU^{*} = UU^{\natural} = e_0$, so $\tilde U_{\mathrm b} = e_0$ and $\tilde u_{\mathrm r} = U$. The real quaternions therefore have no boost: their polar representation is the quaternion polar representation, and the two representations agree term by term.

### The Null Elements

If $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = 0$ and $\tilde{Q}\neq0$ the element is a zero divisor and no decomposition exists, as shown in the section on the domain. The failure is not uniform in the structure of the element: for $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = 0$ the matrix $\mathsf{M}_2(\tilde{Q})$ has rank one, its columns span a minimal left ideal, and the element is a multiple of an idempotent; the companion article on biquaternion zero divisors treats the classification. What is relevant here is only that no product of the four factors can reproduce it, because the biquaternion norm of such a product is a positive real.

## The Roots of One in the Two Exponential Forms

### The Polar Word at a Root of One

The elements with $\tilde\Xi^2 = e_0$ are the **square roots of the algebra unit**. The norm is multiplicative, so taking norms in $\tilde\Xi^2 = e_0$ gives $\langle\tilde\Xi,\tilde\Xi\rangle_{\natural}^{2} = e_0$, and the norm of a root of one is one of the two square roots of the unit,

$$
\langle\tilde\Xi,\tilde\Xi\rangle_{\natural} = \pm e_0 .
$$

Since $\langle\tilde\Xi,\tilde\Xi\rangle_{\natural} = r^2e^{2i\alpha}$ with $r>0$ and $\alpha\in(-\pi/2,\pi/2]$, the two signs are the two cases of the word.

**The unit-norm roots.** For $\langle\tilde\Xi,\tilde\Xi\rangle_{\natural} = e_0$ the modulus and the phase are trivial, $r = 1$ and $\alpha = 0$, and the word reduces to the Cartan case $\tilde\Xi = \tilde U_{\mathrm b}\tilde u_{\mathrm r}$ of §*Degenerate Cases*. The roots of one of unit norm are exactly the central pair. The halving element $\tilde\Pi_- = \tfrac12(e_0-\tilde\Xi)$ is an idempotent,

$$
\tilde\Pi_-^2 = \tfrac14\bigl(e_0-2\tilde\Xi+\tilde\Xi^2\bigr) = \tfrac12(e_0-\tilde\Xi) = \tilde\Pi_- ,
$$

and the norm of an idempotent is an idempotent complex number, hence $0$ or $1$; here the norm is

$$
\langle\tilde\Pi_-,\tilde\Pi_-\rangle_{\natural} = \tfrac14\bigl(1+\langle\tilde\Xi,\tilde\Xi\rangle_{\natural}-2\Xi_0\bigr) = \tfrac12(1-\Xi_0),
$$

so $\Xi_0 = \pm1$. Writing $\tilde\Xi = \Xi_0e_0+\vec\Xi$ with $\vec\Xi = \Xi_1e_1+\Xi_2e_2+\Xi_3e_3$, the square is $\tilde\Xi^2 = \bigl(\Xi_0^2-(\vec\Xi,\vec\Xi)\bigr)e_0+2\Xi_0\vec\Xi$, and its vector part $2\Xi_0\vec\Xi$ vanishes: $\tilde\Xi = \pm e_0$. The two elements $\pm e_0$ are the only involutions of unit norm in the algebra.

**The roots of norm $-e_0$.** For $\langle\tilde\Xi,\tilde\Xi\rangle_{\natural} = -e_0$ the modulus is $r = 1$ and the phase solves $e^{2i\alpha} = -1$, so $\alpha = \pi/2$, the phase factor is $e^{i\alpha} = i$, and the word is

$$
\tilde\Xi = i\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r} , \qquad (\tilde U_{\mathrm b}\tilde u_{\mathrm r})^2 = -e_0 .
$$

The condition is not automatic: it says that the unit product $\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ is itself a unit-norm root of $-e_0$. Read on the two axes, it says that the two axes are orthogonal and that the rotor is pure,

$$
\hat u_{\mathrm b}\perp\hat u_{\mathrm r} , \qquad \tilde u_{\mathrm r} = \hat u_{\mathrm r}\in\mathcal{A} \quad (\theta = \pi) ,
$$

so that the rotor is a point of the axis sphere, its stored half-angle is $\pi/2$ and its rotation angle is $\pi$. The equivalence is the classification of the roots of one of the plain algebra (*Square Roots of One and the Idempotents of the General Plain Algebra*) read in the word, and it was verified in double precision. The family that remains has the four real parameters of that classification: the rapidity $\psi$, the rotor axis $\hat u_{\mathrm r}$ (two parameters), and the boost axis $\hat u_{\mathrm b}$ in the plane orthogonal to the rotor axis (one).

### The Idempotent Exponential Form of a Root of One

Every root of one has a one-exponential form, built on the same halving element. Since $\tilde\Pi_-$ is idempotent its exponential series truncates,

$$
\exp\bigl(i\pi\tilde\Pi_-\bigr) = e_0 + \bigl(e^{i\pi}-1\bigr)\tilde\Pi_- = e_0 - 2\tilde\Pi_- ,
$$

and the last element is the root itself:

$$
\tilde\Xi = \exp\bigl(i\pi\tilde\Pi_-\bigr), \qquad \tilde\Pi_- = \tfrac12(e_0-\tilde\Xi), \qquad \tilde\Pi_-^2 = \tilde\Pi_- .
$$

The form is a **single exponential of one element**, where the polar word is an ordered product of four. The two ends of the halving are the two trivial roots: $\tilde\Xi = e_0$ gives $\tilde\Pi_- = 0$ and $\exp(0) = e_0$, while $\tilde\Xi = -e_0$ gives $\tilde\Pi_- = e_0$ and $\exp(i\pi) = -e_0$. The exponent $i\pi\tilde\Pi_-$ is not the sum of the four exponents of the word, and the two are two different factorisations of the same root set.

### The Bridge Between the Two Forms

The two forms are tied by the **product of the last two factors** of the word, read at a root of one. On the roots of norm $-e_0$ the word is $\tilde\Xi = i\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r}$, so that product is recovered from the root by the left multiplication by $-i$,

$$
-i\,\tilde\Xi = \tilde U_{\mathrm b}\,\tilde u_{\mathrm r} , \qquad \bigl(-i\,\tilde\Xi\bigr)^2 = -e_0 , \qquad \langle -i\,\tilde\Xi , -i\,\tilde\Xi \rangle_{\natural} = e_0 ,
$$

the first equality the extraction, the second the statement that the extracted element is a root of $-e_0$, and the third that it has unit norm; its argument is $0$, so its phase is trivial and the extraction is already the polar factorisation of the read element. The element $-i\tilde\Xi$ is therefore a unit-norm root of $-e_0$ whenever the root has norm $-e_0$, and it is the product of the last two factors of the word. On the two central roots it is instead $-i$ and $+i$, both of norm $-e_0$, and the extraction carries no polar information.

Substituting the extraction into the halving idempotent and into the idempotent form gives both directions in closed shape,

$$
\tilde\Pi_- = \tfrac12\bigl(e_0-\tilde\Xi\bigr) = \tfrac12\bigl(e_0-i\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r}\bigr) , \qquad \tilde U_{\mathrm b}\,\tilde u_{\mathrm r} = i\,\bigl(2\tilde\Pi_--e_0\bigr) ,
$$

so the halving idempotent determines the product of the last two factors completely, and conversely. The exponent of the single exponential is $i\pi\tilde\Pi_-$, which the extraction expands into a **central part and a two-factor part**,

$$
\tilde\Xi = \exp\bigl(i\pi\tilde\Pi_-\bigr) = \exp\Bigl(\tfrac{i\pi}{2}e_0+\tfrac{\pi}{2}\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r}\Bigr) = \exp\Bigl(i\pi\,\frac{e_0-i\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r}}{2}\Bigr) ,
$$

the central part fixed at $\tfrac{i\pi}{2}e_0$ and the two-factor part the last two factors of the word multiplied by the real half-turn $\tfrac{\pi}{2}$. The exponent is not the sum of the four exponents of the word, and the polar word is the polar decomposition of the root of $-e_0$ read from the root by $-i\tilde\Xi$.

### The Hermitian Roots

The roots of one that are Hermitian, $\tilde\Xi^{*} = \tilde\Xi$, are the elements whose word carries a trivial boost. On a root of norm $-e_0$ the word is $\tilde\Xi = i\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ with $\tilde u_{\mathrm r} = \hat u_{\mathrm r}$ pure and the axes orthogonal, and its Hermitian conjugate is $\tilde\Xi^{*} = i\hat u_{\mathrm r}\tilde U_{\mathrm b}$; the two differ by $-2\sinh\tfrac{\psi}{2}\,\hat u_{\mathrm b}\hat u_{\mathrm r}$, which vanishes exactly when the boost is trivial. The Hermitian roots of one are therefore

$$
\tilde\Xi = \pm e_0 , \qquad \tilde\Xi = i\hat u_{\mathrm n} \quad \text{over the unit pure real quaternions } \hat u_{\mathrm n} ,
$$

the central pair and the purely imaginary family, and in the idempotent form the halving element of a Hermitian root is Hermitian.

### The Two Pure Elements as the Source of the Word and of the Idempotents

The whole section is generated by **two pure elements** and two central dials, in three steps.

**Two pure elements give a Hermitian root of one.** Let $\hat u_{\mathrm b}$ and $\hat u_{\mathrm r}$ be orthogonal unit pure quaternions of $\mathbb{R}^3$. Their product is again a unit pure quaternion, and the product with the fixed central $i$ is a root of one of norm $-e_0$,

$$
\hat u_{\mathrm n} = \hat u_{\mathrm b}\,\hat u_{\mathrm r} , \qquad \hat u_{\mathrm n}^2 = -e_0 , \qquad \tilde\Xi_0 = i\,\hat u_{\mathrm b}\,\hat u_{\mathrm r} , \qquad \tilde\Xi_0^2 = e_0 , \qquad \langle\tilde\Xi_0,\tilde\Xi_0\rangle_{\natural} = -e_0 , \qquad \tilde\Xi_0^{*} = \tilde\Xi_0 .
$$

At this stage there is no angle and no dilatation: the two pure elements, their product, and the central $i$. The root so built is the Hermitian one, $\tilde\Xi_0 = i\hat u_{\mathrm n}$, of the subsection above.

**The angles give the full root set.** Give the two elements their angles, the boost its rapidity $\psi$ and the rotor its angle $\theta$, and keep the rotor pure so that the two factors close:

$$
\tilde U_{\mathrm b} = \exp\Bigl(i\tfrac{\psi}{2}\hat u_{\mathrm b}\Bigr) , \qquad \tilde u_{\mathrm r} = \hat u_{\mathrm r} \quad (\theta = \pi) , \qquad \tilde\Xi = i\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r} , \qquad (\tilde U_{\mathrm b}\tilde u_{\mathrm r})^2 = -e_0 .
$$

This is the whole norm-$-e_0$ root set, the Hermitian one at $\psi = 0$ and the rest by the boost, which is its non-Hermitian part.

**The dilatation and the phase give the element.** The same two non-central factors, dialled by the central scale and the central phase, are the general element,

$$
\tilde Q = r\,e^{i\alpha}\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r} = \bigl(r\,e^{i\alpha}\bigr)\cdot\bigl(\text{the two non-central factors}\bigr) .
$$

So the root is the central dial $i$ and the element is the central dial $r e^{i\alpha}$ on the same two factors. When the two factors close, the element and the root are central multiples of one another on those shared factors, $\tilde Q = -i\,r\,e^{i\alpha}\,\tilde\Xi$; in general the element carries its own two factors, of the same kind, and the root is the closing case of them.

**The root is the source of the idempotents and of the Peirce decomposition.** A root of one is carried by the halving map into the complementary idempotent pair $\tilde\Pi_\pm = \tfrac12(e_0\pm\tilde\Xi)$, and the pair splits the algebra into four **Peirce pieces**,

$$
\mathbb{B} = \tilde\Pi_+\mathbb{B}\tilde\Pi_+ \;\oplus\; \tilde\Pi_+\mathbb{B}\tilde\Pi_- \;\oplus\; \tilde\Pi_-\mathbb{B}\tilde\Pi_+ \;\oplus\; \tilde\Pi_-\mathbb{B}\tilde\Pi_- ,
$$

each of real dimension two for a root other than $\pm e_0$, the four summing to the real dimension eight of the algebra; the pieces are the ideals of *Ideals and Peirce Decomposition of the General Plain Algebra* and the Hermitian idempotents of *Hermitian Idempotents and the Peirce Decomposition*. The chain is thus

$$
\text{two pure elements} \;\longrightarrow\; \text{the root of one} \;\longrightarrow\; \text{the idempotents} \;\longrightarrow\; \text{the Peirce decomposition} ,
$$

and the same two pure elements, with their angles and the central dial, give the general element.

## The Commutative Four-Dimensional Alternative

The four-factor representation above is the polar form of $\mathbb{B}$. The commutative four-dimensional algebra has its own, and it is the corpus's only polar form built for a commutative algebra of dimension four; it is recorded for the contrast, the two answering the same question differently.

The algebra is $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\oplus\mathbb{C}$, the reduced biquaternion algebra of *List of Algebras by Dimension*: an element is $q = A_1+A_2e$ with $e^2=+1$ and $A_1,A_2\in\mathbb{C}$. Pei, Chang and Ding construct its polar form (*IEEE Trans. Signal Processing* **52** (2004) 2012–2022, §III) and prove three things about it.

**Existence.** The form exists if and only if $\langle q,q\rangle_{\natural} = A_1^2-A_2^2\neq0$ — the domain condition of this article, and here it is also a factorisation statement, since $\langle q,q\rangle_{\natural} = \lambda_+\lambda_-$ in the idempotent coordinates $\lambda_\pm = A_1\pm A_2$. The excluded set is thus the union of the two ideals $\mathbb{C}e_+ \cup \mathbb{C}e_-$, with $e_\pm = \tfrac12(1\pm e)$, on which the element is a multiple of an idempotent; this is the commutative image of the null elements of the section above, and of the cone on which the four factors here fail.

**Uniqueness.** The form carries a scale and three phases, and it is unique once the ranges of the three phases are fixed; the uniqueness is proved by showing that the equations for the phases have exactly one solution in those ranges. The uniqueness here is therefore purchased by a range convention, whereas the uniqueness above is a theorem about the factorisation itself.

**Compatibility.** When the second component vanishes the form reduces to the ordinary complex polar form of *Complex Polar Element Representation*, which is the sense in which its authors select it as compatible with the complex case.

The form is useful for the two operations it is useful for here. Multiplication becomes trivial, moduli multiplying and phases adding, and the paper proves a **De Moivre theorem** for it; the inverse is read off directly; and the **geometric meaning** is stated — one scaling, four rotations in the coordinate planes $(1,2)$, $(3,4)$, $(1,4)$ and $(2,3)$, and two Lorentz transformations in the planes $(1,3)$ and $(2,4)$. That is the precise form of the claim recorded with this family of algebras in *The Three Two-Dimensional Algebras and the Three Kinds of Rotation*: the four-dimensional commutative algebra carries the elliptic rotations of its complex factor and the hyperbolic transformations of its split factor at the same time, and its authors attach the reading to the special theory of relativity.

One application is a use of a polar form the corpus does not otherwise have. The colour space is three-dimensional and the algebra four-dimensional, so the representation of a colour by an element of the algebra is not unique; the paper removes the redundancy by setting one of the three phases to zero, giving what it calls the **simplified polar form**, whose data are the brightness, hue and saturation of the colour and in which the norm and the conjugation of the element take their simplest forms. It is used for colour template matching and colour-sensitive edge detection, with the transforms of *Biquaternion Discrete Harmonic Analysis*.

## Relation to the Two Partial Forms

The relation of the present representation to the Hamilton, complex and Cartan representations is the following, stated here and proved in the companion article *Biquaternion Partial Polar Element Representations*.

The **Hamilton form** writes $\tilde{Q} = R\exp(\hat\Xi\Theta)$ with $R$ a complex scalar and $\hat\Xi$ a non-central root of $-1$ parallel to the vector part; in the present notation its two factors are

$$
R = r\,e^{i\alpha}, \qquad \exp(\hat\Xi\Theta) = \tilde U_{\mathrm b}\,\tilde u_{\mathrm r} ,
$$

so that it groups the first two of the four factors into the modulus $R$ and the last two into the exponential. It is available whenever the vector part is non-null, which is a stronger condition than $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\neq0$.

The **complex form** writes $\tilde{Q} = Q\exp(i\Psi)$ with $Q$ a real quaternion; in the present notation its two factors are

$$
Q = r\,\tilde u_{\mathrm r} , \qquad \exp(i\Psi) = e^{i\alpha}\,\tilde u_{\mathrm r}^{\natural}\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r} ,
$$

so that it groups the scale with the rotor into the quaternion modulus and the phase with a conjugated boost into the exponential. Its construction in the companion article proceeds from the real quaternion part of $\tilde{Q}$ and requires that part to be invertible, again a stronger condition than $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\neq0$.

Both partial forms are therefore regroupings of the same four factors, taken in pairs; there are exactly three ways to pair four objects into two pairs, and the third pairing, in which the scale is grouped with the boost and the phase with the rotor, is the Cartan form $\tilde{Q} = (r\tilde U_{\mathrm b})(e^{i\alpha}\tilde u_{\mathrm r})$, the matrix polar decomposition into a positive Hermitian factor and a unitary factor. All three are treated in the companion article.

| representation | modulus | second factor | condition on $\tilde{Q}$ |
|---|---|---|---|
| Hamilton | $R = r\,e^{i\alpha}$ | $\exp(\hat\Xi\Theta) = \tilde U_{\mathrm b}\,\tilde u_{\mathrm r}$ | the vector part is non-null |
| complex | $Q = r\,\tilde u_{\mathrm r}$ | $\exp(i\Psi) = e^{i\alpha}\,\tilde u_{\mathrm r}^{\natural}\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r}$ | the real quaternion part is invertible |
| Cartan | $r\,\tilde U_{\mathrm b}$ | $e^{i\alpha}\,\tilde u_{\mathrm r}$ | $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\neq0$ |

## Summary

Every biquaternion with non-vanishing norm has a unique polar representation

$$
\tilde{Q} = r\,e^{i\alpha}\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r} , \qquad r = \sqrt{|\langle\tilde{Q},\tilde{Q}\rangle_{\natural}|} > 0, \quad \alpha = \tfrac{1}{2}\arg \langle\tilde{Q},\tilde{Q}\rangle_{\natural}, \quad \tilde U_{\mathrm b} \in \mathbb{M}_+, \quad \tilde u_{\mathrm r}\in\mathrm{Sp}(1) ,
$$

in which $\tilde U_{\mathrm b}$ is the Hermitian positive unit-norm boost and $\tilde u_{\mathrm r}$ the unit real quaternion rotor. The modulus of the decomposition is the complex number $\rho = re^{i\alpha} = \sqrt{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}}$, and the positive real factor $r$ is its absolute value, so a positive scale is always available and the phase is one of the four factors rather than a correction. The four factors have real dimensions $1+1+3+3 = 8$, they are unique, and the failure of the decomposition is exactly the null cone $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = 0$. The decomposition is the reference form of the series: the Hamilton and complex forms of the companion article are the two other pairings of the same four factors, and the Cartan form of the physics articles is the special case $N = 1$ in which the scale and the phase are trivial.

Each of the four factors is itself an exponential of a single element of the algebra:

- $r = \exp(\ln r)$;
- $e^{i\alpha} = \exp(i\alpha)$;
- $\tilde U_{\mathrm b} = \exp\bigl(i\frac{\psi}{2}\hat u_{\mathrm b}\bigr)$, with the exponent traceless in $\mathbb{M}_+$;
- $\tilde u_{\mathrm r} = \exp\bigl(\tfrac{\theta}{2}\hat u_{\mathrm r}\bigr)$, with $\tfrac{\theta}{2}\hat u_{\mathrm r}$ a real pure quaternion.

So the polar word is an ordered product of four exponentials. The product is not the exponential of the sum of the exponents, because the two non-central exponents do not commute; the last two of them do collapse to a single exponential, $\tilde U_{\mathrm b}\tilde u_{\mathrm r} = \exp(\hat\Xi\Theta)$, whenever the vector part is non-null, which is the Hamilton form $\tilde{Q} = R\exp(\hat\Xi\Theta)$ of the companion article. The same word written at a root of one, $\langle\tilde\Xi,\tilde\Xi\rangle_{\natural} = \pm e_0$, gives $\pm e_0$ on the unit-norm roots and $i\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ on the roots of norm $-e_0$, with the boost axis orthogonal to the rotor axis and the rotor pure; the root set has the second form $\tilde\Xi = \exp(i\pi\tilde\Pi_-)$ on its halving idempotent $\tilde\Pi_- = \tfrac12(e_0-\tilde\Xi)$, tied to the word by the product of its last two factors, $-i\tilde\Xi = \tilde U_{\mathrm b}\tilde u_{\mathrm r}$. The two non-central factors are themselves generated by two pure unit elements with their angles, and the root of one, through its halving idempotents, is the source of the idempotents and of the Peirce decomposition of the algebra.

## Summary of Notation

| symbol | set | meaning |
|---|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | — | the biquaternion algebra, $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ |
| $e_0 = 1$, $e_1,e_2,e_3$ | basis of $\mathbb{B}$ | the algebra unit and the quaternion units, $e_k^2 = -e_0$, $e_1e_2 = e_3$ |
| $Q_\mu$ | $\mathbb{C}$ | the four complex coefficients of $\tilde{Q}$ |
| $\Xi_\mu$ | $\mathbb{C}$ | the four complex coefficients of a root of one $\tilde\Xi$ |
| $i$ | $\mathbb{C}_{\mathbb{B}}$, $i^2 = -1$ | the central scalar imaginary |
| $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = \sum_\mu Q_\mu^2$ | $\mathbb{C}$, central | the biquaternion norm, equal to $\det\mathsf{M}_2(\tilde{Q})$ |
| $\rho = \sqrt{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}}$ | $\mathbb{C}\setminus\{0\}$ | the complex modulus, the principal square root |
| $r = \sqrt{|\langle\tilde{Q},\tilde{Q}\rangle_{\natural}|}$ | $\mathbb{R}$, $r > 0$ | the scale, a positive real |
| $\alpha = \tfrac{1}{2}\arg \langle\tilde{Q},\tilde{Q}\rangle_{\natural}$ | $\left(-\frac{\pi}{2},\frac{\pi}{2}\right]$ | the phase angle |
| $U = \tilde{Q}/\rho$ | $\mathbb{B}^{\times}_1$, $N(U)=e_0$ | the unit-norm part |
| $S = UU^{*} = \sigma e_0 + i\vec w$ | $\mathbb{M}_+$, positive definite, $N(S)=e_0$ | the Hermitian positive element, $\sigma\in\mathbb{R}$, $\sigma\ge1$, $\vec w\in\mathbb{R}^3$ |
| $\tilde U_{\mathrm b} = \sqrt{S}$ | $\mathbb{M}_+$, positive definite, $N(\tilde U_{\mathrm b})=e_0$ | the boost, a Hermitian positive unit element |
| $\psi$ | $\mathbb{R}$, $\psi\ge0$ | the rapidity of the boost |
| $\hat u_{\mathrm b}$ | $\mathcal{A}$, a unit vector of $\mathbb{R}^3$ | the axis of the boost |
| $i\frac{\psi}{2}\hat u_{\mathrm b}$ | traceless in $\mathbb{M}_+$ | the boost exponent |
| $\theta$ | $[0,2\pi]$ | the rotation angle of the rotor, whose stored half-angle is $\frac{\theta}{2}\in[0,\pi]$ |
| $\hat u_{\mathrm r}$ | $\mathcal{A}$, a unit vector of $\mathbb{R}^3$ | the axis of the rotor |
| $\hat u_{\mathrm n} = \hat u_{\mathrm b}\hat u_{\mathrm r}$ | $\mathcal{A}$, a unit vector of $\mathbb{R}^3$ | the composed pure axis of a Hermitian root of one, $i\hat u_{\mathrm n}$ |
| $\frac{\theta}{2}\hat u_{\mathrm r}$ | real pure quaternion | the rotor exponent |
| $\hat\Xi$ | $\mathbb{B}$, $\hat\Xi^2 = -e_0$ | the Hamilton axis, the pure root of $-1$ parallel to the vector part |
| $\tilde u_{\mathrm r} = \tilde U_{\mathrm b}^{\natural}U$ | $\mathrm{Sp}(1)$ | the rotor, a unit real quaternion |
| $\exp(\ln r)\,\exp(i\alpha)\,\exp\bigl(i\frac{\psi}{2}\hat u_{\mathrm b}\bigr)\,\exp\bigl(\frac{\theta}{2}\hat u_{\mathrm r}\bigr)$ | — | the polar word as an ordered product of four exponentials, $\theta\in[0,2\pi]$ |
| $\tilde\Xi$ | $\mathbb{B}$, $\tilde\Xi^2 = e_0$ | a square root of the unit, the subject of §*The Roots of One in the Two Exponential Forms*; not to be confused with the Hamilton axis $\hat\Xi$, a root of $-e_0$ |
| $\tilde\Pi_- = \tfrac12(e_0-\tilde\Xi)$ | $\mathbb{B}$, $\tilde\Pi_-^2=\tilde\Pi_-$ | the halving idempotent of a root of one, whose exponential is the root, $\tilde\Xi = \exp(i\pi\tilde\Pi_-)$ |
| $-i\tilde\Xi = \tilde U_{\mathrm b}\tilde u_{\mathrm r}$ | $\mathbb{B}$, $(-i\tilde\Xi)^2=-e_0$ | the product of the last two factors of the polar word, read from a root of one of norm $-e_0$ |
| $\mathbb{M}_+$ | subspace of $\mathbb{B}$ | the Hermitian subspace, real scalar part and imaginary vector part |
| $\mathbb{M}_-$ | subspace of $\mathbb{B}$ | the anti-Hermitian subspace, the material sector of the physics articles |
| $\mathbb{H}_{\mathbb{B}}$ | subspace of $\mathbb{B}$ | the real quaternion subspace, the fixed space of complex conjugation |
| $\mathrm{Sp}(1)$ | $Sp(1) = SU(2)$ | the unit real quaternions |

## Further Reading

- *Biquaternions as a Vector Space over $\mathbb{C}$* (`articles_maths/biquaternions-as-a-vector-space-over-c.md`), for the algebra, the four conjugations and the remarkable subspaces.
- *Biquaternion Partial Polar Element Representations* (`articles_maths/biquaternion-partial-polar-element-representations.md`), for the Hamilton, complex and Cartan representations as the three two-factor groupings of these four factors, with their domains.
- *Split-Biquaternion Polar Element Representation* (`articles_maths/split-biquaternion-polar-element-representation.md`), for the semisimple analogue, whose modulus is split complex and whose rotor is six-dimensional.
- *Quaternion Polar Element Representation* (`articles_maths/quaternion-polar-element-representation.md`), for the two-factor case that this decomposition restricts to on the real quaternions.
- *Complex Polar Element Representation* (`articles_maths/complex-polar-element-representation.md`) and *Split-Complex Polar Element Representation* (`articles_maths/split-complex-polar-element-representation.md`), for the two-dimensional members of the series, where the rule of the exponential is stated once and the slots are counted in the smallest cases.
- *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* (`articles_physics/the-2x2-matrix-element-representation-m2c-of-biquaternions.md`), for the isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$, the determinant, and the matrix polar decomposition.
- *The Lorentz Group in Biquaternionic Form — Structure and Representations* (`articles_physics/the-lorentz-group-in-biquaternionic-form-structure-and-representations.md`), for the boost and rotation rotors and the Thomas-Wigner rotation.
- *Ideals and Peirce Decomposition of the General Plain Algebra* (`articles_maths/ideals-and-peirce-decomposition-of-the-general-plain-algebra.md`) and *Hermitian Idempotents and the Peirce Decomposition* (`articles_maths/hermitian-idempotents-and-the-peirce-decomposition.md`), for the Peirce pieces below, into which a root of one splits the algebra through its halving idempotents.
- *Square Roots of One and the Idempotents of the General Plain Algebra and the General Plain Sesqualgebra in Exponential Form* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-general-plain-algebra-and-the-general-plain-sesqualgebra-in-exponential-form.md`), for the classification of the roots of one in exponential form and the idempotent reading of the same roots.
- S. J. Sangwine and E. Hitzer, "Polar decomposition of complexified quaternions and octonions", *Advances in Applied Clifford Algebras* (2020), DOI 10.1007/s00006-020-1048-y; technical report CES-535, University of Essex (2019), for the published two-exponential factorisation of the unit semi-norm elements and, in the general case, its Corollary 1 — whose trigonometric factor is the rotor $\tilde u_{\mathrm r}$ of this article and whose hyperbolic factor is the boost about the rotor-conjugated axis, $\tilde U_{\mathrm b} = \tilde u_{\mathrm r}^{-1}H\tilde u_{\mathrm r}$ with the same rapidity and norm — for Lemma 1, the trichotomy of the exponential of a hypercomplex root of $-1$, $0$ or $+1$, and for the degenerate word on the null cone of the boundary subsection above. The order of the two non-central factors is reversed there, angle first, and the complex modulus is kept whole rather than split into a scale and a phase, which is the difference of count $2+3+3$ against $1+1+3+3$; the corpus fixes the branch and proves uniqueness, while the paper admits both orders.
- Soo-Chang Pei, Ja-Han Chang and Jian-Jiun Ding, "Commutative reduced biquaternions and their Fourier transform for signal and image processing applications", *IEEE Transactions on Signal Processing* **52** (2004) 2012–2022, for the reduced biquaternion algebra — the commutative four-dimensional algebra $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\oplus\mathbb{C}$, equivalently the double-complex, tessarine or commutative hypercomplex algebra — and for its polar form, its uniqueness under the phase-range convention, its De Moivre theorem and the simplified polar form for colour images.
