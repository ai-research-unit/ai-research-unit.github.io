
# __The Signed Adjoint Sandwich on a Topological Ring__

## Introduction

The signed sandwich is the two-sided operator $\Sigma^\alpha_{a,b}(x) = a\,\alpha(x)\,b$, the sandwich twisted by the grade involution $\alpha$, and it is the operator that realises the reflections and the signed conjugations. Its adjoint with respect to the form of the category is again a signed sandwich, now with the two parameters replaced by their images under $\delta = \sigma\alpha$, and the comparison of the adjoint with the inverse produces the unitarity condition: the sandwich is unitary exactly when a certain product is central and a second product is the unit, the centrality being forced by the two-sidedness of the operator. This article computes the adjoint, the inverse and the composition of the signed sandwiches, derives the exact unitarity condition, specialises it to the reflection and the one-sided operators of the following articles, and reads the whole thing through the topology, where the grade involution is continuous, the adjoint is continuous and the unitary sandwiches are the form-preserving ones.

The article assumes the topological ring and the bounded operators from *Topological Rings and Fields* and *Operators on a Topological Ring*; the left and right multiplications from *The Left and Right Multiplication Operators on a Topological Ring*; the signed sandwich, its factorisation, its composition laws and its inverse from *The Signed Sandwich on a Topological Ring*; the involution, the grade involution and the closedness of the fixed set from *Involutive Topological Rings and Fields*; the operator adjoint and the form of the category from *The Involution on Bounded Operators of a Ring*; and the adjoint of the left multiplication from *The Adjoint of the Left Multiplication on a Topological Ring*. The reflection is *The Signed Adjoint of the Reflection on a Topological Ring*, the one-sided operator is *The Signed Adjoint of the Left Multiplication on a Topological Ring*, and the graded case over a module is *The Graded Adjoint Action on a Module over a Topological Ring*.

Throughout, $R$ is a Hausdorff topological ring with a continuous involution $\sigma$, a continuous $\sigma$-invariant trace $\tau$ with $\tau\circ\alpha = \tau$, and a continuous **grade involution** $\alpha$, an involutive automorphism commuting with $\sigma$; $\delta = \sigma\alpha$ is the twist, an involutive anti-automorphism of order two commuting with $\alpha$ and $\sigma$; the **form of the category** is $\{x,y\} = \tau(x\sigma(y))$; the **signed sandwich** is

$$
\Sigma^\alpha_{a,b}(x) = a\,\alpha(x)\,b = (L_a\,\alpha\,R_{\alpha(b)})(x) ;
$$

and the adjoint $T^\dagger$ is defined by $\{Tx,y\} = \{x,T^\dagger y\}$.

## The Adjoint, the Inverse and the Composition

**Theorem (the explicit form of the adjoint).** With respect to the form of the category,

$$
\bigl(\Sigma^\alpha_{a,b}\bigr)^\dagger = \Sigma^\alpha_{\delta(a),\delta(b)} , \qquad \delta = \sigma\alpha ,
$$

so the adjoint of a signed sandwich is the signed sandwich of the two $\delta$-images, with the order of the parameters **not** reversed, and the adjoint operation is an involution on the class of signed sandwiches.

**Proof.** By the factorisation and the anti-multiplicativity of the adjoint, $(\Sigma^\alpha_{a,b})^\dagger = (L_a\alpha R_{\alpha(b)})^\dagger = R_{\alpha(b)}{}^\dagger\alpha^\dagger L_a{}^\dagger = R_{\sigma(\alpha(b))}\alpha L_{\sigma(a)}$, using $(L_a)^\dagger = L_{\sigma(a)}$, $(R_b)^\dagger = R_{\sigma(b)}$ and $\alpha^\dagger = \alpha$ from $\tau\circ\alpha = \tau$. Applying to $x$ gives $\alpha(\sigma(a)\,x)\,\sigma(\alpha(b)) = \sigma(\alpha(a))\,\alpha(x)\,\sigma(\alpha(b)) = \delta(a)\,\alpha(x)\,\delta(b)$, which is $\Sigma^\alpha_{\delta(a),\delta(b)}(x)$; the double adjoint is $\delta^2 = \mathrm{id}$.

**Proposition (inverse and composition).** The inverse is

$$
\bigl(\Sigma^\alpha_{a,b}\bigr)^{-1} = \Sigma^\alpha_{\alpha(a)^{-1},\,\alpha(b)^{-1}} , \qquad a, b \text{ units} ,
$$

and the composition of two signed sandwiches is a two-sided operator but not a signed sandwich,

