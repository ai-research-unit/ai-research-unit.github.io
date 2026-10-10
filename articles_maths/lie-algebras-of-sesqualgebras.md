# __Lie Algebras of Sesqualgebras__

## Introduction

A bilinear product carries a Lie algebra in its antisymmetrisation: the bracket $[x,y] = \tfrac12(xy - yx)$ is anticommutative and satisfies the Jacobi identity, and the compatibility of that bracket with the symmetrisation is the Lie–Jordan decomposition of *The Lie–Jordan Decomposition of a Bilinear Product and the Jordan Triple System*. A sesquilinear product is bilinear in one slot and conjugate-linear in the other, and the question of this article is what becomes of that construction. The answer has three parts, and the first of them is negative.

The antisymmetrisation of a sesquilinear product is not a Lie bracket. It is antisymmetric, and it is linear over the fixed ring rather than over $R$: the antisymmetrisation of a sesquilinear product is a *bilinear* bracket, so the most it can be is a Lie algebra over $R^{\varsigma}$, and it is never a Lie sesqualgebra; and the Jacobi identity fails, with a witness in $M_{2}(\mathbb{C})$ that uses two Hermitian idempotents and one matrix unit. This is §*The Two Halves and the Obstruction*. The Lie structure that a sesqualgebra does carry comes instead from its *associative* product: the commutator $xy - yx$ makes $A$ a Lie algebra over $R$, the involution makes that Lie algebra $\mathbb{Z}/2$-graded with even part the skew-Hermitian elements and odd part the Hermitian ones, and the skew-Hermitian part is a Lie subalgebra, over the fixed ring. This is §*The Commutator Lie Algebra*, and the inner derivations attached to it are *Derivations of a Sesqualgebra*, §*The Inner Derivations*. What survives on the whole space, when the binary structure is unavailable, is ternary: the Lie triple system $[[x,y],z]$, which satisfies its three identities whatever the involution does. This is §*The Ternary Companion*.

The companion article is *Jordan Algebras of Sesqualgebras*. The two are the sesquilinear counterparts of the two halves of the bilinear decomposition; they share their framing, that the binary structure lives on one half of the algebra over the fixed ring, and they are read together. The setting is that of *Sesqualgebras*: $R$ is a commutative ring with $1$, $\varsigma$ is an involution of $R$, $A$ is an associative $R$-algebra with a $\varsigma$-semilinear involution $*$, the derived sesquilinear operation is $x \star y = xy^{*}$, and $H(A) = \{x : x^{*} = x\}$ and $S(A) = \{x : x^{*} = -x\}$ are the two halves of *Hermitian and Skew-Hermitian Elements*, which also supplies the decomposition $A = H(A) \oplus S(A)$ when $2$ is invertible. The general theory is *Lie Algebras*, its structure theory is *Structure of Lie Algebras*, and the sesquilinear bracket itself, treated for its own sake, is *The Sesquilinear Commutator*.

---

## The Two Halves and the Obstruction

### The Antisymmetrisation

**Definition.** The **antisymmetrisation** of the sesquilinear product is the bracket

$$
[x,y]_{\varsigma} = x \star y - y \star x .
$$

**Proposition.** For all $x, y$ and all $\lambda \in R$,

$$
[x,y]_{\varsigma} = -[y,x]_{\varsigma} , \qquad [\lambda x, y]_{\varsigma} = \lambda [x,y]_{\varsigma} + \bigl(\lambda - \varsigma(\lambda)\bigr)(y \star x) ,
$$

and consequently the bracket is linear over the fixed ring $R^{\varsigma}$ in each variable, and linear over all of $R$ exactly in the degenerate case $(\varsigma(\lambda) - \lambda)A = 0$ for every $\lambda$, the case in which the product of $A$ is bilinear.

**Proof.** Antisymmetry is the antisymmetry of the subtraction. For the scalar rule, $(\lambda x) \star y = \lambda(x \star y)$ by the first scalar rule of *Sesqualgebras* and $y \star (\lambda x) = \varsigma(\lambda)(y \star x)$ by the second, so

