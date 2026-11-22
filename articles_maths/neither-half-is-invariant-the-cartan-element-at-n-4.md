# __Neither Half Is Invariant: the Cartan Element Carries $\operatorname{Sym}$ into $\Lambda$__

## Introduction

**The subject.** The algebra splits into symmetric and antisymmetric matrices, and the copy acts by conjugation. The diagonal generator already breaks the splitting: it carries a symmetric matrix to an antisymmetric one. The two halves are therefore not invariant under the copy, although each single anti-Hermitian generator preserves a different splitting, the one given by the Hermitian adjoint.

**The order of the article.** The first section fixes the two halves and their dimensions. The second computes the example that breaks the splitting. The third proves the general statement and separates the two involutions, the transpose and the Hermitian adjoint. The fourth explains what the failure costs and what it leaves intact. The fifth draws the boundary with the parity rule, where the splitting does hold.

**It assumes** *The Clebsch–Gordan Decomposition of $M_4(\mathbb{C})$* for the carriers and *The Parity Rule: $\operatorname{Sym}^{2}=V_3\oplus V_1$ and $\Lambda^{2}=V_2\oplus V_0$* for the splitting of the module. The row at order two is *Neither Half Is Invariant: the Cartan Element*.

**The result in one line.** $[J_z,E_{01}+E_{10}]=E_{01}-E_{10}$, so $\operatorname{ad}_{J_z}$ carries $\operatorname{Sym}$ into $\Lambda$ and no generator of the complexified copy preserves the splitting.

**Boundaries.** The article does not compute the intersections of the carriers with the halves; those dimensions are the subject of *The Intersection Table*. It does not treat the real forms, which belong to *The Quaternionic Structure of the Module at $n=4$*.

## The Two Halves

**Definition.** $\operatorname{Sym}=\{X:X^{\mathsf T}=X\}$ and $\Lambda=\{X:X^{\mathsf T}=-X\}$ are the eigenspaces of the transpose involution $\theta(X)=X^{\mathsf T}$ for the eigenvalues $+1$ and $-1$.

**Proposition.** Both halves are complex subspaces, of complex dimensions $10$ and $6$ and real dimensions $20$ and $12$, and the algebra is their direct sum.

*Proof.* The transpose is complex-linear and involutive, so its eigenspaces are complex subspaces; the dimension of $\operatorname{Sym}$ is $4\cdot5/2=10$ and of $\Lambda$ is $4\cdot3/2=6$, and the two add to sixteen.

**Corollary.** The trace vanishes on $\Lambda$ and the identity lies in $\operatorname{Sym}$.

*Proof.* $\operatorname{tr}X=-\operatorname{tr}X^{\mathsf T}=-\operatorname{tr}X$ on $\Lambda$, and the identity is symmetric.

**Corollary.** Neither half is stable under multiplication: the product of two symmetric matrices is not symmetric unless they commute, and the product of two antisymmetric matrices is symmetric.

*Proof.* $(XY)^{\mathsf T}=Y^{\mathsf T}X^{\mathsf T}$; for symmetric factors this is $YX$, which differs from $XY$ in general, and for antisymmetric factors it is $(-X)(-Y)=XY$.

## The Example That Breaks the Splitting

**Proposition.** With $J_z$ the diagonal generator and $E_{ij}$ the matrix units,

$$
[J_z,E_{01}+E_{10}]=E_{01}-E_{10}.
$$

The left side is the image of a symmetric matrix under the adjoint action of a generator, and the right side is antisymmetric.

*Proof.* $[J_z,E_{01}]=(m_0-m_1)E_{01}=E_{01}$ and $[J_z,E_{10}]=(m_1-m_0)E_{10}=-E_{10}$; adding the two gives the display. The matrix $E_{01}+E_{10}$ is symmetric and $E_{01}-E_{10}$ is antisymmetric.

**Corollary.** $\operatorname{ad}_{J_z}$ does not preserve $\operatorname{Sym}$ and does not preserve $\Lambda$; it exchanges them.

*Proof.* On a symmetric matrix with $J_z$ symmetric, $(J_zX-XJ_z)^{\mathsf T}=XJ_z-J_zX=-(J_zX-XJ_z)$, so the image is antisymmetric; the same computation with the signs reversed gives the other inclusion.

**Corollary.** The copy does not preserve the splitting: the conjugated matrix $\Phi_q(E_{01}+E_{10})$ is not symmetric for $q$ whose generator has a nonzero $J_z$ component.

*Proof.* The derivative at the identity of $q\mapsto\Phi_q(X)$ is $\operatorname{ad}_{\xi}X$ for $\xi$ in the Lie algebra; if the derivative is antisymmetric and nonzero, the curve leaves $\operatorname{Sym}$.

**The reading.** The failure is not a failure of the group but a failure of the complexified action: the real Lie algebra preserves other splittings, and the complex-linear combinations of its elements do not preserve this one.

## The Two Involutions

**Proposition.** The transpose is complex-linear and the Hermitian adjoint is anti-linear; the first has the halves $\operatorname{Sym}$ and $\Lambda$ as eigenspaces, the second has the Hermitian and anti-Hermitian matrices.

*Proof.* $(X+Y)^{\mathsf T}=X^{\mathsf T}+Y^{\mathsf T}$ and $(cX)^{\mathsf T}=cX^{\mathsf T}$; while $(cX)^{\dagger}=\bar cX^{\dagger}$. The eigenspaces are read off from $X^{\mathsf T}=\pm X$ and $X^{\dagger}=\pm X$.