$$
\Sigma^\alpha_{c,d}\circ\Sigma^\alpha_{a,b} = L_{c\alpha(a)}\,R_{\alpha(b)d} .
$$

**Proof.** $\Sigma^\alpha_{c,d}(\Sigma^\alpha_{a,b}(x)) = c\,\alpha(a\alpha(x)b)\,d = c\,\alpha(a)\,x\,\alpha(b)\,d$, using $\alpha^2 = \mathrm{id}$ and that $\alpha$ is an automorphism; the inverse is the case in which the result is $x$ for all $x$, and the composition formula is the same computation.

## The Unitarity Condition

**Theorem (the exact condition).** The signed sandwich is **unitary** for the form of the category,

$$
\bigl(\Sigma^\alpha_{a,b}\bigr)^\dagger\Sigma^\alpha_{a,b} = \Sigma^\alpha_{a,b}\bigl(\Sigma^\alpha_{a,b}\bigr)^\dagger = \mathrm{id} ,
$$

exactly when the two products are central and their products with the complements are the unit:

$$
\delta(a)\alpha(a) \in Z(R) , \quad a\sigma(a)\in Z(R) , \quad \delta(a)\alpha(a)\,\alpha(b)\delta(b) = 1 , \quad a\sigma(a)\,\sigma(b)b = 1 .
$$

**Proof.** By the theorem and the composition formula, $(\Sigma^\alpha_{a,b})^\dagger\Sigma^\alpha_{a,b} = \Sigma^\alpha_{\delta(a),\delta(b)}\circ\Sigma^\alpha_{a,b} = L_{\delta(a)\alpha(a)}R_{\alpha(b)\delta(b)}$, and $L_cR_d = \mathrm{id}$ iff $c\in Z(R)$ and $cd = 1$: the necessity of $cd=1$ is $x=1$, and the necessity of centrality is that $cxd=x$ for all $x$ forces $c$ to commute with every $x$ once $d = c^{-1}$. The other order is $L_{a\sigma(a)}R_{\sigma(b)b}$ by the same computation, using $\alpha\delta = \alpha\sigma\alpha = \sigma$, giving the second pair of conditions.

**Corollary (the normalised unitary sandwiches).** If the two products are the unit, $\delta(a)\alpha(a) = 1$ and $\alpha(b)\delta(b) = 1$, the sandwich is unitary; and the sandwich is unitary with the products central and mutually inverse in general. For $b = \alpha(a)^{-1}$, the case of the reflection, the product conditions are automatic and unitarity reduces to the centrality of $\delta(a)\alpha(a)$ and of $a\sigma(a)$.

**Proof.** The first statement is that the unit is central; for the reflection, $\delta(a)\alpha(a)\,\alpha(b)\delta(b) = \delta(a)\alpha(a)\cdot\alpha(a)^{-1}\delta(a)^{-1} = 1$ by $\delta^2 = \mathrm{id}$, and $a\sigma(a)\sigma(b)b = a\sigma(a)\sigma(a)^{-1}a^{-1} = 1$; the conditions reduce to centrality.

**Remark (the group case).** On a topological group the analogous identity criterion for a signed sandwich involves the centre, $c'^{-1}c\in Z(G)$, by *The Signed Adjoint Sandwich on a Topological Group*; the ring condition is the same shape, and the centrality is not an artefact of the proof but a genuine two-sided condition. The normalised condition $\delta(a)\alpha(a) = 1$, $\alpha(b)\delta(b)=1$ is the case in which the two central products are each the unit.

## The Equality Criterion and the Inner Case

**Theorem (the equality of two sandwiches).** For units $a,b,c,d$, two signed sandwiches agree as operators,

$$
\Sigma^\alpha_{a,b} = \Sigma^\alpha_{c,d} \iff (c, d) = (\lambda a, \lambda^{-1}b) \text{ for some } \lambda\in Z(R)^\times .
$$

Hence the parametrisation has kernel the central units embedded as $z\mapsto(z,z^{-1})$, and it is injective on the pairs modulo the action $(a,b)\mapsto(za,z^{-1}b)$ of $Z(R)^\times$; the neutral element of the signed family is $\Sigma^\alpha_{1,1} = \alpha$.

**Proof.** The operator $\Sigma^\alpha_{a,b}$ is the tensor $a\otimes b$ acting by $x\mapsto a\alpha(x)b$; since $\alpha$ is onto, equality of two signed sandwiches is equality of the unsigned sandwiches $\Sigma_{a,b} = \Sigma_{c,d}$, that is $axb = cxd$ for all $x$. Setting $x = a^{-1}wd^{-1}$ gives $wd^{-1}b = ca^{-1}w$ for all $w$, so $ca^{-1} = d^{-1}b = z$ is central and $c = za$, $b = zd$, that is $d = z^{-1}b$; conversely a central $z$ gives $cxd = zaxz^{-1}b = axb$. The kernel is the case $c = d = 1$ and the neutral statement is $\Sigma^\alpha_{1,1} = \alpha$.

