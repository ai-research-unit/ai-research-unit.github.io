
# __The Square of the General Quaternionic Sesquilinear Product and the Two Halves__

## Introduction

The biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ carries four general products on its underlying $\mathbb{C}$-vector space (*The Four General Products of the Biquaternion $\mathbb{C}$ Space*), and the fourth of them,

$$
\tilde Q_1 \star \tilde Q_2 = \tilde Q_1^{\natural}\tilde Q_2^{*} ,
$$

is the subject of this group. The rule and the scalar–vector form are *The Four General Products of the Biquaternion $\mathbb{C}$ Space* §*The General Quaternionic Sesquilinear Product*; the sesqualgebra it defines and the two actions of the unit are *Introduction to the General Quaternionic Sesqualgebra*. The symbols are those of the group: ${}^{\natural}$ is the natural conjugation $\tilde Q_1^{\natural} = Q_{1t} - \vec Q_1$, ${}^{*}$ is the star conjugation $\tilde Q_1^{*} = \overline{Q_{1t}} - \overline{\vec Q_1}$, the bar is the coefficientwise complex conjugation, and $\langle\tilde Q_1\rangle_{\natural} = \tilde Q_1\tilde Q_1^{\natural} = \sum_\mu Q_{1\mu}^{2}$ is the norm form.

The subject of this article is the **square** of the multiplication on a single element, $\tilde Q \star \tilde Q$, and its reading on the two halves of the algebra. The square is the computation every later article of the group uses: it is the equation of the idempotents of *Square Roots of One and the Idempotents of the General Quaternionic Sesqualgebra*, it is the residue of the associator of *The Associator of the General Quaternionic Sesquilinear Product*, and it is the value the operators of *The Left and Right Multiplications of the General Quaternionic Sesquilinear Product* reproduce. The article establishes three things. First, the square has the closed form

$$
\tilde Q \star \tilde Q = \bigl(\overline{\tilde Q}\tilde Q\bigr)^{\natural} = \tilde Q^{\natural}\tilde Q^{*} ,
$$

with scalar part $\sum_\mu \varepsilon_\mu Q_\mu\overline{Q_\mu} = \lvert Q_t\rvert^{2} - \lvert Q_x\rvert^{2} - \lvert Q_y\rvert^{2} - \lvert Q_z\rvert^{2}$, an indefinite form of signature $(2,2)$. Second, on the two halves $\mathbb{M}_{+}$ and $\mathbb{M}_{-}$ the square collapses to the centre with opposite signs, $\tilde Q \star \tilde Q = \pm \langle\tilde Q\rangle_{\natural}e_t$, the sign being that of the half. Third, the elements whose square vanishes form a **proper** subfamily of the zero-divisor cone: every square-zero element has norm $0$, and not every element of norm $0$ has square zero, a fact that separates this product from both bilinear products.

The article owns the square, its scalar part, its behaviour on the two halves and the square-zero set. It cites the rule and the four scalar parts to *The Four General Products of the Biquaternion $\mathbb{C}$ Space* and *Relations Between the Four General Products* §*The Four Scalar Parts*; it cites the two halves and their definition to *Introduction to the Remarkable Subspaces*, *Decompositions Along the Remarkable Subspaces* and *Hermitian and Skew-Hermitian Elements*; it cites the zero-divisor criterion to *Zero Divisors of the Biquaternion Algebra*; and it does not treat the idempotents, which are *Square Roots of One and the Idempotents of the General Quaternionic Sesqualgebra*, nor the operators, which are *The Left and Right Multiplications of the General Quaternionic Sesquilinear Product*.

## The Square of an Element

### The Rule

**Proposition (the square).** For every biquaternion $\tilde Q$,

$$
\boxed{\; \tilde Q \star \tilde Q = \bigl(\overline{\tilde Q}\tilde Q\bigr)^{\natural} = \tilde Q^{\natural}\tilde Q^{*} \;}.
$$

