# __The Symmetric and Antisymmetric Parts of a Product__

## Introduction

**The symmetric part of a product is $S\circ S'+K\circ K'$ plus two brackets, and the antisymmetric part is $\tfrac12[S,S']+\tfrac12[K,K']$ plus two anticommutators: each of the four pieces of the product contributes to both halves, and the contributions are the four products of the next article.**

The article derives the two formulas from the split $A=S+K$, verifies them for random elements at $n=2,3,4,6$, and draws three consequences: the trace of a product sees only the like pieces, $\operatorname{tr}(AB)=\operatorname{tr}(SS')+\operatorname{tr}(KK')$; the commutator and the anticommutator split by the same rule with the brackets and the anticommutators exchanged; and the two projections commute with the product only for commuting factors. It assumes *The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric* for the split and *The Two Halves as Orthogonal Complements* for the orthogonality used in the trace computation. It defers the systematic tables to *The Four Multiplication Tables: $SS$, $SK$, $KS$, $KK$* and the operator version to *The Symmetric and Antisymmetric Parts of the Operator Space*.

## The Product of Two Elements

**Write each factor as its two halves and multiply out.** For $A=S+K$ and $B=S'+K'$ with $S,S'$ symmetric and $K,K'$ antisymmetric,

$$
AB=SS'+SK'+KS'+KK' .
$$

The four terms are distinct in general and none of them vanishes identically, so the product of two elements of the algebra is a sum of four products of halves. The two halves of $A$ and the two of $B$ give the four terms of the table, and the order matters: $SK'$ and $K'S$ are different matrices.

**Taking the transpose exchanges the halves and reverses the order.** Since $(XY)^{\mathsf T}=Y^{\mathsf T}X^{\mathsf T}$,

$$
(AB)^{\mathsf T}=S'S-S'K-K'S+K'K ,
$$

so the transpose of the product is the product of the transposed factors in the reversed order, and each term of the expansion changes its half: $SS'$ stays symmetric and $KK'$ stays symmetric, while $SK'$ and $KS'$ become $-S'K$ and $-K'S$. The two halves of $AB$ are therefore read from the same four terms with signs.

**The projections onto the halves are applied term by term.** With $\pi_{\pm}(X)=\tfrac12(X\pm X^{\mathsf T})$,

$$
\pi_{+}(AB)=\pi_{+}(SS')+\pi_{+}(KK')+\pi_{+}(SK'+KS'),\qquad
\pi_{-}(AB)=\pi_{-}(SS')+\pi_{-}(KK')+\pi_{-}(SK'+KS'),
$$

because $SS'$ and $KK'$ contribute anti-Hermitian parts and $SK'+KS'$ contributes both. The computation of the four pieces is the content of the next section.

## The Four Contributions

**The symmetric parts of the four terms are computable one at a time.** For symmetric $S,S'$ and antisymmetric $K,K'$,

