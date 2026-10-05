# __Topological Sesquialgebras__

## Introduction

Part I developed the sesquialgebras without a topology: an $R$-module with a product linear in the first slot and $\varsigma$-semilinear in the second, the collapse at $\varsigma = \mathrm{id}$, the derived operation and the ternary product that its failure of associativity forces, and the standard examples. This article opens the layer in which the operations are continuous. It is the entry of the category *Topology on Sesquialgebras*, and it stands to *Sesquialgebras* as *Topological Algebras and Banach Algebras* stands to *Algebras*: the base ring is a topological ring, the module is a topological module, and the product is required to be continuous.

The one new ingredient with respect to the bilinear layer is the twist. The base is an **involutive topological ring** $(R,\varsigma)$ in the sense of *Involutive Topological Rings and Fields*: $R$ is a commutative topological ring with $1$, and $\varsigma$ is a continuous involution of it. The continuity of $\varsigma$ is what makes the twisted action $\lambda \cdot x = \varsigma(\lambda)x$ a continuous action, so that the conjugate module of Part I is again a topological module and the two slots of the product can be read in one category.

Three facts organise the article. The conjugate module $A^{\varsigma}$ is a topological module for the twisted action, with the same topological abelian group as $A$, and the product is a separately continuous $R$-bilinear map $A \times A^{\varsigma} \to A$: the definition of the layer is the bilinear definition of Part I, read in topological modules. The additive group of $A$ is a topological group, so its topology is determined at $0$ and the closure of $\{0\}$ is a two-sided ideal, the obstruction to being Hausdorff, whose quotient is again a topological sesquialgebra over the same datum. And at the trivial involution the twisted action is the ordinary one, the product is bilinear and the object is a topological algebra in the sense of the bilinear layer; for an object of **full type** the algebraic collapse applies unchanged, so a topological sesquialgebra of full type with a nontrivial involution is not an ordinary algebra in disguise.

The article defines the layer and its standing hypotheses, reads the conjugate module topologically, states the continuity of the product and of the two one-sided multiplications, treats the separation and the quotient by the closure of zero, and proves the collapse, keeping the topological arguments and the algebraic ones apart. It names no form and no norm: the forms belong to *Topological Sesquialgebras with a Form*, the normed and complete objects to *Banach Sesquialgebras*, the locally convex ones to *Fréchet and Locally Convex Sesquialgebras*, the conjugate dual to *The Conjugate Dual of a Sesquialgebra*, the completion to *The Completion of a Sesquialgebra*, and the continuity of the two involutions, of the base and of the algebra, to *The Continuity of the Involution*. Throughout, $(R,\varsigma)$ is a commutative involutive topological ring with $1$, $A$ is a topological $R$-module carrying a product, and the topological spaces are Hausdorff except where the separation of $A$ itself is at stake.

## The Layer

### The Definition

**Definition.** Let $(R,\varsigma)$ be an involutive topological ring. A **topological sesquialgebra** over $(R,\varsigma)$ is a topological $R$-module $A$ with a product $A \times A \to A$, written $(x,y) \mapsto xy$, additive in each variable, separately continuous, and satisfying

$$
(\lambda x)y = \lambda(xy), \qquad x(\lambda y) = \varsigma(\lambda)(xy)
$$

for all $\lambda \in R$ and all $x, y \in A$.

The definition is that of *Sesquialgebras*, §*The Two Scalar Rules*, with three topological hypotheses: the base ring carries a topology for which its operations are continuous, the module carries a topology for which its operations are continuous, and the product is continuous in each variable separately. Nothing else is assumed. The product need not be associative, need not have a unit and need not be commutative; no form is named, and no norm is required.

**Remark (separate continuity is checked at zero).** The product is additive in each variable, so for fixed $a$ the two maps $x \mapsto ax$ and $x \mapsto xa$ are homomorphisms of the additive group, and a homomorphism of topological groups is continuous if and only if it is continuous at $0$, because it commutes with the translations. A product additive in each variable is therefore separately continuous exactly when, for every $a$, these two maps are continuous at $0$, which is the form in which the hypothesis is verified in the examples below.

**Example (the discrete objects).** Every algebraic sesquialgebra of Part I, with the discrete topology on $R$ and on $A$, is a topological sesquialgebra: every map on a discrete space is continuous, and the two scalar rules are the algebraic ones. The topological layer therefore contains the algebraic one, and the two differ exactly where a topology that is not discrete is imposed, which is where the limits of the analysis live.

