
# __The Square of the Quaternionic Sesquilinear Product and the Two Halves__

## Introduction

The biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ carries four products on its underlying $\mathbb{C}$-vector space (*The Four Biquaternion Complex Products*), and the fourth of them,

$$
\tilde P \star \tilde Q = \tilde P^{\natural}\tilde Q^{*} ,
$$

is the subject of this group. The rule and the scalar–vector form are *The Four Biquaternion Complex Products* §*The Complex Quaternionic Sesquilinear Product*; the sesquialgebra it defines and the two actions of the unit are *Biquaternions as a Quaternionic Sesquialgebra over $\mathbb{C}$*. The symbols are those of the group: ${}^{\natural}$ is the natural conjugation $\tilde P^{\natural} = P_0 - \mathbf P$, ${}^{*}$ is the star conjugation $\tilde P^{*} = \overline{P_0} - \overline{\mathbf Q}$, the bar is the coefficientwise complex conjugation, and $N(\tilde P) = \tilde P\tilde P^{\natural} = \sum_\mu P_\mu^{2}$ is the norm form.

The subject of this article is the **square** of the multiplication on a single element, $\tilde Q \star \tilde Q$, and its reading on the two halves of the algebra. The square is the computation every later article of the group uses: it is the equation of the idempotents of *Idempotents of the Quaternionic Sesquilinear Product*, it is the residue of the associator of *The Associator of the Quaternionic Sesquilinear Product*, and it is the value the operators of *The Left and Right Multiplications of the Quaternionic Sesquilinear Product* reproduce. The article establishes three things. First, the square has the closed form

$$
\tilde Q \star \tilde Q = \bigl(\overline{\tilde Q}\tilde Q\bigr)^{\natural} = \tilde Q^{\natural}\tilde Q^{*} ,
$$

with scalar part $\sum_\mu \varepsilon_\mu Q_\mu\overline{Q_\mu} = \lvert Q_0\rvert^{2} - \lvert Q_1\rvert^{2} - \lvert Q_2\rvert^{2} - \lvert Q_3\rvert^{2}$, an indefinite form of signature $(2,2)$. Second, on the two halves $\mathbb{M}_{+}$ and $\mathbb{M}_{-}$ the square collapses to the centre with opposite signs, $\tilde Q \star \tilde Q = \pm N(\tilde Q)e_0$, the sign being that of the half. Third, the elements whose square vanishes form a **proper** subfamily of the zero-divisor cone: every square-zero element has norm $0$, and not every element of norm $0$ has square zero, a fact that separates this product from both bilinear products.

The article owns the square, its scalar part, its behaviour on the two halves and the square-zero set. It cites the rule and the four scalar parts to *The Four Biquaternion Complex Products* and *Relations Between the Four Biquaternion Products* §*The Four Scalar Parts*; it cites the two halves and their definition to *Introduction to the Six Subspaces*, *Decompositions Along the Six Subspaces* and *Hermitian and Skew-Hermitian Elements*; it cites the zero-divisor criterion to *Biquaternion Zero Divisors*; and it does not treat the idempotents, which are *Idempotents of the Quaternionic Sesquilinear Product*, nor the operators, which are *The Left and Right Multiplications of the Quaternionic Sesquilinear Product*.

## The Square of an Element

### The Rule

**Proposition (the square).** For every biquaternion $\tilde Q$,

$$
\tilde Q \star \tilde Q = \bigl(\overline{\tilde Q}\tilde Q\bigr)^{\natural} = \tilde Q^{\natural}\tilde Q^{*} .
$$

**Proof.** The second expression is the rule at equal arguments. For the first, the natural conjugation is an anti-automorphism of the plain product and the two conjugations commute, so $\bigl(\overline{\tilde Q}\tilde Q\bigr)^{\natural} = \tilde Q^{\natural}\bigl(\overline{\tilde Q}\bigr)^{\natural} = \tilde Q^{\natural}\tilde Q^{*}$, since $\bigl(\overline{\tilde Q}\bigr)^{\natural} = \overline{\tilde Q^{\natural}} = \tilde Q^{*}$. $\square$