$$
[\lambda x, y]_{\varsigma} = \lambda(x \star y) - \varsigma(\lambda)(y \star x) = \lambda[x,y]_{\varsigma} + \bigl(\lambda - \varsigma(\lambda)\bigr)(y \star x) ,
$$

and the second slot is the same computation read through the transposition of *The Sesquilinear Product*. For $\lambda \in R^{\varsigma}$ the correction term vanishes and the bracket is linear; if the correction vanishes for all $x, y$ at a fixed $\lambda$, then $\bigl(\lambda - \varsigma(\lambda)\bigr)A = 0$ because $y \star x$ runs over $A$ when $A$ has a right unit, and the general case is the degeneracy condition of *Sesqualgebras*. $\square$

**Remark.** The bracket has one of the two properties of a Lie bracket for free, and the other not at all: it is antisymmetric, and it is not $R$-bilinear. The correction term $(\lambda - \varsigma(\lambda))(y \star x)$ is the whole of the difference between the sesquilinear case and the bilinear one at this level, and it vanishes identically only when the twist is invisible. Over the fixed ring there is no correction, which is why the fixed ring is the natural ring of scalars for every structure of this article and of its Jordan companion.

**Remark (a Lie algebra over the fixed ring, not a Lie sesqualgebra).** The obstruction is already visible in the two scalar rules, before they are subtracted. A scalar in the first slot meets the two products one at a time,

$$
(\lambda x) \star y = \lambda\,(x \star y), \qquad y \star (\lambda x) = \varsigma(\lambda)\,(y \star x),
$$

so the antisymmetrisation carries $\lambda$ on one of its two terms and $\varsigma(\lambda)$ on the other. For the bracket to be linear at $\lambda$ the two scalars would have to agree, and for it to be $\varsigma$-semilinear they would have to agree in the opposite pairing; both conditions are $\lambda = \varsigma(\lambda)$. No scalar is at once $\lambda$ and $\varsigma(\lambda)$ unless the involution fixes it, so the bracket obeys no scalar rule over $R$. Over the fixed ring the two scalars coincide and the bracket is bilinear, and where the Jacobi identity holds it is a **Lie algebra over $R^{\varsigma}$**. It is never a sesquilinear structure. The title says this exactly: the antisymmetrisation of a sesqualgebra returns a Lie algebra, not a Lie sesqualgebra.

### The Failure of the Jacobi Identity

**Theorem.** The Jacobi identity for the antisymmetrisation of the derived sesquilinear product fails in general. In $A = M_{2}(\mathbb{C})$ with the conjugate transpose, for $x = E_{11}$, $y = E_{22}$ and $z = E_{12}$,

$$
[[x,y]_{\varsigma}, z]_{\varsigma} + [[y,z]_{\varsigma}, x]_{\varsigma} + [[z,x]_{\varsigma}, y]_{\varsigma} = E_{21} - E_{12} \neq 0 .
$$

**Proof.** The three inner brackets are

$$
[E_{11},E_{22}]_{\varsigma} = E_{11}E_{22} - E_{22}E_{11} = 0 , \qquad [E_{12},E_{11}]_{\varsigma} = E_{12}E_{11} - E_{11}E_{21} = 0 ,
$$

$$
[E_{22},E_{12}]_{\varsigma} = E_{22}E_{12}^{*} - E_{12}E_{22}^{*} = E_{22}E_{21} - E_{12}E_{22} = E_{21} - E_{12} ,
$$

using $E_{ab}E_{cd} = \delta_{bc}E_{ad}$ and the reality of the matrix units. The first and the third of the three terms therefore vanish, and the middle one is

$$
[E_{21} - E_{12}, E_{11}]_{\varsigma} = (E_{21} - E_{12})E_{11}^{*} - E_{11}(E_{21} - E_{12})^{*} = (E_{21} - E_{12})E_{11} - E_{11}(E_{12} - E_{21}) = E_{21} - E_{12} ,
$$

again by the matrix-unit rule. The sum is $E_{21} - E_{12}$, which is not zero. $\square$

