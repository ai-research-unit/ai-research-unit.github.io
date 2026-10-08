# __Operators on a Topological Clifford Algebra__

## Introduction

The operators of a topological Clifford algebra are the multiplications and the sandwiches: the left multiplication $L_{x}(y)=xy$, the right multiplication $R_{x}(y)=yx$, the sandwich $T_{x,y}(z)=xzy$, the inner conjugation $T_{x,x^{-1}}$ of a unit, and the intrinsic anti-involutions of the algebra, the grade involution, the reversion and the Clifford conjugation. All of them are linear maps of the algebra into itself, and the layer consists of the statements that are topological about them: which are continuous, which are bounded with respect to a norm, what the operator norm of a multiplication is, and when the product of the algebra is jointly continuous. This article is the entry of the operator theory of the category; the companions are *The Bounded Left and Right Multiplication on a Clifford Algebra*, *The Bounded Sandwich and the Continuous Inner Conjugation* and *Bounded Clifford Modules and the Continuous Spin Representation*.

The organising object is the algebra $\mathcal{B}(\mathrm{Cl}(V,q))$ of **bounded** operators of the algebra with the operator norm, together with the embedding of the algebra into it by the left regular representation. That embedding is the reason the operator theory is not an appendix to the algebra: the map $x\mapsto L_{x}$ is an isometric algebra isomorphism onto its image when the norm of the algebra is submultiplicative and the unit has norm one, so the algebra and a subalgebra of its bounded operators are the same normed algebra; the sandwich is the product $L_{x}R_{y}$ of a left and a right multiplication, and the inner conjugation is the sandwich of a unit with its inverse. The two continua that occur in the layer are the continuity of the product in each variable separately, which is part of the definition of the algebra, and the **joint** continuity of the product, which is not assumed and which the companions characterise.

The article treats the operators of the layer, the algebra of bounded operators and its embedding, the continuity of the structure, and the case of the completion. The adjoint of a multiplication is a statement of the **Hermitian** layer, where a form gives it a meaning, and is owned by *The Adjoint of the Left and the Right Multiplication*, *The Adjoint of the Sandwich on a Hermitian Algebra* and *The Adjoint of the Left Multiplication on a Hermitian Algebra* of `Topology on Sesqualgebras with a degree-2 form`; the Hilbert structure of the algebra is owned by *The Euclidean Form, the Norm and the Completion on a Clifford Algebra*; the canonical anticommutation relations and the Fock representation are *Infinite-Dimensional Clifford Algebras and CAR with Inner Conjugation*; the two completions are *The Completion of a Clifford Algebra*. Throughout, $\mathrm{Cl}(V,q)$ is the topological Clifford algebra of *Topological Clifford Algebras*, carrying the quotient topology of the tensor algebra, and a **normed** algebra below means one carrying a norm that induces its topology.

## The Operators of the Layer

**Definition.** The operators attached to the elements of the algebra are

$$
L_{x}(y)=xy,\qquad R_{x}(y)=yx,\qquad T_{x,y}(z)=xzy,\qquad \chi_{x}=T_{x,\alpha(x)^{-1}},
$$

the **left multiplication**, the **right multiplication**, the **sandwich** and the **signed inner conjugation**, the last for $x$ a unit and $\alpha$ the grade involution; the **intrinsic anti-involutions** are the grade involution $\alpha$, the reversion $x\mapsto x^{r}$ and the Clifford conjugation $x^{\natural}=\alpha(x^{r})$ of *Topological Clifford Algebras*, §*The Conventions of the Category*, read as linear maps of the algebra into itself.

**Proposition (the algebraic identities).** The maps are linear; $L_{x}L_{y}=L_{xy}$, $R_{x}R_{y}=R_{yx}$, $L_{x}R_{y}=R_{y}L_{x}$ and $T_{x,y}T_{u,v}=T_{xu,vy}$; $T_{x,y}=L_{x}R_{y}=R_{y}L_{x}$; and $T_{x,z}$ is the inner automorphism $y\mapsto xyx^{-1}$ when $z=x^{-1}$, with $\chi_{x}(v)=xv\alpha(x)^{-1}$ the twisted conjugation of the Part I entries.

*Proof.* Each is associativity of the product, together with the multiplicativity of $\alpha$ and of the reversion and conjugation as (anti-)automorphisms; the identities are those of *Two-Sided Operators on a Clifford Algebra* and *The Sandwich on a Clifford Algebra*, quoted and not re-derived. $\square$

**Definition.** When the algebra carries a norm the operator norm of a linear map $S$ is $\lVert S\rVert=\sup\{\lVert Sx\rVert : \lVert x\rVert\le1\}$, and the algebra of **bounded** operators is

