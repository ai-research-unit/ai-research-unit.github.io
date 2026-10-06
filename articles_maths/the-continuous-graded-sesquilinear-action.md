# __The Continuous Graded Sesquilinear Action__

## Introduction

*The Graded Sesquilinear Action* defines the action of a graded sesquialgebra on a graded module that carries a conjugation: the element $a$ acts on $m$ through $\theta$, by $a\star m=a\cdot\theta(m)$, an operation linear in the algebra and $\varsigma$-semilinear in the module, and the compatibility of the conjugation with the action is an identity on the even part that the odd part obstructs. The present article is the entry of the topological layer, and it adds exactly one ingredient: continuity. The object is a topological sesquialgebra of *Topological Sesquialgebras* whose grading is a decomposition into closed submodules, the module is a topological graded module with a continuous conjugation, and the derived action is continuous and bounded.

The new ingredient has three consequences, and they are the content of the article. The grading is topological, so the even part $A^{0}$ is a closed unital sub-sesquialgebra and the odd part $A^{1}$ is a closed bimodule over it, and the grading of a normed object is a topological direct sum. The derived action $a\star m=a\cdot\theta(m)$ is the composite of the action with the conjugation, so it is continuous as soon as both are, and in the normed case it satisfies the estimate $\lVert a\star m\rVert\le C\lVert a\rVert\lVert m\rVert$ with the constant of the action; the conjugation is the datum the sesquilinear kind adds, exactly as in Part I, and the action map of the graded layer is the case $\theta=\mathrm{id}$. And the graded $\varsigma$-compatibility, the identity $\theta(a\cdot m)=a^{*}\cdot\theta(m)$ on the even part together with its failure on the odd part, is a **closed** condition, because both sides are continuous; the even part of the algebra is therefore the largest part that can be an intertwiner for a module with a nontrivial odd action, and it is closed.

**The boundaries.** The graded algebra, the module, the degree rule and the Koszul sign are *The Graded Action on a Module over an Algebra* and *Involutive Graded Algebras*; the graded $\varsigma$-compatibility, the conjugation and the factorisation are *The Graded Sesquilinear Action*, which this article topologises and does not re-derive; the layer and the norm are *Topological Sesquialgebras* and *Banach Sesquialgebras*; the conjugate module and the two readings of the product are *The Conjugate Dual of a Sesquialgebra*; and the bounded operators of the layer are *Bounded Operators on a Sesquialgebra*. This article stops before the spectral theory of the later entries.

Throughout, $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$, $\varsigma$ is its continuous involution, and $A=A^{0}\oplus A^{1}$ is a **graded topological sesquialgebra** over $(\mathbb{K},\varsigma)$: a topological sesquialgebra that is the topological direct sum of two closed submodules, with $A^{i}A^{j}\subseteq A^{i+j}$ and $1\in A^{0}$. In the normed case the norm is submultiplicative, $\lVert xy\rVert\le\lVert x\rVert\lVert y\rVert$, the involution is isometric, $\lVert x^{*}\rVert=\lVert x\rVert$, and $A$ is the standard example $x\star y=xy^{*}$ in the sense of *Banach Sesquialgebras*. The module is a **graded topological module** $M=M^{0}\oplus M^{1}$, a topological direct sum of closed submodules with $A^{i}M^{j}\subseteq M^{i+j}$ and a continuous action $A\times M\to M$; a **graded sesquilinear module** carries in addition a **conjugation** $\theta$, a continuous involutive $\varsigma$-semilinear map of degree zero, $\theta^{2}=\mathrm{id}$ and $\theta(M^{j})\subseteq M^{j}$. Homogeneous elements carry the degree $\lvert x\rvert\in\{0,1\}$, and the derived action is

$$
\star:A\times M\longrightarrow M,\qquad a\star m=a\cdot\theta(m).
$$

## The Graded Topological Sesquialgebra

### The Grading and the Closed Parts

**Definition.** A **graded topological sesquialgebra** is a topological sesquialgebra $A$ with a decomposition $A=A^{0}\oplus A^{1}$ that is a topological direct sum, $A^{0}A^{0}\subseteq A^{0}$, $A^{1}A^{1}\subseteq A^{0}$, $A^{0}A^{1}\cup A^{1}A^{0}\subseteq A^{1}$, and $1\in A^{0}$; equivalently, the two projections $\pi_{i}:A\to A^{i}$ are continuous and the product respects the sum.