**Caution (the two squares).** The square of this multiplication is not the plain square $\tilde Q\tilde Q = \tilde Q^{2}$, nor the square of the sibling bilinear product $\tilde Q^{\natural}\tilde Q = \bigl(\sum_\mu Q_\mu^{2}\bigr)e_0$. The three are different elements of $\mathbb{B}$, and their agreement is exceptional (*Biquaternions as a Quaternionic Sesquialgebra over $\mathbb{C}$*, §*The Square, the Idempotents and the Ternary Product*; *Biquaternions as a Quaternionic Algebra over $\mathbb{C}$*, §*The Square and the Elements It Distinguishes*). The plain square and the square of the sibling bilinear product are the two other elements built from the element and its two conjugations, and the comparison of the four squares is *Comparison Between the Four Biquaternion Products* §*The Squares, the Idempotents and the Roots*.

### The Scalar Part

**Proposition (the scalar part of the square).** For every biquaternion $\tilde Q$,

$$
\mathrm{Sc}\bigl(\tilde Q \star \tilde Q\bigr) = \sum_{\mu=0}^{3}\varepsilon_\mu Q_\mu\overline{Q_\mu} = \lvert Q_0\rvert^{2} - \lvert Q_1\rvert^{2} - \lvert Q_2\rvert^{2} - \lvert Q_3\rvert^{2} , \qquad \varepsilon = (1,-1,-1,-1) .
$$

**Proof.** The scalar part of the square is the scalar part of $\tilde Q^{\natural}\tilde Q^{*}$. On the coordinates, $\bigl(\tilde Q^{\natural}\bigr)_\mu = \varepsilon_\mu Q_\mu$ and $\bigl(\tilde Q^{*}\bigr)_\mu = \varepsilon_\mu\overline{Q_\mu}$, and the scalar part of the plain product is the signed diagonal pairing $\sum_\mu \varepsilon_\mu(\tilde Q^{\natural})_\mu(\tilde Q^{*})_\mu = \sum_\mu \varepsilon_\mu^{3} Q_\mu\overline{Q_\mu} = \sum_\mu\varepsilon_\mu Q_\mu\overline{Q_\mu}$, since $\varepsilon_\mu^{3} = \varepsilon_\mu$. The second display is the definition of the sign vector. $\square$

**Remark.** The scalar part is the **Krein form** of the four coordinates: a nondegenerate form of signature $(2,2)$, positive on the scalar coordinate and negative on the three vector coordinates. It is the first of the two properties that decide the element theory of the product, and it is what makes the square-zero problem different from the zero-divisor problem. The same form is the scalar part of the product off the diagonal, $\mathrm{Sc}(\tilde P\star\tilde Q) = \sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$, which is *The Four Biquaternion Complex Products* read with the two signs, and it is the fourth of the four scalar parts of *Relations Between the Four Biquaternion Products* §*The Four Scalar Parts*.

### The Vector Part

**Proposition (the vector part of the square).** For every biquaternion $\tilde Q$,

$$
\mathrm{Vec}\bigl(\tilde Q \star \tilde Q\bigr) = -\Bigl(\overline{Q_0}\,\mathbf Q + Q_0\,\overline{\mathbf Q} + \overline{\mathbf Q}\times\mathbf Q\Bigr) ,
$$

the dot and cross products being the complex bilinear ones.

**Proof.** The square is the ${}^{\natural}$-image of $\overline{\tilde Q}\tilde Q$, and ${}^{\natural}$ fixes the scalar coordinate and negates the vector coordinate; hence $\mathrm{Vec}\bigl(\tilde Q\star\tilde Q\bigr) = -\mathrm{Vec}\bigl(\overline{\tilde Q}\tilde Q\bigr)$. The vector part of the plain product $\overline{\tilde Q}\tilde Q$ is $\overline{Q_0}\mathbf Q + Q_0\overline{\mathbf Q} + \overline{\mathbf Q}\times\mathbf Q$ by the scalar–vector form of *The Four Biquaternion Complex Products*, with the first factor $\tilde P = \overline{\tilde Q}$ of scalar part $\overline{Q_0}$ and vector part $\overline{\mathbf Q}$. $\square$

