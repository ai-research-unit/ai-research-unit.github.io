# __The $\mathrm{SU}(2)$ of $M_4(\mathbb{C})$ Acting on Sixteen Dimensions__

## Introduction

**The subject.** The principal copy acts on the algebra, and the algebra is a complex space of dimension sixteen, hence a real space of dimension thirty-two. The article separates the two numbers, describes the action, and compares it with the action at order two, where the algebra is four-real-dimensional.

**The order of the article.** The first section fixes the two dimensions and the real dimensions of the carriers. The second describes the action and the loss of the algebra structure. The third compares the adjoint action with the left multiplication and the different decompositions they give. The fourth makes the comparison with the biquaternion case. The fifth draws the boundary.

**It assumes** *The Clebsch–Gordan Decomposition of $M_4(\mathbb{C})$* and *The Four Carrier Lists of One Algebra at $n=4$*. The row at order two is *The $\mathrm{SU}(2)$ of the Biquaternion Algebra Acting on Four Dimensions*.

**The result in one line.** The algebra is sixteen-dimensional over $\mathbb{C}$ and thirty-two-dimensional over $\mathbb{R}$, the four carriers have real dimensions $14,10,6,2$, and the copy acts orthogonally with the kernel $\{\pm\mathrm I\}$.

**Boundaries.** The article treats the principal copy only; the other groups acting on the same space are the subject of *The Four Carrier Lists of One Algebra*.

## The Two Dimensions

**Proposition.** $\dim_{\mathbb{C}}M_4(\mathbb{C})=16$ and $\dim_{\mathbb{R}}M_4(\mathbb{C})=32$.

*Proof.* The complex dimension is $4^{2}=16$ and the real dimension is twice the complex one.

**Corollary.** The carriers have complex dimensions $7,5,3,1$ and real dimensions $14,10,6,2$.

*Proof.* A complex subspace of complex dimension $d$ is a real subspace of dimension $2d$.

**Corollary.** The four real dimensions sum to $32$, as the four complex ones sum to $16$.

*Proof.* $14+10+6+2=32$.

**The reading.** The number sixteen in the title is the complex dimension; the real space on which the copy acts has dimension thirty-two, and the phrase "acting on sixteen dimensions" refers to the complex count.

## The Action

**Proposition.** The action $\Phi_q(X)=\rho(q)X\rho(q)^{-1}$ is a real-linear action of $SU(2)$ by complex-linear maps, and its kernel is $\{\pm\mathrm I\}$.

*Proof.* Conjugation by a matrix is complex-linear and invertible; it preserves the product, so it is an algebra automorphism; the kernel is computed as in *Why the Conjugation Labels Are Integer*.

**Corollary.** The action is orthogonal for the Hermitian form $\operatorname{tr}(X^{\dagger}Y)$, and it preserves the real and imaginary parts of the entries.

*Proof.* $\operatorname{tr}((\rho X\rho^{-1})^{\dagger}\rho Y\rho^{-1})=\operatorname{tr}(X^{\dagger}Y)$ because $\rho$ is unitary; a complex-linear map preserving the Hermitian form preserves the real and imaginary parts.

**Corollary.** The action does not preserve the algebra structure as an object of the category of algebras: it preserves the product, but the decomposition into carriers is not a decomposition into ideals.

*Proof.* The carriers are not closed under multiplication, as *The Truncated Rule* shows.

**The reading.** The action is by automorphisms, so it preserves the product; what it does not do is respect the product in the sense of splitting the algebra into subalgebras.

## Two Commuting Actions

**Proposition.** Left multiplication $X\mapsto AX$ and right multiplication $X\mapsto XB$ commute, and the adjoint action is the composition of a left multiplication by $\rho(q)$ with a right multiplication by $\rho(q)^{-1}$.

*Proof.* $(AX)B=A(XB)$; and $\rho(q)X\rho(q)^{-1}$ is exactly the composition.

**Corollary.** The adjoint action is a subaction of the product of the two one-sided actions, and the two-sided operators $T_{A,B}$ contain the adjoint action as the case $B=A^{-1}$.

*Proof.* The definitions.

**Corollary.** The decompositions given by left multiplication and by the adjoint action are different: the left action is the defining action on $\mathbb{C}^{4}$ copied sixteen times, with the pieces of dimension four given by the columns, while the adjoint action gives the four carriers.

*Proof.* Left multiplication by $A$ acts on the columns of $X$ each as $A$ acts on $\mathbb{C}^{4}$; the adjoint action mixes the entries.

**The reading.** The same space carries the module sixteen times under left multiplication and the four carriers under conjugation, which is another instance of the ambiguity of the word "spin".

## The Biquaternion Comparison

**Proposition.** The biquaternion algebra $\mathbb{B}$ is four-real-dimensional, and the conjugation action of its copy $SU(2)$ decomposes it as the triplet $V_1$ and the scalars $V_0$, of real dimensions $3+1$.

