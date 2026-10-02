
# __The Signed Sandwich on a Topological Ring__

## Introduction

The two-sided sandwich of a ring is the operator $x \mapsto axb$ obtained by multiplying on the left by $a$ and on the right by $b$; when the ring carries a **grade involution**, an automorphism of order two that is the sign change of a grading, the sandwich acquires a twist, $x \mapsto a\,\alpha(x)\,b$, and it is the twisted operator that realises the reflections of the ring. This article treats the twisted, or **signed**, sandwich on a topological ring: it fixes the operator, proves its continuity from the continuity of the grade involution, computes its composition law and the group it generates from the units, shows that the signed family is the unsigned family composed with the grade involution and that the twist is inoperative exactly when the grade involution is inner, and reads the signed conjugations that the signed sandwich realises, with the involution condition that controls them.

The article assumes the two-sided sandwich, its composition, the unsigned sandwich group and the correspondence with the reflections from *The Signed Sandwich on a Ring*; the grade involution of a graded ring, its order two, its fixed and skew parts and the sign rule from *Graded Rings* and *The Grade Involution*; the topological ring and the continuity of its product from *Topological Rings and Fields*; the operator layer, the one-sided multiplications, their composition and their failure of commutation, and the sandwich $L_aR_b$ from *The Left and Right Multiplication Operators on a Topological Ring*; the signed one-sided operators as the case $b=1$ from *The Signed Left Multiplication on a Topological Ring*; and the signed sandwiches and the reflections on a group, treated in parallel, from *The Signed Sandwich on a Topological Group*. The **involution** of the ring in the sense of an anti-automorphism of order two is *Involutive Topological Rings and Fields* and belongs to the `- * Theory` group; it is not the grade involution used here, and the two are kept apart. No adjoint and no form occurs; the adjoint of the signed sandwich is *The Signed Adjoint Sandwich on a Topological Ring*, later in this category.

Throughout, $R$ is a topological ring, unital and Hausdorff, with group of units $R^\times$ and centre $Z(R)$; $\alpha$ is a **grade involution**, that is an involutive ring automorphism of $R$, assumed continuous, with fixed subring $R^\alpha = \{x : \alpha(x) = x\}$ and skew set; $L_a$ and $R_b$ are the one-sided multiplications of *The Left and Right Multiplication Operators on a Topological Ring*; and the unsigned and signed sandwiches are

$$
\Sigma_{a,b}(x) = a\,x\,b, \qquad \Sigma^\alpha_{a,b}(x) = a\,\alpha(x)\,b .
$$

## The Grade Involution

**Definition.** A **grade involution** of $R$ is a ring automorphism $\alpha$ with $\alpha^2 = \mathrm{id}$. A graded ring $R = \bigoplus_{k} R_k$ carries the grade involution $\alpha(x) = (-1)^k x$ for $x \in R_k$ when the odd part squares to the even part, and this is the origin of the name; here $\alpha$ is any involutive automorphism, and the graded case is the model.

**Proposition (the basic identities).** For a grade involution $\alpha$: $\alpha(1) = 1$, $\alpha(xy) = \alpha(x)\alpha(y)$, $\alpha(x + y) = \alpha(x) + \alpha(y)$, $\alpha^{-1} = \alpha$, and $\alpha$ carries the units onto the units, $\alpha(R^\times) = R^\times$, and the centre onto the centre, $\alpha(Z(R)) = Z(R)$.

**Proof.** An automorphism fixes $1$ and preserves products, sums and the property of being a unit; an automorphism carries the centre onto itself; involutivity is $\alpha^2 = \mathrm{id}$, so $\alpha^{-1} = \alpha$.

**Proposition (continuity is a genuine hypothesis).** Assume $\alpha$ continuous. Then $\alpha$ is a homeomorphism and a topological automorphism of $R$, every signed sandwich is continuous, and $\alpha$ maps the closure of a set onto the closure of its image. The hypothesis is not automatic: on $\mathbb{R}[x]$ with the $(x)$-adic topology the map $f(x) \mapsto f(1 - x)$ is an involutive automorphism that is not continuous, as *Involutive Topological Rings and Fields* records for the order-two maps of that ring.

