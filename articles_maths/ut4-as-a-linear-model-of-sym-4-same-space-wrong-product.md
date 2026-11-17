# __$UT_4$ as a Linear Model of $\operatorname{Sym}_4$: Same Space, Wrong Product__

## Introduction

**The symmetric matrices and the upper triangular ones both have dimension $10$, and there is an explicit linear isomorphism between them that fixes the diagonal and sends the symmetric pair $E_{ij}+E_{ji}$ to the single unit $E_{ij}$; transported along it, the associative product of the triangular space is not the Jordan product of the symmetric space, and the two algebras agree on the space, the trace and the unit and on nothing else.**

The article writes the isomorphism, proves that it preserves the trace and the unit, exhibits two symmetric matrices whose products differ under the two readings, and lists what the linear model preserves and what it loses: the product, the cone, the Peirce decomposition, the rank and the determinant.

It assumes *$UT_4$ as the Complement of the Antisymmetric Part* and *The Jordan Algebra $\operatorname{Sym}_4$*. The case $n=2$ is *$UT_2$ as a Linear Model of $\operatorname{Sym}_2$: Same Space, Wrong Product*; the operator side is *The Two-Sided Operators and the Segre Cone at $n=4$*.

## The Isomorphism

**Definition.** Let $\varphi:\operatorname{Sym}_4\to UT_4$ be the linear map fixed on the basis by

$$
\varphi(E_{ii})=E_{ii},\qquad \varphi(E_{ij}+E_{ji})=E_{ij}\ \ (i<j).
$$

**Theorem.** $\varphi$ is an isomorphism of vector spaces.

**Proof.** Symmetric matrices have the basis $E_{ii}$ for $1\le i\le4$ and $E_{ij}+E_{ji}$ for $i<j$, ten elements in all; upper triangular matrices have the basis $E_{ij}$ for $i\le j$, also ten. The map sends one basis to the other, so it is invertible.

**The inverse.** $\varphi^{-1}(E_{ij})=E_{ij}+E_{ji}$ for $i<j$ and $\varphi^{-1}(E_{ii})=E_{ii}$.

**Proof.** Read the definition backwards.

**Proposition.** $\varphi$ preserves the trace and the unit: $\operatorname{tr}\varphi(A)=\operatorname{tr}A$ and $\varphi(\mathrm I_4)=\mathrm I_4$.

**Proof.** Both bases consist of matrices whose trace is $0$ off the diagonal and $1$ on it, and $\mathrm I_4$ is the sum of the four diagonal units in both spaces.

**The choice behind it.** The map is determined by the flag: the strict upper unit $E_{ij}$ is the image of the symmetric pair because $E_{ij}$ is the part above the diagonal. Changing the flag changes the map, and the diagonal is the only part that every choice fixes.

**Proof.** A different complement of $\operatorname{Skew}_4$ gives a different ten-dimensional space and a different basis pairing, while the diagonal lies in every complement considered here.

## The Two Products Do Not Correspond

**Definition.** On $\operatorname{Sym}_4$ the product is $A\circ B=\tfrac12(AB+BA)$; on $UT_4$ it is the ordinary product. The model transports the second to the first by $A*B=\varphi^{-1}(\varphi(A)\varphi(B))$.

**Proposition.** The product $*$ differs from $\circ$.

**Proof.** It is enough to find one pair where the two disagree, which the next proposition does.

**Proposition.** With $A=E_{12}+E_{21}$ one has $A\circ A=E_{11}+E_{22}$ and $\varphi(A)*\varphi(A)=0$.

**Proof.** $A^{2}=E_{12}E_{21}+E_{21}E_{12}=E_{11}+E_{22}$ since $E_{12}E_{12}=E_{21}E_{21}=0$. And $\varphi(A)=E_{12}$ with $E_{12}E_{12}=0$.

**Corollary.** The two products on the ten-dimensional space are not related by any scalar: one square is nonzero and the other is zero.

**Proof.** A scalar multiple of a nonzero matrix is nonzero.

**A second pair.** With $A=E_{11}$ and $B=E_{12}+E_{21}$, the Jordan product is $A\circ B=\tfrac12(E_{12}+E_{21})$, while the transported product is $\varphi(A)\varphi(B)=E_{11}E_{12}=E_{12}$, twice as large on the same entries.

**Proof.** $E_{11}E_{12}=E_{12}$ and $E_{12}E_{11}=0$.

**The structural reason.** $\varphi$ is not multiplicative because it is not built from the algebra: it identifies a symmetric pair, which is one element of $\operatorname{Sym}_4$, with a single unit, which is one element of $UT_4$, and the product of two such units depends on the order in a way the anticommutator does not see.

**Proof.** $E_{ij}E_{kl}=\delta_{jk}E_{il}$ while $\tfrac12\{(E_{ij}+E_{ji}),(E_{kl}+E_{lk})\}$ has terms in both orders; the two differ by the commutator.

## What Survives

**The table of invariants.**

| Property | Preserved by $\varphi$ |
|---|---|
| dimension | yes, $10$ |
| trace | yes |
| trace pairing | on the diagonal and across it, not between two pairs |
| unit | yes |
| diagonal subspace | yes |
| the flag | no: only $UT_4$ carries one |
| product | no |
| idempotents | no |
| cone of squares | no |
| rank of an element | no |
| the determinant of the image | no |

**Proposition.** The trace pairing is preserved on the diagonal and across it, and it is not preserved between two symmetric pairs: $\beta(E_{ii},E_{jj})=\beta(\varphi(E_{ii}),\varphi(E_{jj}))=\delta_{ij}$, and $\beta(E_{ii},E_{jk}+E_{kj})=\beta(E_{ii},E_{jk})=0$ for $j<k$, but $\beta(E_{12}+E_{21},E_{12}+E_{21})=2$ while $\beta(E_{12},E_{12})=0$.

