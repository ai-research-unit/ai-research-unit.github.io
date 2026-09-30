# __Biquaternion Polar Element Representation__

## Introduction

This article is about the **polar representation** of a biquaternion: the statement that every biquaternion with non-vanishing norm is the product of four factors,

$$
\tilde{Q} = r\,e^{i\alpha}\,B\,\hat{q} ,
$$

a positive real **scale** $r$, a central **phase** $e^{i\alpha}$, a Hermitian positive **boost** $B$, and a unit real quaternion **rotor** $\hat{q}$. The four factors are unique, and their real dimensions $1+1+3+3$ sum to the eight real dimensions of the algebra.

This is the reference form of the series. The three named polar representations of the corpus — the **Hamilton**, **complex** and **Cartan** representations, which the companion article *Biquaternion Partial Polar Element Representations* treats — are each available only on a part of the algebra, each loses information, and each calls a composite object the modulus. The four-factor representation is the reference in two senses: every biquaternion on which any of the three is available has this one, and the four factors it produces are exactly the objects that the three regroup. The verification that each named representation is a two-factor grouping of these four factors is the subject of the companion article.

The key point of the construction, and the reason it is available where the three named representations are not, is the treatment of the modulus. The modulus of the representation is the **complex** number

$$
\rho = \sqrt{N(\tilde{Q})} , \qquad N(\tilde{Q}) = \sum_{\mu=0}^{3}Q_\mu^2 ,
$$

whose modulus and phase are the first two of the four factors:

$$
\rho = r\,e^{i\alpha}, \qquad r = |\rho| = \sqrt{|N(\tilde{Q})|} \ \ge 0, \qquad \alpha = \arg\rho = \tfrac{1}{2}\arg N(\tilde{Q}) .
$$

The positive real factor $r$ is therefore always available: the square root of a complex number can always be taken with a non-negative modulus, and the only obstruction is the vanishing of $N(\tilde{Q})$ itself, which is the vanishing of the determinant of the $2\times2$ matrix image. The phase $e^{i\alpha}$ is one of the four factors precisely because the modulus is complex; it is not an accessory, and the partial forms of the companion article differ from this one by which factor absorbs it.

The conventions are those of the corpus. The algebra is $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, an element is written $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ with complex coefficients, the conjugations are the quaternion conjugation $\bar{\tilde{Q}}$, the complex conjugation $\tilde{Q}^*$, the Hermitian conjugation $\tilde{Q}^\dagger = \bar{\tilde{Q}}^{*}$, the centre is $\mathbb{C}_{\mathbb{B}}$, the quaternion subspace is $\mathbb{H}_{\mathbb{B}}$, the Hermitian subspace is $\mathbb{M}_+$, and the scalar imaginary is $i$, central. No physics is invoked. Every numerical value displayed below was recomputed in double precision.

## Why Four Factors

### The Centre and the Phase

The centre of $\mathbb{B}$ is $\mathbb{C}_{\mathbb{B}} \cong \mathbb{C}$, the complex scalars. An element of the centre commutes with everything, so a central factor can be moved through the other factors without changing the product, and the central group $U(1)$ is therefore a free one-parameter factor of any decomposition. The phase $e^{i\alpha}$ of the representation is this factor, and the corpus's articles on Noether's theorem and the gauge principle rest on the same centrality.

### The Hermitian and the Anti-Hermitian Halves

The Hermitian conjugation $\dagger$ is an involution, so the algebra splits into its fixed space and its anti-fixed space,

$$
\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_- , \qquad \mathbb{M}_\pm = \{\tilde{Q} : \tilde{Q}^\dagger = \pm\tilde{Q}\},
$$

with $\mathbb{M}_+$ the Hermitian subspace (real scalar part, purely imaginary vector part) and $\mathbb{M}_-$ the anti-Hermitian subspace. In the matrix model, $\mathbb{M}_+$ is the subspace of Hermitian matrices and $\mathbb{M}_-$ the subspace of anti-Hermitian ones, and this is the split that the matrix polar decomposition uses: the positive factor of a polar decomposition is a Hermitian matrix with positive eigenvalues, and the unitary factor is an element of the unitary group.

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

with $H^3 = SL(2,\mathbb{C})/SU(2)$ the three-dimensional hyperbolic space, and the four factors of the product are exactly the four factors of the decomposition: the scale $\mathbb{R}_{>0}$, the phase $U(1)$, the rotor $SU(2)$ and the boost $H^3$. The factorisation is the polar decomposition of a complex matrix, read as a statement about the algebra. It is a factorisation of manifolds and not a direct product of groups: the multiplication map $(z,M)\mapsto zM$ is two-to-one, since $(-z,-M)$ has the same image, and the two preimages are the two branches of the square root of the determinant. The two counts of the four factors are nevertheless the same, and the doubling is the same sign ambiguity that the branch $\alpha\in(-\pi/2,\pi/2]$ removes in the representation.

### The Counting

The real dimensions of the four factors are

$$
\dim r = 1, \qquad \dim e^{i\alpha} = 1, \qquad \dim B = 3, \qquad \dim \hat{q} = 3 ,
$$

and their sum is the real dimension of the algebra,

$$
1+1+3+3 = 8 = \dim_{\mathbb{R}}\mathbb{B} .
$$

The additivity is the structural statement that the four factors are independent, and it is the reason the representation is the reference one: no named form can exhibit more than two of the four slots at a time. The companion articles on $\mathbb{H}$, $\mathbb{H}_{\mathrm{s}}$ and $\mathbb{H}_{\mathbb{D}}$ obtain $1+0+0+3$, $1+0+2+1$ and $1+1+0+6$ in the same four slots.

### The Order of the Factors

**The order is part of the word, because $B$ is not central.** The additivity $1+1+3+3 = 8$ counts the four factors as **parameters**, and it does not say that they may be written in any order. The four factors are unique as an ordered quadruple, in the word

$$
\tilde{Q} = r\,e^{i\alpha}B\hat{q} ,
$$

and the position of each factor in it is part of the statement. Three of the four are exponentials of a single exponent — the phase $e^{i\alpha}$, the boost $B = \exp(i\tfrac{\psi}{2}\hat{\mathbf{n}})$ and the rotor $\hat{q} = \exp(\theta\hat{\mathbf{u}})$ — and the three exponents do not commute: only the exponent $i\alpha$ is central.