**Remark.** The witness uses two Hermitian idempotents and one matrix unit, so the failure does not require any exotic element: $E_{11}$ and $E_{22}$ lie in $H(A)$ and $E_{12}$ is an off-diagonal unit. It also shows where the associativity that would save the identity is lost: the computation of the middle term uses $E_{21}E_{11} = E_{21}$ and $E_{11}E_{21} = 0$, two products whose asymmetry is exactly the noncommutativity of $A$, and it is that asymmetry that the reassociation of a Jacobi identity cannot absorb once the two slots of the product carry different involution rules.

**Remark (the failure needs noncommutativity).** The obstruction is not the twist alone. In the commutative model $\mathbb{C}$ over $(\mathbb{C},\varsigma)$ with $x \star y = x\bar y$ the bracket is $[x,y]_{\varsigma} = x\bar y - y\bar x$, antisymmetric and real-linear, and the Jacobi identity holds identically; the failure of the theorem above is produced by the noncommutativity of $M_{2}(\mathbb{C})$ and not by the semilinearity, and in the commutative case the bracket is a Lie bracket over the fixed ring. This is the same dichotomy the biquaternion layer records, where among the four antisymmetrisations of the four general products exactly the commutator satisfies Jacobi and the sesquilinear ones do not, at the explicit triples of *The 12 Products of the Biquaternion Complex Space*.

**Remark (the twist of the involution also breaks Jacobi).** The first witness uses $\varsigma \neq \mathrm{id}$; the involution $*$ can break the identity on its own. Take $\varsigma = \mathrm{id}$ and $A = M_{2}(\mathbb{C})$ with $*$ the transpose, so that the derived operation $x \star y = xy^{\mathrm{T}}$ is $\mathbb{C}$-bilinear but not associative. Its antisymmetrisation fails the Jacobi identity on 58 of 60 random triples tested, so the twist of the base involution is not the only obstruction: the antisymmetrisation is a Lie bracket only when both involutions are trivial, the collapse forcing $\varsigma = \mathrm{id}$ and the associativity at $\varsigma = \mathrm{id}$ forcing $* = \mathrm{id}$.

### When the Antisymmetrisation Is a Lie Bracket

**Theorem (Lie-admissibility collapses to the bilinear case).** Let $A$ be an associative $R$-algebra with a $\varsigma$-semilinear involution, and let $\star$ be the derived operation.

(i) If $\star$ is associative, then the antisymmetrisation $[\ ,\ ]_{\varsigma}$ satisfies the Jacobi identity; it is $R$-bilinear, and hence a Lie bracket over $R$, exactly when $\varsigma = \mathrm{id}$ or $(\varsigma(\lambda) - \lambda)A = 0$ for every $\lambda$.

(ii) If $A$ is unital and faithful and $\star$ is associative, then $\varsigma = \mathrm{id}$ **and** $* = \mathrm{id}$: the derived operation is the product of an ordinary associative algebra and the antisymmetrisation is its commutator. If either involution is non-trivial, then $\star$ is not associative; the antisymmetrisation is then a bracket over the fixed ring $R^{\varsigma}$ alone, and its Jacobi identity fails in the noncommutative case, by the two witnesses above.

**Proof.** (i) For any product $\star$ the antisymmetrisation satisfies the Jacobi identity as soon as $\star$ is associative, the identity being the standard rearrangement of the associativity; the scalar statement is the proposition on the scalar rules of the definition, the correction term vanishing under the stated degeneracy condition. (ii) The associativity of $\star$ of full type forces $\varsigma = \mathrm{id}$, by the collapse theorem of *Sesqualgebras*, §*The Collapse at the Identity*, and the commutativity of $\star$ does the same. That gives the first involution. For the second, $*$ being an $R$-linear involution, associativity at $\varsigma = \mathrm{id}$ reads $(xy^{*})z^{*} = x(yz^{*})^{*}$, that is $xy^{*}z^{*} = xzy^{*}$ for all $x, y, z$; putting $x = 1$ and $y = 1$ gives $z^{*} = z$ for all $z$, so $* = \mathrm{id}$. With both involutions trivial the derived operation is the product and the antisymmetrisation is the commutator. Conversely $* \neq \mathrm{id}$ leaves $\star$ non-associative, and the transpose of the remark below exhibits the failure. $\square$