**Corollary (self-adjointness of a sandwich).** The signed sandwich is self-adjoint, $(\Sigma^\alpha_{a,b})^\dagger = \Sigma^\alpha_{a,b}$, exactly when there is a central unit $\lambda$ with

$$
\delta(a) = \lambda a , \qquad \delta(b) = \lambda^{-1}b ,
$$

that is when both defects $\delta(a)a^{-1}$ and $\delta(b)b^{-1}$ lie in the centre and are mutually inverse; in particular the sandwich with $\delta(a) = a$ and $\delta(b) = b$ is self-adjoint.

**Proof.** By the adjoint theorem and the equality criterion, $(\Sigma^\alpha_{a,b})^\dagger = \Sigma^\alpha_{\delta(a),\delta(b)}$ equals $\Sigma^\alpha_{a,b}$ exactly when $\delta(a) = \lambda a$ and $\delta(b) = \lambda^{-1}b$ for a central unit $\lambda$; multiplying the two relations gives $\delta(a)\delta(b) = ab$, which holds automatically from $\delta(ab) = \delta(a)\delta(b)$ read with $\delta^2 = \mathrm{id}$, and the defect conditions are the stated centrality.

**Corollary (the involutive sandwiches).** The square of a signed sandwich is

$$
\bigl(\Sigma^\alpha_{a,b}\bigr)^2 = L_{a\alpha(a)}\,R_{\alpha(b)b} ,
$$

so the sandwich is an involution exactly when $a\alpha(a)$ is central and $a\alpha(a)\alpha(b)b = 1$, and it is an involution and unitary at once only under the conjunction of the two sets of centrality and unit conditions.

**Proof.** The composition formula with the two parameters equal gives the square; the identity $L_cR_d = \mathrm{id}$ is $c$ central and $cd = 1$ by the unitarity theorem; the conjunction is the two criteria read together.

**Remark (the inner case).** When the grade involution is inner, $\alpha = c_z$, the signed sandwich is the unsigned sandwich $\Sigma_{az,z^{-1}b}$ by *The Signed Sandwich on a Topological Ring*, the signed and unsigned families coincide, and the signed adjoint is then computed with $\delta = \sigma c_z$; the degeneracy removes the distinction between the signed and the unsigned theory without changing the adjoint formulas.

## Topological Compatibility

**Theorem (continuity and closedness).** The signed sandwich is bounded and continuous when $\alpha$ is continuous and the multiplication is continuous; the adjoint map is continuous on the adjointable operators; and the set of unitary signed sandwiches is closed in the operator algebra under the topology of bounded convergence.

**Proof.** The signed sandwich is the composite of continuous bounded operators and is therefore bounded and continuous; the adjoint map is continuous by *The Involution on Bounded Operators of a Ring*; the unitary condition is the conjunction of two closed conditions, the centrality (a closed condition on the product) and the two product equations (closed by continuity), so its solution set is closed.

**Corollary (the unitary sandwiches are form-preserving).** A unitary signed sandwich is a form-preserving operator, and it is invertible with inverse $\bigl(\Sigma^\alpha_{a,b}\bigr)^{-1} = \Sigma^\alpha_{\alpha(a)^{-1},\alpha(b)^{-1}}$. The unitary signed sandwiches are closed under the adjoint and under inversion; they do **not** in general form a subgroup of the form-preserving operators, because the composite of two signed sandwiches is the two-sided operator $L_{c\alpha(a)}R_{\alpha(b)d}$, which is a signed sandwich only in the special cases of the reflection $b = d$; the subgroup generated is the closed group of form-preserving operators carrying the grading data, and the reflections of the next article are the subfamily closed under composition.

**Proof.** A unitary operator preserves the form by definition, and the inverse of an operator preserving a nondegenerate form preserves it; the inverse formula is the proposition, and the adjoint of a unitary sandwich is its inverse, a sandwich, by unitarity. The failure of closure is the composition formula, which returns a two-sided operator with the left factor $c\alpha(a)$ and the right factor $\alpha(b)d$; the reflection case $b = a^{-1}$, $d = c^{-1}$ returns a signed sandwich by the reflection composition of *The Signed Adjoint of the Reflection on a Topological Ring*.

## Examples

