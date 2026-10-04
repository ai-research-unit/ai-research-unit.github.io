# __The Six Subspaces and the Ideals__

## Introduction

A **left ideal** of $\mathbb{B}$ is a $\mathbb{C}$-subspace $I$ with $\mathbb{B}I \subseteq I$, where the product of a subspace with a subspace is the span of the products; a **right ideal** is a subspace $J$ with $J\mathbb{B} \subseteq J$, and a **two-sided ideal** is both. The ideals of the biquaternion algebra are classified in *Biquaternion Ideals and Peirce Decomposition*: $\mathbb{B}$ is **simple** over $\mathbb{C}$, its only two-sided ideals being the zero subspace and $\mathbb{B}$, and it has **length two** as a left module over itself, so that every nonzero proper left ideal is a **minimal** left ideal, of real dimension $4$, and dually every nonzero proper right ideal is a minimal right ideal of real dimension $4$. The subject here is what that classification sees of the six distinguished subspaces.

The first half of the answer is a flat negative, and it is not special to the six. Since the only two-sided ideals are $0$ and $\mathbb{B}$, **no subspace of the six is a two-sided ideal**; no proper nonzero subspace of a simple algebra can be one. The one-sided statement is a flat positive instead: each of the six **generates the whole algebra on both sides**,

$$
\mathbb{B}\mathbb{S} = \mathbb{S}\mathbb{B} = \mathbb{B} \qquad \text{for each of the six subspaces } \mathbb{S} ,
$$

because a left ideal containing a unit is everything — if $\tilde U \in I$ is invertible then $\tilde U^{-1}\tilde U = e_0 \in I$ — and each of the six contains a unit: $e_0$ is in the centre, in the quaternion subspace and in $\mathbb{M}_+$, the element $e_1$ is in the vector subspace and in $\mathbb{M}_-$, and $ie_0$ is in the anti-quaternion subspace. So the six are not ideals, and each is as far from being one as a subspace can be.

The interest is in between: the **minimal** one-sided ideals, which are exactly the ones the six do determine, through their zero divisors. Two statements carry the article.

**Theorem (the annihilators of the zero divisors).** Let $\tilde Q \neq 0$ be a zero divisor of $\mathbb{B}$, so that $N(\tilde Q) = 0$. Write $I_{\tilde Q}$ for the set of $\tilde X$ with $\tilde X\tilde Q = 0$ and $J_{\tilde Q}$ for the set of $\tilde X$ with $\tilde Q\tilde X = 0$. Then $I_{\tilde Q}$ is a minimal left ideal, $J_{\tilde Q}$ is a minimal right ideal, and each has real dimension $4$.

**Theorem (the ideal generated against the annihilator).** For a nonzero **nilpotent** of the vector subspace, $\mathbf{P}^2 = 0$, the ideal generated and the annihilator coincide,

$$
\mathbb{B}\mathbf{P} = I_{\mathbf{P}} , \qquad \mathbf{P}\mathbb{B} = J_{\mathbf{P}} ;
$$

for every other zero divisor $\tilde Q$ the two are distinct and therefore complementary,

$$
\mathbb{B} = \mathbb{B}\tilde Q \oplus I_{\tilde Q} = \tilde Q\mathbb{B} \oplus J_{\tilde Q} .
$$

The subspaces of the six that carry a zero divisor are the vector subspace, $\mathbb{M}_+$ and $\mathbb{M}_-$, by *The Six Subspaces and the Zero Divisors*; the other three, the centre, the quaternion subspace and the anti-quaternion subspace, consist of $0$ and units, and determine no minimal ideal at all. So the ideal content of the six is carried by three of them:

| subspace | left ideal generated | right ideal generated | units in it | minimal one-sided ideals determined |
|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $\mathbb{B}$ | $\mathbb{B}$ | all $Ae_0$ with $A \neq 0$ | none |
| $\mathrm{Vect}(\mathbb{B})$ | $\mathbb{B}$ | $\mathbb{B}$ | $e_1$ | $\mathbb{B}\mathbf{P} = I_{\mathbf{P}}$ and $\mathbf{P}\mathbb{B} = J_{\mathbf{P}}$, $\mathbf{P}$ a nonzero nilpotent |
| $\mathbb{H}_{\mathbb{B}}$ | $\mathbb{B}$ | $\mathbb{B}$ | $e_0$ | none |
| $i\mathbb{H}_{\mathbb{B}}$ | $\mathbb{B}$ | $\mathbb{B}$ | $ie_0$ | none |
| $\mathbb{M}_+$ | $\mathbb{B}$ | $\mathbb{B}$ | $e_0$ | $\mathbb{B}\tilde\Pi$, $I_{\tilde\Pi} = \mathbb{B}(e_0-\tilde\Pi)$ and their right-hand twins, $\tilde\Pi$ a Hermitian idempotent |
| $\mathbb{M}_-$ | $\mathbb{B}$ | $\mathbb{B}$ | $e_1$ | the same four, unchanged |

## The Centre Subspace

A central element is $Ae_0$, invertible exactly when $A \neq 0$, so the centre is a field and contains no zero divisor; it determines no minimal ideal, and the left ideal it generates is $\mathbb{B}$, by $e_0 \in \mathbb{C}_{\mathbb{B}}$. Its only idempotents are $0$ and $e_0$.

The centre is worth one remark on the Peirce side. A **central** idempotent $e$ gives the Peirce decomposition $\mathbb{B} = \mathbb{B}e \oplus \mathbb{B}(e_0-e)$, and this is more than a direct sum: the two summands are two-sided ideals and the decomposition is a product of algebras, $\mathbb{B} = \mathbb{B}e \times \mathbb{B}(e_0-e)$, as *Biquaternion Ideals and Peirce Decomposition* records. For the biquaternion algebra that is impossible unless one factor is zero, because $\mathbb{B}$ is simple; and indeed the only central idempotents are $0$ and $e_0$, the two cases in which one factor is $\mathbb{B}$ and the other is $0$. **The Peirce decomposition relative to a central idempotent is trivial for $\mathbb{B}$**, and this is the same fact as simplicity, read through the centre.

## The Vector Subspace

The vector subspace is the one of the six in which the two opposite kinds of element meet. Its roots of $-1$ are the pure roots, by *The Six Subspaces and the Roots of Minus One*, and those are units; its nilpotents are the nonzero solutions of $(\mathbf{P},\mathbf{P}) = 0$, and those are zero divisors. The units generate $\mathbb{B}$, as above; the nilpotents generate minimal ideals, and for them the ideal and the annihilator are the same set.

**Proof of the nilpotent case of the second theorem.** If $\mathbf{P}^2 = 0$ then $(\tilde X\mathbf{P})\mathbf{P} = \tilde X\mathbf{P}^2 = 0$ for every $\tilde X$, so $\mathbb{B}\mathbf{P} \subseteq I_{\mathbf{P}}$, and $\mathbb{B}\mathbf{P}$ contains $\mathbf{P} \neq 0$ while $I_{\mathbf{P}}$ is proper, so both are nonzero proper left ideals; by the length-two statement they are both minimal of real dimension $4$, hence equal. The right-hand statement is the mirror image, using $(\mathbf{P}\tilde X)\mathbf{P} = 0$ on the left instead. $\square$

An explicit case is $\mathbf{P} = e_1 + ie_2$, with $\mathbf{P}^2 = 0$ and

$$
\mathbb{B}\mathbf{P} = I_{\mathbf{P}} = \operatorname{span}_{\mathbb{R}}\left\{e_1 + ie_2,\; e_2 - ie_1,\; e_0 - ie_3,\; e_3 + ie_0\right\},
$$