**Proof.** The second expression is the rule at equal arguments. For the first, the natural conjugation is an anti-automorphism of the plain product and the two conjugations commute, so $\bigl(\overline{\tilde Q}\tilde Q\bigr)^{\natural} = \tilde Q^{\natural}\bigl(\overline{\tilde Q}\bigr)^{\natural} = \tilde Q^{\natural}\tilde Q^{*}$, since $\bigl(\overline{\tilde Q}\bigr)^{\natural} = \overline{\tilde Q^{\natural}} = \tilde Q^{*}$.

**Caution (the two squares).** The square of this multiplication is not the plain square $\tilde Q\tilde Q = \tilde Q^{2}$, nor the square of the sibling bilinear product $\tilde Q^{\natural}\tilde Q = \bigl(\sum_\mu Q_\mu^{2}\bigr)e_t$. The three are different elements of $\mathbb{B}$, and their agreement is exceptional (*Introduction to the General Quaternionic Sesqualgebra*, §*The Square, the Idempotents and the Ternary Product*; *Introduction to the General Quaternionic Algebra*, §*The Square and the Elements It Distinguishes*). The plain square and the square of the sibling bilinear product are the two other elements built from the element and its two conjugations, and the comparison of the four squares is *Comparison Between the Four General Products* §*The Squares, the Idempotents and the Roots*.

### The Scalar Part

**Proposition (the scalar part of the square).** For every biquaternion $\tilde Q$,

$$
\mathrm{Sc}\bigl(\tilde Q \star \tilde Q\bigr) = \sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu Q_\mu\overline{Q_\mu} = \lvert Q_t\rvert^{2} - \lvert Q_x\rvert^{2} - \lvert Q_y\rvert^{2} - \lvert Q_z\rvert^{2} , \qquad \varepsilon = (1,-1,-1,-1) .
$$

**Proof.** The scalar part of the square is the scalar part of $\tilde Q^{\natural}\tilde Q^{*}$. On the coordinates, $\bigl(\tilde Q^{\natural}\bigr)_\mu = \varepsilon_\mu Q_\mu$ and $\bigl(\tilde Q^{*}\bigr)_\mu = \varepsilon_\mu\overline{Q_\mu}$, and the scalar part of the plain product is the signed diagonal pairing $\sum_\mu \varepsilon_\mu(\tilde Q^{\natural})_\mu(\tilde Q^{*})_\mu = \sum_\mu \varepsilon_\mu^{3} Q_\mu\overline{Q_\mu} = \sum_\mu\varepsilon_\mu Q_\mu\overline{Q_\mu}$, since $\varepsilon_\mu^{3} = \varepsilon_\mu$. The second display is the definition of the sign vector.

**Remark.** The scalar part is the **Krein form** of the four coordinates: a nondegenerate form of signature $(2,2)$, positive on the scalar coordinate and negative on the three vector coordinates. It is the first of the two properties that decide the element theory of the product, and it is what makes the square-zero problem different from the zero-divisor problem. The same form is the scalar part of the product off the diagonal, $\mathrm{Sc}(\tilde Q_1\star\tilde Q_2) = \sum_\mu\varepsilon_\mu Q_{1\mu}\overline{Q_{2\mu}}$, which is *The Four General Products of the Biquaternion $\mathbb{C}$ Space* read with the two signs, and it is the fourth of the four scalar parts of *Relations Between the Four General Products* §*The Four Scalar Parts*.

### The Vector Part

**Proposition (the vector part of the square).** For every biquaternion $\tilde Q$,

$$
\mathrm{Vec}\bigl(\tilde Q \star \tilde Q\bigr) = -\Bigl(\overline{Q_t}\,\vec Q + Q_t\,\overline{\vec Q} + \overline{\vec Q}\times\vec Q\Bigr) ,
$$

the dot and cross products being the general plain bilinear ones.