### The Trichotomy of the Exponential

The three exponentials are the non-degenerate rows of a single rule, which every algebra of the polar series follows. For an element $\nu$ and a real $\theta$, the sign of $\nu^2$ decides the character of the exponential.

**Proposition.** The exponential of $\nu\theta$ is given by the case

| case | $\nu^2$ | $\exp(\nu\theta)$ | the factor produced here |
|---|---|---|---|
| trigonometric | $-e_0$ | $\cos\theta\,e_0 + \nu\sin\theta$ | the phase ($\nu = i$, central) and the rotor ($\nu = \hat{\mathbf{u}}$, a unit pure real quaternion) |
| parabolic | $0$ | $e_0 + \nu\theta$, the series truncating | no factor: the exponential of a nilpotent |
| hyperbolic | $+e_0$ | $\cosh\theta\,e_0 + \nu\sinh\theta$ | the boost ($\nu = i\hat{\mathbf{n}}$, Hermitian) |

*Proof.* The exponential is the series $\exp(\nu\theta) = \sum_{n\ge0}\nu^n\theta^n/n!$. For $\nu^2 = -e_0$ the powers repeat with period four as $e_0, \nu, -e_0, -\nu$, for $\nu^2 = 0$ every power from the second onward vanishes, and for $\nu^2 = +e_0$ they repeat as $e_0, \nu$; summing each case gives the stated closed form.

All three rows are non-empty in $\mathbb{B}$. The trigonometric row contains the central phase and the rotor, and the hyperbolic row contains the boost. The parabolic row contains no factor of the polar representation but is not empty: the element $\nu = e_1 + ie_2$ satisfies $\nu^2 = 0$ exactly, so its exponential truncates to $\exp(\nu) = e_0 + (e_1+ie_2)$, of norm one and neither a rotor nor a boost. The nilpotent $\nu$ itself lies on the null cone, since $N(\nu) = 0$, and the cone contains the idempotents as well; the boundary word of the polar family is built from those, as the boundary subsection below records. The rule is Lemma 1 of Sangwine & Hitzer, stated there for a hypercomplex root of $-1$, $0$ or $+1$, and the two diagonal rows are what give the four factors.

Since the centre $\mathbb{C}_{\mathbb{B}}$ is the whole of the central elements, the phase may be transposed at no cost, $e^{i\alpha}B\hat{q} = B\hat{q}\,e^{i\alpha}$ exactly, and the same holds for the scale. The other two factors may not be transposed. With $B$ of rapidity $\psi = 0.7$ about $\hat{\mathbf{n}} = (1,0.3,0.2)/\|(1,0.3,0.2)\|$ and $\hat{q}$ of angle $\theta = 0.6$ about $\hat{\mathbf{u}} = (\sin0.5,\ 0,\ \cos0.5)$,

$$
\left\|B\hat{q} - \hat{q}B\right\| = 0.296621057 ,
$$

where $\|\cdot\|$ denotes the largest modulus among the coefficient differences. The difference vanishes exactly when the two axes are parallel, and then the word is a single boost-rotation about the common axis. In general the two orders are related by a conjugation,

$$
\hat{q}B = \left(\hat{q}B\hat{q}^{-1}\right)\hat{q} ,
$$

so reversing the order replaces the boost by the conjugate boost: the rapidity is unchanged, the axis is rotated by the rotor, and the element is a different one. The modulus is not affected, since a conjugation preserves the biquaternion norm, so the reversed word has the same $r$ and the same $\alpha$: the non-commutativity lives in the last two factors alone.

Both orders are single exponentials of the Hamilton form, and comparing their exponents shows what the order does and does not change. For the same pair,

$$
B\hat{q} = \exp(\xi_1\Theta) , \qquad \hat{q}B = \exp(\xi_2\Theta) , \qquad \Theta = 0.549803506 + 0.235625491\,i , \qquad \left\|\xi_1 - \xi_2\right\| = 0.553422443 ,
$$

with $\xi_1,\xi_2$ roots of $-1$: the complex angle $\Theta$, whose imaginary part is the rapidity and whose real part is the rotation angle, is the same in both orders, and only the root changes. The exponent of a **product** is a different matter and is not the sum of the exponents of the factors,

$$
\exp\left(\log B + \log\hat{q}\right)\neq B\hat{q} , \qquad \left\|\exp\left(\log B + \log\hat{q}\right) - B\hat{q}\right\| = 0.160024643 , \qquad \left\|\left[\log B,\ \log\hat{q}\right]\right\| = 0.308850825 \neq 0 ,
$$

so the rapidity of a product is not the sum of the rapidities, and its rotation angle is not the sum of the rotation angles. Only the modulus is additive, $r = r_1r_2$ and $\alpha = \alpha_1 + \alpha_2$, and it is exactly so.

The non-commutativity is a property of the boost factor rather than of the representation. The boost $B$ is Hermitian and positive definite of norm one, so it is a multiple of the unit only when $B = e_0$; it is therefore non-central whenever it is nontrivial, and that non-centrality is what forbids the transposition. The word becomes order-free in exactly the cases in which one of the two non-central factors is trivial or the two axes coincide: on the two halves, where $B = e_0$; on the branches of the two sectors on which the rotor is $\pm e_0$; on the centre, where both are trivial; and for a rotor about the axis of the boost. In the last case the element is a single boost-rotation, which is why two boosts along the same line have no residual rotation.

The three pairings of the companion article *Biquaternion Partial Polar Element Representations* are not reorderings of the word. All three keep $B$ before $\hat{q}$; what a pairing moves is the single central factor, and where it needs the two non-central factors in the other order — as the complex form does, to stand its boost to the right of its modulus — it pays with a conjugation $\hat{q}^{-1}B\hat{q}$, which is the boost about the rotated axis and not the original boost. The freedom of grouping and the lack of freedom of ordering are different freedoms, and the count $1+1+3+3$ is silent about both.

## The Complex Modulus

### The Biquaternion Norm

The biquaternion norm is

$$
N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_{\mu=0}^{3}Q_\mu^2 ,
$$

the sum of the squares of the four complex coefficients. It is a complex number, it is central, and it is multiplicative,

$$
N(\tilde{P}\tilde{Q}) = N(\tilde{P})N(\tilde{Q}).
$$