**Proposition (the parts are closed, and the even part is a sub-sesquialgebra).** In a graded topological sesquialgebra the projections are continuous, $A^{0}$ is a closed unital sub-sesquialgebra and $A^{1}$ is a closed $A^{0}$-bimodule. In the normed case the decomposition is the direct sum of the closed subspaces $A^{0}$ and $A^{1}$ and the norm is equivalent to $\lVert a^{0}\rVert+\lVert a^{1}\rVert$.

**Proof.** The definition of a topological direct sum makes the projections continuous and the pieces closed. The closure of $A^{0}$ under the product and the unit is the grading rule $A^{0}A^{0}\subseteq A^{0}$, and $A^{0}$ is complete when $A$ is, hence a closed sub-sesquialgebra; $A^{0}A^{1}\cup A^{1}A^{0}\subseteq A^{1}$ makes $A^{1}$ a bimodule. In the normed case a finite direct sum of closed subspaces is a topological direct sum, and all norms on the finite-dimensional space of the decomposition are equivalent. $\square$

**Proposition (the involution is even).** Let $*$ be a $\varsigma$-semilinear involution of a graded sesquialgebra whose parts are closed. Then $*$ preserves the grading, $*(A^{i})\subseteq A^{i}$, and it is continuous exactly when the graded pieces are given the topology of the object; in the normed case it is isometric.

**Proof.** The degree count of *The Graded Sesquilinear Action*, $\lvert x^{*}\rvert=\lvert x\rvert+\delta$ with $\delta=2\delta$, gives $\delta=0$, an algebraic statement independent of the topology; the continuity is the standing hypothesis of the normed case, where the involution is isometric. $\square$

**Remark.** The count is Part I and the topology adds nothing to it; what the topology adds is that the two parts are closed and that the degree is a continuous projection, so the even and the odd $*$-stable summands are genuine topological subobjects.

## The Graded Module and the Derived Action

### The Derived Action

**Definition.** Let $M$ be a graded topological module with conjugation $\theta$. The **derived action** of $A$ on $M$ is $a\star m=a\cdot\theta(m)$.

**Theorem (continuity and the bound).** The derived action is the composite of the action with the conjugation, $(a,m)\mapsto(a,\theta(m))\mapsto a\cdot\theta(m)$, so it is continuous whenever the action and $\theta$ are; if the action is separately continuous, so is the derived action. In the normed case, if the action satisfies $\lVert a\cdot m\rVert\le C\lVert a\rVert\lVert m\rVert$ and the conjugation satisfies $\lVert\theta(m)\rVert\le D\lVert m\rVert$, then

$$
\lVert a\star m\rVert\le CD\,\lVert a\rVert\lVert m\rVert,
$$

and with a normed module action ($C=1$) and an isometric conjugation ($D=1$) the constant is one.

**Proof.** The factorisation exhibits the derived action as a composite of continuous maps, and the estimate is the product of the two bounds. $\square$

**Proposition (the parities and the degree).** The derived action is linear in the algebra element and $\varsigma$-semilinear in the module element, and it is homogeneous:

$$
(\lambda a)\star m=\lambda(a\star m),\qquad a\star(\lambda m)=\varsigma(\lambda)(a\star m),\qquad A^{i}\star M^{j}\subseteq M^{i+j}.
$$

**Proof.** The two scalar rules are the linearity of the action in the first slot and the $\varsigma$-semilinearity of $\theta$; the degree is $\lvert a\star m\rvert=\lvert a\rvert+\lvert\theta(m)\rvert=\lvert a\rvert+\lvert m\rvert$, the conjugation being even. $\square$

**Remark.** The derived action is not an action and is not $\mathbb{K}$-bilinear; it is the module-level form of the derived product $x\star y=xy^{*}$ of the standard example, and $\theta=\mathrm{id}$ recovers the action map. The continuity is the only respect in which the topological statement differs from the algebraic one, and it is free, being a composite.

### The Module of Continuous Elements

**Proposition (the closure of the compatible even action).** Suppose a subset $M_{0}\subseteq M$ is invariant under $\theta$ and under every $a\cdot$ with $a\in A^{0}$, and that $\theta$ intertwines the even action on $M_{0}$, $\theta(a\cdot m)=a^{*}\cdot\theta(m)$ for $m\in M_{0}$. Then the same identity holds on the closure $\overline{M_{0}}$.

**Proof.** Both sides are continuous in $m$ and agree on the dense subset $M_{0}$. $\square$

**Remark.** The proposition is the topological use of the compatibility: an identity of continuous maps, checked on a dense set, extends to the closure. In the normed case every closed invariant submodule is available as such an $M_{0}$.

## The Graded $\varsigma$-Compatibility

**Definition.** A graded sesquilinear module over $A$ is **compatible** when