**Remark.** The vector part is the reason the square is not generally an element of the Hermitian subspace. The scalar part is real, being a sum of moduli with signs, but the vector part is a general complex vector and it is not the imaginary multiple of a real vector; the square can be Hermitian, as for $\tilde Q = e_1 + ie_2$ where it is $-2e_0 - 2ie_3$, but it need not be, and the element $\tilde Q = e_0 + e_3$ is a witness: its square is $-2e_3$, whose star is $+2e_3$ and whose natural conjugate is $+2e_3$, neither equal to the square. This is the contrast with the sibling sesquilinear product, whose square $\tilde P\tilde P^{*}$ is Hermitian for every element by the identity $(\tilde P\tilde P^{*})^{*} = \tilde P\tilde P^{*}$.

## The Two Halves

### The Square on the Hermitian Half

**Proposition.** For $\tilde P \in \mathbb{M}_{+}$,

$$
\tilde P \star \tilde P = N(\tilde P)\, e_0 ,
$$

a real scalar; the square lies in the centre and is fixed by both conjugations.

**Proof.** Let $\tilde P \in \mathbb{M}_{+}$, so that $\tilde P^{*} = \tilde P$ and the scalar coordinate $P_0$ is real while the vector coordinates $P_k$ are purely imaginary; then $\overline{\tilde P} = \tilde P^{\natural}$. The square is $\tilde P^{\natural}\tilde P^{*} = \tilde P^{\natural}\tilde P$, and the $\natural$-product of an element with its natural conjugate is the central scalar $\tilde P^{\natural}\tilde P = \bigl(\sum_\mu P_\mu^{2}\bigr)e_0 = N(\tilde P)e_0$ (*Biquaternions as a Quaternionic Algebra over $\mathbb{C}$* §*The Square and the Elements It Distinguishes*). $\square$

### The Square on the Anti-Hermitian Half

**Proposition.** For $\tilde K \in \mathbb{M}_{-}$,

$$
\tilde K \star \tilde K = -N(\tilde K)\, e_0 ,
$$

a real scalar; in particular the square is the negative of the central scalar of the Hermitian case.

**Proof.** Let $\tilde K \in \mathbb{M}_{-}$, so that $\tilde K^{*} = -\tilde K$ and the scalar coordinate is purely imaginary while the vector coordinates are real; then $\overline{\tilde K} = -\tilde K^{\natural}$. The square is $\tilde K^{\natural}\tilde K^{*} = -\tilde K^{\natural}\tilde K = -\bigl(\sum_\mu K_\mu^{2}\bigr)e_0 = -N(\tilde K)e_0$, by the same central-scalar identity. $\square$

### The Sign of the Half

**Corollary.** The square on the two halves is the central scalar with the sign of the half,

$$
\tilde P \star \tilde P = N(\tilde P)e_0 \ \ (\tilde P \in \mathbb{M}_{+}) , \qquad \tilde K \star \tilde K = -N(\tilde K)e_0 \ \ (\tilde K \in \mathbb{M}_{-}) ,
$$

so that the multiplication reads the splitting $\mathbb{B} = \mathbb{M}_{+} \oplus \mathbb{M}_{-}$ by the sign.

**Proof.** The two displays are the two propositions. The splitting is the order-two property of the involution ${}^{*}$, which is *Hermitian and Skew-Hermitian Elements*; the multiplication does not preserve the splitting, but on a multiple of a single half its square is the central scalar with the sign of that half. $\square$

**Remark.** The sign is the operator-level form of the anti-fixed property of the involution. The two halves are the fixed and the anti-fixed spaces of ${}^{*}$, and the same sign that distinguishes them, $\tilde K^{*} = -\tilde K$ against $\tilde P^{*} = \tilde P$, appears in the square as the sign $\pm N$. The group article records the two displays as *The Product Does Not Exchange the Halves*, and they are the exact sense in which the multiplication reads the two halves while failing to preserve them: it does not keep a product of two Hermitian elements Hermitian, but it keeps a square of either half in the centre.

## The Square-Zero Elements

### The Criterion

**Proposition (criterion).** For every biquaternion $\tilde Q$,