**Proof.** The square is the ${}^{\natural}$-image of $\overline{\tilde Q}\tilde Q$, and ${}^{\natural}$ fixes the scalar coordinate and negates the vector coordinate; hence $\mathrm{Vec}\bigl(\tilde Q\star\tilde Q\bigr) = -\mathrm{Vec}\bigl(\overline{\tilde Q}\tilde Q\bigr)$. The vector part of the plain product $\overline{\tilde Q}\tilde Q$ is $\overline{Q_t}\vec Q + Q_t\overline{\vec Q} + \overline{\vec Q}\times\vec Q$ by the scalar–vector form of *The Four General Products of the Biquaternion $\mathbb{C}$ Space*, with the first factor $\overline{\tilde Q}$ of scalar part $\overline{Q_t}$ and vector part $\overline{\vec Q}$.

**Remark.** The vector part is the reason the square is not generally an element of the Hermitian subspace. The scalar part is real, being a sum of moduli with signs, but the vector part is a general complex vector and it is not the imaginary multiple of a real vector; the square can be Hermitian, as for $\tilde Q = \vec e_x + i\vec e_y$ where it is $-2e_t - 2i\vec e_z$, but it need not be, and the element $\tilde Q = e_t + \vec e_z$ is a witness: its square is $-2\vec e_z$, whose star is $+2\vec e_z$ and whose natural conjugate is $+2\vec e_z$, neither equal to the square. This is the contrast with the sibling sesquilinear product, whose square $\tilde Q\tilde Q^{*}$ is Hermitian for every element by the identity $(\tilde Q\tilde Q^{*})^{*} = \tilde Q\tilde Q^{*}$.

## The Two Halves

### The Square on the Hermitian Half

**Proposition.** For $\tilde Q_1 \in \mathbb{M}_{+}$,

$$
\tilde Q_1 \star \tilde Q_1 = \langle\tilde Q_1\rangle_{\natural}\, e_t ,
$$

a real scalar; the square lies in the centre and is fixed by both conjugations.

**Proof.** Let $\tilde Q_1 \in \mathbb{M}_{+}$, so that $\tilde Q_1^{*} = \tilde Q_1$ and the scalar coordinate $Q_{1t}$ is real while the vector coordinates $Q_{1k}$ are purely imaginary; then $\overline{\tilde Q_1} = \tilde Q_1^{\natural}$. The square is $\tilde Q_1^{\natural}\tilde Q_1^{*} = \tilde Q_1^{\natural}\tilde Q_1$, and the $\natural$-product of an element with its natural conjugate is the central scalar $\tilde Q_1^{\natural}\tilde Q_1 = \bigl(\sum_\mu Q_{1\mu}^{2}\bigr)e_t = \langle\tilde Q_1\rangle_{\natural}e_t$ (*Introduction to the General Quaternionic Algebra* §*The Square and the Elements It Distinguishes*).

### The Square on the Anti-Hermitian Half

**Proposition.** For $\tilde Q_2 \in \mathbb{M}_{-}$,

$$
\tilde Q_2 \star \tilde Q_2 = -\langle\tilde Q_2\rangle_{\natural}\, e_t ,
$$

a real scalar; in particular the square is the negative of the central scalar of the Hermitian case.

**Proof.** Let $\tilde Q_2 \in \mathbb{M}_{-}$, so that $\tilde Q_2^{*} = -\tilde Q_2$ and the scalar coordinate is purely imaginary while the vector coordinates are real; then $\overline{\tilde Q_2} = -\tilde Q_2^{\natural}$. The square is $\tilde Q_2^{\natural}\tilde Q_2^{*} = -\tilde Q_2^{\natural}\tilde Q_2 = -\bigl(\sum_\mu Q_{2\mu}^{2}\bigr)e_t = -\langle\tilde Q_2\rangle_{\natural}e_t$, by the same central-scalar identity.

### The Sign of the Half

**Corollary.** The square on the two halves is the central scalar with the sign of the half,