where the first two elements are further nilpotents of the vector subspace and the last two are a Hermitian element and $i$ times it — $e_0 - ie_3 = 2\cdot\tfrac{1}{2}(e_0 - ie_3)$ and $e_3 + ie_0 = i(e_0 - ie_3) = 2i\cdot\tfrac{1}{2}(e_0 - ie_3)$. So this minimal ideal is the sum of a complex line of the vector subspace, a real line of $\mathbb{M}_+$ and a real line of $\mathbb{M}_-$; it contains no basis element of the algebra, so it is not a sum of coordinate blocks, and it is not one of the six.

## The Quaternion Subspace

The quaternion subspace is a division algebra, so every nonzero element of it is a unit and it contains no zero divisor. The left ideal generated by any of its nonzero elements is $\mathbb{B}$, the left ideal generated by the subspace is $\mathbb{B}$, and no minimal ideal arises from it. This is the sharpest of the three negative cases: not merely the subspace as a whole, but **every single nonzero element** of $\mathbb{H}_{\mathbb{B}}$ generates the whole algebra on both sides, so the ideal theory sees nothing of it beyond the identity element it shares with the centre and $\mathbb{M}_+$.

The quaternion subspace is closed under the product, one of the two among the six that are (the centre being the other), but it is not an ideal: $ie_1 \in \mathbb{B}$ and $\mathbb{H}_{\mathbb{B}} \ni e_1$ give $ie_1e_1 = -i \notin \mathbb{H}_{\mathbb{B}}$, so left multiplication by an element of $\mathbb{B}$ already leaves it.

## The Anti-Quaternion Subspace

The anti-quaternion subspace is $i\mathbb{H}_{\mathbb{B}}$, and multiplication by the central unit $i$ carries $\mathbb{H}_{\mathbb{B}}$ bijectively to it and preserves products and linear combinations. So everything said of the quaternion subspace holds of it verbatim: it is a division algebra, every nonzero element is a unit, no zero divisor lies in it, and every nonzero element generates $\mathbb{B}$ on both sides. It is not an ideal: $e_1 \in \mathbb{B}$ and $ie_1 \in i\mathbb{H}_{\mathbb{B}}$ give $e_1 \cdot ie_1 = -i \notin i\mathbb{H}_{\mathbb{B}}$.

## The Hermitian Subspace

The Hermitian subspace carries the idempotents, and with them the minimal ideals. Let $\tilde\Pi = \tfrac{1}{2}(e_0 + i\mathbf{u})$ be a Hermitian idempotent and $f = e_0 - \tilde\Pi = \tfrac{1}{2}(e_0 - i\mathbf{u})$ its complement, from *The Six Subspaces and the Idempotents and Projections*. The annihilators are the complement ideals themselves, in the plain sense

$$
I_{\tilde\Pi} = \left\{\tilde X : \tilde X\tilde\Pi = 0\right\} = \left\{\tilde X\,f : \tilde X \in \mathbb{B}\right\} = \mathbb{B}f , \qquad J_{\tilde\Pi} = f\mathbb{B} ,
$$

the first because $\tilde X\tilde\Pi = 0$ leaves $\tilde X = \tilde X(\tilde\Pi + f) = \tilde X f$, and conversely $(\tilde X f)\tilde\Pi = \tilde X f\tilde\Pi = 0$. Here $\tilde\Pi$ is not nilpotent, its square being $2\tilde\Pi$, so the second theorem applies with its second alternative and

$$
\mathbb{B} = \mathbb{B}\tilde\Pi \oplus \mathbb{B}f = \tilde\Pi\mathbb{B} \oplus f\mathbb{B} ,
$$

four nonzero proper one-sided ideals, all minimal, all of real dimension $4$, arranged in two complementary pairs.

The four are the halves of the Peirce decomposition. Expanding $\tilde X$ as $\tilde\Pi\tilde X\tilde\Pi + \tilde\Pi\tilde X f + f\tilde X\tilde\Pi + f\tilde X f$ gives

$$
\mathbb{B} = \tilde\Pi\mathbb{B}\tilde\Pi \oplus \tilde\Pi\mathbb{B}f \oplus f\mathbb{B}\tilde\Pi \oplus f\mathbb{B}f ,
$$

