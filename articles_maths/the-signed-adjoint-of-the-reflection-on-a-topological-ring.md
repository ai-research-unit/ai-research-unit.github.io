
# __The Signed Adjoint of the Reflection on a Topological Ring__

## Introduction

A reflection on a ring with a grade involution $\alpha$ and an involution $\sigma$ is the signed two-sided operator $\rho_u(x) = u\,\alpha(x)\,u^{-1}$, the conjugation by a unit composed with the grade involution; it is the signed sandwich $\Sigma^\alpha_{u,u^{-1}}$, its square is the inner automorphism by $u\alpha(u)$, and it is an involution exactly when $u\alpha(u)$ is central. Its signed adjoint with respect to the form of the category is the reflection in the element $\delta(u) = \sigma\alpha(u)$, so the reflection is self-adjoint exactly when the defect $\delta(u)u^{-1}$ is central; when the defect is not central the self-adjointness fails and the adjoint is a genuinely different reflection. This article computes the adjoint of the reflection, proves the self-adjointness criterion and its failure, identifies the nondegenerate self-adjoint reflections, and reads the whole thing through the topology, where the reflection is a homeomorphism, its fixed set is closed, and the self-adjointness passes to the completion.

The article assumes the topological ring and the bounded operators from *Topological Rings and Fields* and *Operators on a Topological Ring*; the reflection as a signed two-sided operator, its square and its fixed set from *Reflections as Signed Two-Sided Operators on a Topological Ring*; the signed sandwich, its adjoint, its inverse and its composition from *The Signed Adjoint Sandwich on a Topological Ring*; the involution, the grade involution and the closedness of the fixed set from *Involutive Topological Rings and Fields*; the operator adjoint and the form of the category from *The Involution on Bounded Operators of a Ring*; and the self-adjoint and unitary elements from *Involutive Topological Division Rings*.

Throughout, $R$ is a Hausdorff topological ring with a continuous involution $\sigma$, a continuous grade involution $\alpha$ commuting with $\sigma$, a continuous trace $\tau$ with $\tau\circ\alpha = \tau$ and the **form of the category** $\{x,y\} = \tau(x\sigma(y))$; $\delta = \sigma\alpha$; $u$ is a unit; the **reflection** is $\rho_u = \Sigma^\alpha_{u,u^{-1}}$, that is

$$
\rho_u(x) = u\,\alpha(x)\,u^{-1} ;
$$

and $\rho_v$ denotes the signed sandwich $\Sigma^\alpha_{v,v^{-1}}$, so that the adjoint reflection is written $\rho_{\delta(u)}$ when its parameter need not be the same as $u$.

## The Reflection and its Square

**Theorem (the square and the involution case).** The reflection is additive, bijective and bounded, and its square is the conjugation by $u\alpha(u)$:

$$
\rho_u^2(x) = u\alpha(u)\,x\,\bigl(u\alpha(u)\bigr)^{-1} .
$$

Hence $\rho_u$ is an **involution**, $\rho_u^2 = \mathrm{id}$, exactly when $u\alpha(u)$ is central; in that case it is a reflection of order two and its fixed set is $\{x : u\alpha(x) = xu\}$, closed in $R$.

**Proof.** $\rho_u(\rho_u(x)) = u\alpha(u\alpha(x)u^{-1})u^{-1} = u\alpha(u)\,\alpha^2(x)\,\alpha(u)^{-1}u^{-1} = u\alpha(u)\,x\,(u\alpha(u))^{-1}$, using that $\alpha$ is an automorphism and $\alpha^2 = \mathrm{id}$. The square is the identity exactly when the conjugating element $u\alpha(u)$ is central; the fixed set is the solution set of the continuous equation $u\alpha(x)u^{-1} = x$, hence closed.

**Remark (the degenerate square).** When $u\alpha(u)$ is not central, $\rho_u$ has order two only modulo the centre, and its square is the inner automorphism $\operatorname{inn}_{u\alpha(u)}$; the reflection is then not an involution on the ring but an operation of order two on the centre. The article keeps the involution case and notes the degenerate one at the boundary.

## The Signed Adjoint

**Theorem (the explicit form).** With respect to the form of the category,

$$
\rho_u^\dagger = \Sigma^\alpha_{\delta(u),\,\delta(u)^{-1}} = \rho_{\delta(u)} ,
$$

so the signed adjoint of a reflection is the reflection in the element $\delta(u) = \sigma\alpha(u)$; the adjoint is again a reflection, and the adjoint operation is an involution on the class of reflections.

**Proof.** This is $(\Sigma^\alpha_{u,u^{-1}})^\dagger = \Sigma^\alpha_{\delta(u),\delta(u^{-1})}$ of *The Signed Adjoint Sandwich on a Topological Ring*, together with $\delta(u^{-1}) = \delta(u)^{-1}$ because $\delta$ is an involution.

**Theorem (self-adjointness).** The reflection is self-adjoint, $\rho_u^\dagger = \rho_u$, exactly when

