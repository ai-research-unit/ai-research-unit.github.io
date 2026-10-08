# __The Bounded Sandwich and the Continuous Inner Conjugation__

## Introduction

The sandwich $T_{x,y}(z)=xzy$ is the two-sided operator of a Clifford algebra, and the inner conjugation is the sandwich of a unit with its inverse. Both are bounded operators as soon as the one-sided multiplications are, because $T_{x,y}=L_{x}R_{y}$ and $\lVert L_{x}R_{y}\rVert\le\lVert x\rVert\lVert y\rVert$ for a submultiplicative norm; the interest of the sandwich is therefore not in the boundedness of each one of them but in the **norm of the family**, which is the multiplication constant of the product, and in the continuity of the parametrisation $(x,y)\mapsto T_{x,y}$, which is the joint continuity of the product in operator form. For a submultiplicative norm the constant is at most one and the sandwich is a contraction; for the Euclidean norm of the definite case it **exceeds one** — the ratio $\sqrt2$ is attained at the idempotent $\tfrac12(1+e_{1})$ of *The Bounded Left and Right Multiplication on a Clifford Algebra* — and the two-variable map is not jointly continuous in infinite dimension.

The second subject is the conjugation. For a unit $x$ the sandwich $T_{x,x^{-1}}$ is an algebra automorphism, the inner automorphism of $x$, and the map $x\mapsto T_{x,x^{-1}}$ from the group of units to the group of automorphisms is a homomorphism with kernel the centre; the layer asks for its continuity, which holds because the group of units of a topological algebra is a topological group and the parametrisation is built from the product and the inversion. The **signed** inner conjugation $\chi_{x}=T_{x,\alpha(x)^{-1}}$, in which the inverse is twisted by the grade involution, is the map under which the Clifford, Pin and Spin groups act on the vectors, $\chi_{x}(v)=xv\alpha(x)^{-1}$, and the continuity of the twisted parametrisation is the continuity of the covering of *The Topological Orthogonal Group and the Spin Group*: the sandwich is the algebraic side of that covering and this article is its operator side.

The article treats the sandwich and its bound, the multiplication constant of the family, the continuity in both variables, the inner conjugation on the group of units and the signed conjugation with its versor subgroups. The one-sided multiplications and the criterion for joint continuity are *The Bounded Left and Right Multiplication on a Clifford Algebra*; the action on a module is *Bounded Clifford Modules and the Continuous Spin Representation*; the two-sided operators as algebra are *Two-Sided Operators on a Clifford Algebra*, *The Sandwich on a Clifford Algebra* and *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*; the covering and the reflections are *The Topological Orthogonal Group and the Spin Group*; the adjoint of the sandwich is the Hermitian layer's *The Adjoint of the Sandwich on a Hermitian Algebra*.

## The Sandwich and its Bound

**Definition.** The **sandwich** of $x,y$ is the two-sided operator $T_{x,y}(z)=xzy$, and the family of the sandwiches is $\mathcal{T}=\{T_{x,y} : x,y\in\mathrm{Cl}(V,q)\}$.

**Proposition (the algebra of the family).** $T_{x,y}=L_{x}R_{y}=R_{y}L_{x}$ and $T_{x,y}T_{u,v}=T_{xu,vy}$; hence $\mathcal{T}$ is closed under composition and is the image of the bilinear map $T:\mathrm{Cl}\times\mathrm{Cl}\to\mathcal{B}(\mathrm{Cl})$, $(x,y)\mapsto T_{x,y}$, whose image contains the one-sided multiplications, $L_{x}=T_{x,1}$ and $R_{y}=T_{1,y}$.

*Proof.* Straightforward computation of the composition, together with the commutation of the left and the right multiplications; the identifications $T_{x,1}=L_{x}$ and $T_{1,y}=R_{y}$ are the definitions. $\square$

**Theorem (the bound and the multiplication constant).** For a submultiplicative norm with $\lVert1\rVert=1$

$$
\lVert T_{x,y}\rVert\le\lVert x\rVert\lVert y\rVert ,
$$

and in general the norm of the bilinear map $T$ is the **multiplication constant** of the algebra,

$$
\lVert T\rVert = \sup\Bigl\{\frac{\lVert xzy\rVert}{\lVert x\rVert\lVert y\rVert\lVert z\rVert} : x,y,z\neq0\Bigr\} = \sup\Bigl\{\frac{\lVert xy\rVert}{\lVert x\rVert\lVert y\rVert} : x,y\neq0\Bigr\} ,
$$

so that $\lVert T\rVert\le1$ exactly when the norm is submultiplicative, while $1<\lVert T\rVert\le2^{n/2}$ for the Euclidean norm of the definite case, the value $\sqrt2$ being attained at the idempotent $\tfrac12(1+e_{1})$ and $2^{n/2}$ being the Cauchy–Schwarz estimate.