$$
\boxed{\; \tilde Q_1 \star \tilde Q_1 = \langle\tilde Q_1\rangle_{\natural}e_t \ \ (\tilde Q_1 \in \mathbb{M}_{+}) , \qquad \tilde Q_2 \star \tilde Q_2 = -\langle\tilde Q_2\rangle_{\natural}e_t \ \ (\tilde Q_2 \in \mathbb{M}_{-}) \;},
$$

so that the multiplication reads the splitting $\mathbb{B} = \mathbb{M}_{+} \oplus \mathbb{M}_{-}$ by the sign.

**Proof.** The two displays are the two propositions. The splitting is the order-two property of the involution ${}^{*}$, which is *Hermitian and Skew-Hermitian Elements*; the multiplication does not preserve the splitting, but on a multiple of a single half its square is the central scalar with the sign of that half.

**Remark.** The sign is the operator-level form of the anti-fixed property of the involution. The two halves are the fixed and the anti-fixed spaces of ${}^{*}$, and the same sign that distinguishes them, $\tilde Q_2^{*} = -\tilde Q_2$ against $\tilde Q_1^{*} = \tilde Q_1$, appears in the square as the sign $\pm N$. The group article records the two displays as *The Product Does Not Exchange the Halves*, and they are the exact sense in which the multiplication reads the two halves while failing to preserve them: it does not keep a product of two Hermitian elements Hermitian, but it keeps a square of either half in the centre.

## The Square-Zero Elements

### The Criterion

**Proposition (criterion).** For every biquaternion $\tilde Q$,

$$
\tilde Q \star \tilde Q = 0 \iff \overline{\tilde Q}\,\tilde Q = 0 .
$$

**Proof.** The square is $(\overline{\tilde Q}\tilde Q)^{\natural}$, and ${}^{\natural}$ is an involution and hence injective: $(\overline{\tilde Q}\tilde Q)^{\natural} = 0$ if and only if $\overline{\tilde Q}\tilde Q = 0$.

**Remark.** The criterion is the plain product $\overline{\tilde Q}\tilde Q$ and not the norm $\tilde Q\tilde Q^{*}$. The two differ: $\overline{\tilde Q}\tilde Q$ is the square read without the star, and it need not be a scalar. The square-zero condition is thus a condition on the pair $(\overline{\tilde Q},\tilde Q)$, and it is stronger than the vanishing of the norm, as the next subsections show.

### Every Square-Zero Element Has Zero Norm

**Proposition.** For every biquaternion $\tilde Q$,

$$
\boxed{\; N\bigl(\tilde Q \star \tilde Q\bigr) = \lvert \langle\tilde Q\rangle_{\natural}\rvert^{2} \;};
$$

in particular, if the square of $\tilde Q$ vanishes then $\langle\tilde Q\rangle_{\natural} = 0$.

**Proof.** The norm is multiplicative for the plain product, $\langle\tilde Q_1\tilde Q_2\rangle_{\natural} = \langle\tilde Q_1\rangle_{\natural}\langle\tilde Q_2\rangle_{\natural}$, and conjugates under the coefficientwise conjugation, $\langle\overline{\tilde Q_1}\rangle_{\natural} = \overline{\langle\tilde Q_1\rangle_{\natural}}$. Applied to $\overline{\tilde Q_2}\tilde Q_2$, whose ${}^{\natural}$-image is the square, and using the invariance of $\langle\cdot\rangle_{\natural}$ under ${}^{\natural}$,

$$
N\bigl(\tilde Q \star \tilde Q\bigr) = N\bigl(\overline{\tilde Q}\tilde Q\bigr) = \langle\overline{\tilde Q}\rangle_{\natural}\langle\tilde Q\rangle_{\natural} = \overline{\langle\tilde Q\rangle_{\natural}}\langle\tilde Q\rangle_{\natural} = \lvert \langle\tilde Q\rangle_{\natural}\rvert^{2} .
$$

The last clause is the vanishing of the left-hand side.