$$
\Sigma^\alpha_{\delta(u),\delta(u)^{-1}} = \Sigma^\alpha_{u,u^{-1}} \iff \delta(u) = \lambda u \text{ for some central } \lambda \iff \delta(u)u^{-1}\in Z(R) .
$$

In particular a **$\delta$-symmetric** unit, $\delta(u) = u$, gives a self-adjoint reflection, and so does $\delta(u) = \lambda u$ with $\lambda$ central; the set of units $u$ for which $\rho_u$ is self-adjoint is closed when the multiplication and the inversion are continuous.

**Proof.** Two signed sandwiches with unit parameters agree as operators exactly when their rank-one tensors agree, that is $\delta(u) = \lambda u$ and $\delta(u)^{-1} = \lambda^{-1}u^{-1}$ for a central $\lambda$; dividing gives the condition $\delta(u)u^{-1}\in Z(R)$. The closure is that the condition is the vanishing of the commutators $[\delta(u)u^{-1},x]$ for all $x$, a closed condition by continuity.

**Corollary (failure in the degenerate case).** If $\delta(u)u^{-1}$ is not central, the reflection is not self-adjoint: its adjoint is the reflection $\rho_{\delta(u)}$, which conjugates by the different unit $\delta(u)$, and the two operators agree only on the elements commuting with $\delta(u)u^{-1}$. The self-adjointness holds for the $\delta$-symmetric units and their central multiples, and fails as soon as the unitarity defect leaves the centre.

**Proof.** The adjoint is $\rho_{\delta(u)}$ and the two differ when $\delta(u)u^{-1}$ is not central, by the equality criterion read in the converse direction; the agreement on the centraliser is the comparison of the two conjugations, $uxu^{-1}$ and $\delta(u)x\delta(u)^{-1}$, which coincide exactly when $x$ commutes with $\delta(u)u^{-1}$.

## The Reflection and the Form

**Theorem (form preservation).** The reflection preserves the form, $B(\rho_u x, \rho_u y) = B(x,y)$ for all $x,y$, exactly when it is unitary, that is exactly when $\delta(u)\alpha(u)$ and $u\sigma(u)$ are central; in general the defect of form preservation is measured by the two central products, and the reflection is an isometry of the form precisely on the unitary elements.

**Proof.** Form preservation is the identity $\rho_u^\dagger\rho_u = \mathrm{id}$, which for the reflection $\rho_u = \Sigma^\alpha_{u,u^{-1}}$ is the unitarity criterion of *The Signed Adjoint Sandwich on a Topological Ring*, giving the centrality of the two products.

**Corollary (the three classes of reflections).** The reflections fall into three classes: the **involutions**, with $u\alpha(u)$ central; the **self-adjoint** reflections, with $\delta(u)u^{-1}$ central; and the **orthogonal** (form-preserving, unitary) reflections, with $\delta(u)\alpha(u)$ and $u\sigma(u)$ central. The self-adjointness and the orthogonality are independent conditions on a general unit; a $\delta$-symmetric unitary with $u\alpha(u)$ central is an orthogonal involution, the model case of a reflection of the ring.

**Proof.** The three conditions are the three theorems of this article and of *The Signed Adjoint Sandwich on a Topological Ring*; the model case combines $\delta(u) = u$ with the unitarity and the involution conditions.

## The Three Conditions

**Theorem (involution, self-adjointness, unitarity).** For a reflection the three conditions are

$$
\rho_u^2 = \mathrm{id} \iff u\alpha(u)\in Z(R) , \qquad \rho_u^\dagger = \rho_u \iff \delta(u)u^{-1}\in Z(R) , \qquad \rho_u^\dagger \rho_u = \mathrm{id} \iff \delta(u)\alpha(u)\in Z(R) \text{ and } u\sigma(u)\in Z(R) .
$$

The reflection is an orthogonal involution, that is an involution and self-adjoint, exactly when both $u\alpha(u)$ and $\delta(u)u^{-1}$ are central; it is unitary when the two products of the sandwich criterion are central.

**Proof.** The first is the square computation; the second is the self-adjointness theorem; the third is the unitarity of *The Signed Adjoint Sandwich on a Topological Ring* specialised to $b = u^{-1}$, where the two product equations are automatic and only the centrality of $\delta(u)\alpha(u)$ and of $u\sigma(u)$ remains.

**Remark (the model case).** When $\alpha = \mathrm{id}$ the reflection is the conjugation $uxu^{-1}$, $\delta = \sigma$, and the self-adjointness condition is $\sigma(u)u^{-1}\in Z(R)$, that is the unitarity defect of $u$ lies in the centre; the $\sigma$-symmetric units give the self-adjoint conjugations. When in addition $\sigma = \mathrm{id}$, every reflection is self-adjoint and the condition is void, the degenerate commutative case.

## Topological Compatibility

**Theorem (continuity, closedness and the completion).** A reflection is a homeomorphism, its fixed set is closed, the self-adjointness defect is continuous in $u$, and the self-adjoint reflections form a closed subset of the operator algebra; the reflection of the completion has the adjoint computed by the extended involution, and self-adjointness passes to the completion.