**Remark.** The hypothesis that makes the antisymmetrisation a Lie bracket is therefore associativity, and for a unital faithful algebra associativity forces both involutions to be trivial: at the level of the product there is no Lie algebra *of* a genuinely sesqualgebra, and the antisymmetrisation is a Lie bracket only in the fully bilinear case, in which the derived operation is the product itself. The rest of the article is about where the Lie structure goes instead.

---

## The Commutator Lie Algebra

### The Lie Algebra Underneath

**Theorem (recalled).** Let $A$ be an associative $R$-algebra. Then $A$ with the **commutator**

$$
[x,y] = xy - yx
$$

is a Lie algebra over $R$.

**Proof.** The commutator is $R$-bilinear by the bilinearity of the product, alternating by construction, and the Jacobi identity is the expansion

$$
[[x,y],z] + [[y,z],x] + [[z,x],y] = (xy - yx)z - z(xy-yx) + (yz-zy)x - x(yz-zy) + (zx-xz)y - y(zx-xz),
$$

in which every term appears twice with opposite signs once the products are reassociated; this is the classical theorem of *Lie Algebras*, §*The Commutator Bracket*, and it needs nothing of the involution. $\square$

**Remark.** The commutator of the *associative* product has both properties that the antisymmetrisation of the sesquilinear product lacks: it is $R$-bilinear, and it satisfies Jacobi. It is therefore the ambient Lie algebra in which the Lie structures of the sesqualgebra live, and the involution is what selects them.

### The Graded Structure

**Theorem (the commutator is graded by the involution).** Let $A$ be an associative $R$-algebra with a $\varsigma$-semilinear involution $*$, and let $H(A)$ and $S(A)$ be the Hermitian and the skew-Hermitian elements. Then

$$
[S,S] \subseteq S , \qquad [S,H] \subseteq H , \qquad [H,H] \subseteq S ,
$$

so that $A$, as a Lie algebra over $R$ under the commutator, is **$\mathbb{Z}/2$-graded** with even part $S(A)$ and odd part $H(A)$, the degree of an element being $1$ on $H(A)$ and $0$ on $S(A)$. Moreover $[x,y]^{*} = -[x^{*},y^{*}]$: the involution reverses the commutator, so it is not an automorphism of the Lie algebra but a graded anti-automorphism, and the negation is a central correction.

**Proof.** For $s, t \in S(A)$ one has $(st - ts)^{*} = t^{*}s^{*} - s^{*}t^{*} = (-t)(-s) - (-s)(-t) = ts - st$, so $[s,t] \in S(A)$; for $s \in S(A)$ and $h \in H(A)$, $[s,h]^{*} = (sh - hs)^{*} = h^{*}s^{*} - s^{*}h^{*} = h(-s) - (-s)h = sh - hs$, so $[s,h] \in H(A)$; for $h_1, h_2 \in H(A)$, $[h_1,h_2]^{*} = h_2h_1 - h_1h_2 = -[h_1,h_2]$, so $[h_1,h_2] \in S(A)$. The last identity is the same computation read for arbitrary $x, y$. The gradings are the parity of the degrees under the rule that the degree of $[x,y]$ is the sum of the degrees: $0+0 = 0$, $0+1 = 1$ and $1+1 = 0$ in $\mathbb{Z}/2$. $\square$

**Remark.** The Hermitian elements are not a Lie subalgebra, since $[H,H] \subseteq S$ and not $H$; it is the *skew*-Hermitian half that is a subalgebra, and this is the first structural asymmetry of the two halves in the sesquilinear layer. In the bilinear language $S(A)$ is the fixed set of the map $-*$, and the grading says that the Lie algebra is the direct sum of an even part on which the bracket is internal and an odd part on which it is twisted.