$$
\tilde Q \star \tilde Q = 0 \iff \overline{\tilde Q}\,\tilde Q = 0 .
$$

**Proof.** The square is $(\overline{\tilde Q}\tilde Q)^{\natural}$, and ${}^{\natural}$ is an involution and hence injective: $(\overline{\tilde Q}\tilde Q)^{\natural} = 0$ if and only if $\overline{\tilde Q}\tilde Q = 0$. $\square$

**Remark.** The criterion is the plain product $\overline{\tilde Q}\tilde Q$ and not the norm $\tilde Q\tilde Q^{*}$. The two differ: $\overline{\tilde Q}\tilde Q$ is the square read without the star, and it need not be a scalar. The square-zero condition is thus a condition on the pair $(\overline{\tilde Q},\tilde Q)$, and it is stronger than the vanishing of the norm, as the next subsections show.

### Every Square-Zero Element Has Zero Norm

**Proposition.** For every biquaternion $\tilde Q$,

$$
N\bigl(\tilde Q \star \tilde Q\bigr) = \lvert N(\tilde Q)\rvert^{2} ;
$$

in particular, if the square of $\tilde Q$ vanishes then $N(\tilde Q) = 0$.

**Proof.** The norm is multiplicative for the plain product, $N(\tilde P\tilde Q) = N(\tilde P)N(\tilde Q)$, and conjugates under the coefficientwise conjugation, $N(\overline{\tilde P}) = \overline{N(\tilde P)}$. Applied to $\overline{\tilde Q}\tilde Q$, whose ${}^{\natural}$-image is the square, and using the invariance of $N$ under ${}^{\natural}$,

$$
N\bigl(\tilde Q \star \tilde Q\bigr) = N\bigl(\overline{\tilde Q}\tilde Q\bigr) = N(\overline{\tilde Q})N(\tilde Q) = \overline{N(\tilde Q)}N(\tilde Q) = \lvert N(\tilde Q)\rvert^{2} .
$$

The last clause is the vanishing of the left-hand side. $\square$

**Corollary.** Every square-zero element is a zero divisor, since $N = 0$ is the zero-divisor criterion of *Biquaternion Zero Divisors*.

### A Proper Subfamily of the Zero Divisors

The converse of the corollary fails, and this is the second of the two properties that decide the element theory of the product.

**Theorem (the square-zero set is proper).** There are elements of norm $0$ whose square in the multiplication does not vanish. The element

$$
\tilde Q = i e_0 + e_1 + e_2 + i e_3
$$

has $N(\tilde Q) = i^{2} + 1 + 1 + i^{2} = 0$ and square

$$
\tilde Q \star \tilde Q = -2e_0 - 2i e_1 + 2i e_2 - 2e_3 \neq 0 .
$$

Hence the square-zero elements form a proper subfamily of the zero-divisor cone $\{ N = 0 \}$.

**Proof.** The norm is $N(\tilde Q) = \sum_\mu Q_\mu^{2} = i^{2} + 1^{2} + 1^{2} + i^{2} = -1 + 1 + 1 - 1 = 0$, so $\tilde Q$ is a zero divisor. For the square, the criterion reads $\overline{\tilde Q}\tilde Q$ with $\overline{\tilde Q} = -i e_0 + e_1 + e_2 - i e_3$; the plain product computed on the coordinates is $\overline{\tilde Q}\tilde Q = -2e_0 + 2i e_1 - 2i e_2 + 2e_3$, whose ${}^{\natural}$-image, the square, is the displayed value and does not vanish. The element is therefore a zero divisor whose square is nonzero, so the implication of the preceding corollary is not an equivalence. The scalar part of the square is $\lvert Q_0\rvert^{2} - \sum_k\lvert Q_k\rvert^{2} = 1 - (1+1+1) = -2$, in agreement with the scalar-part formula. $\square$

**Example (a square-zero element).** The element $\tilde Q = e_0 + i e_1$ has $N(\tilde Q) = 1 - 1 = 0$ and square zero: $\overline{\tilde Q} = e_0 - i e_1$ and $\overline{\tilde Q}\tilde Q = (e_0 - ie_1)(e_0 + ie_1) = e_0 + ie_1 - ie_1 - i^{2}e_1^{2} = e_0 - e_0 = 0$. It is a zero divisor and a square-zero element at once, and it is the simplest witness of the inclusion.