**Proof.** A continuous involutive map is its own continuous inverse, hence a homeomorphism; the signed sandwich is $\Sigma_{a,b}\circ\alpha$, a composite of continuous maps; a homeomorphism preserves closures. The counterexample is quoted from *Involutive Topological Rings and Fields*, where continuity is shown to be a real hypothesis.

## The Signed Sandwich

**Definition.** The **signed sandwich** with parameters $a, b \in R$ is the operator

$$
\Sigma^\alpha_{a,b} : R \longrightarrow R, \qquad \Sigma^\alpha_{a,b}(x) = a\,\alpha(x)\,b .
$$

The **unsigned sandwich** is $\Sigma_{a,b} = \Sigma^{\mathrm{id}}_{a,b}$. The operator is also written $\Sigma_{a,b}\alpha$ because it is the composite of the grade involution followed by the unsigned sandwich.

**Proposition (decomposition and additivity).** The signed sandwich is the composite

$$
\Sigma^\alpha_{a,b} = L_a \circ \alpha \circ R_{\alpha(b)} ,
$$

it is additive, and it is continuous whenever $\alpha$ is; in particular it lies in $\operatorname{End}_c(R)$. The signed sandwich is the unsigned sandwich followed by the grade involution,

$$
\Sigma^\alpha_{a,b} = \Sigma_{a,b}\circ\alpha ,
$$

so the signed family is the set $\Sigma(R)\circ\alpha$ of all unsigned sandwiches composed on the right with $\alpha$.

**Proof.** $R_{\alpha(b)}(x) = x\alpha(b)$, so $\alpha(R_{\alpha(b)}x) = \alpha(x)\alpha(\alpha(b)) = \alpha(x)b$, and applying $L_a$ gives $a\alpha(x)b$, which is $\Sigma^\alpha_{a,b}$; this proves the decomposition and, with the continuity of $L_a$, $R_{\alpha(b)}$ and $\alpha$, the continuity. For the second, $\Sigma_{a,b}(\alpha(x)) = a\alpha(x)b = \Sigma^\alpha_{a,b}(x)$.

**Remark (the two parametrisations).** The article uses the parametrisation $\Sigma^\alpha_{a,b}(x) = a\alpha(x)b$, in which the composition law below is symmetric, and the identity $\Sigma^\alpha_{a,b} = \Sigma_{a,b}\circ\alpha$ records the relation to the unsigned family; the decomposition $\Sigma^\alpha_{a,b} = L_a\circ\alpha\circ R_{\alpha(b)}$ expresses the same operator through the one-sided multiplications.

## Composition and the Group

**Proposition (composition law).** For all $a, b, c, d \in R$,

$$
\Sigma^\alpha_{a,b}\circ\Sigma^\alpha_{c,d} = \Sigma^\alpha_{a\,\alpha(c),\,\alpha(d)\,b} .
$$

**Proof.** Compute $\Sigma^\alpha_{a,b}(\Sigma^\alpha_{c,d}(x)) = a\,\alpha(c\,\alpha(x)\,d)\,b = a\,\alpha(c)\,\alpha(\alpha(x))\,\alpha(d)\,b = a\,\alpha(c)\,x\,\alpha(d)\,b$, using multiplicativity of $\alpha$ and $\alpha^2 = \mathrm{id}$. This is the signed sandwich with left parameter $a\alpha(c)$ and right parameter $\alpha(d)b$.

**Theorem (the signed sandwich group).** The signed sandwiches with both parameters in $R^\times$ are exactly the invertible signed sandwiches, they form a group $\Sigma^\alpha(R^\times)$ under composition, and the map

$$
R^\times \times R^\times \longrightarrow \Sigma^\alpha(R^\times), \qquad (a, b) \longmapsto \Sigma^\alpha_{a,b} ,
$$

is a surjective group homomorphism whose kernel is

$$
\ker = \bigl\{ (a, a^{-1}) : a \in R^\times, \ c_a = \alpha \bigr\} ,
$$

the set of units inducing the grade involution. This kernel is trivial when $\alpha$ is not inner; when $\alpha$ is inner it is the coset of the central units over any one unit inducing $\alpha$, and in particular it is $\{(z, z^{-1}) : z \in Z(R)\cap R^\times\}$ when $\alpha = \mathrm{id}$. Hence $\Sigma^\alpha(R^\times) \cong (R^\times\times R^\times)/\ker$.