### The Skew-Hermitian Half

**Theorem.** Let $A$ be an associative $R$-algebra with a $\varsigma$-semilinear involution $*$. Then $S(A)$ is a Lie subalgebra of the commutator Lie algebra, and it is a Lie algebra over the fixed ring $R^{\varsigma}$: it is an $R^{\varsigma}$-submodule of $A$, the commutator is $R^{\varsigma}$-bilinear on it, and the Jacobi identity holds. No hypothesis on $2$ is needed, since the closure of the bracket in $S(A)$ uses only that $*$ reverses the order of a product.

**Proof.** The closure $[S,S] \subseteq S$ is the theorem above, and the Jacobi identity is inherited from the commutator Lie algebra of $A$. For the scalars, $S(A)$ is an $R^{\varsigma}$-submodule of $A$ by *Hermitian and Skew-Hermitian Elements*, §*The Scalar Action*, and the commutator is $R$-bilinear, hence $R^{\varsigma}$-bilinear on a submodule over $R^{\varsigma}$. $\square$

**Remark.** The Lie algebra is the object that *The Unitary Lie Algebra* develops for its own sake, and it is the **unitary Lie algebra** of $A$: in the matrix model it is the Lie algebra of the unitary group, whose elements are *Units and the Unitary Elements*. It is a Lie algebra over the fixed ring and not over $R$: over $R$ the multiplication by a scalar with $\varsigma(\lambda) = -\lambda$ carries $S(A)$ into $H(A)$, so $S(A)$ is not an $R$-submodule. The pair $\bigl(H(A), S(A)\bigr)$ is therefore an algebra over one ring in two halves, and the Lie algebra lives on the half whose range is closed.

### The Action and the Derivations

**Theorem (recalled, *Derivations of a Sesqualgebra*).** Suppose $A$ associative and $2$ invertible. The map $a \mapsto \mathrm{ad}_{a}$, $\mathrm{ad}_{a}(x) = ax - xa$, carries $S(A)$ onto the inner $*$-derivations of $A$, and

$$
[\mathrm{ad}_{s}, \mathrm{ad}_{t}] = \mathrm{ad}_{[s,t]}
$$

for $s, t \in S(A)$, so that $s \mapsto \mathrm{ad}_{s}$ is a homomorphism of Lie algebras over $R^{\varsigma}$ from the unitary Lie algebra onto the Lie algebra of the inner $*$-derivations, with kernel the central skew-Hermitian elements.

**Proof.** The bracket identity and the description of the image and the kernel are the theorem and the corollary of *Derivations of a Sesqualgebra*, §*The Inner Derivations*; what is added here is only their reading: since $S(A)$ is closed under the commutator, the source of the homomorphism is a Lie algebra over the fixed ring, and the target is a Lie subalgebra of the Lie algebra of the derivations of that article. $\square$

**Remark.** The Hermitian elements act too, and by the skew derivations: $\mathrm{ad}_{h}$ for $h \in H(A)$ satisfies $\mathrm{ad}_{h}(x^{*}) = -\mathrm{ad}_{h}(x)^{*}$ and is not a $*$-derivation, so the $*$-derivations come from the skew half and the skew derivations from the Hermitian half. The parallel with the Jordan side is exact and is the subject of the comparison below: there the Hermitian elements act by the quadratic representation, here the skew-Hermitian elements act by the adjoint representation.

---

## The Ternary Companion

### The Lie Triple System

**Definition.** For a Lie algebra $\mathfrak{g}$ and $x, y, z \in \mathfrak{g}$ put

$$
\{x,y,z\}_{\mathrm{L}} = [[x,y],z] .
$$

**Proposition.** The operation $\{\cdot,\cdot,\cdot\}_{\mathrm{L}}$ satisfies the three **Lie triple system identities**

$$
\{x,y,z\}_{\mathrm{L}} = -\{y,x,z\}_{\mathrm{L}} , \qquad \{x,y,z\}_{\mathrm{L}} + \{y,z,x\}_{\mathrm{L}} + \{z,x,y\}_{\mathrm{L}} = 0 ,
$$