$$
\pi_{+}(SS')=\tfrac12(SS'+S'S)=S\circ S',\qquad \pi_{+}(KK')=\tfrac12(KK'+K'K)=K\circ K',
$$

$$
\pi_{+}(SK')=\tfrac12(SK'-K'S)=\tfrac12[S,K'],\qquad \pi_{+}(KS')=\tfrac12(KS'-S'K)=\tfrac12[K,S'] .
$$

The first two are the Jordan products, and the second two are the brackets of a symmetric with an antisymmetric matrix, which are symmetric by the closure rule of *The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric*. Hence

$$
\pi_{+}(AB)=S\circ S'+K\circ K'+\tfrac12[S,K']+\tfrac12[K,S'] .
$$

**The antisymmetric parts are computed the same way, and the signs flip.** For the same four terms,

$$
\pi_{-}(SS')=\tfrac12(SS'-S'S)=\tfrac12[S,S'],\qquad \pi_{-}(KK')=\tfrac12[K,K'],
$$

$$
\pi_{-}(SK')=\tfrac12(SK'+K'S)=\tfrac12\{S,K'\},\qquad \pi_{-}(KS')=\tfrac12\{K,S'\},
$$

so that

$$
\pi_{-}(AB)=\tfrac12[S,S']+\tfrac12[K,K']+\tfrac12\{S,K'\}+\tfrac12\{K,S'\} .
$$

Both formulas were verified at $n=2,3,4,6$ against the direct computation of $\tfrac12(AB\pm(AB)^{\mathsf T})$, with agreement to machine precision.

**The rule behind the signs is the parity of the two factors.** A product of two elements of the same half contributes a symmetric part equal to the Jordan product and an antisymmetric part equal to the bracket; a product of two elements of opposite halves contributes the other way round, a bracket to the symmetric part and an anticommutator to the antisymmetric part. In one line,

$$
\pi_{\epsilon}(XY)=\tfrac12\big(XY+\epsilon\,Y^{\mathsf T}X^{\mathsf T}\big)
$$

takes the symmetric part at $\epsilon=+1$ and the antisymmetric part at $\epsilon=-1$, and the four formulas are its four evaluations.

**The four terms of the expansion are not independent.** They satisfy the single identity $SK'+KS'=(SK'+K'S)+(KS'-S'K)$ split into an anticommutator and a bracket, which is the polarisation of the product. The identity is what allows the mixed terms to be distributed between the two halves, and it is the reason the two formulas above contain four terms each rather than two.

## The Trace of a Product

**The trace of a product sees only the like pieces.** Since $\operatorname{tr}(SK')=\operatorname{tr}(KS')=0$ for a symmetric $S$ and an antisymmetric $K'$,

$$
\operatorname{tr}(AB)=\operatorname{tr}(SS')+\operatorname{tr}(KK') .
$$

The cross terms of the expansion are traceless one by one, so the trace pairing between $A$ and $B$ is the sum of the pairings of the symmetric halves and of the antisymmetric halves. The identity was verified at $n=2,3,4,6$ and it holds for every $n$, since $\operatorname{tr}(XY)=\operatorname{tr}(YX)$ makes $\operatorname{tr}(SK')=-\operatorname{tr}(SK')$.

**The trace of a product is therefore the sum of a positive and a negative definite pairing.** On the symmetric halves $\operatorname{tr}(SS')$ is the positive definite trace form, and on the antisymmetric halves $\operatorname{tr}(KK')$ is the negative definite one. So

$$
\operatorname{tr}(A^{2})=\operatorname{tr}(S^{2})+\operatorname{tr}(K^{2})
$$

with the first term positive and the second negative, which is the inertia statement of *The Trace Form and Its Inertia on the Two Halves* read on a single element.

**The trace of a product is not the product of the traces, and the defect is the cross term.** For $A=S+K$ and $B=S'+K'$ the difference $\operatorname{tr}(A)\operatorname{tr}(B)-\operatorname{tr}(AB)$ equals $\operatorname{tr}(S)\operatorname{tr}(K')+\operatorname{tr}(K)\operatorname{tr}(S')+\operatorname{tr}(K)\operatorname{tr}(K')-\operatorname{tr}(KK')$, which vanishes only under conditions on the pieces. The comparison is the standard one between a form and a product and it is not used further in the category.

## The Commutator and the Anticommutator

**The commutator splits by the same rule with the two products exchanged.** Since $[A,B]=AB-BA$ and the expansion of $BA$ is the same four terms in the other order,

$$
\pi_{+}([A,B])=[S,K']+[K,S'],\qquad \pi_{-}([A,B])=[S,S']+[K,K'] .
$$

So the symmetric part of a commutator is made of the two mixed brackets and the antisymmetric part of the two like brackets; both identities were verified at $n=2,3,4,6$. In particular $[S,S']$ and $[K,K']$ are antisymmetric, which is the statement $[\operatorname{Sym},\operatorname{Sym}]\subseteq\operatorname{Skew}$ and $[\mathfrak{so},\mathfrak{so}]\subseteq\mathfrak{so}$ at once.

**The anticommutator splits with the anticommutators in the symmetric part.** Since $\{A,B\}=AB+BA$,

$$
\pi_{+}(\{A,B\})=2S\circ S'+2K\circ K',\qquad \pi_{-}(\{A,B\})=\{S,K'\}+\{K,S'\} .
$$

The symmetric part of the anticommutator depends only on the like pieces, and the antisymmetric part only on the mixed ones. So the two operations $\{A,B\}$ and $[A,B]$ separate the four pieces of the table completely: the anticommutator sees the like pieces in its symmetric part, the commutator sees them in its antisymmetric part.

**The two operations together recover the product and its transpose.** From $AB=\tfrac12\{A,B\}+\tfrac12[A,B]$ and the two splits, the four formulas of §*The Four Contributions* are the same statement written twice. The economy is not an accident: the product, its transpose, the commutator and the anticommutator are four readings of one bilinear map, and the split of the algebra into two halves is what makes the four readings visible.

## The Case $n=2$

**At $n=2$ the formulas reduce to products of Pauli matrices.** With $S=a\mathrm{I}+b\sigma_1+c\sigma_3$ and $K=\theta J$,

$$
S\circ S'=(aa'+bb'+cc')\mathrm{I}+(ab'+a'b)\sigma_1+(ac'+a'c)\sigma_3,\qquad K\circ K'=-\theta\theta'\mathrm{I},
$$

the second because $J^{2}=-\mathrm{I}$, so two rotations compose to a negative scalar in the Jordan product. The brackets are $[S,K']=2\theta'(b\sigma_3-c\sigma_1)$ and $[K,S']=2\theta(c'\sigma_1-b'\sigma_3)$, which the computation confirms, and their sum is the symmetric part of the mixed contribution.

**The trace identity is the Euclidean one.** At $n=2$, $\operatorname{tr}(SS')=2(aa'+bb'+cc')$ and $\operatorname{tr}(KK')=-2\theta\theta'$, so

$$
\operatorname{tr}(AB)=2(aa'+bb'+cc'-\theta\theta'),
$$

the inertia $(3,1)$ of *The Two Halves as Orthogonal Complements* written on the four coordinates.

**The biquaternion reading makes the split visible in one product.** The Peirce idempotents $\tilde\Pi_\pm=\tfrac12(e_t\pm\tilde{Ζ})$ are symmetric, so a product of two of them has a symmetric part given by the Jordan product and an antisymmetric part given by the bracket, and the bracket of the two idempotents is $\tfrac12[\tilde{Ζ},\cdot]$ read on the frame. The companion nilpotents $\vec\Upsilon_{+-}$ and $\vec\Upsilon_{-+}$ are neither symmetric nor antisymmetric, so they contribute to both halves of every product they enter, which is the algebraic form of the statement that a mixed corner is not stable under the transpose.

## Summary

For $A=S+K$ and $B=S'+K'$ the product expands into the four terms $SS'$, $SK'$, $KS'$ and $KK'$, and its two halves are $\pi_{+}(AB)=S\circ S'+K\circ K'+\tfrac12[S,K']+\tfrac12[K,S']$ and $\pi_{-}(AB)=\tfrac12[S,S']+\tfrac12[K,K']+\tfrac12\{S,K'\}+\tfrac12\{K,S'\}$. The trace of a product is $\operatorname{tr}(SS')+\operatorname{tr}(KK')$, so the cross terms are invisible to the trace and the trace form splits into a positive definite part on $\operatorname{Sym}_n$ and a negative definite part on $\operatorname{Skew}_n$. The commutator has symmetric part $[S,K']+[K,S']$ and antisymmetric part $[S,S']+[K,K']$, the anticommutator has symmetric part $2S\circ S'+2K\circ K'$ and antisymmetric part $\{S,K'\}+\{K,S'\}$, and the four readings together are the product and its transpose.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A=S+K$ | the split into symmetric and antisymmetric halves |
| $S\circ S'=\tfrac12(SS'+S'S)$ | the Jordan product of two symmetric matrices |
| $[S,S']=SS'-S'S$ | the commutator |
| $\{S,K'\}=SK'+K'S$ | the anticommutator, antisymmetric for a symmetric and an antisymmetric factor |
| $\pi_{\pm}(X)=\tfrac12(X\pm X^{\mathsf T})$ | the two projections onto the halves |
| $\operatorname{tr}(AB)=\operatorname{tr}(SS')+\operatorname{tr}(KK')$ | the trace of a product, blind to the cross terms |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the polarisation of a product into its symmetric and antisymmetric parts.
- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (AMS, 1968), for the Jordan product and the identity $S\circ S'=\pi_{+}(SS')$.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the transpose of a product and the trace identities.
- [The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric](the-two-halves-over-r-symmetric-and-antisymmetric.html), for the closure rules used in the two formulas.
- [The Two Halves as Orthogonal Complements](the-two-halves-as-orthogonal-complements.html), for the trace form and its inertia on each half.
- [The Triangular Decomposition $h\oplus n_+\oplus n_-$](the-triangular-decomposition-h-n-plus-n-minus.html), for the trace pairing computed on the summands.