*Proof.* $\mathbb{B}\cong\mathbb{C}\otimes\mathbb{H}$ has real dimension four and complex dimension two; under conjugation the imaginary quaternions form a triplet and the scalars a singlet.

**Corollary.** The biquaternion action is the defining action on the triplet, and the algebra is the sum of the defining module and the trivial one.

*Proof.* The conjugation action on $\mathbb{H}$ fixes the real line and rotates the imaginary part.

**Corollary.** The number sixteen is not a dimension at order two: the complex dimension is four and the real dimension is four as well, since the algebra is a real algebra of real dimension four.

*Proof.* $\mathbb{B}$ is four-real-dimensional, and its complexification is $M_2(\mathbb{C})$.

**The reading.** The two rows share the law $n^{2}$ for the complex dimension and nothing else about the number sixteen; at order two the algebra is four-real-dimensional, and at order four it is thirty-two-real-dimensional.

## The Boundary

**Against the four lists.** The four carrier lists are lists of pieces for four groups; this article fixes the principal one and the dimensions of the space on which it acts.

**Against the ideals.** The left multiplication by the algebra is not the conjugation action; the ideals are invariant under the first and not under the second.

**Against the module.** The module has complex dimension four and real dimension eight, and it is not a subspace of the algebra; its action is the defining one and not the adjoint one.

## A Final Observation

**The real count.** The algebra has sixteen complex dimensions and thirty-two real dimensions, and the copy acts by thirty-two-by-thirty-two real matrices; the complex count sixteen is the one that matches the four carriers, and the real count is twice it.

**The invariant subspaces.** The invariant real subspaces are the real forms of the complex carriers, and their dimensions are twice the complex dimensions; the four carriers therefore account for the whole real space, with no leftover.

## The Note on Order Two

**The lower analogue.** At order two the copy acts on the algebra of four complex dimensions, so the analogue of the sixteen-dimensional space is four-dimensional; the carriers are the scalars and the triplet, and the invariant form is the trace form of the quaternions.

**The comparison.** The multiplication of the dimensions by four between the two rows is the same factor that takes the module of dimension two to the module of dimension four, and the pattern of the carriers is the same with one term fewer.

## The Check of the Action

**The invariant subspaces.** The action preserves the four carriers, each of which is irreducible, and it preserves the trace form and the Hermitian form; the invariant subspaces are therefore exactly the sums of carriers, and there are sixteen of them, one for each subset of the four labels.

**The generators.** The three generators act on the algebra by the commutator, and their matrices are sixteen-by-sixteen; the bracket of two of them is the third, so the image of the copy in the algebra of endomorphisms is three-dimensional. Its centraliser is the sum of the four matrix algebras $\operatorname{End}(V_k)$, of total dimension $49+25+9+1=84$, and the algebra generated by the left and right multiplications, of dimension $32$, sits inside it as a proper subalgebra.

**The trace.** The trace of every generator on the algebra vanishes, because the algebra is the tensor square of the module with its dual and the trace is the product of two traceless factors; the action therefore lies in the special linear algebra, as it must.

## Summary

The algebra is sixteen-dimensional over $\mathbb{C}$ and thirty-two-dimensional over $\mathbb{R}$, and the principal copy acts on it by conjugation, which is a real-linear action by complex-linear automorphisms with kernel $\{\pm\mathrm I\}$. The four carriers have real dimensions $14,10,6,2$.

Left multiplication and the adjoint action commute and give different decompositions: the first is the defining action on the columns, the second is the carrier decomposition. The adjoint action is the case $B=A^{-1}$ of the two-sided operators.

The biquaternion algebra is four-real-dimensional, and its conjugation action gives the triplet and the scalars, of real dimensions $3+1$; the number sixteen is not a dimension there.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $16$, $32$ | the complex and real dimensions of $M_4(\mathbb{C})$ |
| $14,10,6,2$ | the real dimensions of the carriers |
| $\Phi_q$ | the conjugation action |
| $T_{A,B}$ | the two-sided operator $X\mapsto AXB$ |

## Further Reading

- [The Four Carrier Lists of One Algebra at $n=4$](the-four-carrier-lists-of-one-algebra-at-n-4.html), for the other groups.
- [The Ten Ranks of the Two-Sided Operators at $n=4$](the-ten-ranks-of-the-two-sided-operators-at-n-4.html), for $T_{A,B}$.
- [The Spin Content of $M_4(\mathbb{C})$](the-spin-content-of-m4c.html), for the content.
- [The $\mathrm{SU}(2)$ of the Biquaternion Algebra Acting on Four Dimensions](the-su2-of-the-biquaternion-algebra-acting-on-four-dimensions.html), for the row at order two.
- [The Clebsch–Gordan Decomposition of $M_4(\mathbb{C})$](the-clebsch-gordan-decomposition-of-m4c.html), for the carriers.