$$
\{x,y,\{u,v,w\}_{\mathrm{L}}\}_{\mathrm{L}} = \{\{x,y,u\}_{\mathrm{L}},v,w\}_{\mathrm{L}} + \{u,\{x,y,v\}_{\mathrm{L}},w\}_{\mathrm{L}} + \{u,v,\{x,y,w\}_{\mathrm{L}}\}_{\mathrm{L}} .
$$

**Proof.** The first is the antisymmetry of the commutator: $[[x,y],z] = -[[y,x],z]$. The second is the Jacobi identity, rewritten: $[[x,y],z]$ is one of its three cyclic terms. The third is the Jacobi identity applied to the pair $[x,y]$ and the pair $[u,v]$, or equivalently the identity $[[x,y],[u,v]] = [[[x,y],u],v] - [u,[[x,y],v]]$ expanded with Jacobi. $\square$

**Remark.** The triple system is where the Lie structure survives on the whole space, and it is the ternary companion of the antisymmetrisation: it needs the commutator and not the sesquilinear product, it is available whatever the involution does, and it inherits its identities from the associativity of the product. Its operator form, $z \mapsto \mathrm{ad}_{[x,y]}(z) = [[x,y],z]$, is one of the operators of *The Ternary Product as an Operator*.

### The Two Triple Systems

**Remark.** The two layers of the sesquilinear kind carry two ternary products of the same shape. The Jordan layer carries $\{x,y,z\} = xy^{*}z$ and the Jordan triple identity, the axioms of the algebraic $J^{*}$-algebra of *Algebraic J\*-Algebras*; the Lie layer carries $\{x,y,z\}_{\mathrm{L}} = [[x,y],z]$ and the three identities above. Neither is a binary structure, both exist on the whole space with no involution fixed, and the binary structures of the two articles are recovered from them only on a half or at a unit. This is the precise sense in which the sesquilinear kind carries its Lie and Jordan theory at the ternary level first: the binary products of the bilinear theory are the specialisations, and *The Lie–Jordan Decomposition of a Bilinear Product and the Jordan Triple System* is the bilinear case, where the two binary structures and the triple system are all present at once.

---

## The Scalars and the Bilinear Case

**Theorem (the degeneration).** Put $\varsigma = \mathrm{id}$. Then the base involution is the identity, the fixed ring is all of $R$, the derived operation is $R$-bilinear, and the structures of this article become $R$-linear: the commutator Lie algebra of $A$ is the ordinary one, the grading by the involution stands, the skew-Hermitian part is a Lie algebra over $R$, and the antisymmetrisation is that of the $R$-bilinear product $xy^{*}$, which is the commutator of $A$ when in addition $* = \mathrm{id}$ and is still not a Lie bracket when $* \neq \mathrm{id}$.

**Proof.** With $\varsigma = \mathrm{id}$ the second scalar rule is the first, so $x \star y = xy^{*}$ is $R$-bilinear and no correction term survives in the scalar rule of the bracket, so the fixed ring is all of $R$; the commutator Lie algebra, the grading and the closure of the skew-Hermitian part are the theorems above, whose hypotheses then hold with $R^{\varsigma} = R$. The antisymmetrisation is $xy^{*} - yx^{*}$, which is the commutator only when $* = \mathrm{id}$, and the transpose remark shows that $* \neq \mathrm{id}$ leaves the Jacobi identity failing. $\square$

**Remark.** The degeneration is the one of *Sesqualgebras*, §*The Collapse at the Identity*, and it has two independent steps: $\varsigma = \mathrm{id}$ makes the product bilinear, and $* = \mathrm{id}$ makes the derived operation the product. Only in the second case is the antisymmetrisation the commutator, and it is the first case that the structures of this article need in order to be Lie algebras over $R$ rather than over $R^{\varsigma}$.

The two cases are collected in the table.