$$
\theta(a\cdot m)=a^{*}\cdot\theta(m)\qquad\text{for all }a\in A^{0},\ m\in M .
$$

**Theorem (the even part intertwines, the odd part obstructs).** The condition of the definition is a closed condition on the pair $(A,M,\theta)$, and the even part $A^{0}$ acts on a compatible module through $\theta$; the identity cannot be extended to the odd part, because $\theta(a\cdot m)=a^{*}\cdot\theta(m)$ fails for every conjugation as soon as some $a\in A^{1}$ acts nontrivially.

**Proof.** The two sides of the even identity are continuous, so the set of pairs for which it holds is closed, and its restriction to $A^{0}$ is the intertwining; this is the closedness. For the odd part, choose $a\in A^{1}$ with $a\cdot m\neq0$ for some $m$; the witness of *The Graded Sesquilinear Action*, §*The Graded $\varsigma$-Compatibility* is reproduced there for the matrix superalgebra, and it is a finite algebraic computation that uses neither a norm nor a limit. Its content is that the involution reverses the order of a product of two odd elements and does not reverse it on the even part, so the odd part cannot be intertwined. $\square$

**Example (the matrix superalgebra with the operator norm).** Let $A=M_{1|1}(\mathbb{C})$ with the parity grading, the conjugate transpose as the involution and the operator norm, and let $M=\mathbb{C}^{1|1}$ with the Euclidean norm, the standard action and the coefficientwise conjugation $\theta(\lambda f_{1}+\mu f_{2})=\varsigma(\lambda)f_{1}+\varsigma(\mu)f_{2}$. The module is compatible: the conjugate transpose fixes the two idempotents of $A^{0}$, so the identity holds on $A^{0}$. It fails on $A^{1}$: with $a=E_{12}$ and $m=f_{2}$ one has $\theta(a\cdot m)=f_{1}\neq0=(a^{*}\cdot\theta(m))$. Both are continuous modules with an isometric conjugation, so the derived action is bounded with constant one, and the failure is visible at finite witnesses.

**Remark.** The even part is therefore the largest part of $A$ on which $\theta$ can be an intertwiner for a module with a nontrivial odd action, and it is closed. In the normed case the compatibility can be stated as the agreement of the two bounded operators $m\mapsto\theta(a\cdot m)$ and $m\mapsto a^{*}\cdot\theta(m)$ of norm at most $\lVert a\rVert D$ and $\lVert a^{*}\rVert D$; that both are defined is the content of the bound of the derived action.

## The Bilinear Collapse

**Theorem (the degeneration).** Put $\varsigma=\mathrm{id}$ and $*=\mathrm{id}$, so that $A$ is a commutative topological algebra, and take $\theta=\mathrm{id}$. Then the derived action is the action, the conjugation adds nothing, and the article reduces to *The Graded Action on a Module over an Algebra*.

**Proof.** With $\varsigma=\mathrm{id}$ the module is a topological module in the ordinary sense and the derived action is $a\cdot m$; with $*=\mathrm{id}$ the involution is trivial and the product is bilinear, so the object is a topological algebra of the bilinear layer; and the compatibility of the definition is the identity $\theta(a\cdot m)=a\cdot\theta(m)$, which $\theta=\mathrm{id}$ satisfies. The degree rule and the module structure are those of the graded action. $\square$

**Remark.** As in *Sesquialgebras*, the collapse has the two independent steps of *Topological Sesquialgebras*: $\varsigma=\mathrm{id}$ removes the conjugate-linearity and $*=\mathrm{id}$ removes the involution, and what is lost is the conjugation and its obstruction. The continuous graded sesquilinear action is therefore a structure on top of the graded action, with one more datum and one more obstruction, and the topology is carried along by both.

## Worked Case

### The Matrix Superalgebra

Let $A=M_{1|1}(\mathbb{C})$ with the even part spanned by $E_{11},E_{22}$, the odd part by $E_{12},E_{21}$, the conjugate transpose and the operator norm; let $M=\mathbb{C}^{1|1}$ with the Euclidean norm, the standard action $E_{ij}\cdot f_{k}=\delta_{jk}f_{i}$ and the coefficientwise conjugation $\theta$. The grading is a topological direct sum with isometric projections, $A^{0}$ is the closed unital subalgebra of the diagonal matrices and $A^{1}$ the closed off-diagonal bimodule. The derived action $a\star m=a\cdot\theta(m)$ is continuous with $\lVert a\star m\rVert\le\lVert a\rVert\lVert m\rVert$ because the action is the standard one of norm one and the conjugation is isometric; it is $\mathbb{C}$-linear in $a$ and $\varsigma$-semilinear in $m$, and homogeneous of degree $\lvert a\rvert+\lvert m\rvert$. The module is compatible on $A^{0}$ and the identity fails on $A^{1}$ at the witness $a=E_{12}$, $m=f_{2}$; the operators of the two sides of the odd identity have the same norm $\lVert a\rVert D$ and differ, so the compatibility is a genuine restriction and not a norm coincidence. On the regular module $M=A$ with $\theta=*$ the even identity fails already at $E_{11}E_{12}$ against $E_{11}^{*}(E_{12}^{*})$, as *The Graded Sesquilinear Action* records; the topology changes nothing, the failure being algebraic.