**Example (the base itself).** Let $R = \mathbb{K} = \mathbb{R}$ or $\mathbb{C}$ with its usual topology, and let $A = \mathbb{K}$ with the product $x \star y = x\,\varsigma(y)$, where $\varsigma$ is the conjugation. The product is continuous, additive in each variable, and satisfies the two rules; hence $\mathbb{K}$ is a topological sesquialgebra over itself which is not a topological algebra of the bilinear layer unless $\varsigma = \mathrm{id}$.

### The Conjugate Module

**Proposition.** Let $A$ be a topological $R$-module and put $\lambda \cdot x = \varsigma(\lambda)x$. The twisted action $R \times A \to A$ is continuous and is an action of $R$ on the set $A$. Consequently the conjugate module $A^{\varsigma}$ of *Sesquialgebras*, §*The Conjugate Module* is a topological $R$-module with the same topology and the same additive group as $A$, and $(A^{\varsigma})^{\varsigma} = A$.

*Proof.* The twisted action is the composite of the continuous map $(\lambda, x) \mapsto (\varsigma(\lambda), x)$ with the continuous action of $R$, hence continuous. The action identities hold: $\lambda \cdot (\mu \cdot x) = \varsigma(\lambda)\varsigma(\mu)x = \varsigma(\mu\lambda)x = (\mu\lambda) \cdot x = (\lambda\mu) \cdot x$, the middle equality by the multiplicativity of $\varsigma$ and the last by the commutativity of $R$; and $1 \cdot x = \varsigma(1)x = x$ because an involution fixes $1$. The module axioms of a topological module are inherited from $A$, whose underlying topological abelian group and scalar action for the twisted structure are the ones displayed, and conjugating twice returns $\varsigma(\varsigma(\lambda))x = \lambda x$. $\square$

### The Two Slots

**Theorem (the product is bilinear on the pair).** Let $A$ be a topological sesquialgebra over $(R,\varsigma)$. Read as a map $A \times A^{\varsigma} \to A$, the product is $R$-bilinear and separately continuous. Conversely, an $R$-bilinear separately continuous map $A \times A^{\varsigma} \to A$ is a $\varsigma$-sesquilinear product, making $A$ a topological sesquialgebra over $(R,\varsigma)$.

*Proof.* The algebraic statement is the theorem of *Sesquialgebras*, §*The Conjugate Module*: in the second slot the scalar acts as $\lambda \cdot y = \varsigma(\lambda)y$, and the second rule reads $x(\lambda \cdot y) = \varsigma(\varsigma(\lambda))(xy) = \lambda(xy)$, so the product is linear in each of the two variables. Separate continuity is the hypothesis, the topology of $A^{\varsigma}$ being that of $A$. $\square$

**Remark.** The theorem is the reason the layer needs no new algebra: an object is a topological $R$-module with a separately continuous $R$-bilinear map into itself from the module and its conjugate. Every statement about the layer can be read in that form, and the bookkeeping of which copy of $A$ carries which action is the whole of the difference from the bilinear case.

## The Product and the One-Sided Multiplications

### The One-Sided Multiplications

**Proposition (the left and the right multiplication).** Let $a \in A$ and let $L_a(x) = ax$ and $R_a(x) = xa$. Then $L_a$ is continuous and $\varsigma$-semilinear, while $R_a$ is continuous and $R$-linear.

*Proof.* Continuity is the separate continuity of the product. For the scalars, $L_a(\lambda x) = a(\lambda x) = \varsigma(\lambda)(ax) = \varsigma(\lambda)L_a(x)$ by the second rule, and $R_a(\lambda x) = (\lambda x)a = \lambda(xa) = \lambda R_a(x)$ by the first. $\square$

The two parities are the algebraic ones of *The Left and Right Multiplication Operators of a Sesquialgebra*, and the topology adds only the continuity: the one-sided multiplications are the two classes of operators that the operator theory of the layer carries.

### Joint Continuity

**Remark (joint continuity).** Joint continuity, that the product be continuous as a map $A \times A \to A$ for the product topology, implies separate continuity and is in general strictly stronger; when the topology of $A$ comes from a complete norm the two agree, by the uniform boundedness principle, and that case belongs to *Banach Sesquialgebras*. The matrix, the field, the collapsed and the discrete examples below are jointly continuous; the endomorphism example with the topology of pointwise convergence is the one in which the argument above supplies separate continuity alone, joint continuity needing an equicontinuity hypothesis on the convergent families, and that is why the layer carries the separate hypothesis rather than the joint one.

### The Matrix and the Endomorphism Examples