**Proof.** $\rho_u = L_u\alpha R_{u^{-1}}$ is a composite of homeomorphisms when $u$ is a unit and the multiplication and inversion are continuous, hence a homeomorphism; the fixed set is closed by the first theorem; the defect $u\mapsto\delta(u)u^{-1}$ is continuous, and the centrality condition is closed; the completion statement is *The Involution and the Completion of a Ring* applied to the operator algebra.

**Corollary (compactness).** On a locally compact ring the fixed set of an involutive reflection is closed and, when bounded, compact; the orthogonal involutions of the operator algebra form a closed set, and on the matrix algebra over a local field the $\delta$-symmetric unitaries realise the reflections of the compact unitary group.

**Proof.** Closed and bounded in a locally compact space is compact; the matrix statement is the example below.

## Examples

**Example (the orthogonal reflection).** $R = M_n(\mathbb{R})$, $\sigma$ the transpose, $\alpha = \mathrm{id}$, and $u$ a symmetric involution $u = I - 2vv^{\mathrm t}$ with $v^{\mathrm t}v = 1$; $\rho_u(x) = uxu^{-1} = uxu$ is the reflection in the hyperplane orthogonal to $v$, it is an involution because $u^2 = I$ is central, and it is self-adjoint because $\delta(u) = u^{\mathrm t} = u$, so $\delta(u)u^{-1} = I$ is central.

**Example (the graded reflection).** With a $\mathbb{Z}/2$-grading and a homogeneous unit $u$, $u\alpha(u) = \pm u^2$ according to the degree; the reflection is an involution when $u^2$ is central with the sign of the degree, and self-adjoint when $\sigma\alpha(u) = u$ up to a central factor.

**Example (the degenerate case).** For $R = M_n(\mathbb{R})$ and a non-symmetric unit $u$, the defect $\delta(u)u^{-1} = u^{\mathrm t}u^{-1}$ is non-central in general; the reflection $\rho_u$ is not self-adjoint, and its adjoint is the reflection $\rho_{u^{\mathrm t}}$, the reflection by the transpose of $u$, agreeing with $\rho_u$ only on the centraliser of the defect.

**Example (the complex reflection).** $R = \mathbb{C}$, $\sigma$ the conjugation, $\alpha = \mathrm{id}$, $u = i$; the reflection $\rho_u(x) = uxu^{-1} = x$ is the identity, self-adjoint trivially; for $u = i$ the defect $\bar u u^{-1} = (-i)/i = -1$ is central and the criterion holds.

## Summary

The reflection $\rho_u(x) = u\alpha(x)u^{-1} = \Sigma^\alpha_{u,u^{-1}}$ has square the conjugation by $u\alpha(u)$, so it is an involution exactly when $u\alpha(u)$ is central, with fixed set $\{x : u\alpha(x) = xu\}$, closed. Its signed adjoint with respect to the form of the category is $\rho_u^\dagger = \Sigma^\alpha_{\delta(u),\delta(u)^{-1}} = \rho_{\delta(u)}$, the reflection in $\delta(u) = \sigma\alpha(u)$; the reflection is self-adjoint exactly when $\delta(u)u^{-1}$ is central, in particular for the $\delta$-symmetric units and their central multiples, and it fails as soon as the defect leaves the centre, the adjoint being then the reflection in the different unit $\delta(u)$. The three conditions — involution, self-adjointness and unitarity — are the centrality of $u\alpha(u)$, of $\delta(u)u^{-1}$, and of $\delta(u)\alpha(u)$ and $u\sigma(u)$. A reflection is a homeomorphism, its fixed set is closed, the self-adjoint reflections are closed in the operator algebra, and self-adjointness passes to the completion.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\rho_u(x) = u\alpha(x)u^{-1}$ | The reflection |
| $\rho_u = \Sigma^\alpha_{u,u^{-1}}$ | The reflection is a signed sandwich |
| $\rho_u^2 = \operatorname{inn}_{u\alpha(u)}$ | The square; involution iff $u\alpha(u)$ central |
| $\operatorname{Fix}(\rho_u) = \{x : u\alpha(x) = xu\}$ | The fixed set, closed |
| $\rho_u^\dagger = \Sigma^\alpha_{\delta(u),\delta(u)^{-1}} = \rho_{\delta(u)}$ | The signed adjoint |
| $\delta(u)u^{-1}\in Z(R)$ | Self-adjointness criterion |
| $\delta(u) = u$ | The $\delta$-symmetric (nondegenerate) reflections |
| $u\alpha(u)$, $\delta(u)\alpha(u)$, $u\sigma(u)$ central | Involution and unitarity conditions |

## Further Reading

- Nathan Jacobson, *Structure of Rings*, American Mathematical Society Colloquium Publications 37 (1964), for the conjugations and the reflections of the regular representation and their adjoints.
- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the self-adjoint and the skew operators of a ring with involution.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the reflections of a unitary group and their relation to the involution.
- Nicolas Bourbaki, *Algebra I*, Chapters 1–3 (Springer, 1998), for the reflections, the hyperplane of fixed vectors and the adjoint under a form.
- Seth Warner, *Topological Fields* (North-Holland, 1989), for the continuous operators and the closed fixed sets of a topological ring.