and each of the four Peirce spaces is a complex line, so that the decomposition is

$$
\mathbb{B} = \mathbb{C}\tilde\Pi \oplus \mathbb{C}\tilde R \oplus \mathbb{C}\tilde T \oplus \mathbb{C}f , \qquad \mathbb{C}\tilde R = \tilde\Pi\mathbb{B}f , \quad \mathbb{C}\tilde T = f\mathbb{B}\tilde\Pi .
$$

For $\tilde\Pi = \tfrac{1}{2}(e_0 + ie_1)$ the lines are spanned by

$$
\tilde\Pi\mathbb{B}\tilde\Pi = \mathbb{C}\tilde\Pi , \quad \tilde\Pi\mathbb{B}f = \mathbb{C}(e_3 - ie_2) , \quad f\mathbb{B}\tilde\Pi = \mathbb{C}(e_3 + ie_2) , \quad f\mathbb{B}f = \mathbb{C}f ,
$$

and the same four, grouped in pairs, are the four minimal one-sided ideals:

$$
\mathbb{B}\tilde\Pi = \mathbb{C}\tilde\Pi \oplus \mathbb{C}(e_3 + ie_2) , \quad \mathbb{B}f = \mathbb{C}f \oplus \mathbb{C}(e_3 - ie_2) , \quad \tilde\Pi\mathbb{B} = \mathbb{C}\tilde\Pi \oplus \mathbb{C}(e_3 - ie_2) , \quad f\mathbb{B} = \mathbb{C}f \oplus \mathbb{C}(e_3 + ie_2) .
$$

Two of the four lines are the **idempotent lines** $\mathbb{C}\tilde\Pi$ and $\mathbb{C}f$, each meeting $\mathbb{M}_+$ and $\mathbb{M}_-$ in one real dimension — $\tilde\Pi$ is Hermitian and $i\tilde\Pi$ is anti-Hermitian — and two are the **nilpotent lines** $\mathbb{C}(e_3 \mp ie_2)$, lying wholly in the vector subspace, since $e_3 \pm ie_2$ is a nilpotent and $i$ times a nilpotent is again pure. So each minimal ideal is the sum of a complex line of the vector subspace, a real line of $\mathbb{M}_+$ and a real line of $\mathbb{M}_-$, and of nothing else.

## The Anti-Hermitian Subspace

The anti-Hermitian subspace is $i\mathbb{M}_+$: multiplication by the central unit $i$ is a bijection of $\mathbb{M}_+$ onto $\mathbb{M}_-$ that preserves products and linear combinations and therefore preserves ideals. So the zero divisors of $\mathbb{M}_-$ are the purely imaginary multiples of the Hermitian idempotents, by *The Six Subspaces and the Zero Divisors*, and the minimal ideals they determine are the very same four, $\mathbb{B}\tilde\Pi$, $\mathbb{B}f$, $\tilde\Pi\mathbb{B}$ and $f\mathbb{B}$, with the same elements. **The subspace $\mathbb{M}_-$ adds no ideal to those already determined by $\mathbb{M}_+$**, and the same relation holds between $i\mathbb{H}_{\mathbb{B}}$ and $\mathbb{H}_{\mathbb{B}}$, and between the centre and itself, so that up to the central unit $i$ the ideal theory of the six is carried by the three subspaces $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$ and $\mathbb{M}_+$.

## Summary