**Proposition.** The adjoint action of the anti-Hermitian generators $iJ_k$ preserves both the Hermitian and the anti-Hermitian halves, while the adjoint action of the Hermitian generators $J_k$ exchanges them.

*Proof.* If $X$ is Hermitian and $J$ is Hermitian, $(JX-XJ)^{\dagger}=XJ-JX=-(JX-XJ)$, so $\operatorname{ad}_{J}X$ is anti-Hermitian; multiplying by $i$ gives $\operatorname{ad}_{iJ}X=i\operatorname{ad}_{J}X$, which is Hermitian. Hence $\operatorname{ad}_{iJ}$ preserves the Hermitian half, and the same computation with the signs reversed preserves the anti-Hermitian half.

**Corollary.** The Lie algebra of the copy, consisting of the anti-Hermitian matrices, acts on the algebra preserving the Hermitian splitting; the complexification does not preserve the symmetric splitting.

*Proof.* The two propositions: the real form acts by $\operatorname{ad}_{iJ}$, which preserves one splitting, and the complex-linear generator $\operatorname{ad}_{J}$ breaks the other.

**Corollary.** The two splittings are different: a matrix can be symmetric and anti-Hermitian at once, for instance $i(E_{01}-E_{10})$.

*Proof.* $i(E_{01}-E_{10})$ is antisymmetric and Hermitian, as computed from the two involutions.

## What the Failure Costs

**Proposition.** The carriers are not contained in either half, and neither half is a sum of carriers.

*Proof.* If $\operatorname{Sym}$ were a sum of carriers it would be invariant, since each carrier is; but $\operatorname{ad}_{J_z}$ carries a symmetric matrix out of $\operatorname{Sym}$, so $\operatorname{Sym}$ is not invariant, and the same holds for $\Lambda$.

**Corollary.** The decomposition of the algebra into carriers cuts across the splitting: each carrier has a nonzero part in each half except the centre, which lies entirely in $\operatorname{Sym}$.

*Proof.* The intersection dimensions of the next article, or the argument that a carrier contained in one half would make that half invariant.

**Corollary.** The symmetric and antisymmetric parts of an element of a carrier are not separately in the carrier, and the operation $X\mapsto(X+X^{\mathsf T})/2$ does not commute with the copy.

*Proof.* The projection onto $\operatorname{Sym}$ is $\theta$-equivariant, and $\theta$ does not commute with the complex-linear action.

**The reading.** The failure costs the possibility of treating the symmetric and antisymmetric parts of a carrier as carriers. It leaves intact the decomposition into carriers, which is cut by the Casimir and not by the transpose.

## The Boundary

**Against the parity rule.** The squares of the module do split by parity, and the splitting of the module into symmetric and alternating squares is a splitting into invariant subspaces. The difference is that the module carries a bilinear form and the algebra carries an involution: on the module the flip of two factors is an operator commuting with the action, and on the algebra the transpose is an operator that does not.

**Against the intersection table.** The failure does not prevent the computation of the dimensions of the intersections, which are the subject of the next article; it only prevents them from being zero or full.

**Against the Hermitian splitting.** The Hermitian splitting is preserved by the real form and not by the complexification, which is the mirror image of the statement for the symmetric splitting.

## The Check of the Cartan Element

**The two eigenvalues.** The Cartan element acts on the module with the four distinct eigenvalues $\pm\tfrac32,\pm\tfrac12$, so no two-dimensional subspace spanned by weight vectors is invariant; the only invariant subspaces are the sums of weight spaces, and the halves are not of that form.

## Summary

The algebra splits into symmetric and antisymmetric matrices, of complex dimensions ten and six, and the transpose is a complex-linear involution with these eigenspaces. The diagonal generator carries $E_{01}+E_{10}$ to $E_{01}-E_{10}$, so it carries the symmetric half into the antisymmetric half and the splitting is not preserved by the copy.

The two involutions behave differently: the transpose is complex-linear and is broken by the complexified action, while the Hermitian adjoint is anti-linear and its splitting is preserved by the anti-Hermitian generators, which are the elements of the Lie algebra.

No carrier is contained in either half, and neither half is a sum of carriers; the centre is the only carrier that lies in one half. The decomposition into carriers stands, and the splitting by the transpose is not a decomposition into carriers.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{Sym}$ | the symmetric matrices, dimension ten |
| $\Lambda$ | the antisymmetric matrices, dimension six |
| $\theta(X)=X^{\mathsf T}$ | the transpose involution |
| $X^{\dagger}$ | the Hermitian adjoint |
| $\operatorname{ad}_{J_z}$ | the adjoint action of the diagonal generator |
| $iJ_k$ | the anti-Hermitian generators of the Lie algebra |

## Further Reading

- [The Intersection Table: Where Each Carrier Meets $\operatorname{Sym}$ and $\Lambda$](the-intersection-table-of-the-carriers-with-the-two-halves-at-n-4.html), for the dimensions.
- [The Parity Rule: $\operatorname{Sym}^{2}=V_3\oplus V_1$ and $\Lambda^{2}=V_2\oplus V_0$](the-parity-rule-the-two-squares-of-the-module-at-n-4.html), for the splitting that does hold.
- [The Clebsch–Gordan Decomposition of $M_4(\mathbb{C})$](the-clebsch-gordan-decomposition-of-m4c.html), for the carriers.
- [Neither Half Is Invariant: the Cartan Element](neither-half-is-invariant-the-cartan-element.html), for the row at order two.
- [The Spin Content of $M_4(\mathbb{C})$](the-spin-content-of-m4c.html), for the Hermitian splitting.