In the matrix model it is the determinant, $N(\tilde{Q}) = \det\Phi(\tilde{Q})$, so $N(\tilde{Q}) = 0$ is exactly the condition that $\tilde{Q}$ be a zero divisor, and the set $\{N = 0\}$ is the algebra's null cone.

### The Square Root and the Branch

The modulus is the square root of the biquaternion norm. To make it single valued, fix the branch once and for all. Write the biquaternion norm in polar form in $\mathbb{C}$,

$$
N(\tilde{Q}) = |N(\tilde{Q})|\,e^{i\varphi}, \qquad \varphi = \arg N(\tilde{Q}) \in (-\pi,\pi] ,
$$

and define

$$
\rho = \sqrt{|N(\tilde{Q})|}\;e^{i\varphi/2} ,
$$

which is the principal square root of $N(\tilde{Q})$. Its modulus and argument are

$$
r = |\rho| = \sqrt{|N(\tilde{Q})|} \ \ge 0, \qquad \alpha = \arg\rho = \frac{\varphi}{2} \in \left(-\frac{\pi}{2},\frac{\pi}{2}\right] .
$$

The pair $(r,\alpha)$ is unique: the modulus is non-negative by construction and the angle lies in a half-open interval of length $\pi$, so no two pairs give the same $\rho$. The square root $\rho$ is one of the two solutions of $\tilde T^2 = N(\tilde{Q})$, and the branch choice above selects one of them; the other, $-\rho$, has angle $\alpha\pm\pi$ and is outside the interval.

### The Positive Real Part and the Phase

The modulus is the first two factors of the decomposition written as one,

$$
\rho = r\,e^{i\alpha},
$$

with $r$ a positive real and $e^{i\alpha}$ central. This is the sense in which the representation always supplies a positive real factor: the positive real part of the complex square root of the biquaternion norm exists whenever the biquaternion norm is nonzero, and it is the absolute value $|N(\tilde{Q})|^{1/2}$.

The phase is not a normalisation constant, and its value carries information: it is one half of the argument of the determinant of $\tilde{Q}$, and it is nonzero exactly when $N(\tilde{Q})$ is not a positive real. In the physical reading of the companion articles, $e^{i\alpha}$ is the central phase that the corpus's Noether and gauge articles identify as the algebra's continuous symmetry.

## The Hermitian Positive Factor

### The Element of Unit Norm

Divide the biquaternion by its modulus:

$$
U = \frac{\tilde{Q}}{\rho} .
$$

Then $U$ has unit norm,

$$
N(U) = \frac{N(\tilde{Q})}{\rho^2} = \frac{N(\tilde{Q})}{N(\tilde{Q})} = 1 ,
$$

so $U$ lies in the algebra's analogue of the special linear group, and the whole content of the decomposition now sits in the split $U = B\hat{q}$.

### The Square Root of $UU^\dagger$

Form the Hermitian element

$$
S = U U^{\dagger} .
$$

It is Hermitian, since $S^\dagger = (UU^\dagger)^\dagger = UU^\dagger = S$, and it is positive definite, because in the matrix model $\Phi(S) = \Phi(U)\Phi(U)^\dagger$ is a positive definite Hermitian matrix whenever $\Phi(U)$ is invertible. Its biquaternion norm is

$$
N(S) = N(U)\,N(U^\dagger) = N(U)\,N(U)^{*} = 1 ,
$$

using multiplicativity, the reality of $N(U) = 1$, and $N(U^\dagger) = N(U)^*$.

The element $S$ is not itself the boost. The boost is its Hermitian positive square root,

$$
B = \sqrt{S} , \qquad B^2 = S ,
$$

which exists and is unique: a positive definite Hermitian matrix has exactly one positive definite Hermitian square root, and the condition $N(S) = 1$ is inherited as $N(B)^2 = N(S) = 1$, so $N(B) = 1$ for the positive root. The element $B$ is not arbitrary in $\mathbb{M}_+$: the square root of a norm-one element has norm one, and that is the normalisation of the boost.

### The Closed Form of the Boost

The matrix square root can be written out in the algebra, and this is what makes the decomposition an algorithm rather than an existence statement. Write the Hermitian element $S$ in its own parameters,

$$
S = \sigma\,e_0 + i\mathbf{w}, \qquad \sigma \in \mathbb{R}, \qquad \mathbf{w} \in \mathbb{R}^3 ,
$$

with real scalar part $\sigma$ and purely imaginary vector part $i\mathbf{w}$. Then $\sigma = \tfrac{1}{2}\operatorname{tr}\Phi(S) \ge 1$, since the two eigenvalues of a positive definite matrix of determinant one and trace $2\sigma$ are positive and multiply to one; and

$$
B = \sqrt{\frac{1+\sigma}{2}}\;e_0 + \frac{i\,\mathbf{w}}{\sqrt{2(1+\sigma)}} .
$$

*Verification.* Square the right-hand side. The cross term is $2\sqrt{\frac{1+\sigma}{2}}\frac{i\mathbf{w}}{\sqrt{2(1+\sigma)}} = i\mathbf{w}$, the square of the second term is $\frac{\mathbf{w}^2}{2(1+\sigma)} = -\frac{|\mathbf{w}|^2}{2(1+\sigma)}$ because the square of a real pure quaternion is the negative of its biquaternion norm, and the scalar part is therefore

$$
\frac{1+\sigma}{2} - \frac{|\mathbf{w}|^2}{2(1+\sigma)} = \frac{(1+\sigma)^2 - |\mathbf{w}|^2}{2(1+\sigma)} = \frac{2\sigma(1+\sigma)}{2(1+\sigma)} = \sigma ,
$$

where $|\mathbf{w}|^2 = \sigma^2-1$ was used, which is the statement $N(S) = \sigma^2-|\mathbf{w}|^2 = 1$ for the Hermitian element $S$. The result is $\sigma + i\mathbf{w} = S$.

### The Rapidity and the Axis

The closed form shows that the boost is determined by one positive number and one direction. Writing

$$
B = \cosh\frac{\psi}{2}\,e_0 + i\sinh\frac{\psi}{2}\,\hat{\mathbf{n}} , \qquad \psi \ge 0, \qquad \hat{\mathbf{n}} \in S^2 ,
$$

with $\cosh\psi = \sigma$ and $\hat{\mathbf{n}} = \mathbf{w}/|\mathbf{w}|$, the number $\psi$ is the boost's **rapidity** and $\hat{\mathbf{n}}$ its axis. The comparison of the two writings gives the dictionary