**Proof.** For $a, b \in R^\times$ the composition law with $(c,d) = (\alpha(a)^{-1}, b^{-1})$ gives $\Sigma^\alpha_{a,b}\circ\Sigma^\alpha_{\alpha(a)^{-1},b^{-1}} = \Sigma^\alpha_{a\alpha(\alpha(a)^{-1}),\,\alpha(b^{-1})b} = \Sigma^\alpha_{1,1} = \mathrm{id}$ and the same from the other side, so $\Sigma^\alpha_{a,b}$ is invertible with inverse $\Sigma^\alpha_{\alpha(a)^{-1},\,b^{-1}}$, and the image of $R^\times\times R^\times$ is contained in the group of invertible additive operators. Conversely, by the decomposition $\Sigma^\alpha_{a,b} = L_a\circ\alpha\circ R_{\alpha(b)}$ and the invertibility of $\alpha$, the operator $\Sigma^\alpha_{a,b}$ is invertible exactly when $L_a$ and $R_{\alpha(b)}$ are, that is exactly when $a$ and $\alpha(b)$ are units, by *Operators on a Topological Ring*; so the invertible signed sandwiches are exactly the unit-parametrised ones. The composition law makes $(a,b)\mapsto\Sigma^\alpha_{a,b}$ a surjective homomorphism, and its kernel consists of the pairs with $a\alpha(x)b = x$ for all $x$; setting $x = 1$ gives $ab = 1$, so $b = a^{-1}$, and then $a\alpha(x)a^{-1} = x$ for all $x$, that is $c_a = \alpha$. So the kernel is $\{(a, a^{-1}) : c_a = \alpha\}$, trivial when $\alpha$ is not inner and the coset of the central units over a unit inducing $\alpha$ when $\alpha$ is inner.

**Corollary (the parametrisation of the reflections).** The signed sandwiches $\rho_u = \Sigma^\alpha_{u,u^{-1}}$ for $u \in R^\times$ are the **signed conjugations**; they satisfy the composition law $\rho_u\rho_v = \Sigma^\alpha_{u\alpha(v),\,\alpha(v^{-1})u^{-1}}$ and they are involutions exactly when $u\alpha(u)$ is central, because

$$
\rho_u^2 = \Sigma^\alpha_{u\alpha(u),\,\alpha(u^{-1})u^{-1}} = c_{u\alpha(u)},
$$

and $c_{u\alpha(u)} = \mathrm{id}$ exactly when $u\alpha(u) \in Z(R)$.

**Proof.** Apply the composition law with $(a,b) = (c,d) = (u,u^{-1})$: $\Sigma^\alpha_{u,u^{-1}}\Sigma^\alpha_{u,u^{-1}} = \Sigma^\alpha_{u\alpha(u),\,\alpha(u^{-1})u^{-1}}$. Directly, for $t = u\alpha(u)$ one has $\alpha(u^{-1})u^{-1} = \alpha(u)^{-1}u^{-1} = (u\alpha(u))^{-1} = t^{-1}$, so the square is $\Sigma^\alpha_{t,t^{-1}}$, and evaluating at $x$ gives $u\alpha(u\alpha(x)u^{-1})u^{-1} = u\alpha(u)\,x\,\alpha(u)^{-1}u^{-1} = t x t^{-1} = c_t(x)$. Hence $\rho_u^2 = c_{u\alpha(u)}$, which is the identity exactly when $u\alpha(u) \in Z(R)$.

## The Relation to the Unsigned Sandwich

**Proposition (the signed family is a coset of the unsigned family).** As sets of operators,

$$
\Sigma^\alpha(R) = \Sigma(R)\circ\alpha = \{\Sigma_{a,b}\alpha : a, b \in R\} ,
$$

and the signed sandwich group is the image of the unsigned sandwich group under right composition with $\alpha$. On the units, $\Sigma^\alpha_{u,v} = \Sigma_{u,\alpha(v)}\alpha$.