**Corollary.** Every square-zero element is a zero divisor, since $N = 0$ is the zero-divisor criterion of *Zero Divisors of the Biquaternion Algebra*.

### A Proper Subfamily of the Zero Divisors

The converse of the corollary fails, and this is the second of the two properties that decide the element theory of the product.

**Theorem (the square-zero set is proper).** There are elements of norm $0$ whose square in the multiplication does not vanish. The element

$$
\tilde Q = i e_t + \vec e_x + \vec e_y + i \vec e_z
$$

has $\langle\tilde Q\rangle_{\natural} = i^{2} + 1 + 1 + i^{2} = 0$ and square

$$
\tilde Q \star \tilde Q = -2e_t - 2i \vec e_x + 2i \vec e_y - 2\vec e_z \neq 0 .
$$

Hence the square-zero elements form a proper subfamily of the zero-divisor cone $\{ N = 0 \}$.

**Proof.** The norm is $\langle\tilde Q\rangle_{\natural} = \sum_\mu Q_\mu^{2} = i^{2} + 1^{2} + 1^{2} + i^{2} = -1 + 1 + 1 - 1 = 0$, so $\tilde Q$ is a zero divisor. For the square, the criterion reads $\overline{\tilde Q}\tilde Q$ with $\overline{\tilde Q} = -i e_t + \vec e_x + \vec e_y - i \vec e_z$; the plain product computed on the coordinates is $\overline{\tilde Q}\tilde Q = -2e_t + 2i \vec e_x - 2i \vec e_y + 2\vec e_z$, whose ${}^{\natural}$-image, the square, is the displayed value and does not vanish. The element is therefore a zero divisor whose square is nonzero, so the implication of the preceding corollary is not an equivalence. The scalar part of the square is $\lvert Q_t\rvert^{2} - \sum_k\lvert Q_k\rvert^{2} = 1 - (1+1+1) = -2$, in agreement with the scalar-part formula.

**Example (a square-zero element).** The element $\tilde Q = e_t + i \vec e_x$ has $\langle\tilde Q\rangle_{\natural} = 1 - 1 = 0$ and square zero: $\overline{\tilde Q} = e_t - i \vec e_x$ and $\overline{\tilde Q}\tilde Q = (e_t - i\vec e_x)(e_t + i\vec e_x) = e_t + i\vec e_x - i\vec e_x - i^{2}\vec e_x^{2} = e_t - e_t = 0$. It is a zero divisor and a square-zero element at once, and it is the simplest witness of the inclusion.

### The Comparison with the Other Products

**Theorem (the square-zero sets of the four general products).** The four general products have four different square-zero sets, and the square-zero set of the fourth is a proper subfamily of the zero-divisor cone:

| product | square-zero elements |
|---|---|
| $\tilde Q_1\tilde Q_2$ | the pure isotropic cone $\{ Q_{1t} = 0,\ (\vec Q_1,\vec Q_1) = 0 \}$, a proper subfamily of the cone |
| $\tilde Q_1^{\natural}\tilde Q_2$ | the whole zero-divisor cone $\{ \langle\tilde Q_1\rangle_{\natural} = 0 \}$ |
| $\tilde Q_1\tilde Q_2^{*}$ | only $0$ |
| $\tilde Q_1^{\natural}\tilde Q_2^{*}$ | a proper subfamily of the cone, containing $e_t + i\vec e_x$ and not $ie_t + \vec e_x + \vec e_y + i\vec e_z$ |