$$
\cosh\frac{\psi}{2} = \sqrt{\frac{1+\sigma}{2}}, \qquad \sinh\frac{\psi}{2} = \frac{|\mathbf{w}|}{\sqrt{2(1+\sigma)}} ,
$$

which are the half-angle identities applied to $\sigma = \cosh\psi$ and $|\mathbf{w}| = \sinh\psi$. The boost therefore carries three parameters, $\psi$ and the two angles of $\hat{\mathbf{n}}$, and the boost set is the three-dimensional hyperbolic space $H^3$ of the previous section. The notation is the corpus's: $\tilde{\Lambda} = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\hat{\mathbf{n}}$ is the boost biquaternion of the physics articles, Hermitian and of unit norm.

## The Unitary Factor

### The Residual and Its Unitarity

The rotor is the residual factor,

$$
\hat{q} = B^{-1}U = \bar{B}\,U ,
$$

where $B^{-1} = \bar{B}$ because $N(B) = 1$ and $B\bar{B} = N(B)e_0 = e_0$. It is unitary in the matrix sense,

$$
\hat{q}\,\hat{q}^{\dagger} = B^{-1}UU^{\dagger}B^{-1} = B^{-1}S\,B^{-1} = B^{-1}B^2B^{-1} = e_0 ,
$$

using $S = B^2$ and the Hermitian character of $B$, which lets $B^{-1}$ pass through the product. So $\hat{q}$ is an element of the unitary group $U(2)$ in the matrix model.

### Why It Is a Real Quaternion

More is true: $\hat{q}$ is a real quaternion, that is, an element of the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, all four of whose coefficients are real. Two conditions are needed and both hold. First,

$$
N(\hat{q}) = \frac{N(U)}{N(B)} = 1 ,
$$

by multiplicativity, so $\hat{q}$ is a unimodular unitary element, hence in $SU(2)$ in the matrix model. Second, the elements of $\mathbb{B}$ that are simultaneously unitary and of unit norm are exactly the unit real quaternions: an element of $U(2)$ is of the form $e^{i\beta}\tilde A$ with $\tilde A$ a unit real quaternion, and its biquaternion norm is $N(e^{i\beta}\tilde A) = e^{2i\beta}N(\tilde A) = e^{2i\beta}$, so the additional condition $N = 1$ forces $e^{2i\beta} = 1$, hence $\beta = 0$ modulo $\pi$, and leaves $\tilde A$ up to the sign that $N = 1$ fixes.

The rotor is therefore an element of

$$
\mathrm{Sp}(1) = SU(2) = S^3 ,
$$

the group of unit real quaternions, of dimension three. It is compact, and it is the same group that appears as the unit factor of the quaternion polar representation of the companion article. By the companion article on the Lorentz group, it acts on the material sector as a spatial rotation; the central phase $e^{i\alpha}$ has been split off from it, which is what distinguishes the present factor from the unitary factor of the matrix polar decomposition.

## The Theorem

### Statement

**Theorem (polar representation).** Let $\tilde{Q}\in\mathbb{B}$ with $N(\tilde{Q})\neq0$. Then there are unique

$$
r \in \mathbb{R}, \quad r>0, \qquad \alpha \in \left(-\frac{\pi}{2},\frac{\pi}{2}\right], \qquad B = \cosh\frac{\psi}{2}+i\sinh\frac{\psi}{2}\hat{\mathbf{n}} \in \mathbb{M}_+, \qquad \hat{q} \in \mathrm{Sp}(1),
$$

such that

$$
\tilde{Q} = r\,e^{i\alpha}\,B\,\hat{q} .
$$

Equivalently, $\tilde{Q} = \rho B\hat{q}$ with $\rho = re^{i\alpha} = \sqrt{N(\tilde{Q})}$ the principal square root.

### Existence

The construction of the three preceding sections gives the factors: $\rho$ from the branch of the square root of the biquaternion norm, $U = \tilde{Q}/\rho$ of unit norm, $S = UU^\dagger$ Hermitian positive definite of norm one, $B = \sqrt{S}$ its unique Hermitian positive square root, and $\hat{q} = B^{-1}U$, which is unitary and of norm one, hence a unit real quaternion. The product reproduces the element,

$$
r\,e^{i\alpha}B\hat{q} = \rho\,B\left(B^{-1}U\right) = \rho U = \tilde{Q} .
$$

### Uniqueness

Suppose $\tilde{Q} = r e^{i\alpha}B\hat{q} = r'e^{i\alpha'}B'\hat{q}'$ with both quadruples admissible. Taking norms and using $N(B\hat{q}) = N(B)N(\hat{q}) = 1$ gives $r^2e^{2i\alpha} = (r')^2e^{2i\alpha'}$, so the two principal square roots of $N(\tilde{Q})$ agree, and since $r,r' > 0$ with $\alpha,\alpha'$ in the same half-open interval of length $\pi$, one has $r = r'$ and $\alpha = \alpha'$. Then $U = \tilde{Q}/\rho$ is the same element in both decompositions, so $UU^\dagger$ is the same, and its Hermitian positive square root is unique, so $B = B'$; then $\hat{q} = B^{-1}U = \hat{q}'$.

### The Domain and the Light Cone

The theorem is stated on the complement of the null cone, $\{N(\tilde{Q})\neq0\}$, and that is exactly its domain: for $N(\tilde{Q}) = 0$ and $\tilde{Q}\neq0$ the element is a zero divisor, the matrix $\Phi(\tilde{Q})$ is singular, and no factorisation of the stated shape exists, since the product of the four factors has norm $r^2\cdot1\cdot1\cdot1 = r^2 > 0$ while $N(\tilde{Q}) = 0$. The null cone is the algebra's light cone, and it is treated in the companion article on biquaternion zero divisors. Among the decompositions of this series it is the mildest possible failure: a single cone, of real codimension two in the eight-dimensional algebra, whereas the partial forms of the companion article fail on larger sets.

**The condition of existence, in one line.** The polar representation of $\tilde{Q}$ exists if and only if

$$
N(\tilde{Q})\neq0 ,
$$