**Proof.** $\Sigma_{a,b}\alpha(x) = a\alpha(x)b = \Sigma^\alpha_{a,b}(x)$, which shows the set identity and the group statement; the unit statement is the same computation with $u, v$ in place of $a, b$.

**Theorem (the degenerate case: the grade involution is inner).** The signed family equals the unsigned family, $\Sigma^\alpha(R) = \Sigma(R)$, if and only if the grade involution is inner, $\alpha = c_z$ for some $z \in R^\times$; in that case

$$
\Sigma^\alpha_{a,b} = \Sigma_{az,\,z^{-1}b} ,
$$

so every signed sandwich is an unsigned sandwich, and the twisting is inoperative. If $\alpha$ is not inner then $\Sigma^\alpha(R) \neq \Sigma(R)$ and the signed family is a proper coset of the unsigned family in the group they generate.

**Proof.** If $\alpha = c_z$ then $\alpha(x) = zxz^{-1}$ and $\Sigma^\alpha_{a,b}(x) = a z x z^{-1} b = \Sigma_{az, z^{-1}b}(x)$, so the signed family is contained in the unsigned one and conversely; if the families are equal then in particular the signed sandwich $\Sigma^\alpha_{1,1} = \alpha$ is unsigned, say $\alpha = \Sigma_{a,b}$, which gives $\alpha(x) = axb$ for all $x$; setting $x = 1$ gives $ab = 1$, so $b = a^{-1}$ and $\alpha = c_a$ is inner. When $\alpha$ is not inner the two sets differ, because $\alpha = \Sigma^\alpha_{1,1}$ is a signed sandwich but is not an unsigned sandwich.

**Proposition (the signed and unsigned sandwich groups).** When $\alpha$ is not inner the two sandwich groups $\Sigma^\alpha(R^\times)$ and $\Sigma(R^\times)$ meet only in the identity, and each is a quotient of $R^\times\times R^\times$ by the central kernel; when $\alpha$ is inner the two groups coincide. In the non-inner case the map $(u, v) \mapsto \Sigma^\alpha_{u,v}$ is an isomorphism $R^\times\times R^\times \to \Sigma^\alpha(R^\times)$, and the map $(u, v) \mapsto \Sigma_{u,v}$ is an isomorphism of $(R^\times\times R^\times)/(Z(R)^\times)$ onto the unsigned group, where $Z(R)^\times = Z(R)\cap R^\times$ is embedded as $z \mapsto (z, z^{-1})$.

**Proof.** If a signed sandwich $\Sigma^\alpha_{u,u^{-1}}$ were also unsigned, say $\Sigma^\alpha_{u,u^{-1}} = \Sigma_{A,B}$, then evaluating at $1$ gives $AB = 1$, so $B = A^{-1}$ and $u\alpha(x)u^{-1} = AxA^{-1}$ for all $x$, that is $\alpha = c_{u^{-1}A}$, and $\alpha$ would be inner; so when $\alpha$ is not inner only the identity lies in both. The isomorphism statements are the kernel computations of the sandwich groups in the two cases $\alpha$ and $\mathrm{id}$.

## Reflections and the Degenerate Case

**Definition.** The **reflections** of the ring, in the sense of the signed sandwich block, are the signed conjugations $\rho_u = \Sigma^\alpha_{u,u^{-1}}$ for units $u$ with $u\alpha(u)$ central; the **carrying unit** is $u$, and the **reflection group** is the set of such $\rho_u$.

**Proposition (which signed sandwiches are reflections).** The signed conjugation $\rho_u$ is an involution exactly when $u\alpha(u) \in Z(R)$, and it fixes the closed subring $\{x : \alpha(x) = u^{-1}xu\}$ pointwise; the signed sandwiches that are reflections are exactly the $\rho_u$ with $u\alpha(u)$ central, and the map $u \mapsto \rho_u$ has kernel the units inducing the grade involution, $\{a \in R^\times : c_a = \alpha\}$, which is trivial when $\alpha$ is not inner and is the coset of the central units over a unit inducing $\alpha$ when $\alpha$ is inner.