$$
\mathcal{B}(\mathrm{Cl}(V,q)) = \{S : \lVert S\rVert<\infty\}
$$

with the operator norm, a normed algebra because $\lVert ST\rVert\le\lVert S\rVert\lVert T\rVert$, and a Banach algebra when the algebra is a Banach space.

**Proposition (the embedding).** Let the norm of the algebra be submultiplicative with $\lVert1\rVert=1$. Then $\lVert L_{x}\rVert=\lVert R_{x}\rVert=\lVert x\rVert$, the left regular representation $x\mapsto L_{x}$ is an **isometric** algebra isomorphism of $\mathrm{Cl}(V,q)$ onto its image, and that image is a closed subalgebra of $\mathcal{B}(\mathrm{Cl}(V,q))$ when the algebra is complete.

*Proof.* Submultiplicativity gives $\lVert L_{x}y\rVert\le\lVert x\rVert\lVert y\rVert$, so $\lVert L_{x}\rVert\le\lVert x\rVert$; the reverse inequality follows from $\lVert L_{x}\rVert\ge\lVert L_{x}1\rVert/\lVert1\rVert=\lVert x\rVert$ when the unit has norm one. Multiplicativity of the representation is the proposition above, and an isometry of a complete space onto its image has closed image. $\square$

**Theorem (the continuity of the operators).** Let the product of the algebra be continuous in each variable separately, as in the definition of the layer. Then $x\mapsto L_{x}$ and $x\mapsto R_{x}$ are continuous for the topology of pointwise convergence of the operators, the map $(x,y)\mapsto T_{x,y}$ is continuous in the same sense, and $x\mapsto T_{x,x^{-1}}$ is continuous on the open group of units into the invertible operators. If the algebra is normed and complete the maps take values in the bounded operators and are continuous for the operator norm when the norm is submultiplicative.

*Proof.* For fixed $y$, the map $x\mapsto xy$ is continuous by the separate continuity of the product, and the pointwise limit of continuous maps is continuous for the topology of pointwise convergence; the sandwich is the composite of two such maps and the inner conjugation is the composite of the sandwich with the continuous inversion of the unit group. In the normed case the bound $\lVert xy\rVert\le\lVert x\rVert\lVert y\rVert$ gives the operator norm estimates $\lVert L_{x}\rVert\le\lVert x\rVert$ and $\lVert T_{x,y}\rVert\le\lVert x\rVert\lVert y\rVert$, whence continuity in the operator norm. $\square$

**Remark (what the layer does not assume).** The product of the layer is continuous in each variable separately and **not** jointly: joint continuity is an extra hypothesis, and the companions prove that it holds in the complete normed case, characterise it by a uniform bound, and show that it fails for the Euclidean norm of the definite case. Nothing in this entry uses an adjoint, a positivity or a Hilbert structure; those belong to the Hermitian layer of `Topology on Sesqualgebras with a degree-2 form`.

## The Continuity of the Structure

**Proposition (the intrinsic anti-involutions).** In finite dimension the grade involution, the reversion and the Clifford conjugation are continuous, being linear maps of a finite-dimensional space; in general they are continuous whenever their restriction to the generating module $V$ is, and they are isometries for a norm that is invariant under them.

*Proof.* An (anti-)automorphism of the algebra is determined by its values on $V$, and a linear map on a finite-dimensional Hausdorff space is continuous. In general the values on $V$ determine the map on the tensor algebra and hence on the quotient, by the universal property of the quotient topology; the isometry statement is the invariance of the norm under the induced permutations of the grades, which holds for the Euclidean norm of the Hermitian layer. $\square$

**Theorem (the closure of the algebra of operators).** Let the algebra be normed and complete with a submultiplicative norm and $\lVert1\rVert=1$. Then the set $\{L_{x}\}$, the set $\{R_{x}\}$ and the set of sandwiches are closed under composition, and the closure in $\mathcal{B}(\mathrm{Cl}(V,q))$ of the image of the left regular representation is a closed subalgebra isometrically isomorphic to the completion of the algebra; the operator $L_{x}$ extends by continuity to the completion with the same norm.

*Proof.* The compositions are given by the proposition on the algebraic identities, so the images are subalgebras; the image of an isometry between complete spaces is closed, and the extension of a bounded operator to a completion is the standard one, with the norm preserved because the operator is an isometry on a dense subspace. $\square$

## Worked Cases

### The Finite-Dimensional Case

For a finite-dimensional algebra over a complete valued field every linear map is bounded and $\mathcal{B}(\mathrm{Cl}(V,q))$ is the finite-dimensional algebra $\operatorname{End}(\mathrm{Cl}(V,q))$; the operator norm is the unique norm up to equivalence, the group of units is open, and the sandwich map $(x,y)\mapsto T_{x,y}$ is continuous in both variables jointly, since it is bilinear on a finite product of finite-dimensional spaces. Every statement of the entry is therefore trivial here, and the content of the operator theory is in the infinite-dimensional case.