| | bilinear, $\varsigma = \mathrm{id}$ | sesquilinear, $\varsigma \neq \mathrm{id}$ |
|---|---|---|
| the antisymmetrisation | $R$-bilinear, the commutator when $* = \mathrm{id}$ | $R^{\varsigma}$-bilinear, the commutator never; Jacobi fails |
| where the Lie algebra lives | on all of $A$ | on $S(A)$, under the commutator |
| the scalars | $R$ | $R^{\varsigma}$ |
| the Hermitian part | a Lie algebra under the commutator as well | $[H,H] \subseteq S$, not a subalgebra |
| the involution on the bracket | invisible | reverses it, $[x,y]^{*} = -[x^{*},y^{*}]$ |
| the ternary companion | the Lie triple system of the commutator | the same, and it is the structure that always exists |

## Examples

### The Complex Matrices

For $A = M_{n}(\mathbb{C})$ with the conjugate transpose, $S(A)$ is the space of the skew-Hermitian matrices, the Lie algebra $\mathfrak{u}(n)$ of the unitary group, a Lie algebra over $\mathbb{R}$; $H(A)$ is the space of the Hermitian matrices, not a Lie subalgebra since the commutator of two Hermitian matrices is skew-Hermitian; and the commutator Lie algebra of $A$ is $\mathfrak{gl}(n,\mathbb{C})$ read as a real Lie algebra, graded by the involution as $\mathfrak{u}(n) \oplus i\,\mathfrak{u}(n)$. The antisymmetrisation of the derived product is not a Lie bracket, with the witness of $M_{2}(\mathbb{C})$ above.

### The Field

For $A = \mathbb{C}$ over $(\mathbb{C},\varsigma)$ with $\varsigma$ the conjugation and $x \star y = x\bar y$, the skew-Hermitian elements are the purely imaginary numbers, $S(A) = i\mathbb{R}$, an abelian Lie algebra over $R^{\varsigma} = \mathbb{R}$, and the Hermitian elements are the reals. The antisymmetrisation is $[x,y]_{\varsigma} = 2i\,\mathrm{Im}(x\bar y)$: it is real-linear, antisymmetric and satisfies Jacobi, so it is a Lie bracket over $\mathbb{R}$, and the case shows that the Jacobi failure of the theorem above is produced by the noncommutativity and not by the twist. Over $\mathbb{C}$ the bracket is not bilinear, and as a Lie algebra over $\mathbb{R}$ it is abelian, its bracket carrying no information beyond its vanishing.

### The Quaternions

For $A = \mathbb{H}$ with the quaternion conjugation over $(\mathbb{R},\mathrm{id})$ the twist is invisible, the case is bilinear, and $S(A)$ is the space of the imaginary quaternions, the Lie algebra $\mathfrak{su}(2)$ under the commutator; the derived operation is the product, and the antisymmetrisation is the commutator. It is the case in which the sesquilinear layer and the bilinear one coincide, and it is the reason the cross product appears as a Lie bracket.

### The Biquaternion Algebra

For $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with the star-involution the commutator makes $\mathbb{B}$ a Lie algebra over $\mathbb{C}$, isomorphic to $\mathfrak{gl}(2,\mathbb{C})$, with the trace-free part isomorphic to $\mathfrak{sl}(2,\mathbb{C})$, and the skew-Hermitian elements form the Lie subalgebra $\mathbb{M}_{-}$ of *Remarkable Subspaces and the Four General Products* and *The 12 Products of the Biquaternion Complex Space*. That layer also exhibits the failure of the theorem above: of the four antisymmetrisations of the four general products of the biquaternion algebra exactly the commutator satisfies Jacobi, the star-bracket failing it at the triple $(e_1,e_2,ie_3)$ with the value $4ie_0$.

## Summary

A sesqualgebra does not carry a Lie algebra by antisymmetrising its own product. The antisymmetrisation $[x,y]_{\varsigma} = x \star y - y \star x$ is antisymmetric, but it is linear only over the fixed ring $R^{\varsigma}$ and its Jacobi identity fails as soon as the algebra is noncommutative, with the witness $E_{11}, E_{22}, E_{12}$ in $M_{2}(\mathbb{C})$ whose Jacobi sum is $E_{21} - E_{12}$; it is a Lie bracket exactly in the cases where the product being antisymmetrised is associative, and for a unital faithful algebra associativity forces $\varsigma = \mathrm{id}$ and $* = \mathrm{id}$, so the antisymmetrisation is the commutator of an ordinary associative algebra only in the fully bilinear case.

