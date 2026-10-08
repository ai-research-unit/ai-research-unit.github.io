# __The Bounded Left and Right Multiplication on a Clifford Algebra__

## Introduction

The left multiplication $L_{x}(y)=xy$ and the right multiplication $R_{x}(y)=yx$ are the two operators of a Clifford algebra that carry a single element, and their theory is the theory of the product of the algebra written in operator form. Two questions organise it. The first is the **norm** of the operators: for a submultiplicative norm with a unit of norm one, $\lVert L_{x}\rVert=\lVert R_{x}\rVert=\lVert x\rVert$, so the left regular representation is an isometry and the algebra is a closed subalgebra of its bounded operators; the sandwich of the companion article is then the product $L_{x}R_{y}$, and everything about the sandwich follows from the two multiplications. The second is the difference between **separate** and **joint** continuity: the product of the layer is continuous in each variable separately by hypothesis, which makes each $L_{x}$ and $R_{x}$ a bounded operator and the maps $x\mapsto L_{x}$, $x\mapsto R_{x}$ continuous pointwise, while the product is jointly continuous only when a **uniform** bound over the unit ball exists, and the uniform boundedness principle then shows that on a complete normed algebra separate continuity already forces joint continuity.

The last point is the substance of the article, and it is also where a warning is needed. The uniform boundedness principle applies to a bilinear map defined on the whole product of two complete normed spaces; it does not apply to a product that is only defined on a proper subset of the completion, and that is exactly what happens with the **Euclidean** norm of the definite case. The one-sided multiplications of the algebraic Clifford algebra are bounded for that norm, the product is separately continuous on the algebra, and the completion is complete — yet the product does not extend to the completion, so there is no bilinear map on which the principle could act; this is the same failure of the completion to be an algebra that *The Completion of a Clifford Algebra*, §*The Euclidean Norm and the Failure of Joint Continuity* records, and the article states the two sides of it.

The article treats the multiplications and their norms, the embedding of the algebra into its bounded operators, the criterion for joint continuity, the uniform boundedness theorem and the failure of its hypothesis for the Euclidean norm. The sandwich is *The Bounded Sandwich and the Continuous Inner Conjugation*; the modules and the spin representation are *Bounded Clifford Modules and the Continuous Spin Representation*; the completion is *The Completion of a Clifford Algebra*; the adjoints of the multiplications are the Hermitian layer's *The Adjoint of the Left and the Right Multiplication*. Throughout, $\mathrm{Cl}(V,q)$ is a normed Clifford algebra of the layer with a norm inducing its topology, submultiplicative and with $\lVert1\rVert=1$ where stated.

## The Multiplications and their Norms

**Definition.** The **left** and the **right multiplication** by $x$ are $L_{x}(y)=xy$ and $R_{x}(y)=yx$, linear maps of the algebra into itself.

**Theorem (the norm of a multiplication).** Let the norm be submultiplicative with $\lVert1\rVert=1$. Then for every $x$

$$
\lVert L_{x}\rVert=\lVert R_{x}\rVert=\lVert x\rVert ,
$$

and the maps $x\mapsto L_{x}$ and $x\mapsto R_{x}$ are **isometric** algebra anti-isomorphisms of $\mathrm{Cl}(V,q)$ onto their images; their images are closed subalgebras of the bounded operators when the algebra is complete.

*Proof.* Submultiplicativity gives $\lVert L_{x}y\rVert\le\lVert x\rVert\lVert y\rVert$, whence $\lVert L_{x}\rVert\le\lVert x\rVert$; and $\lVert L_{x}\rVert\ge\lVert L_{x}1\rVert/\lVert1\rVert=\lVert x\rVert$, whence equality. The representation law $L_{x}L_{y}=L_{xy}$ makes $x\mapsto L_{x}$ multiplicative and hence an isomorphism onto its image, and $R_{x}R_{y}=R_{yx}$ makes $x\mapsto R_{x}$ an anti-isomorphism; an isometry onto its image is injective and its image is closed when the target is complete. $\square$

**Proposition (the two representations commute).** For all $x,y$ one has $L_{x}R_{y}=R_{y}L_{x}$, the operator $L_{x}R_{y}$ is the sandwich $T_{x,y}$, and $\lVert T_{x,y}\rVert\le\lVert x\rVert\lVert y\rVert$.