**Proof.** The diagonal units pair by $\delta_{ij}$ in both spaces, and a diagonal unit kills both the pair and the single unit that is its image; the last computation is that of the corollary below.

**Corollary.** The model is not an isometry on the whole space: $\beta(A,A)=2$ for $A=E_{12}+E_{21}$ while $\beta(\varphi(A),\varphi(A))=\operatorname{tr}(E_{12}E_{12})=0$.

**Proof.** $A^{2}=E_{11}+E_{22}$ has trace $2$, and $E_{12}^{2}=0$.

**The one structure that carries over intact.** The subspace structure: the diagonal, the off-diagonal pairs, the strict upper part and the dimensions of all the pieces that are defined by position.

**Proof.** $\varphi$ sends the diagonal to the diagonal and the symmetric pair of the positions $(i,j)$ to the single position $(i,j)$; the counts agree because both are indexed by the same set of pairs.

## What Does Not Survive

**The cone.** The cone of squares of $\operatorname{Sym}_4(\mathbb{R})$ is the cone of positive semidefinite matrices, of dimension $10$; its image under $\varphi$ is not the set of squares of $UT_4$, which is not even a cone in the same sense.

**Proof.** The squares of $\operatorname{Sym}_4$ are the positive semidefinite matrices, while a square of an upper triangular matrix is upper triangular and need not be symmetric.

**The idempotents.** $E_{11}$ is an idempotent in both readings, but the rank-one projection $P=\tfrac12(E_{11}+E_{12}+E_{21}+E_{22})$ onto the line spanned by $e_1+e_2$ is a symmetric idempotent whose image is not idempotent.

**Proof.** $P^{2}=P$ by direct expansion. Its image is $\varphi(P)=\tfrac12(E_{11}+E_{12}+E_{22})$, whose square is $\tfrac14(E_{11}+2E_{12}+E_{22})$, which is not $\varphi(P)$.

**The rank and the determinant.** $\det A=-1$ for $A=E_{12}+E_{21}$, while $\det\varphi(A)=0$; the model does not preserve invertibility.

**Proof.** The eigenvalues of $A$ are $\pm1$; $E_{12}$ is nilpotent.

**The Peirce decomposition.** The Peirce spaces of a symmetric idempotent are defined by the Jordan product and do not correspond to the position spaces of the matrix units.

**Proof.** The Peirce rule $2E\circ X=X$ is an equation in the Jordan product, which the model does not preserve.

**The moral.** Dimension, trace and the diagonal are cheap invariants; the product, the cone and the rank are the expensive ones. A linear model preserves the cheap ones and can be written down in one line, which is exactly why it is dangerous: everything that the algebra is for lives in the part it does not preserve.

**Proof.** The table above lists the preserved properties as those defined by the linear structure and the trace, and the lost ones as those defined by the product.

## The Same Phenomenon at Order Two

**Proposition.** At $n=2$ the same construction gives an isomorphism between $\operatorname{Sym}_2$ and $UT_2$, both of dimension $3$, and the same failure: the symmetric matrix $E_{12}+E_{21}$ squares to $E_{11}+E_{22}$ while its image $E_{12}$ squares to zero.

**Proof.** The computation is the one above restricted to the first two coordinates.

**Corollary.** The failure is not a feature of the fourth order; what the fourth order adds is the size of the lost structure, since both the Jordan algebra and the triangular algebra become non-trivial at order four.

**Proof.** At order two both products are nearly trivial; at order four the Jordan algebra has degree four and the triangular algebra is a full Borel.

## Summary

The symmetric and the upper triangular matrices have the same dimension, and the map fixing the diagonal and sending a symmetric pair to the corresponding single unit is an isomorphism of vector spaces preserving the trace and the unit.

The associative product of the triangular space and the Jordan product of the symmetric space do not correspond under it: $E_{12}+E_{21}$ squares to $E_{11}+E_{22}$ in one reading and its image squares to zero in the other, so no scalar can repair the difference.

What survives is the linear structure, the trace, the unit and the position subspaces; what is lost is the product, the cone, the idempotents, the rank, the determinant and the Peirce decomposition. The model is a warning about dimension as an invariant, and the same warning holds at order two.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\varphi$ | the linear isomorphism $\operatorname{Sym}_4\to UT_4$ |
| $A*B=\varphi^{-1}(\varphi(A)\varphi(B))$ | the transported product |
| $A\circ B$ | the Jordan product, the true product of the half |
| $E_{ij}+E_{ji}\mapsto E_{ij}$ | the rule on the off-diagonal pairs |
| $\beta$ | the trace pairing, preserved on the diagonal only |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the distinction between a linear isomorphism and an isomorphism of algebras.
- [The Jordan Algebra $\operatorname{Sym}_4$](the-jordan-algebra-sym-4.html), for the product that the model fails to carry.
- [$UT_4$ as the Complement of the Antisymmetric Part](ut4-as-the-complement-of-the-antisymmetric-part.html), for the space on which the model lives.
- [The Two-Sided Operators and the Segre Cone at $n=4$](the-two-sided-operators-and-the-segre-cone-at-n-4.html), for the operator reading that does respect the product.
- [$UT_2$ as a Linear Model of $\operatorname{Sym}_2$: Same Space, Wrong Product](ut2-as-a-linear-model-of-sym-2-same-space-wrong-product.html), for the same construction at order two.