**Proof.** For the plain product the square is $\tilde Q_1^{2} = \bigl(Q_{1t}^{2} - (\vec Q_1,\vec Q_1)\bigr) + 2Q_{1t}\vec Q_1$, which vanishes exactly when $Q_{1t} = 0$ and $(\vec Q_1,\vec Q_1) = 0$; this is the pure isotropic cone, and it is proper because the zero-divisor cone is the larger set $Q_{1t}^{2} + (\vec Q_1,\vec Q_1) = 0$. For the sibling bilinear product the square is $\bigl(\sum_\mu Q_{1\mu}^{2}\bigr)e_t = \langle\tilde Q_1\rangle_{\natural}e_t$, which vanishes exactly on the cone. For the sibling sesquilinear product the square is $\tilde Q_1\tilde Q_1^{*}$, whose scalar part is $\sum_\mu\lvert Q_{1\mu}\rvert^{2}$, a positive sum that vanishes only at $\tilde Q_1 = 0$; so the only square-zero element is $0$. For the fourth product the two examples above exhibit the proper inclusion. The four rows are the square-zero row of *Comparison Between the Four General Products* §*The Squares, the Idempotents and the Roots*, read with the sign vector of this article.

**Remark.** The square-zero set is one of the two element problems on which the four general products genuinely differ, the other being the idempotents of *Square Roots of One and the Idempotents of the General Quaternionic Sesqualgebra*. The zero divisors themselves are the same set for all four general products, the cone $\{N = 0\}$ (*Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, being written in parallel). What this article adds is the location of the fourth product's square-zero set strictly inside that common cone, so that the fourth product detects less than the two quaternionic products and more than the two complex ones: the two bilinear products include the pure isotropic cone and the whole cone as their square-zero sets, the sibling sesquilinear product has nothing but $0$, and the fourth lies strictly between the last two.

## The Conjugation Symmetry of the Square

### The Coefficientwise Conjugation Is an Automorphism

**Proposition.** The coefficientwise conjugation is an automorphism of the multiplication,

$$
\overline{\tilde Q_1 \star \tilde Q_2} = \overline{\tilde Q_1} \star \overline{\tilde Q_2} ,
$$

for all $\tilde Q_1, \tilde Q_2$; it is $\mathbb{R}$-linear and conjugate-$\mathbb{C}$-linear, and it is the conjugation that commutes with the insertion of the rule.

**Proof.** The coefficientwise conjugation is an automorphism of the plain product, $\overline{\tilde Q_1\tilde Q_2} = \overline{\tilde Q_1}\,\overline{\tilde Q_2}$, and it commutes with both ${}^{\natural}$ and ${}^{*}$, since each of the two acts coordinatewise and the conjugation is coordinatewise; hence

$$
\overline{\tilde Q_1 \star \tilde Q_2} = \overline{\tilde Q_1^{\natural}\tilde Q_2^{*}} = \overline{\tilde Q_1^{\natural}}\,\overline{\tilde Q_2^{*}} = \overline{\tilde Q_1}^{\natural}\,\overline{\tilde Q_2}^{*} = \overline{\tilde Q_1} \star \overline{\tilde Q_2} .
$$

The parities are those of the coefficientwise conjugation.

**Remark.** The coefficientwise conjugation is the Galois action of $\mathbb{C}$ over $\mathbb{R}$, and it is the symmetry of the multiplication that is a symmetry of the sesquilinear structure: it commutes with the insertion ${}^{\natural}$ and with the involution ${}^{*}$ because it acts on each coefficient, so it carries the rule to the rule. It is the automorphism that makes the complex-linear theory of $\mathbb{B}$ reducible to the real-linear theory of the quaternion algebra, and every complex statement of this article has a conjugate counterpart under it. The two other conjugations are not automorphisms of the multiplication: they insert their sign in one slot and not in the other, and the two sides of the identity $\natural(\tilde Q_1\star\tilde Q_2) = \natural(\tilde Q_1)\star\natural(\tilde Q_2)$ then differ on general elements.

### The Invariant Subsets

**Corollary.** The coefficientwise conjugation preserves the square-zero set and the set of idempotents.

**Proof.** The square-zero set is $\{\tilde Q : \tilde Q\star\tilde Q = 0\}$; if $\tilde Q$ is in it, then $\overline{\tilde Q}\star\overline{\tilde Q} = \overline{\tilde Q\star\tilde Q} = 0$ by the proposition, so $\overline{\tilde Q}$ is in it too. The idempotent condition is $\tilde\Pi\star\tilde\Pi = \tilde\Pi$; conjugating both sides gives $\overline{\tilde\Pi}\star\overline{\tilde\Pi} = \overline{\tilde\Pi}$, so the conjugate is again an idempotent.