**Proof.** The involution condition is the corollary above. The fixed set of $\rho_u$ is $\{x : u\alpha(x)u^{-1} = x\} = \{x : \alpha(x) = u^{-1}xu\}$, which is the equalizer of the continuous maps $\alpha$ and $c_{u^{-1}}$, hence closed. The kernel of $u \mapsto \rho_u$ is the set of units $v$ with $\Sigma^\alpha_{v,v^{-1}} = \mathrm{id}$, which by the sandwich-group theorem is $\{a : c_a = \alpha\}$.

**Remark (the correspondence with the elements).** The passage from the elements of a set acted on by reflections to the operators realising the reflections, the **correspondence between the elements and the reflections**, is the subject of *Reflections as Signed Two-Sided Operators on a Topological Ring*, later in this group, and of its Part I sibling. This article only records which signed sandwiches are the reflections; the correspondence and its failure in the degenerate cases are treated there. The topological gain, that the fixed sets and the carrying cosets are closed, is used there and is proved here for the fixed sets.

## The Topological Reading

**Proposition (the signed sandwich is continuous and the group is topological).** When $\alpha$ is continuous, every signed sandwich is a continuous additive operator; the signed sandwich group $\Sigma^\alpha(R^\times)$ is a topological group for the topology of pointwise convergence when $R^\times$ is open, and the map $(a, b) \mapsto \Sigma^\alpha_{a,b}$ is a continuous homomorphism of topological groups.

**Proof.** Continuity of the signed sandwich is the decomposition and the continuity of $L_a$, $R_b$ and $\alpha$. The composition law is continuous in the parameters because the ring operations are; when $R^\times$ is open, $R^\times\times R^\times$ is a topological group and the quotient by the kernel, which is discrete in the non-inner case, is a topological group, so the image is a topological group. The map is continuous because each coordinate is.

**Proposition (the action on the ideals).** A signed sandwich acts on the ideals by $\Sigma^\alpha_{a,b}(I) = a\,\alpha(I)\,b$; for a two-sided ideal $I$ this is the conjugate $aIb$ up to the grade involution, and an inner grade involution acts trivially on the two-sided ideals when the parameters are units.

**Proof.** The image of an ideal under an automorphism and the one-sided multiplications is an ideal of the corresponding kind; the two-sided case is the action of the inner automorphism together with the sandwich $L_aR_b$, which for units and a two-sided ideal leaves it unchanged by *Operators on a Topological Ring*.

**Remark (the boundary to the involution and the adjoints).** The involution of the `- * Theory` group is an anti-automorphism of order two, and the signed sandwich with respect to a grade involution is the automorphic analogue; the two structures meet in *Involutive Topological Rings and Fields*, where the fixed sets of the anti-automorphism are treated. The adjoint of the signed sandwich with respect to the form of the category is *The Signed Adjoint Sandwich on a Topological Ring*, and the graded version is *The Graded Action on a Module over a Topological Ring*, both later in this category.

## Examples

**Example (the graded ring $k[x]/(x^2)$).** With the grading in which $x$ is odd and $k$ is even, the grade involution is $\alpha(a + bx) = a - bx$; the signed sandwich $\Sigma^\alpha_{1,1} = \alpha$ is the sign change, it is continuous for the discrete topology, and it is not inner because the ring is commutative and $\alpha$ is not the identity on the odd part; the signed and unsigned families therefore differ.

**Example (the matrix ring with the transpose grading).** Let $R = M_n(k)\times M_n(k)$ with the involution exchanging the factors; the grade involution $\alpha(A, B) = (B, A)$ is an involutive automorphism, and it is inner exactly when the two factors are conjugate by an invertible element, which fails in general; the signed sandwich $\Sigma^\alpha_{(A,B),(C,D)}$ exchanges the factors and is the model of a signed two-sided operator with a non-inner grade involution.

**Example (a commutative ring).** For a commutative $R$ and any $\alpha$, the products are symmetric, $\Sigma^\alpha_{a,b} = \Sigma^\alpha_{b,a}$, and the signed sandwich group is abelian; the unsigned sandwich $\Sigma_{a,b}$ depends only on the product $ab$, and the signed one only on $a\alpha(b)$, so the parametrisation collapses and the group is a quotient of $R^\times$.