**Example (the matrix sandwich).** $R = M_n(F)$ with the transpose $\sigma$, the trace form and the grade involution $\alpha$ from a $\mathbb{Z}/2$-grading; the signed sandwich is $X\mapsto A\alpha(X)B$, its adjoint is $X\mapsto \delta(A)\alpha(X)\delta(B)$ with $\delta = \sigma\alpha$, and the unitary sandwiches are those with the central products equal to the unit, which for the transpose are the sandwich pairs whose products are scalar.

**Example (the conjugation).** For $\alpha = \mathrm{id}$, the signed sandwich is $x\mapsto axb$, its adjoint is $x\mapsto\sigma(a)x\sigma(b)$, and the sandwich is unitary when $\sigma(a)a$ is central and $\sigma(a)a b\sigma(b) = 1$; this is the unsigned sandwich of *The Adjoint of the Left Multiplication on a Topological Ring* read with the two parameters.

**Example (the grade involution).** For $a = b = 1$ the signed sandwich is the grade involution $\alpha$, whose adjoint is $\Sigma^\alpha_{\delta(1),\delta(1)} = \alpha$; it is self-adjoint and unitary, the latter automatic.

**Example (the reflection).** For $b = u^{-1}$ the signed sandwich is the reflection $\rho_u$; it is unitary exactly when $\delta(u)\alpha(u)$ and $u\sigma(u)$ are central, which is the unitarity of the reflection computed independently in *The Signed Adjoint of the Reflection on a Topological Ring*.

## Summary

The signed sandwich $\Sigma^\alpha_{a,b}(x) = a\alpha(x)b$ has signed adjoint $\Sigma^\alpha_{\delta(a),\delta(b)}$ with respect to the form of the category, where $\delta = \sigma\alpha$ and the parameters are not reversed; its inverse is $\Sigma^\alpha_{\alpha(a)^{-1},\alpha(b)^{-1}}$ and its composition is $L_{c\alpha(a)}R_{\alpha(b)d}$, a two-sided operator that is not a signed sandwich. The sandwich is unitary exactly when the two products $\delta(a)\alpha(a)$ and $a\sigma(a)$ are central and their products with the complements are the unit; the normalised condition $\delta(a)\alpha(a) = 1$, $\alpha(b)\delta(b) = 1$ is sufficient, and for the reflection $b = \alpha(a)^{-1}$ the product conditions are automatic and unitarity reduces to the centrality of the two products. The signed sandwiches are bounded and continuous, the adjoint map is continuous, and the unitary sandwiches are form-preserving and closed under the adjoint; the signed sandwiches are not closed under composition, the composite being the two-sided operator $L_{c\alpha(a)}R_{\alpha(b)d}$. The reflection and the one-sided operators are the specialisations $b = u^{-1}$ and $b = 1$ of the following articles, and the graded case over a module is the article that closes the group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\sigma$, $\alpha$, $\delta = \sigma\alpha$ | Involution, grade involution, twist |
| $\Sigma^\alpha_{a,b}(x) = a\alpha(x)b$ | The signed sandwich |
| $\Sigma^\alpha_{a,b} = L_a\alpha R_{\alpha(b)}$ | Factorisation |
| $(\Sigma^\alpha_{a,b})^\dagger = \Sigma^\alpha_{\delta(a),\delta(b)}$ | The signed adjoint; no swap |
| $(\Sigma^\alpha_{a,b})^{-1} = \Sigma^\alpha_{\alpha(a)^{-1},\alpha(b)^{-1}}$ | Inverse |
| $\Sigma^\alpha_{c,d}\circ\Sigma^\alpha_{a,b} = L_{c\alpha(a)}R_{\alpha(b)d}$ | Composition |
| $\delta(a)\alpha(a)$ central, $a\sigma(a)$ central | Unitarity: centrality |
| $\delta(a)\alpha(a)\alpha(b)\delta(b) = 1$, $a\sigma(a)\sigma(b)b = 1$ | Unitarity: the unit conditions |

## Further Reading

- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the adjoint of a sandwich, the unitary elements and the centrality conditions.
- Nathan Jacobson, *Structure of Rings*, American Mathematical Society Colloquium Publications 37 (1964), for the two-sided operators of the regular representation and their adjoints.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the unitary groups and the unitarity condition of an involution.
- Nicolas Bourbaki, *Algebra I*, Chapters 1–3 (Springer, 1998), for adjoints under a sesquilinear pairing and the unitarity condition.
- Seth Warner, *Topological Fields* (North-Holland, 1989), for the continuous operators of a topological ring and the closed subgroups of the form-preserving operators.