**Remark.** The idempotent statement is the one the group uses: the nontrivial idempotents $\tilde\Pi(\vec u) = -\tfrac12e_t+\tfrac{\sqrt3}{2}\vec u$ with $\vec u$ in the real vector subspace of norm $\tfrac34$ are carried by the coefficientwise conjugation to the idempotents $\tilde\Pi(\vec u)$ with the same $\vec u$, because $\vec u$ has real coordinates and the conjugation fixes it; the two *other* conjugations change the sign of $\vec u$ and reach $\tilde\Pi(-\vec u)$, which is again an idempotent. The square-zero statement is what lets the witness $ie_t + \vec e_x + \vec e_y + i\vec e_z$ of the proper-inclusion theorem be replaced by its conjugate; both are zero divisors and both have nonzero square.

## The Squares of the Idempotents

**Proposition (the square of an idempotent).** Let $\tilde\Pi$ be an idempotent of the multiplication, so that $\tilde\Pi \star \tilde\Pi = \tilde\Pi$. Then $\overline{\tilde\Pi}\tilde\Pi = \tilde\Pi^{\natural}$, and the plain square of $\tilde\Pi$ is $\tilde\Pi^{2} = \tilde\Pi^{\natural}$.

**Proof.** The criterion of idempotence is $\overline{\tilde\Pi}\tilde\Pi = \tilde\Pi^{\natural}$ (*Square Roots of One and the Idempotents of the General Quaternionic Sesqualgebra*), which is the first statement. Applying ${}^{\natural}$ to the definition and using the criterion, or expanding $\tilde\Pi^{2}$ on the coordinates, gives the plain square: for a nontrivial idempotent $\tilde\Pi(\vec u) = -\tfrac12e_t+\tfrac{\sqrt3}{2}\vec u$ with $(\vec u,\vec u)=1$,

$$
\tilde\Pi^{2} = \Bigl(\tfrac14 - \tfrac34\Bigr)e_t + 2\cdot\Bigl(-\tfrac12\Bigr)\vec u = -\tfrac12 e_t - \tfrac{\sqrt3}{2}\vec u = \tilde\Pi^{\natural} ,
$$

the vector part being $\vec u$.

**Remark.** The example is the one the idempotents of the family supply. Along the three coordinate axes the idempotents are $\tilde\Pi = -\tfrac12 e_t + \tfrac{\sqrt3}{2}\vec u$ with $\vec u \in \{\pm \vec e_x, \pm \vec e_y, \pm \vec e_z\}$, and each has plain square $\tilde\Pi^{\natural} = -\tfrac12 e_t - \tfrac{\sqrt3}{2}\vec u$ and square in the multiplication $\tilde\Pi$ itself. The scalar part of the square is $\lvert-\tfrac12\rvert^{2} - \tfrac34 = -\tfrac12$, the scalar coordinate of the idempotent, in agreement with the scalar-part formula, and it is negative, which is why the family of idempotents is not the positive cone of the sibling product.

## Summary