**Example (the matrices).** Let $A = M_n(\mathbb{C})$ with the entrywise topology, which for a module of finite rank coincides with the operator topology, and let the product be $S \star T = ST^{*}$ with $\varsigma$ the conjugation. The entries of a product are polynomials in the entries of the factors, so the product is jointly continuous, hence separately continuous; the scalar rules hold with $\varsigma$ the conjugation; and the object is a topological sesquialgebra over $(\mathbb{C},\varsigma)$. It is not associative: for $n = 2$ the matrix units give

$$
(E_{22} \star E_{12}) \star E_{11} = E_{21} \neq 0 = E_{22} \star (E_{12} \star E_{11}) .
$$

The algebraic structure of the example, its Hermitian and unitary elements and its trace are those of *Matrix Sesquialgebras*.

**Example (the endomorphism algebra).** Let $M$ be an $R$-module with a fixed topology and let $\dagger$ be a $\varsigma$-semilinear involution of its endomorphism ring, of the adjoint type, so that $S^{\dagger}$ is defined; let $A = \operatorname{End}_R(M)$ with the product $S \star T = S T^{\dagger}$ and the topology of pointwise convergence. The semilinearity of the involution is what carries the second scalar rule, $S \star (\lambda T) = S(\lambda T)^{\dagger} = \varsigma(\lambda)(S \star T)$, and the composition is separately continuous — if $S_\alpha \to S$ pointwise then $S_\alpha T \to ST$ and $S T_\alpha \to ST$ pointwise — so with $\dagger$ continuous as well the object is a topological sesquialgebra over $(R,\varsigma)$. The structure, the involutions of the adjoint type it admits and the worked cases are *The Sesquilinear Structure of the Endomorphism Algebra*.

## The Closure of Zero

### The Ideal of the Closure

**Proposition.** Let $A$ be a topological sesquialgebra and let $N = \overline{\{0\}}$. Then $N$ is a closed submodule of $A$ and a two-sided ideal, and $A$ is Hausdorff if and only if $N = \{0\}$.

*Proof.* The additive group of $A$ is a topological group, so the separation criterion is the theorem of *Topological Groups*, §*Separation*, which characterises $\overline{\{0\}}$ as the intersection of the neighbourhoods of $0$ and proves that it is a subgroup, and the group is Hausdorff exactly when that subgroup is trivial. For the scalars, the maps $x \mapsto \lambda x$ and $x \mapsto -x$ are continuous and carry $0$ to $0$, so they carry $\overline{\{0\}}$ into $\overline{\{0\}}$, and $N$ is a submodule. For the products, fix $a \in A$; the maps $L_a$ and $R_a$ are continuous and carry $0$ to $0$, so $aN \subseteq N$ and $Na \subseteq N$, which is the two-sided ideal property. $\square$

### The Quotient

**Theorem.** Let $N = \overline{\{0\}}$. The quotient $A/N$ with the quotient topology is a Hausdorff topological sesquialgebra over the same datum $(R,\varsigma)$, its product being the descended map $(x + N)(y + N) = xy + N$, and the quotient map $q : A \to A/N$ is $R$-linear and multiplicative.

*Proof.* The set $N$ is a submodule, so by *Topological Modules and Vector Spaces*, §*Quotient Modules* the quotient is a topological $R$-module, with $q$ continuous and open, and it is Hausdorff because $N$ is closed in a topological group. The product descends: for $x' = x + n$ and $y' = y + m$ with $n, m \in N$ one has $x'y' = xy + xm + ny + nm$ with $xm, ny, nm \in N$, since $N$ is a two-sided ideal, so the class of $x'y'$ is that of $xy$. It is additive in each variable because the product of $A$ is and $q$ is additive. It is separately continuous: for fixed $x$, the map $y + N \mapsto xy + N$, composed with $q$, is the continuous map $L_x$, so it is continuous by the universal property of the quotient topology, and the case of a fixed $y$ is the same. The first scalar rule is inherited from $A$, and the second follows from $x(\lambda y) = \varsigma(\lambda)(xy)$ on representatives. $\square$

The quotient is the standard device that removes the defect of a non-Hausdorff topology: it is the largest Hausdorff quotient of $A$, and it carries the sesquilinear structure over the same base datum, the involution of the base being that of $R$ and not of $A$.

## The Collapse at the Trivial Involution

### The Collapse