that is, if and only if $\tilde{Q}$ lies outside the null cone; equivalently, by the determinant criterion of *Biquaternion Norm and Invertibility*, if and only if $\tilde{Q}$ is invertible. The excluded elements are exactly the zero divisors, and no excluded element is reached as a limit of admissible ones: along a path to the cone the modulus $\rho = \sqrt{N(\tilde{Q})}$ tends to zero, while the norm-one part $\tilde{Q}/\rho$ has no limit in the algebra.

**The cone is thin in the algebra.** The condition $N(\tilde{Q}) = 0$ is one complex equation, hence two real equations, $\mathrm{Re}\,N = 0$ and $\mathrm{Im}\,N = 0$, and their gradients are independent away from the origin, so the cone has real codimension two. Counting real dimensions,

$$
\dim_{\mathbb{R}}\mathbb{B} = 8, \qquad
\dim_{\mathbb{R}}\{N = 0\} = 8 - 2 = 6, \qquad
\dim_{\mathbb{R}}\mathbb{B}^{\times} = 8 ,
$$

and deleting the cone does not lower the dimension of the algebra: the group of units $\mathbb{B}^{\times}$ and the algebra $\mathbb{B}$ are both eight-dimensional, and the domain of the polar representation is the algebra with a codimension-two set removed. The cone is stratified: away from the origin a generic point is a matrix of rank one, and at the single point $\tilde{Q} = 0$ the two gradients vanish together, so the cone is singular there, exactly as the classification of the zero divisors describes.

### The Boundary of the Family

The statement above says that on the null cone no factorisation of the four-factor shape exists; it does not say what the boundary of the family is. The limit of the boost family says it. Take the boost about the axis $-e_3$ and the real scale that collapses with it,

$$
r(\psi)\,B(\psi) = e^{-\psi/2}\left(\cosh\tfrac{\psi}{2}\,e_0 - i\sinh\tfrac{\psi}{2}\,e_3\right) \longrightarrow \tfrac12\left(e_0 - ie_3\right), \qquad \psi \to \infty,
$$

verified at $\psi = 20, 40, 80$, the difference from the limit being exactly $\tfrac12e^{-\psi}$ in each of the two non-zero coefficients. The limit is the minimal idempotent $\tfrac12(e_0 + \xi i)$ with $\xi = -e_3$, the object classified in the companion article on biquaternion zero divisors: Hermitian, of norm zero, and idempotent. The word at the boundary therefore keeps a real scale and a trigonometric factor and fills the hyperbolic slot with a Hermitian idempotent of norm zero, one factor short of the four. Sangwine & Hitzer exhibit the same degeneration on a divisor of zero,

$$
\tilde P = \tfrac12\left(e_0 + e_1 + ie_2 - ie_3\right) = \sqrt2\cdot\frac{e_0+e_1}{\sqrt2}\cdot\tfrac12\left(e_0 - ie_3\right),
$$

whose last factor is that idempotent, and whose numerical factor $\sqrt2$ is not the modulus of $\tilde P$, which vanishes, but the modulus of the real part of $\tilde P$. The unbounded direction of the boost group and the null cone are thus a single cone, seen once as the boundary of the domain and once as the set of minimal idempotents, and the failure at that boundary is the collapse of the boost's positive factor rather than a discontinuity of the algebra.

## The Algorithm

### The Five Steps

The proof above is effective, and it is worth recording as a procedure. Given $\tilde{Q}$ with $N(\tilde{Q})\neq0$:

1. Compute the biquaternion norm $N = \sum_\mu Q_\mu^2 \in \mathbb{C}$.
2. Take its principal square root: write $N = |N|e^{i\varphi}$ with $\varphi\in(-\pi,\pi]$, and put $\rho = \sqrt{|N|}e^{i\varphi/2}$, so that $r = \sqrt{|N|}$ and $\alpha = \varphi/2$.
3. Put $U = \tilde{Q}/\rho$, of unit norm.
4. Compute $S = UU^\dagger$, and write it as $\sigma e_0 + i\mathbf{w}$ with $\sigma\in\mathbb{R}$, $\mathbf{w}\in\mathbb{R}^3$; then put
   $B = \sqrt{\frac{1+\sigma}{2}}\,e_0 + \frac{i\mathbf{w}}{\sqrt{2(1+\sigma)}}$, and read the rapidity and axis off by $\cosh\psi = \sigma$, $\hat{\mathbf{n}} = \mathbf{w}/|\mathbf{w}|$.
5. Put $\hat{q} = \bar{B}U$, and verify that its coefficients are real and that $N(\hat{q}) = 1$.

The factors so obtained satisfy $\tilde{Q} = r e^{i\alpha}B\hat{q}$ identically. The only step that requires a convention rather than a formula is step 2, where the branch of the square root is fixed by $\alpha \in (-\pi/2,\pi/2]$; the other four steps are forced.

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

and $N(U) = 1$ as required.

*Step 4.* The Hermitian element $S = UU^\dagger$ is

$$
S = 1.299867367\,e_0 - 0.371390676\,i\,e_1 - 0.742781353\,i\,e_2 ,
$$

so $\sigma = 1.299867367$, $\mathbf{w} = (-0.371390676, -0.742781353, 0)$ and $|\mathbf{w}| = 0.830454799$; the identity $\sigma^2-|\mathbf{w}|^2 = 1$ holds to $7\times10^{-16}$. The boost is therefore

$$
B = 1.072349609\,e_0 - 0.173166789\,i\,e_1 - 0.346333577\,i\,e_2 ,
$$

with rapidity $\psi = 2\operatorname{arccosh}(1.072349609) = 0.756273220$, corresponding to the speed $\tanh(\psi/2) = 0.361088126$ in units $c = 1$, and axis $\hat{\mathbf{n}} = -(1,2,0)/\sqrt{5}$. The verification $B^2 = S$ was carried out to $2.2\times10^{-16}$ in the coefficients.

*Step 5.* The rotor is

$$
\hat{q} = \bar{B}U = 0.470592172\,e_0 + 0.394599292\,e_1 + 0.789198585\,e_2 ,
$$

all of whose coefficients are real, with $N(\hat{q}) = 1$; its rotation angle is $2.161669$ rad about the axis $(1,2,0)/\sqrt{5}$.

The reconstruction $\tilde{Q} = r e^{i\alpha}B\hat{q}$ was verified in double precision and agrees with $\tilde{Q}$ to $1.6\times10^{-16}$ in each coefficient. Note that the boost axis and the rotation axis are opposite in this example, which is a coincidence of the element and not a structural relation: no relation between the two axes is imposed by the decomposition, and a random element generally has them unrelated.