The square of the general quaternionic sesquilinear multiplication is $\tilde Q \star \tilde Q = (\overline{\tilde Q}\tilde Q)^{\natural} = \tilde Q^{\natural}\tilde Q^{*}$, an element with scalar part $\sum_\mu\varepsilon_\mu Q_\mu\overline{Q_\mu} = \lvert Q_t\rvert^{2} - \lvert Q_x\rvert^{2} - \lvert Q_y\rvert^{2} - \lvert Q_z\rvert^{2}$, the Krein form of signature $(2,2)$, and vector part $-(\overline{Q_t}\vec Q + Q_t\overline{\vec Q} + \overline{\vec Q}\times\vec Q)$. On the two halves the square collapses to the centre with the sign of the half, $\tilde Q_1 \star \tilde Q_1 = \langle\tilde Q_1\rangle_{\natural}e_t$ on $\mathbb{M}_{+}$ and $\tilde Q_2 \star \tilde Q_2 = -\langle\tilde Q_2\rangle_{\natural}e_t$ on $\mathbb{M}_{-}$, so that the multiplication reads the Hermitian splitting by a sign although it does not preserve it. The square-zero elements are the solutions of $\overline{\tilde Q}\tilde Q = 0$; every one of them has norm $0$, since $\langle\tilde Q \star \tilde Q\rangle_{\natural} = \lvert \langle\tilde Q\rangle_{\natural}\rvert^{2}$, and the converse fails, the element $ie_t + \vec e_x + \vec e_y + i\vec e_z$ being a zero divisor whose square is nonzero while $e_t + i\vec e_x$ is square-zero. The square-zero set of the product is therefore a proper subfamily of the common zero-divisor cone, placed strictly between the empty set of the sibling sesquilinear product and the whole cone of the sibling general quaternionic bilinear product. The squares of the idempotents return the idempotents, and their plain squares are their natural conjugates. The coefficientwise conjugation is an automorphism of the multiplication, $\overline{\tilde Q_1 \star \tilde Q_2} = \overline{\tilde Q_1} \star \overline{\tilde Q_2}$, so it preserves the square-zero set and the set of idempotents and reduces the complex theory to the real one; the two other conjugations are not automorphisms of the multiplication.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde Q \star \tilde Q = (\overline{\tilde Q}\tilde Q)^{\natural} = \tilde Q^{\natural}\tilde Q^{*}$ | the square |
| $\mathrm{Sc}(\tilde Q \star \tilde Q) = \sum_\mu\varepsilon_\mu Q_\mu\overline{Q_\mu}$ | the scalar part of the square |
| $\varepsilon = (1,-1,-1,-1)$ | the sign vector of the product |
| $\kappa(\tilde Q_1,\tilde Q_2) = \sum_\mu\varepsilon_\mu Q_{1\mu}\overline{Q_{2\mu}}$ | the Krein form, the scalar part of the product |
| $\mathrm{Vec}(\tilde Q \star \tilde Q) = -\mathrm{Vec}(\overline{\tilde Q}\tilde Q)$ | the vector part of the square |
| $\tilde Q_1 \star \tilde Q_1 = \langle\tilde Q_1\rangle_{\natural}e_t$ | the square on $\mathbb{M}_{+}$ |
| $\tilde Q_2 \star \tilde Q_2 = -\langle\tilde Q_2\rangle_{\natural}e_t$ | the square on $\mathbb{M}_{-}$ |
| $\tilde Q \star \tilde Q = 0 \iff \overline{\tilde Q}\tilde Q = 0$ | the square-zero criterion |
| $\langle\tilde Q \star \tilde Q\rangle_{\natural} = \lvert \langle\tilde Q\rangle_{\natural}\rvert^{2}$ | the norm of a square |
| $\tilde Q = ie_t + \vec e_x + \vec e_y + i\vec e_z$ | a zero divisor that is not square-zero |
| $\tilde Q = e_t + i\vec e_x$ | a square-zero element |
| $\overline{\tilde Q_1 \star \tilde Q_2} = \overline{\tilde Q_1} \star \overline{\tilde Q_2}$ | the coefficientwise conjugation is an automorphism of the multiplication |
| $\tilde\Pi^{2} = \tilde\Pi^{\natural}$ | the plain square of an idempotent |

## Further Reading

- Nicolas Bourbaki, *Algebra I, Chapters 1–3* (Springer, 1998), for the square, the associator and the polarisation of a multiplication on a module.
- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the fixed and anti-fixed spaces of an involution and the symmetric elements.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the idempotent and the square in an algebra with an involution.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the Hermitian and the skew-Hermitian elements attached to an involution and the forms they define.