**Example (the group ring and the Clifford model).** In the Clifford algebra of a quadratic space the grade involution is the sign change on the odd part; the signed conjugations $\rho_u$ with $u$ a vector are the reflections of the quadratic space, the condition $u\alpha(u) \in Z(R)$ being $u(-u) = -u^2 \in k$ central, and this is the model for which the signed sandwich is named.

## Summary

The signed sandwich of a topological ring with a continuous grade involution $\alpha$ is the operator $\Sigma^\alpha_{a,b}(x) = a\alpha(x)b$; it is additive and continuous, it decomposes as $L_a\alpha R_b$ and as the unsigned sandwich followed by $\alpha$, and it composes by $\Sigma^\alpha_{a,b}\circ\Sigma^\alpha_{c,d} = \Sigma^\alpha_{a\alpha(c),\alpha(d)b}$. The signed sandwiches with both parameters units form the signed sandwich group, the image of $R^\times\times R^\times$ under a homomorphism whose kernel is trivial when $\alpha$ is not inner and is the graph of the inverse on the central units fixed by $\alpha$ in the inner case; the signed conjugations $\rho_u = \Sigma^\alpha_{u,u^{-1}}$ satisfy $\rho_u^2 = c_{u\alpha(u)}$ and are the reflections exactly when $u\alpha(u)$ is central, with fixed set the closed subring $\{x : \alpha(x) = u^{-1}xu\}$.

The signed family is the coset $\Sigma(R)\alpha$ of the unsigned family, and it coincides with the unsigned family exactly when the grade involution is inner, $\alpha = c_z$, in which case $\Sigma^\alpha_{a,b} = \Sigma_{az,z^{-1}b}$ and the twisting is inoperative; when $\alpha$ is not inner the two families differ and their union generates the group of operators with unit one-sided factors together with $\alpha$. Topologically the signed sandwich is continuous, the signed sandwich group is a topological group when the units are open, it acts on the ideals by $I \mapsto a\alpha(I)b$, and the structure meets the involution of the `- * Theory` group only in the involutive topological rings, the adjoints of the signed sandwiches being later in this category.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\alpha$ | The grade involution, an involutive automorphism, assumed continuous |
| $R^\alpha$ | The fixed subring of the grade involution |
| $\Sigma_{a,b}(x) = axb$ | The unsigned two-sided sandwich |
| $\Sigma^\alpha_{a,b}(x) = a\alpha(x)b$ | The signed sandwich |
| $\Sigma^\alpha_{a,b} = \Sigma_{a,\alpha(b)}\alpha$ | The signed family as a coset of the unsigned family |
| $\Sigma^\alpha_{a,b}\circ\Sigma^\alpha_{c,d} = \Sigma^\alpha_{a\alpha(c),\alpha(d)b}$ | The composition law |
| $\Sigma^\alpha(R^\times)$ | The signed sandwich group |
| $\rho_u = \Sigma^\alpha_{u,u^{-1}}$ | The signed conjugation, a reflection when $u\alpha(u)$ is central |
| $\rho_u^2 = c_{u\alpha(u)}$ | The square of a signed conjugation |
| $c_z$, $\alpha = c_z$ | The inner automorphism, and the degenerate inner grade involution |
| $R^\times\times R^\times$ | Parameters of the sandwich, the kernel being the inner obstruction |

## Further Reading

- Nicolas Bourbaki, *Algebra I, Chapters 1–3* (Springer, 1998), for the two-sided sandwich, the opposite ring and the double centraliser.
- Claude Chevalley, *The Algebraic Theory of Spinors and Clifford Algebras* (Springer, 1997; collected works), for the grade involution, the reflections and the signed conjugations in the Clifford algebra.
- Tsi-Yuen Lam, *A First Course in Noncommutative Rings*, Graduate Texts in Mathematics 131 (Springer, 2nd ed. 2001), for inner automorphisms and the conditions under which an automorphism is inner.
- C. T. C. Wall, "Graded algebras, anti-involutions, simple groups and symmetric spaces", *Bulletin of the American Mathematical Society* **74** (1968), 143–148, for graded algebras, the grade involution and the signed operators.
- Seth Warner, *Topological Fields* (North-Holland, 1989), for the continuity of the ring automorphisms and the topology of pointwise convergence on the operator layer.