### A Second Example: an Element Already in Polar Form

Take the boost biquaternion of the physics articles with speed $0.6c$ along $e_1$,

$$
\tilde{\Lambda} = \cosh\frac{\psi}{2}\,e_0 + i\sinh\frac{\psi}{2}\,e_1 , \qquad \psi = \operatorname{atanh}0.6 = 0.693147181 ,
$$

so that $\tilde{\Lambda} = 1.060660172\,e_0 + 0.353553391\,i\,e_1$. Its biquaternion norm is $N = \cosh^2\frac{\psi}{2}-\sinh^2\frac{\psi}{2} = 1$, a positive real, so the modulus is $\rho = 1$, the scale is $r = 1$ and the phase is $\alpha = 0$. The remaining construction returns $U = \tilde{\Lambda}$, $S = \tilde{\Lambda}^2$, $B = \tilde{\Lambda}$ and $\hat{q} = e_0$, so that the four-factor form collapses to

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
| boost | $B$ | $\cosh\frac{\psi}{2}+i\sinh\frac{\psi}{2}\hat{\mathbf{n}}$, $\psi\ge0$ | $3$ | the Hermitian positive unit-norm factor, in $\mathbb{M}_+$ |
| rotor | $\hat{q}$ | $\mathrm{Sp}(1) = SU(2) = S^3$ | $3$ | the unit real quaternion, in $\mathbb{H}_{\mathbb{B}}$ |

### The Scale

The scale is a positive real number, the only factor that is both central and non-compact on the positive side. It multiplies the element rigidly: replacing $\tilde{Q}$ by $\lambda\tilde{Q}$ with $\lambda>0$ multiplies $r$ by $\lambda$ and leaves the other three factors unchanged. It is the absolute value of the determinant of the matrix image, raised to the power $\tfrac12$, since $|\det\Phi(\tilde{Q})| = |N(\tilde{Q})| = r^2$.

### The Central Phase

The phase is an element of the centre lying on the unit circle, and it is the only factor that is central and compact. It is determined by the argument of the biquaternion norm, $\alpha = \tfrac{1}{2}\arg N(\tilde{Q})$, and it vanishes exactly when the biquaternion norm is a positive real. It commutes with everything, so it may be written on either side of the other factors; in the physical reading it is the algebra's continuous internal symmetry.

### The Boost

The boost is the only factor that is neither central nor compact. It lies in the Hermitian subspace $\mathbb{M}_+$, is positive definite in the matrix picture, has unit norm, and is the exponential of a traceless Hermitian element,

$$
B = \exp(\sigma), \qquad \sigma \in \mathbb{M}_+ \cap \{\text{traceless}\} ,
$$

with $\sigma = i\frac{\psi}{2}\hat{\mathbf{n}}$ in the notation above, a traceless Hermitian element since its scalar part vanishes and its vector part is purely imaginary. The three parameters are the rapidity and the two angles of the axis, and the boost set is the hyperbolic space $H^3$. In the physics articles this factor is the Lorentz boost rotor, and its action on the material sector $\mathbb{M}_-$ is the boost of the frame.

### The Rotor

The rotor is a unit real quaternion: compact, three-dimensional, an element of the same group that the quaternion polar representation of the companion article produces as its unit factor. It is the factor that carries the spatial rotation, and it is the only factor that lies in the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ on the unit sphere. Being non-central, it does not commute with the boost, and that non-commutativity is the algebraic root of the Thomas-Wigner rotation of the physics articles: the product of two boosts is not a boost, and the discrepancy is a rotor.

### What the Sandwich Sees

The four factors are what an operator on the algebra detects, and the dagger sandwich $\mathrm{H}_{\tilde{Q}}(\tilde T)=\tilde{Q}\tilde T\tilde{Q}^{\dagger}$ reads them as follows. The scale enters through the single dilation $\lvert N(\tilde{Q})\rvert^{2}=r^{4}$ of the interval; the central phase enters through nothing at all, since the relation $\mathrm{H}_{z\tilde{Q}}=\lvert z\rvert^{2}\mathrm{H}_{\tilde{Q}}$ makes two elements differing by a unit-modulus central phase have the same operator; and the remaining two factors are the boost part and the rotation part of the action, in the order of composition $B\hat{q}$. The kernel of the operator is the phase circle, so the phase is exactly the factor the action discards, while the scale survives only through its fourth power. The operator itself is in *Biquaternion Rotations and Lorentz Transformations*.

**The operator factorises through the boost and the rotor, and doubles their parameters.** With the polar word $\tilde{Q}=re^{i\alpha}B\hat{q}$ and $\tilde{\Lambda}=B\hat{q}$ of unit norm,

$$
\mathrm{H}_{\tilde{Q}}=r^{2}\,\mathrm{H}_{\tilde{\Lambda}},
$$

because the Hermitian conjugates of the factors are $\hat{q}^{\dagger}=\hat{q}^{-1}$, $B^{\dagger}=B$, $r^{\dagger}=r$ and $(e^{i\alpha})^{\dagger}=e^{-i\alpha}$, so the two central factors cancel against their inverses. The pattern of the four factors as operators is then forced by the bilinearity:

| polar factor | range | as an operator on the algebra |
|---|---|---|
| scale $r$ | $(0,\infty)$ | dilatation by $r^{2}$, the factor counted twice |
| phase $e^{i\alpha}$ | $U(1)$ | none; it cancels and lies in the kernel |
| boost $B$ | rapidity $\psi$, axis $\hat{\mathbf{n}}$ | boost of the **doubled** rapidity |
| rotor $\hat{q}$ | angle $\theta$ | rotation by the **doubled** angle |

A non-central factor occurs once on each side, so its parameter is deposited twice; a central factor occurs on both sides and cancels. The exact diagonal case is

$$
\Phi(B)=\operatorname{diag}\bigl(e^{\psi/2},e^{-\psi/2}\bigr)
\quad\Longrightarrow\quad
\Phi(B)\,\Phi(\tilde T)\,\Phi(B)=\operatorname{diag}\bigl(e^{\psi},e^{-\psi}\bigr)\Phi(\tilde T),
$$