*Proof.* The first inequality is $\lVert L_{x}R_{y}\rVert\le\lVert L_{x}\rVert\lVert R_{y}\rVert=\lVert x\rVert\lVert y\rVert$ by the isometry of the regular representation. For the second, $\lVert T\rVert$ is by definition the supremum of $\lVert T_{x,y}z\rVert/(\lVert x\rVert\lVert y\rVert\lVert z\rVert)=\lVert xzy\rVert/(\lVert x\rVert\lVert y\rVert\lVert z\rVert)$, which is the supremum of $\lVert wy\rVert/(\lVert w\rVert\lVert y\rVert)$ with $w=xz$, and the two expressions therefore agree; the criterion for joint continuity of the companion article identifies $\lVert T\rVert\le1$ with submultiplicativity, and for the Euclidean norm the value $\sqrt2$ is attained at the idempotent $\tfrac12(1+e_{1})$, the bound $2^{n/2}$ being the estimate of the companion article. $\square$

**Remark (the sandwich family is not all the operators of the algebra).** The sandwiches span the linear span of the rank-one-like two-sided operators, which is the algebra of the maps of finite rank in the sense of the two-sided ideal generated by the evaluations; the closure of that span in the operator norm is the compacts-like subalgebra of *Operators on a Topological Clifford Algebra*, §*The Continuity of the Structure*. What the theorem above measures is the size of the *parametrisation*, and it is the multiplication constant, not the operator norm of a single sandwich.

## The Continuity in Both Variables

**Theorem (the continuity of the parametrisation).** Let the product of the algebra be continuous in each variable separately. Then the map $x\mapsto T_{x,y}$ is continuous for each $y$ and the map $y\mapsto T_{x,y}$ for each $x$, so $T$ is separately continuous; $T$ is **jointly** continuous exactly when the product is, that is exactly when $\lVert T\rVert<\infty$ in the normed case; and when the algebra is complete and normed with the product defined everywhere, separate continuity implies joint continuity.

*Proof.* The identity $T_{x,y}=L_{x}R_{y}$ and the continuity of the one-sided multiplications of *Operators on a Topological Clifford Algebra* give the separate statements; the joint statement is the criterion of *The Bounded Left and Right Multiplication on a Clifford Algebra*, since $T$ is bounded exactly when the product is bounded on the unit balls; the last clause is the uniform boundedness theorem of the same article. $\square$

**Corollary (the failure for the Euclidean norm).** For the Euclidean norm of the definite case with $\dim V=\infty$, the map $T$ is separately continuous and not jointly continuous, and $\lVert T\rVert=\infty$; the sandwich of a fixed element is always a bounded operator, and the family is not uniformly bounded over the unit ball.

*Proof.* The bound of the finite-dimensional subalgebras is $2^{n/2}$ and grows without bound with the dimension, so no finite constant bounds $\lVert T_{x,y}\rVert$ over the unit balls; the statements about separate and joint continuity are those of the companion article. $\square$

## The Inner Conjugation

**Definition.** The **inner conjugation** of a unit $x$ is the sandwich $\operatorname{Int}_{x}=T_{x,x^{-1}}$, so that $\operatorname{Int}_{x}(y)=xyx^{-1}$.

**Theorem (the group of inner automorphisms).** Let $x$ range over the group of units $\mathrm{Cl}(V,q)^{\times}$. Then $\operatorname{Int}_{x}$ is an algebra automorphism, $\operatorname{Int}_{x}\operatorname{Int}_{z}=\operatorname{Int}_{xz}$, the map $x\mapsto\operatorname{Int}_{x}$ is a homomorphism of $\mathrm{Cl}^{\times}$ onto the group of inner automorphisms with kernel the centre $Z^{\times}$, and it is **continuous** on the group of units, which is a topological group; consequently the group of inner automorphisms is a topological group, isomorphic to $\mathrm{Cl}^{\times}/Z^{\times}$.

*Proof.* The multiplicativity of the conjugation and its invertibility are the defining properties of an inner automorphism, and the kernel is the set of units whose conjugation is the identity, that is the centre. Inversion is continuous in a topological group by definition, and the product is separately continuous, so $(x,y)\mapsto xyx^{-1}$ is continuous in each variable and hence on the group of units; the quotient by the closed central subgroup carries the quotient topology. $\square$

**Proposition (the action on the vectors and the orthogonal group).** For $v$ a vector, $\operatorname{Int}_{x}(v)$ need not be a vector, while the **signed** conjugation $\chi_{x}(v)=xv\alpha(x)^{-1}$ always is when $x$ is a versor; the map $x\mapsto\chi_{x}$ is continuous on the versor group for a continuous $\alpha$, its kernel is the group $F^{\times}$ of central scalars, and the induced map onto the orthogonal group is the covering of *The Topological Orthogonal Group and the Spin Group*.

*Proof.* The invariance of $V$ under $\chi_{x}$ and the kernel statement are the algebraic facts of *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*; the continuity is the continuity of the product and of the continuous automorphism $\alpha$ of the algebra, and the identification of the image is the covering theorem of the topological article. $\square$

**Remark (why the sign is needed in the layer).** The unsigned conjugation preserves the vector space $V$ only for the even versors; the graded sign $\alpha$ corrects the parity and makes the whole versor group act on $V$, which is why the layer's inner conjugation is the **signed** one. The distinction is invisible in the finite-dimensional algebra, where both maps are continuous, and it matters for the identification of the kernel and of the image of the covering.