**Theorem (the collapse of the layer).** Let $A$ be a topological sesquialgebra over $(R,\varsigma)$ with $\varsigma = \mathrm{id}$. Then the two scalar rules coincide, the twisted action is the ordinary action, $A^{\varsigma} = A$ as topological $R$-modules, and the product is $R$-bilinear: the object is an $R$-algebra whose product is separately continuous, and when the product is jointly continuous and $R = \mathbb{K}$ is the complete valued field it is a topological algebra in the sense of *Topological Algebras and Banach Algebras*, §*Topological Algebras*. Conversely every topological $R$-module with a separately continuous $R$-bilinear product is a topological sesquialgebra over $(R,\mathrm{id})$, so the two categories are the same.

*Proof.* With $\varsigma = \mathrm{id}$ the second rule reads $x(\lambda y) = \lambda(xy)$, which is the first, so the two rules coincide and the product is $R$-bilinear; the twisted action is the ordinary one and the conjugate module is $A$ with its own action. Conversely every topological $R$-module with a separately continuous $R$-bilinear product is a topological sesquialgebra over $(R,\mathrm{id})$, so the two categories are the same. $\square$

**Remark (the defect of the base).** The collapse can occur with $\varsigma \neq \mathrm{id}$ when the defect of the base annihilates the module: if $(\varsigma(\lambda) - \lambda)A = 0$ for every $\lambda$, then the two rules have the same value on every pair and the product is again $R$-bilinear. This is the algebraic reduction of *Sesquialgebras*, §*The Collapse at the Identity* read on the annihilator, and it is a statement about the objects and not about the topology, which plays no role.

### The Objects of Full Type

**Theorem (objects of full type).** Let $A$ be a topological sesquialgebra of **full type** in the sense of *Sesquialgebras*, §*The Collapse at the Identity*: faithful over $R$, with products generating $A$ and no nonzero element annihilating $A$ on the left. If $\varsigma \neq \mathrm{id}$ then $A$ is neither associative nor commutative.

*Proof.* The hypotheses are exactly those of the collapse theorem of *Sesquialgebras*, §*The Collapse at the Identity*, which is a statement about the scalars and the product alone; the topology is not used in its proof and adds nothing to its hypotheses or to its conclusion. $\square$

The theorem is the sense in which the layer does not enlarge the bilinear one: a topological sesquialgebra of full type with a nontrivial involution is never a topological algebra of the bilinear layer, whether the product is continuous, separately continuous, or not continuous at all, because the obstruction is the scalar rule and not the topology. The topological structure adds the convergence of the power series and of the exponentials, which the later entries of the category develop.

## Examples

### The Collapsed and the Degenerate Examples

**Example (the collapsed real algebras).** Let $A$ be $\mathbb{H}$, $\mathbb{D}$ or $\mathbb{D}'$ with an $\mathbb{R}$-linear involution ${}^{*}$ and the derived product $x \star y = xy^{*}$, with the Euclidean topology. The datum is $(\mathbb{R},\mathrm{id})$, the second scalar rule is the first, and the product is $\mathbb{R}$-bilinear, so the object is a topological sesquialgebra of the collapsed kind — a topological algebra of the bilinear layer — and the collapse theorem applies with $\varsigma = \mathrm{id}$. These are the collapsed entries of *Examples of Sesquialgebras*, §*The Real Algebras and the Collapse*, read topologically.

**Example (the zero product).** Let $A = R$ with the zero product and any continuous involution $\varsigma$ of $R$. The product is jointly continuous, additive in each variable and satisfies both scalar rules, the two sides of each being zero. The object is a topological sesquialgebra over $(R,\varsigma)$ whose product is $R$-bilinear, so it is also a topological algebra; it is not of full type, since its products generate the zero submodule and not $A$. It is the boundary case of the collapse theorem, which needs the generation hypothesis, and it is the zero product of *Examples of Sesquialgebras*, §*The Zero Product*.

**Example (a topology that is not discrete).** Let $R$ be a ring with an ideal $I$, the $I$-adic topology and a continuous involution $\varsigma$, and let $A = R$ with the product $x \star y = x\,\varsigma(y)$. The object is a topological sesquialgebra over $(R,\varsigma)$, and it shows that the continuity of $\varsigma$ is a genuine hypothesis: for $R = \mathbb{R}[x]$ with the $(x)$-adic topology the linear involutions $f(x) \mapsto f(b - x)$ are continuous only for $b = 0$, so all but one of them are excluded from the datum. The criterion is that of *Involutive Topological Rings and Fields*, §*The Involution and the $I$-adic Topology*.