in which the operator stores the half-rapidity and produces the rapidity. The same doubling holds for the rotation angle, and it is the geometric origin of the double cover $SL(2,\mathbb{C})\to SO^{+}(1,3)$ read in *Biquaternion Rotations and Lorentz Transformations* as the two-to-one rotor map.

## Degenerate Cases

### The Unit-Norm Elements

If $N(\tilde{Q}) = 1$ then $\rho = 1$, $r = 1$ and $\alpha = 0$, and the representation reduces to

$$
\tilde{Q} = B\,\hat{q} , \qquad N(\tilde{Q}) = 1 .
$$

This is the Cartan form of the physics articles, in which a Lorentz rotor is written as a boost times a spatial rotation. It is the case of the decomposition in which two of the four factors are trivial, and it is the only case the physics corpus uses.

### The Central Elements

If $\tilde{Q} = Q_0e_0$ is a complex scalar then $N(\tilde{Q}) = Q_0^2$, and the construction returns $r = |Q_0|$, $B = e_0$, and for the phase the representative of $\arg Q_0$ in $(-\pi/2,\pi/2]$, with the residual sign carried by $\hat{q} = \pm e_0$. The scalar imaginary itself has the decomposition

$$
i = 1\cdot e^{i\pi/2}\cdot e_0\cdot e_0 ,
$$

which exhibits the phase factor at its extremal value. This element is the sharpest illustration of the point of the four factors: two of the three named representations of the companion article fail on it, since its vector part vanishes and its real quaternion part vanishes, while the representation is available and trivial.

### The Real Quaternions

If all four coefficients of $\tilde{Q}$ are real then $N(\tilde{Q}) = \sum_\mu q_\mu^2$ is a positive real, so $\alpha = 0$ and $r = |\tilde{Q}|$ is the quaternion modulus of the companion article. The element $U = \tilde{Q}/r$ is a unit real quaternion, and $S = UU^\dagger = U\bar{U} = e_0$, so $B = e_0$ and $\hat{q} = U$. The real quaternions therefore have no boost: their polar representation is the quaternion polar representation, and the two representations agree term by term.

### The Null Elements

If $N(\tilde{Q}) = 0$ and $\tilde{Q}\neq0$ the element is a zero divisor and no decomposition exists, as shown in the section on the domain. The failure is not uniform in the structure of the element: for $N(\tilde{Q}) = 0$ the matrix $\Phi(\tilde{Q})$ has rank one, its columns span a minimal left ideal, and the element is a multiple of an idempotent; the companion article on biquaternion zero divisors treats the classification. What is relevant here is only that no product of the four factors can reproduce it, because the biquaternion norm of such a product is a positive real.

## The Commutative Four-Dimensional Alternative

The four-factor representation above is the polar form of $\mathbb{B}$. The commutative four-dimensional algebra has its own, and it is the corpus's only polar form built for a commutative algebra of dimension four; it is recorded for the contrast, the two answering the same question differently.

The algebra is $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\oplus\mathbb{C}$, the reduced biquaternion algebra of *List of Algebras by Dimension*: an element is $q = z_1+z_2e$ with $e^2=+1$ and $z_1,z_2\in\mathbb{C}$. Pei, Chang and Ding construct its polar form (*IEEE Trans. Signal Processing* **52** (2004) 2012–2022, §III) and prove three things about it.

**Existence.** The form exists if and only if $N(q) = z_1^2-z_2^2\neq0$ — the domain condition of this article, and here it is also a factorisation statement, since $N(q) = \lambda_+\lambda_-$ in the idempotent coordinates $\lambda_\pm = z_1\pm z_2$. The excluded set is thus the union of the two ideals $\mathbb{C}e_+ \cup \mathbb{C}e_-$, with $e_\pm = \tfrac12(1\pm e)$, on which the element is a multiple of an idempotent; this is the commutative image of the null elements of the section above, and of the cone on which the four factors here fail.

**Uniqueness.** The form carries a scale and three phases, and it is unique once the ranges of the three phases are fixed; the uniqueness is proved by showing that the equations for the phases have exactly one solution in those ranges. The uniqueness here is therefore purchased by a range convention, whereas the uniqueness above is a theorem about the factorisation itself.

**Compatibility.** When the second component vanishes the form reduces to the ordinary complex polar form of *Complex Polar Element Representation*, which is the sense in which its authors select it as compatible with the complex case.

The form is useful for the two operations it is useful for here. Multiplication becomes trivial, moduli multiplying and phases adding, and the paper proves a **De Moivre theorem** for it; the inverse is read off directly; and the **geometric meaning** is stated — one scaling, four rotations in the coordinate planes $(1,2)$, $(3,4)$, $(1,4)$ and $(2,3)$, and two Lorentz transformations in the planes $(1,3)$ and $(2,4)$. That is the precise form of the claim recorded with this family of algebras in *The Three Two-Dimensional Algebras and the Three Kinds of Rotation*: the four-dimensional commutative algebra carries the elliptic rotations of its complex factor and the hyperbolic transformations of its split factor at the same time, and its authors attach the reading to the special theory of relativity.

One application is a use of a polar form the corpus does not otherwise have. The colour space is three-dimensional and the algebra four-dimensional, so the representation of a colour by an element of the algebra is not unique; the paper removes the redundancy by setting one of the three phases to zero, giving what it calls the **simplified polar form**, whose data are the brightness, hue and saturation of the colour and in which the norm and the conjugation of the element take their simplest forms. It is used for colour template matching and colour-sensitive edge detection, with the transforms of *Biquaternion Discrete Harmonic Analysis*.

## Relation to the Two Partial Forms

The relation of the present representation to the Hamilton, complex and Cartan representations is the following, stated here and proved in the companion article *Biquaternion Partial Polar Element Representations*.

The **Hamilton form** writes $\tilde{Q} = R\exp(\xi\Theta)$ with $R$ a complex scalar and $\xi$ a non-central root of $-1$ parallel to the vector part; in the present notation its two factors are

$$
R = r\,e^{i\alpha}, \qquad \exp(\xi\Theta) = B\,\hat{q} ,
$$

so that it groups the first two of the four factors into the modulus $R$ and the last two into the exponential. It is available whenever the vector part is non-null, which is a stronger condition than $N(\tilde{Q})\neq0$.

The **complex form** writes $\tilde{Q} = Q\exp(i\Psi)$ with $Q$ a real quaternion; in the present notation its two factors are