*Proof.* Both sides send $z$ to $xzy$; the bound is $\lVert L_{x}R_{y}\rVert\le\lVert L_{x}\rVert\lVert R_{y}\rVert=\lVert x\rVert\lVert y\rVert$ by the theorem. $\square$

**Corollary (the algebra is a subalgebra of its bounded operators).** If the algebra is complete and the norm submultiplicative with a unit of norm one, the left regular representation identifies it isometrically with the closed subalgebra $\{L_{x}\}\subseteq\mathcal{B}(\mathrm{Cl}(V,q))$, and the completion of the algebra is identified with the closure of that image.

*Proof.* The theorem gives the isometry and the closure; the completion of the algebra is isometric to the closure of the image because the image is dense in its own closure and isometric to the algebra, and an isometry between dense subspaces extends to an isometry of the completions. $\square$

**Remark (the norm-dependent nature of the statement).** The equality $\lVert L_{x}\rVert=\lVert x\rVert$ uses both the submultiplicativity and $\lVert1\rVert=1$. Without submultiplicativity the operator $\lVert L_{x}\rVert$ can be strictly larger than $\lVert x\rVert$ and there is no isometry; the dimension of the algebra then still permits a norm making the product jointly continuous, but it is not the given one. The operator norm of the regular representation is thus a measure of how far the given norm is from being submultiplicative, and it is the norm of the theorem above precisely when the two agree.

## The Criterion for Joint Continuity

**Definition.** The product of the algebra is **jointly continuous** when the map $\mathrm{Cl}(V,q)\times\mathrm{Cl}(V,q)\to\mathrm{Cl}(V,q)$, $(x,y)\mapsto xy$, is continuous for the product topology; it is **separately continuous** when it is continuous in each variable with the other fixed.

**Theorem (the criterion).** Let the algebra be normed. Then the following are equivalent:

1. the product is jointly continuous;
2. the product is bounded on the product of the closed unit balls, that is $\sup\{\lVert xy\rVert : \lVert x\rVert\le1,\lVert y\rVert\le1\}<\infty$;
3. the operator norms of the multiplications are uniformly bounded, $\sup\{\lVert L_{x}\rVert : \lVert x\rVert\le1\}<\infty$;
4. the norm is equivalent to a submultiplicative norm on the algebra.

*Proof.* (1) implies (2) because a continuous bilinear map is bounded on a product of bounded sets; (2) implies (3) because $\lVert L_{x}\rVert=\sup\{\lVert xy\rVert : \lVert y\rVert\le1\}$, and (3) implies (2) by the same identity; (3) implies (4) with the norm $\lVert x\rVert'=\lVert L_{x}\rVert$, which is a norm because $\lVert x\rVert'\ge\lVert x\rVert/\lVert1\rVert$ and equivalent to the given one by (3), and which is submultiplicative because $\lVert xyz\rVert\le\lVert L_{x}\rVert\lVert yz\rVert$ for every $z$, whence $\lVert xy\rVert'=\lVert L_{xy}\rVert\le\lVert L_{x}\rVert\lVert L_{y}\rVert=\lVert x\rVert'\lVert y\rVert'$; and (4) implies (1) because a submultiplicative norm makes the product continuous. $\square$

**Theorem (complete normed algebras are topological algebras).** Let $\mathrm{Cl}(V,q)$ be a **complete** normed algebra whose product is separately continuous, and suppose the product is defined on the whole product of the space with itself. Then the product is jointly continuous, and the algebra is a topological algebra for its norm.

*Proof.* The uniform boundedness principle: for each fixed $y$ the set $\{L_{x} : \lVert x\rVert\le1\}$ is a family of continuous linear maps with $\sup_{\lVert x\rVert\le1}\lVert L_{x}y\rVert=\lVert R_{y}\rVert<\infty$ for each $y$, because the product is separately continuous and hence $R_{y}$ is bounded; the principle then gives $\sup_{\lVert x\rVert\le1}\lVert L_{x}\rVert<\infty$, which is condition (3) of the criterion. $\square$

**Remark (the hypothesis that cannot be dropped).** The theorem genuinely needs the product to be **defined** on the whole product of the complete space with itself. A bilinear map whose domain is a proper subspace of a complete space is not addressed by the uniform boundedness principle, and the next theorem exhibits the case: a complete normed space that carries a separately continuous product on a dense subalgebra which does not extend. The pair "separate continuity everywhere" and "completeness" is not sufficient without the domain hypothesis, and this is the precise sense in which the completion of the definite case is not a topological algebra.