The Lie structure that a sesqualgebra does carry comes from its associative product. The commutator $xy - yx$ makes $A$ a Lie algebra over $R$, the involution makes it a $\mathbb{Z}/2$-graded Lie algebra with even part the skew-Hermitian elements and odd part the Hermitian ones, the Hermitian part is not a subalgebra while the skew-Hermitian part is, and the involution reverses the bracket. The skew-Hermitian half is a Lie algebra over the fixed ring $R^{\varsigma}$, the unitary Lie algebra, and it acts on $A$ by the inner $*$-derivations, $[\mathrm{ad}_{s},\mathrm{ad}_{t}] = \mathrm{ad}_{[s,t]}$, with kernel the central skew-Hermitian elements. What survives on the whole space is ternary: the Lie triple system $[[x,y],z]$, whose three identities are the antisymmetry of the commutator, the Jacobi identity, and the Jacobi identity read on a bracket of brackets. The degenerate case $\varsigma = \mathrm{id}$ recovers the bilinear scalars and the $R$-linear structures, and it takes $* = \mathrm{id}$ as well for the antisymmetrisation to be the commutator.

## Summary of Notation

| symbol | meaning |
|---|---|
| $[x,y]_{\varsigma} = x \star y - y \star x$ | the antisymmetrisation of the sesquilinear product, not a Lie bracket in general |
| $[x,y] = xy - yx$ | the commutator of the associative product, the Lie bracket that is available |
| $A = H(A) \oplus S(A)$ | the two halves, when $2$ is invertible |
| $H(A) = \{x : x^{*} = x\}$ | the Hermitian elements, the odd part of the graded Lie algebra |
| $S(A) = \{x : x^{*} = -x\}$ | the skew-Hermitian elements, the even part and the unitary Lie algebra |
| $[S,S] \subseteq S$, $[S,H] \subseteq H$, $[H,H] \subseteq S$ | the $\mathbb{Z}/2$-grading by the involution |
| $[x,y]^{*} = -[x^{*},y^{*}]$ | the involution reverses the bracket |
| $R^{\varsigma}$ | the fixed ring, the scalars of the unitary Lie algebra |
| $\mathrm{ad}_{a}(x) = ax - xa$ | the inner map, a $*$-derivation for skew-Hermitian $a$ |
| $\{x,y,z\}_{\mathrm{L}} = [[x,y],z]$ | the Lie triple system |
| $E_{11}, E_{22}, E_{12}$ | the witness triple in $M_2(\mathbb{C})$ for the failure of Jacobi |

## Further Reading

- Nathan Jacobson, *Lie Algebras* (Interscience, 1962; Dover reprint, 1979), for the commutator Lie algebra of an associative algebra, the graded algebras, and the derivations.
- James E. Humphreys, *Introduction to Lie Algebras and Representation Theory* (Springer, 1972), for the structure theory and the classical matrix algebras $\mathfrak{gl}$, $\mathfrak{sl}$ and $\mathfrak{u}$.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society Colloquium Publications 44, 1998), for the involutions, their two halves and the graded structures they produce.
- Ottmar Loos, *Jordan Pairs* (Lecture Notes in Mathematics 460, Springer, 1975), for the Lie and Jordan triple systems as primary objects and the binary algebras as their specialisations.
- The companion articles of this series: *Sesqualgebras*, *The Sesquilinear Product*, *Hermitian and Skew-Hermitian Elements*, *Derivations of a Sesqualgebra*, *The Sesquilinear Commutator*, *The Unitary Lie Algebra*, *The Ternary Product as an Operator*, *Algebraic J\*-Algebras*, and *Jordan Algebras of Sesqualgebras*.