The biquaternion algebra is simple, so its only two-sided ideals are $0$ and $\mathbb{B}$ and no subspace of the six is a two-sided ideal; and each of the six contains a unit, so each of the six generates $\mathbb{B}$ as a left ideal, as a right ideal and as a two-sided ideal. The classification has length two, so every nonzero proper left ideal and every nonzero proper right ideal is minimal of real dimension $4$. Through its zero divisors each of the six determines minimal ideals, and there are none unless the subspace carries a zero divisor: none from the centre, the quaternion subspace or the anti-quaternion subspace, which consist of $0$ and units; from the vector subspace, the minimal ideal $\mathbb{B}\mathbf{P} = I_{\mathbf{P}}$ of any nonzero nilpotent, which coincides with its own annihilator; and from either Hermitian subspace, the four minimal ideals $\mathbb{B}\tilde\Pi$, $\mathbb{B}f$, $\tilde\Pi\mathbb{B}$, $f\mathbb{B}$ of a Hermitian idempotent, which come in two complementary pairs summing to $\mathbb{B}$. For a non-nilpotent zero divisor the ideal generated and the annihilator are distinct and complementary; for a nilpotent they coincide. The four minimal ideals of a Hermitian idempotent are the four Peirce spaces, which are complex lines: the two idempotent lines and the two nilpotent lines, the latter inside the vector subspace. Every one of the minimal ideals determined by the six meets the six in the same way, two real dimensions in the vector subspace, one in $\mathbb{M}_+$ and one in $\mathbb{M}_-$,

| minimal ideal | $\mathbb{C}_{\mathbb{B}}$ | $\mathrm{Vect}(\mathbb{B})$ | $\mathbb{H}_{\mathbb{B}}$ | $i\mathbb{H}_{\mathbb{B}}$ | $\mathbb{M}_+$ | $\mathbb{M}_-$ |
|---|---|---|---|---|---|---|
| each $\mathbb{B}\mathbf{P}$, $\mathbf{P}\mathbb{B}$, $\mathbb{B}\tilde\Pi$, $\mathbb{B}f$, $\tilde\Pi\mathbb{B}$, $f\mathbb{B}$ | $0$ | $2$ | $0$ | $0$ | $1$ | $1$ |

the entries being real dimensions; so the minimal ideals meet exactly the three subspaces that carry zero divisors, and avoid the other three entirely. The classification and the Peirce decomposition are the business of *Biquaternion Ideals and Peirce Decomposition*; what is added here is their restriction to the six.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra |
| $\mathbb{C}_{\mathbb{B}}, \mathrm{Vect}(\mathbb{B})$ | the centre and the vector subspace |
| $\mathbb{H}_{\mathbb{B}}, i\mathbb{H}_{\mathbb{B}}$ | the quaternion and anti-quaternion subspaces |
| $\mathbb{M}_+, \mathbb{M}_-$ | the Hermitian and anti-Hermitian subspaces |
| $I_{\tilde Q}, J_{\tilde Q}$ | the sets of $\tilde X$ with $\tilde X\tilde Q = 0$ and with $\tilde Q\tilde X = 0$ |
| $\tilde\Pi, f$ | a Hermitian idempotent and its complement $e_0 - \tilde\Pi$ |
| $\mathbf{P}$ | a nonzero nilpotent of the vector subspace |

## Further Reading

- *Introduction to the Six Subspaces* (`articles_maths/introduction-to-the-six-subspaces.md`), for the six subspaces themselves, one to a section
- *The Six Subspaces and the Zero Divisors* (`articles_maths/the-six-subspaces-and-the-zero-divisors.md`), for the zero divisors whose annihilators the minimal ideals are
- *The Six Subspaces and the Idempotents and Projections* (`articles_maths/the-six-subspaces-and-the-idempotents-and-projections.md`), for the Hermitian idempotents and the frame they form
- *The Six Subspaces and the Roots of Minus One* (`articles_maths/the-six-subspaces-and-the-roots-of-minus-one.md`), for the pure roots, which are the units of the vector subspace
- *Biquaternion Ideals and Peirce Decomposition* (`articles_maths/biquaternion-ideals-and-peirce-decomposition.md`), for simplicity, the length, the minimal ideals and the Peirce decomposition in the whole algebra
- *The Six Subspaces and the Forms* (`articles_maths/the-six-subspaces-and-the-forms.md`), for the theorem that the minimal one-sided ideals are the maximal totally isotropic one-sided ideals of the bilinear form, and for the Peirce basis in which that form is hyperbolic
- *Biquaternion Multiplication* (`articles_maths/biquaternion-multiplication.md`), for the product formula