$$
Q = r\,\hat{q} , \qquad \exp(i\Psi) = e^{i\alpha}\,\bar{\hat{q}}\,B\,\hat{q} ,
$$

so that it groups the scale with the rotor into the quaternion modulus and the phase with a conjugated boost into the exponential. Its construction in the companion article proceeds from the real quaternion part of $\tilde{Q}$ and requires that part to be invertible, again a stronger condition than $N(\tilde{Q})\neq0$.

Both partial forms are therefore regroupings of the same four factors, taken in pairs; there are exactly three ways to pair four objects into two pairs, and the third pairing, in which the scale is grouped with the boost and the phase with the rotor, is the Cartan form $\tilde{Q} = (rB)(e^{i\alpha}\hat{q})$, the matrix polar decomposition into a positive Hermitian factor and a unitary factor. All three are treated in the companion article.

## Summary

Every biquaternion with non-vanishing norm has a unique polar representation

$$
\tilde{Q} = r\,e^{i\alpha}\,B\,\hat{q} , \qquad r = \sqrt{|N(\tilde{Q})|} > 0, \quad \alpha = \tfrac{1}{2}\arg N(\tilde{Q}), \quad B \in \mathbb{M}_+, \quad \hat{q}\in\mathrm{Sp}(1) ,
$$

in which $B$ is the Hermitian positive unit-norm boost and $\hat{q}$ the unit real quaternion rotor. The modulus of the decomposition is the complex number $\rho = re^{i\alpha} = \sqrt{N(\tilde{Q})}$, and the positive real factor $r$ is its absolute value, so a positive scale is always available and the phase is one of the four factors rather than a correction. The four factors have real dimensions $1+1+3+3 = 8$, they are unique, and the failure of the decomposition is exactly the null cone $N(\tilde{Q}) = 0$. The decomposition is the reference form of the series: the Hamilton and complex forms of the companion article are the two other pairings of the same four factors, and the Cartan form of the physics articles is the special case $N = 1$ in which the scale and the phase are trivial.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra, $\tilde{Q} = \sum_\mu Q_\mu e_\mu$, $Q_\mu\in\mathbb{C}$ |
| $i$ | the central scalar imaginary |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$ | the biquaternion norm, complex and central, equal to $\det\Phi(\tilde{Q})$ |
| $\rho = \sqrt{N(\tilde{Q})}$ | the complex modulus, the principal square root |
| $r = \sqrt{|N(\tilde{Q})|}$ | the scale, a positive real |
| $\alpha = \tfrac{1}{2}\arg N(\tilde{Q})$ | the phase angle, in $(-\pi/2,\pi/2]$ |
| $U = \tilde{Q}/\rho$ | the unit-norm part |
| $S = UU^\dagger = \sigma e_0 + i\mathbf{w}$ | the Hermitian positive element |
| $B = \sqrt{S}$ | the boost, Hermitian positive, $N(B) = 1$ |
| $\psi$, $\hat{\mathbf{n}}$ | the rapidity and axis of the boost |
| $\hat{q} = \bar{B}U$ | the rotor, a unit real quaternion |
| $\mathbb{M}_+$ | the Hermitian subspace, real scalar part and imaginary vector part |
| $\mathbb{M}_-$ | the anti-Hermitian subspace, the material sector of the physics articles |
| $\mathrm{Sp}(1)$ | the unit real quaternions, $SU(2) = S^3$ |

## Further Reading

- *Biquaternion Algebra* (`articles_maths/biquaternion-algebra.md`), for the algebra, the four conjugations and the six subspaces.
- *Biquaternion Partial Polar Element Representations* (`articles_maths/biquaternion-partial-polar-element-representations.md`), for the Hamilton, complex and Cartan representations as the three two-factor groupings of these four factors, with their domains.
- *Split-Biquaternion Polar Element Representation* (`articles_maths/split-biquaternion-polar-element-representation.md`), for the semisimple analogue, whose modulus is split complex and whose rotor is six-dimensional.
- *Quaternion Polar Element Representation* (`articles_maths/quaternion-polar-element-representation.md`), for the two-factor case that this decomposition restricts to on the real quaternions.
- *Complex Polar Element Representation* (`articles_maths/complex-polar-element-representation.md`) and *Split-Complex Polar Element Representation* (`articles_maths/split-complex-polar-element-representation.md`), for the two-dimensional members of the series, where the trichotomy of the exponential is stated once and the slots are counted in the smallest cases.
- *The 2×2 Matrix Element Representation of Biquaternions* (`articles_physics/the-2x2-matrix-element-representation-of-biquaternions.md`), for the isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$, the determinant, and the matrix polar decomposition.
- *The Lorentz Group in Biquaternionic Form* (`articles_physics/the-lorentz-group-in-biquaternionic-form-structure-and-representations.md`), for the boost and rotation rotors and the Thomas-Wigner rotation.
- S. J. Sangwine and E. Hitzer, "Polar decomposition of complexified quaternions and octonions", *Advances in Applied Clifford Algebras* (2020), DOI 10.1007/s00006-020-1048-y; technical report CES-535, University of Essex (2019), for the published two-exponential factorisation of the unit semi-norm elements and, in the general case, its Corollary 1 — whose trigonometric factor is the rotor $\hat{q}$ of this article and whose hyperbolic factor is the boost about the rotor-conjugated axis, $B = \hat{q}^{-1}H\hat{q}$ with the same rapidity and norm — for Lemma 1, the trichotomy of the exponential of a hypercomplex root of $-1$, $0$ or $+1$, and for the degenerate word on the null cone of the boundary subsection above. The order of the two non-central factors is reversed there, angle first, and the complex modulus is kept whole rather than split into a scale and a phase, which is the difference of count $2+3+3$ against $1+1+3+3$; the corpus fixes the branch and proves uniqueness, while the paper admits both orders.
- Soo-Chang Pei, Ja-Han Chang and Jian-Jiun Ding, "Commutative reduced biquaternions and their Fourier transform for signal and image processing applications", *IEEE Transactions on Signal Processing* **52** (2004) 2012–2022, for the reduced biquaternion algebra — the commutative four-dimensional algebra $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\oplus\mathbb{C}$, equivalently the double-complex, tessarine or commutative hypercomplex algebra — and for its polar form, its uniqueness under the phase-range convention, its De Moivre theorem and the simplified polar form for colour images.