## The Failure for the Euclidean Norm

**Theorem (the Euclidean norm).** Let $F=\mathbb{R}$ and let the Clifford algebra of a definite form carry the **Euclidean norm** of *The Euclidean Form, the Norm and the Completion on a Clifford Algebra*, in which the blades of an orthonormal basis are orthonormal. Then:

1. the norm is **not submultiplicative**: the element $x=1+e_{1}$ of $\mathrm{Cl}_{1,0}$ satisfies $x^{2}=2(1+e_{1})$, so that $\lVert x^{2}\rVert=2\sqrt2$ against $\lVert x\rVert^{2}=2$, the ratio $\sqrt2$;
2. in dimension $n$ the product satisfies $\lVert xy\rVert\le2^{n/2}\lVert x\rVert\lVert y\rVert$, the Cauchy–Schwarz bound of *The Euclidean Form, the Norm and the Completion on a Clifford Algebra*, §*Boundedness of the Multiplication Operators*, and the ratio $\sqrt2$ is **attained**, at the idempotent $\tfrac12(1+e_{1})$ of $\mathrm{Cl}_{1,0}\subseteq\mathrm{Cl}(V,q)$, whose norm is $2^{-1/2}$;
3. the bound $2^{n/2}$ grows without bound with $n$, and in an infinite-dimensional space the multiplications have **no uniform bound** over the unit ball of the Euclidean norm, so the criterion of joint continuity above fails;
4. the product does **not extend** to the Hilbert completion, which is the Fock space of the canonical anticommutation relations of *Infinite-Dimensional Clifford Algebras and CAR with Inner Conjugation* and not an algebra; the completions in which it is an algebra are the projective norm and the C*-norm of *The Completion of a Clifford Algebra*.

*Proof.* For (1), $(1+e_{1})^{2}=1+2e_{1}+e_{1}^{2}=2+2e_{1}$ with $e_{1}^{2}=1$ for the definite form, and the blades $1,e_{1}$ are orthonormal, so $\lVert2+2e_{1}\rVert=2\sqrt2$ and $\lVert1+e_{1}\rVert=\sqrt2$. For (2), the estimate is that of *The Euclidean Form, the Norm and the Completion on a Clifford Algebra*, §*Boundedness of the Multiplication Operators*, proved there by Cauchy–Schwarz on the $2^{n}$ coefficients of the expansion in the blade basis. The ratio $\sqrt2$ is attained: $\tfrac12(1+e_{1})$ is a nonzero idempotent of $\mathrm{Cl}_{1,0}\subseteq\mathrm{Cl}(V,q)$ of norm $2^{-1/2}$, and $\lVert x^{2}\rVert/\lVert x\rVert^{2}=1/\lVert x\rVert=\sqrt2$, so the norm is not submultiplicative. For (3), an infinite-dimensional space with a definite form contains an isometric copy of $\mathbb{R}^{n}$ for every $n$; the bound $2^{n/2}$ of the subalgebra grows without bound with the dimension, the multiplications have no uniform bound over the unit ball, and condition (3) of the criterion fails — the failure recorded in *The Completion of a Clifford Algebra*, §*The Euclidean Norm and the Failure of Joint Continuity*. For (4), a product extending to the completion would be a separately continuous product defined on the whole product of a complete normed space with itself, hence jointly continuous by the theorem above, and then the norm would be equivalent to a submultiplicative norm, which (1) and (3) exclude.

**Remark (the correct reading).** The failure is not a pathology of the Clifford case but the general fact that a separately continuous product on a dense subalgebra need not extend to the completion, together with the specific form $2^{n/2}$ of the Cauchy–Schwarz bound of the Euclidean norm. What the Clifford algebra provides is a natural family of examples, one per dimension and signature, and a natural remedy: the projective norm and the C*-norm of *The Completion of a Clifford Algebra*, for which the product **is** submultiplicative, the criterion holds at its fourth line, and the completion is a Banach algebra. The article records the bound, its elementary attainment at the idempotent $\tfrac12(1+e_{1})$, and the failure of the completion to be an algebra in that norm, which is what turns the estimate into a statement about infinite dimension.

## Worked Cases

### The Finite-Dimensional Case