### The Comparison with the Other Products

**Theorem (the square-zero sets of the four products).** The four products have four different square-zero sets, and the square-zero set of the fourth is a proper subfamily of the zero-divisor cone:

| product | square-zero elements |
|---|---|
| $\tilde P\tilde Q$ | the pure isotropic cone $\{ P_0 = 0,\ (\mathbf P,\mathbf P) = 0 \}$, a proper subfamily of the cone |
| $\tilde P^{\natural}\tilde Q$ | the whole zero-divisor cone $\{ N(\tilde P) = 0 \}$ |
| $\tilde P\tilde Q^{*}$ | only $0$ |
| $\tilde P^{\natural}\tilde Q^{*}$ | a proper subfamily of the cone, containing $e_0 + ie_1$ and not $ie_0 + e_1 + e_2 + ie_3$ |

**Proof.** For the plain product the square is $\tilde P^{2} = \bigl(P_0^{2} - (\mathbf P,\mathbf P)\bigr) + 2P_0\mathbf P$, which vanishes exactly when $P_0 = 0$ and $(\mathbf P,\mathbf P) = 0$; this is the pure isotropic cone, and it is proper because the zero-divisor cone is the larger set $P_0^{2} + (\mathbf P,\mathbf P) = 0$. For the sibling bilinear product the square is $\bigl(\sum_\mu P_\mu^{2}\bigr)e_0 = N(\tilde P)e_0$, which vanishes exactly on the cone. For the sibling sesquilinear product the square is $\tilde P\tilde P^{*}$, whose scalar part is $\sum_\mu\lvert P_\mu\rvert^{2}$, a positive sum that vanishes only at $\tilde P = 0$; so the only square-zero element is $0$. For the fourth product the two examples above exhibit the proper inclusion. The four rows are the square-zero row of *Comparison Between the Four Biquaternion Products* §*The Squares, the Idempotents and the Roots*, read with the sign vector of this article. $\square$

**Remark.** The square-zero set is one of the two element problems on which the four products genuinely differ, the other being the idempotents of *Idempotents of the Quaternionic Sesquilinear Product*. The zero divisors themselves are the same set for all four products, the cone $\{N = 0\}$ (*The Annihilating Elements of the Four Products*, being written in parallel). What this article adds is the location of the fourth product's square-zero set strictly inside that common cone, so that the fourth product detects less than the two quaternionic products and more than the two complex ones: the two bilinear products include the pure isotropic cone and the whole cone as their square-zero sets, the sibling sesquilinear product has nothing but $0$, and the fourth lies strictly between the last two.

## The Conjugation Symmetry of the Square

### The Coefficientwise Conjugation Is an Automorphism

**Proposition.** The coefficientwise conjugation is an automorphism of the multiplication,

$$
\overline{\tilde P \star \tilde Q} = \overline{\tilde P} \star \overline{\tilde Q} ,
$$

for all $\tilde P, \tilde Q$; it is $\mathbb{R}$-linear and conjugate-$\mathbb{C}$-linear, and it is the conjugation that commutes with the insertion of the rule.

**Proof.** The coefficientwise conjugation is an automorphism of the plain product, $\overline{\tilde P\tilde Q} = \overline{\tilde P}\,\overline{\tilde Q}$, and it commutes with both ${}^{\natural}$ and ${}^{*}$, since each of the two acts coordinatewise and the conjugation is coordinatewise; hence

$$
\overline{\tilde P \star \tilde Q} = \overline{\tilde P^{\natural}\tilde Q^{*}} = \overline{\tilde P^{\natural}}\,\overline{\tilde Q^{*}} = \overline{\tilde P}^{\natural}\,\overline{\tilde Q}^{*} = \overline{\tilde P} \star \overline{\tilde Q} .
$$

The parities are those of the coefficientwise conjugation. $\square$