### The Degenerate Odd Part

Let $A=\mathbb{K}[x]/(x^{2})$ with $x$ odd, $A^{0}=\mathbb{K}$, $A^{1}=\mathbb{K}x$ and $x^{2}=0$, with the norm $\lvert\cdot\rvert$ of $\mathbb{K}$ on both pieces and the identity involution. The grading is topological, the involution is even and isometric, and the odd part is square-zero, so the two classes of the involution coincide and the matrix witness of the compatibility is unavailable: the odd part acts trivially on the module, $A^{1}\cdot M=0$, and there is no odd obstruction. The example is the degenerate branch of the theorem, and it shows that the obstruction is a statement about the product of the odd part and not about the grading.

## Summary

A graded topological sesquialgebra is a topological sesquialgebra whose grading is a topological direct sum of closed parts, with the even part a closed unital sub-sesquialgebra and the odd part a closed bimodule; the involution is even by the degree count of the algebraic layer, and in the normed case it is isometric. A graded sesquilinear module is a graded topological module with a continuous involutive $\varsigma$-semilinear conjugation $\theta$ of degree zero, and the derived action $a\star m=a\cdot\theta(m)$ is the action composed with $\theta$: it is continuous as soon as the action and the conjugation are, it is linear in the algebra and $\varsigma$-semilinear in the module, homogeneous of the degree sum, and bounded by $CD\lVert a\rVert\lVert m\rVert$ in the normed case, with constant one for a normed module action and an isometric conjugation. The graded $\varsigma$-compatibility is the closed identity $\theta(a\cdot m)=a^{*}\cdot\theta(m)$ on the even part, holding for the diagonal module and failing for the regular module with a nontrivial involution, together with the failure on the odd part, which the matrix superalgebra exhibits at a finite witness and which the degenerate square-zero odd part removes. In the bilinear case the involution and the conjugation are the identity and the article is the graded action of *The Graded Action on a Module over an Algebra*.

## Summary of Notation

| symbol | meaning |
|---|---|
| $A=A^{0}\oplus A^{1}$ | a graded topological sesquialgebra, a topological direct sum of closed parts |
| $A^{0}$ | the closed unital sub-sesquialgebra of the even part |
| $A^{1}$ | the closed $A^{0}$-bimodule of the odd part |
| $M=M^{0}\oplus M^{1}$ | a graded topological module with a continuous action |
| $\theta$ | the conjugation, continuous, involutive, $\varsigma$-semilinear, of degree zero |
| $a\star m=a\cdot\theta(m)$ | the derived action, continuous, linear in $a$ and $\varsigma$-semilinear in $m$ |
| $\lVert a\star m\rVert\le CD\lVert a\rVert\lVert m\rVert$ | the bound, with constants of the action and of the conjugation |
| $\theta(a\cdot m)=a^{*}\cdot\theta(m)$ | the graded $\varsigma$-compatibility, a closed condition on the even part |
| $A^{1}\cdot M=0$ | the degenerate odd part, where the odd obstruction is absent |

## Further Reading

- Manfred Scheunert, *The Theory of Lie Superalgebras* (Lecture Notes in Mathematics 716, Springer, 1979), for the graded algebras, the Koszul sign and the two classes of order-two anti-maps, the conventions of the graded layer.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, volume 1 (Academic Press, 1983), for the continuity of the action of a topological algebra on a topological module and the bound of a continuous bilinear map.
- John B. Conway, *A Course in Functional Analysis* (Graduate Texts in Mathematics 96, Springer, second edition, 1990), for the direct sums of closed subspaces, the continuity of a linear map by the closed graph theorem and the standard estimates of the normed case.
- V. S. Varadarajan, *Supersymmetry for Mathematicians: An Introduction* (Courant Lecture Notes 11, American Mathematical Society, 2004), for the superalgebras, the supertranspose and the graded modules, the setting in which the matrix superalgebra of the worked case is read.