For a finite-dimensional algebra over a complete valued field the criterion is automatic: the unit ball is compact, the product is separately continuous, and a continuous map on a compact set is bounded, so $L_{x}$ is bounded and the family is uniformly bounded. All four conditions of the criterion hold, the norm is equivalent to a submultiplicative one, and the algebra is a topological algebra. The case is the one in which the whole operator theory is trivial, and it is the reason the layer's operator statements are infinite-dimensional.

### The Projective and the C*-Completions

For the projective norm of *The Completion of a Clifford Algebra* the product is submultiplicative by construction, so condition (4) of the criterion holds and the completion is a Banach algebra; for the C*-norm of the Fock representation the same holds by the general theory of C*-algebras, and the left and right multiplications are isometries of the algebra onto their images. The two cases are the two ways of repairing the Euclidean failure.

### The Completion of the Euclidean Algebra

For the Euclidean algebra of an infinite-dimensional space the Euclidean norm fails, with the bound $2^{n/2}$ of the finite-dimensional subalgebras growing without bound; the projective norm and the C*-norm succeed, and the two completions coincide exactly when the coefficient series converge absolutely in the appropriate sense, a comparison left to *The Completion of a Clifford Algebra*.

## Summary

The **left** and the **right multiplication** of a normed Clifford algebra with a submultiplicative norm and a unit of norm one satisfy $\lVert L_{x}\rVert=\lVert R_{x}\rVert=\lVert x\rVert$ and commute, $L_{x}R_{y}=R_{y}L_{x}=T_{x,y}$; consequently the left regular representation is an **isometric isomorphism** of the algebra onto a closed subalgebra of its bounded operators and the algebra is the same normed algebra as that subalgebra.

The product is **jointly continuous** exactly when it is bounded on the product of the unit balls, equivalently when the operator norms of the multiplications are uniformly bounded, equivalently when the norm is equivalent to a submultiplicative one; and on a **complete** normed algebra on which the product is defined everywhere, separate continuity already implies joint continuity, by the **uniform boundedness principle**. That hypothesis — the product defined on the whole product of the complete space — cannot be dropped: for the **Euclidean norm** of the definite case the product is separately continuous on the algebraic algebra, each one-sided multiplication is bounded, and yet the bound $2^{n/2}$ grows without bound with the dimension, so there is no uniform bound and the product does not extend to the completion; the completion is the Fock space of the canonical anticommutation relations and not an algebra. The repair is the projective norm and the C*-norm of *The Completion of a Clifford Algebra*, for which the criterion holds at its fourth line and the completion is a Banach algebra.

## Summary of Notation

| symbol | meaning |
|---|---|
| $L_{x}(y)=xy$, $R_{x}(y)=yx$ | the one-sided multiplications |
| $\lVert L_{x}\rVert=\lVert R_{x}\rVert=\lVert x\rVert$ | the isometry, for a submultiplicative norm with $\lVert1\rVert=1$ |
| $L_{x}L_{y}=L_{xy}$, $R_{x}R_{y}=R_{yx}$ | the representation laws |
| $L_{x}R_{y}=R_{y}L_{x}=T_{x,y}$ | the sandwich as a product of the two |
| $\sup_{\lVert x\rVert\le1}\lVert L_{x}\rVert<\infty$ | the criterion of joint continuity |
| uniform boundedness principle | separate continuity $\Rightarrow$ joint, on a complete algebra |
| Euclidean norm, Cauchy–Schwarz bound $2^{n/2}$ | the counterexample: separate yes, joint no, no extension |

## Further Reading

- Frank F. Bonsall and John Duncan, *Complete Normed Algebras* (Springer, 1973), for the regular representation, the operator norm and the submultiplicative norm.
- Walter Rudin, *Functional Analysis*, 2nd edition (McGraw-Hill, 1991), for the uniform boundedness principle and the continuity of a separately continuous bilinear map.
- Nicolas Bourbaki, *Topological Vector Spaces* (Springer, 1987), for the criterion for the continuity of a bilinear map and the notion of a topological algebra.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, Vol. I (Academic Press, 1983), for the Fock representation and the one-sided multiplications.
- John B. Conway, *A Course in Functional Analysis*, 2nd edition (Springer, 1990), for the equivalence of norms on a finite-dimensional space and the boundedness of a bilinear map on a compact product.
- Ola Bratteli and Derek W. Robinson, *Operator Algebras and Quantum Statistical Mechanics*, Vol. 1 (Springer, 1987), for the C*-norm and the boundedness of the multiplications.