**Remark.** The coefficientwise conjugation is the Galois action of $\mathbb{C}$ over $\mathbb{R}$, and it is the symmetry of the multiplication that is a symmetry of the sesquilinear structure: it commutes with the insertion ${}^{\natural}$ and with the involution ${}^{*}$ because it acts on each coefficient, so it carries the rule to the rule. It is the automorphism that makes the complex-linear theory of $\mathbb{B}$ reducible to the real-linear theory of the quaternion algebra, and every complex statement of this article has a conjugate counterpart under it. The two other conjugations are not automorphisms of the multiplication: they insert their sign in one slot and not in the other, and the two sides of the identity $\natural(\tilde P\star\tilde Q) = \natural(\tilde P)\star\natural(\tilde Q)$ then differ on general elements.

### The Invariant Subsets

**Corollary.** The coefficientwise conjugation preserves the square-zero set and the set of idempotents.

**Proof.** The square-zero set is $\{\tilde Q : \tilde Q\star\tilde Q = 0\}$; if $\tilde Q$ is in it, then $\overline{\tilde Q}\star\overline{\tilde Q} = \overline{\tilde Q\star\tilde Q} = 0$ by the proposition, so $\overline{\tilde Q}$ is in it too. The idempotent condition is $\tilde\Pi\star\tilde\Pi = \tilde\Pi$; conjugating both sides gives $\overline{\tilde\Pi}\star\overline{\tilde\Pi} = \overline{\tilde\Pi}$, so the conjugate is again an idempotent. $\square$

**Remark.** The idempotent statement is the one the group uses: the nontrivial idempotents $\tilde\Pi(\mu) = -\tfrac12 e_0 + \mu$ with $\mu$ in the real vector subspace of norm $\tfrac34$ are carried by the coefficientwise conjugation to the idempotents $\tilde\Pi(\mu)$ with the same $\mu$, because $\mu$ has real coordinates and the conjugation fixes it; the two *other* conjugations change the sign of $\mu$ and reach $\tilde\Pi(-\mu)$, which is again an idempotent. The square-zero statement is what lets the witness $ie_0 + e_1 + e_2 + ie_3$ of the proper-inclusion theorem be replaced by its conjugate; both are zero divisors and both have nonzero square.

## The Squares of the Idempotents

**Proposition (the square of an idempotent).** Let $\tilde\Pi$ be an idempotent of the multiplication, so that $\tilde\Pi \star \tilde\Pi = \tilde\Pi$. Then $\overline{\tilde\Pi}\tilde\Pi = \tilde\Pi^{\natural}$, and the plain square of $\tilde\Pi$ is $\tilde\Pi^{2} = \tilde\Pi^{\natural}$.

**Proof.** The criterion of idempotence is $\overline{\tilde\Pi}\tilde\Pi = \tilde\Pi^{\natural}$ (*Idempotents of the Quaternionic Sesquilinear Product*), which is the first statement. Applying ${}^{\natural}$ to the definition and using the criterion, or expanding $\tilde\Pi^{2}$ on the coordinates, gives the plain square: for a nontrivial idempotent $\tilde\Pi(\mu) = -\tfrac12 e_0 + \mu$ with $(\mu,\mu) = \tfrac34$,

$$
\tilde\Pi^{2} = \Bigl(\tfrac14 - \tfrac34\Bigr)e_0 + 2\cdot\Bigl(-\tfrac12\Bigr)\mu = -\tfrac12 e_0 - \mu = \tilde\Pi^{\natural} ,
$$

the vector part being $\mu$. $\square$

**Remark.** The example is the one the idempotents of the sphere supply. Along the three coordinate axes the idempotents are $\tilde\Pi = -\tfrac12 e_0 + \tfrac{\sqrt3}{2}\hat\mu$ with $\hat\mu \in \{\pm e_1, \pm e_2, \pm e_3\}$, and each has plain square $\tilde\Pi^{\natural} = -\tfrac12 e_0 - \tfrac{\sqrt3}{2}\hat\mu$ and square in the multiplication $\tilde\Pi$ itself. The scalar part of the square is $\lvert-\tfrac12\rvert^{2} - \tfrac34 = -\tfrac12$, the scalar coordinate of the idempotent, in agreement with the scalar-part formula, and it is negative, which is why the sphere of idempotents is not the positive cone of the sibling product.

## Summary