## Worked Cases

### The Finite-Dimensional Case

For a finite-dimensional algebra over a complete valued field every sandwich is a bounded operator, the map $T$ is continuous in both variables jointly because it is bilinear on a finite product of finite-dimensional spaces, $\lVert T\rVert$ is finite, and the group of units is open with the inner automorphisms a topological group. The inner conjugation is the classical description of the automorphism group of a central simple algebra: over $\mathbb{R}$ or $\mathbb{C}$ every automorphism is inner by the Skolem–Noether theorem, so the map $x\mapsto\operatorname{Int}_{x}$ is onto $\operatorname{Aut}$ with kernel $Z^{\times}$.

### The Completion

For the projective norm or the C*-norm of *The Completion of a Clifford Algebra* the product is submultiplicative, $\lVert T\rVert\le1$, the sandwich is a contraction, the parametrisation is jointly continuous, and the inner automorphisms of the completed algebra form a topological group; the sandwiches of the completion are the closures of the sandwiches of the algebra.

### The Euclidean Norm

For the Euclidean norm of the definite case the sandwich of a fixed element is bounded and the family is not: $\lVert T\rVert>1$ in every dimension and $\lVert T\rVert=\infty$ in infinite dimension, so the parametrisation is separately continuous and not jointly continuous; the inner conjugation of a unit is nevertheless a bounded operator with the bound $\lVert\operatorname{Int}_{x}\rVert\le\lVert x\rVert\lVert x^{-1}\rVert$ *when the norm is submultiplicative*, and in the Euclidean case the bound is $\lVert x\rVert\lVert x^{-1}\rVert$ times the constant $2^{n/2}$.

## Summary

The **sandwich** $T_{x,y}=L_{x}R_{y}=R_{y}L_{x}$ satisfies $T_{x,y}T_{u,v}=T_{xu,vy}$, and for a submultiplicative norm $\lVert T_{x,y}\rVert\le\lVert x\rVert\lVert y\rVert$; the norm of the **bilinear map** $T$ is the **multiplication constant** of the algebra, greater than one for the Euclidean norm of the definite case ($\sqrt2$ attained, $2^{n/2}$ the bound), so that $T$ is a contraction exactly when the norm is submultiplicative. The map $(x,y)\mapsto T_{x,y}$ is separately continuous whenever the product is, and jointly continuous exactly when the product is; for the Euclidean norm in infinite dimension it is separately and not jointly continuous, by the unboundedness of the multiplication constant.

The **inner conjugation** $\operatorname{Int}_{x}=T_{x,x^{-1}}$ is an algebra automorphism, the map $x\mapsto\operatorname{Int}_{x}$ is a continuous homomorphism of the group of units onto the group of inner automorphisms with kernel the centre, and the group of inner automorphisms is a topological group; the **signed** inner conjugation $\chi_{x}=T_{x,\alpha(x)^{-1}}$ is the map under which the Clifford, Pin and Spin groups act on the vectors, with kernel the central scalars, and the induced map onto the orthogonal group is the covering of *The Topological Orthogonal Group and the Spin Group*. The one-sided multiplications and the criterion of joint continuity are *The Bounded Left and Right Multiplication on a Clifford Algebra*; the action on a module is *Bounded Clifford Modules and the Continuous Spin Representation*; the adjoint of the sandwich is the Hermitian layer.

## Summary of Notation

| symbol | meaning |
|---|---|
| $T_{x,y}(z)=xzy$ | the sandwich, $=L_{x}R_{y}=R_{y}L_{x}$ |
| $T_{x,y}T_{u,v}=T_{xu,vy}$ | the composition of the sandwiches |
| $\lVert T\rVert$ | the multiplication constant, $>1$ for the Euclidean norm ($\sqrt2$ attained, $2^{n/2}$ the bound) |
| $\operatorname{Int}_{x}=T_{x,x^{-1}}$ | the inner conjugation, an algebra automorphism |
| $x\mapsto\operatorname{Int}_{x}$, kernel $Z^{\times}$ | the group of inner automorphisms as a topological group |
| $\chi_{x}=T_{x,\alpha(x)^{-1}}$ | the signed inner conjugation, $v\mapsto xv\alpha(x)^{-1}$ |
| $\ker\chi=F^{\times}$, image $\mathrm{O}(V,q)$ | the covering of the orthogonal group |

## Further Reading

- Frank F. Bonsall and John Duncan, *Complete Normed Algebras* (Springer, 1973), for the group of units, the inner automorphisms and the operator norm.
- Nicolas Bourbaki, *Topological Groups* (Springer, 1998), for the quotient of a topological group by a closed central subgroup.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the Skolem–Noether theorem and the inner automorphisms of a central simple algebra.
- Claude Chevalley, *The Algebraic Theory of Spinors and Clifford Algebras* (Springer, 1997), for the twisted conjugation and its kernel.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd edition (Cambridge University Press, 2001), for the sandwich action in the classical notation.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the versor groups and the covering of the orthogonal group.