**Example (the indiscrete topology).** Let $A$ be the topological sesquialgebra of the zero product on a Hausdorff base and let $B$ be $A$ with the indiscrete topology over the same product. Every map into the indiscrete space is continuous, so the product and the twisted action are continuous and $B$ is a topological sesquialgebra, with $\overline{\{0\}} = B$; the quotient of the previous section is then the zero object. It is the extreme case of the separation: the closure of zero is the whole module, and the Hausdorff quotient of the group is trivial.

## Summary

A **topological sesquialgebra** over an involutive topological ring $(R,\varsigma)$ is a topological $R$-module with a product additive in each variable, separately continuous, $R$-linear in the first slot and $\varsigma$-semilinear in the second. The continuity of $\varsigma$ makes the twisted action $\lambda \cdot x = \varsigma(\lambda)x$ continuous, so the **conjugate module** $A^{\varsigma}$ is a topological module with the same topology as $A$, and the product is a separately continuous $R$-bilinear map $A \times A^{\varsigma} \to A$. The layer is the bilinear layer of *Topological Algebras and Banach Algebras* with the twist carried along, and the single new datum is the involution of the base.

The **left multiplication** $L_a(x) = ax$ is continuous and $\varsigma$-semilinear, the **right multiplication** $R_a(x) = xa$ is continuous and $R$-linear, and separate continuity of the product is exactly the continuity of these maps; joint continuity is stronger in general and coincides with it in the complete normed case. The additive group of $A$ is a topological group, so the **closure of zero** is a closed two-sided ideal, the group is Hausdorff exactly when that ideal is zero, and the **quotient** by it is a Hausdorff topological sesquialgebra over the same datum, with the descended product. The subtlety of the quotient is that the product descends only because the closure of zero is a two-sided ideal, which is what the separate continuity of the one-sided multiplications supplies.

At $\varsigma = \mathrm{id}$ the twisted action is the ordinary one, the product is bilinear and the object is a topological algebra of the bilinear layer, so the category **collapses**. The collapse is not repaired by the topology: the defect of the base annihilates the module exactly when the product is bilinear over a nontrivial involution, and an object of **full type** — faithful over $R$, with products generating $A$ and no nonzero left annihilator — with $\varsigma \neq \mathrm{id}$ is neither associative nor commutative, by the algebraic theorem of *Sesquialgebras* applied unchanged. The examples are the discrete objects, the base field with the product $x\,\varsigma(y)$, the matrix algebra with $ST^{*}$, the endomorphism algebra with the adjoint, the collapsed real algebras, the zero product, the $I$-adic objects, where the continuity of the involution is a genuine restriction, and the indiscrete objects, where the closure of zero is everything.

## Summary of Notation

| symbol | meaning |
|---|---|
| $(R,\varsigma)$ | a commutative involutive topological ring with $1$, $\varsigma$ continuous |
| $A$ | a topological sesquialgebra over $(R,\varsigma)$ |
| $xy$ | the product, additive in each variable, separately continuous, $R$-linear in $x$ and $\varsigma$-semilinear in $y$ |
| $A^{\varsigma}$ | the conjugate module, with the continuous twisted action $\lambda \cdot x = \varsigma(\lambda)x$ |
| $L_a$, $R_a$ | the left and the right multiplication, $\varsigma$-semilinear and $R$-linear, both continuous |
| $\overline{\{0\}}$ | the closure of zero, a closed two-sided ideal |
| $A/\overline{\{0\}}$ | the Hausdorff quotient, a topological sesquialgebra over $(R,\varsigma)$ |
| full type | faithful over $R$, products generating $A$, no nonzero left annihilator |
| $\varsigma = \mathrm{id}$ | the collapse: the object is a topological algebra of the bilinear layer |

## Further Reading

- Seth Warner, *Topological Rings* (North-Holland, 1993), for topological rings, their modules and their continuous involutions.
- V. K. Balachandran, *Topological Algebras* (North-Holland, 2000), for the bilinear layer that this article lifts, and for separate and joint continuity of a product.
- Maria Fragoulopoulou, *Topological Algebras with Involution* (North-Holland, 2005), for involutive topological algebras and the two parities of the slots.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the faithfulness and generation hypotheses of the collapse.
- Harald Upmeier, *Jordan Algebras in Analysis, Operator Theory, and Quantum Mechanics* (American Mathematical Society, 1987), for the ternary product that the failure of associativity forces.
- Cho-Ho Chu, *Jordan Structures in Geometry and Analysis* (Cambridge University Press, 2012), for the algebraic structure of the derived operation read without a norm.