### The Exterior Algebra

For the exterior algebra of a finite-dimensional space with the norm of the coefficient vector, the left multiplication is the exterior product, $\lVert L_{u}\rVert\le\lVert u\rVert$ with equality when the unit has norm one, and the sandwich $T_{u,v}(w)=u\wedge w\wedge v$ has norm at most $\lVert u\rVert\lVert v\rVert$; the products are universally bounded in the finite-dimensional case and the criterion of joint continuity of the companion article is automatic.

### The Infinite-Dimensional Case

Let the algebra be the completion of the Clifford algebra of a Hilbert space for the projective norm of *The Completion of a Clifford Algebra*. Then the left and right multiplications are bounded, the embedding is isometric onto its image, and the closure of the image is a closed subalgebra of the bounded operators isomorphic to the completion; the operator norm is the C*-norm of the Fock representation of *Infinite-Dimensional Clifford Algebras and CAR with Inner Conjugation*. For the **Euclidean** norm of the definite case, in which the blades are orthonormal, the bound $2^{n/2}$ of the finite-dimensional subalgebras grows without bound with the dimension, so the operator norms of the multiplications are unbounded over the unit ball; that failure of joint continuity is treated in *The Bounded Left and Right Multiplication on a Clifford Algebra*.

## Summary

The operators of the layer are the **left and right multiplications** $L_{x},R_{x}$, the **sandwich** $T_{x,y}=L_{x}R_{y}=R_{y}L_{x}$, the **inner conjugation** $T_{x,x^{-1}}$ and the **signed inner conjugation** $\chi_{x}=T_{x,\alpha(x)^{-1}}$, together with the intrinsic anti-involutions. They satisfy $L_{x}L_{y}=L_{xy}$, $R_{x}R_{y}=R_{yx}$, $T_{x,y}T_{u,v}=T_{xu,vy}$ and the commutation $L_{x}R_{y}=R_{y}L_{x}$.

When the algebra carries a submultiplicative norm with a unit of norm one, the left regular representation is an **isometric** algebra isomorphism onto its image, $\lVert L_{x}\rVert=\lVert R_{x}\rVert=\lVert x\rVert$ and $\lVert T_{x,y}\rVert\le\lVert x\rVert\lVert y\rVert$, and the image is a closed subalgebra of the bounded operators when the algebra is complete; the extension of $L_{x}$ to the completion preserves the norm. The **continuity** of $x\mapsto L_{x}$ and of $(x,y)\mapsto T_{x,y}$ is exactly the separate continuity of the product, which is a hypothesis of the layer; the **joint** continuity is an extra condition, characterised in *The Bounded Left and Right Multiplication on a Clifford Algebra*, and the modulus of a continuous action on a module is *Bounded Clifford Modules and the Continuous Spin Representation*. Nothing here uses an adjoint: the adjoints of these operators belong to the Hermitian layer.

## Summary of Notation

| symbol | meaning |
|---|---|
| $L_{x}(y)=xy$, $R_{x}(y)=yx$ | the left and the right multiplication |
| $T_{x,y}(z)=xzy$ | the sandwich, equal to $L_{x}R_{y}=R_{y}L_{x}$ |
| $\chi_{x}=T_{x,\alpha(x)^{-1}}$ | the signed inner conjugation, $v\mapsto xv\alpha(x)^{-1}$ |
| $\alpha,r,\natural$ | the grade involution, the reversion, the Clifford conjugation |
| $\mathcal{B}(\mathrm{Cl}(V,q))$ | the bounded operators with the operator norm |
| $\lVert L_{x}\rVert=\lVert x\rVert$ | the isometry of the regular representation |
| $\lVert T_{x,y}\rVert\le\lVert x\rVert\lVert y\rVert$ | the bound on the sandwich |

## Further Reading

- Frank F. Bonsall and John Duncan, *Complete Normed Algebras* (Springer, 1973), for the operator norm, the regular representation and the group of units.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, Vol. I (Academic Press, 1983), for the topology of the bounded operators and the separate continuity of the product.
- Nicolas Bourbaki, *Topological Vector Spaces* (Springer, 1987), for the quotient topology of an algebra and the continuity of a bilinear map.
- Claude Chevalley, *The Algebraic Theory of Spinors and Clifford Algebras* (Springer, 1997), for the sandwich and the twisted conjugation.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd edition (Cambridge University Press, 2001), for the operators of a Clifford algebra in the classical notation.
- John B. Conway, *A Course in Functional Analysis*, 2nd edition (Springer, 1990), for the completion of a bounded operator and the extension by continuity.