The square of the complex quaternionic sesquilinear multiplication is $\tilde Q \star \tilde Q = (\overline{\tilde Q}\tilde Q)^{\natural} = \tilde Q^{\natural}\tilde Q^{*}$, an element with scalar part $\sum_\mu\varepsilon_\mu Q_\mu\overline{Q_\mu} = \lvert Q_0\rvert^{2} - \lvert Q_1\rvert^{2} - \lvert Q_2\rvert^{2} - \lvert Q_3\rvert^{2}$, the Krein form of signature $(2,2)$, and vector part $-(\overline{Q_0}\mathbf Q + Q_0\overline{\mathbf Q} + \overline{\mathbf Q}\times\mathbf Q)$. On the two halves the square collapses to the centre with the sign of the half, $\tilde P \star \tilde P = N(\tilde P)e_0$ on $\mathbb{M}_{+}$ and $\tilde K \star \tilde K = -N(\tilde K)e_0$ on $\mathbb{M}_{-}$, so that the multiplication reads the Hermitian splitting by a sign although it does not preserve it. The square-zero elements are the solutions of $\overline{\tilde Q}\tilde Q = 0$; every one of them has norm $0$, since $N(\tilde Q \star \tilde Q) = \lvert N(\tilde Q)\rvert^{2}$, and the converse fails, the element $ie_0 + e_1 + e_2 + ie_3$ being a zero divisor whose square is nonzero while $e_0 + ie_1$ is square-zero. The square-zero set of the product is therefore a proper subfamily of the common zero-divisor cone, placed strictly between the empty set of the sibling sesquilinear product and the whole cone of the sibling quaternionic bilinear product. The squares of the idempotents return the idempotents, and their plain squares are their natural conjugates. The coefficientwise conjugation is an automorphism of the multiplication, $\overline{\tilde P \star \tilde Q} = \overline{\tilde P} \star \overline{\tilde Q}$, so it preserves the square-zero set and the set of idempotents and reduces the complex theory to the real one; the two other conjugations are not automorphisms of the multiplication.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde Q \star \tilde Q = (\overline{\tilde Q}\tilde Q)^{\natural} = \tilde Q^{\natural}\tilde Q^{*}$ | the square |
| $\mathrm{Sc}(\tilde Q \star \tilde Q) = \sum_\mu\varepsilon_\mu Q_\mu\overline{Q_\mu}$ | the scalar part of the square |
| $\varepsilon = (1,-1,-1,-1)$ | the sign vector of the product |
| $\kappa(\tilde P,\tilde Q) = \sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ | the Krein form, the scalar part of the product |
| $\mathrm{Vec}(\tilde Q \star \tilde Q) = -\mathrm{Vec}(\overline{\tilde Q}\tilde Q)$ | the vector part of the square |
| $\tilde P \star \tilde P = N(\tilde P)e_0$ | the square on $\mathbb{M}_{+}$ |
| $\tilde K \star \tilde K = -N(\tilde K)e_0$ | the square on $\mathbb{M}_{-}$ |
| $\tilde Q \star \tilde Q = 0 \iff \overline{\tilde Q}\tilde Q = 0$ | the square-zero criterion |
| $N(\tilde Q \star \tilde Q) = \lvert N(\tilde Q)\rvert^{2}$ | the norm of a square |
| $\tilde Q = ie_0 + e_1 + e_2 + ie_3$ | a zero divisor that is not square-zero |
| $\tilde Q = e_0 + ie_1$ | a square-zero element |
| $\overline{\tilde P \star \tilde Q} = \overline{\tilde P} \star \overline{\tilde Q}$ | the coefficientwise conjugation is an automorphism of the multiplication |
| $\tilde\Pi^{2} = \tilde\Pi^{\natural}$ | the plain square of an idempotent |

## Further Reading

- Nicolas Bourbaki, *Algebra I, Chapters 1–3* (Springer, 1998), for the square, the associator and the polarisation of a multiplication on a module.
- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the fixed and anti-fixed spaces of an involution and the symmetric elements.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the idempotent and the square in an algebra with an involution.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the Hermitian and the skew-Hermitian elements attached to an involution and the forms they define.
