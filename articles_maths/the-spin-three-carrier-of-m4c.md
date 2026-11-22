# __Introduction to the Spin-Three Carrier at $n=4$: the Top of the Chain__

## Introduction

**The subject.** The carrier of label three is the leading summand of the symmetric square of the module, of dimension seven. It is the largest carrier, the one that carries the highest weight of the algebra, and the only one whose weight string runs from $-3$ to $+3$. The article identifies it and computes its invariants.

**The order of the article.** The first section identifies the carrier inside the symmetric square. The second computes the weights. The third computes the Casimir and the projector. The fourth describes the special elements, including the matrix unit of highest weight. The fifth draws the boundary.

**It assumes** *The Parity Rule: $\operatorname{Sym}^{2}=V_3\oplus V_1$ and $\Lambda^{2}=V_2\oplus V_0$* and *The Spin Group at $n=4$*. The row at order two is *The Spin-Zero Carrier of the Biquaternion Algebra*.

**The result in one line.** $V_3$ is the orthogonal complement of $V_1$ in $\operatorname{Sym}^{2}\mathbb{C}^{4}$, of complex dimension seven, with weights $0,\pm1,\pm2,\pm3$ and Casimir eigenvalue twelve.

**Boundaries.** The article introduces the carrier; the Hermitian form, the rank strata and the spectral strata are treated in the following articles.

## The Carrier Inside the Symmetric Square

**Proposition.** $\operatorname{Sym}^{2}\mathbb{C}^{4}=V_3\oplus V_1$, of dimensions $10=7+3$, and $V_3$ is the orthogonal complement of $V_1$ for the trace form.

*Proof.* The symmetric square of a four-dimensional space has dimension ten; the labels appearing in the tensor square of $V_{3/2}$ are $0,1,2,3$, and the symmetric ones are $3$ and $1$; the summands are orthogonal isotypic pieces.

**Corollary.** The carrier is the unique seven-dimensional invariant subspace of the algebra, and its dimension is the largest of the four.

*Proof.* Multiplicities are one in the tensor square with the dual, so each carrier is unique for its label.

**Corollary.** The carrier contains the highest weight vectors of the algebra, of weights $+3$ and $-3$.

*Proof.* The weight-$3$ space of the algebra is one-dimensional and lies in the carrier.

**The reading.** The septet is the top of the chain, and it is the part of the symmetric square not accounted for by the triplet.

## The Weights

**Proposition.** The weights of the carrier are $+3,+2,+1,0,-1,-2,-3$, once each, and the highest weight vector is the matrix unit $E_{03}$.

*Proof.* The symmetric square of the weight string $\tfrac32,\tfrac12,-\tfrac12,-\tfrac32$ gives the sums $3,2,1,0,1,2,3$, the label-three piece keeps all seven, and the weight-$3$ space of the algebra is spanned by $E_{03}$, whose weight is $\tfrac32-(-\tfrac32)=3$.

**Corollary.** The carrier is multiplicity-free and its weight string is the full symmetric string of length seven.

*Proof.* The weights displayed are distinct and symmetric.

**Corollary.** The carrier contains a matrix unit, hence an element of rank one, unlike the carriers of label one and two.

*Proof.* $E_{03}$ is a matrix unit, of rank one.

**The reading.** The septet is the carrier with the longest weight string and the only one that contains a matrix unit.

## The Casimir and the Projector

**Proposition.** The Casimir acts on $V_3$ by the eigenvalue twelve, and the projector onto the carrier is the Lagrange polynomial $\prod_{l\neq12}(C-l)/(12-l)$ over $l\in\{0,2,6\}$.

*Proof.* The Casimir eigenvalue on $V_k$ is $k(k+1)=12$ for $k=3$; the Lagrange polynomial takes the value one on the eigenspace twelve and zero on the others.

**Corollary.** The trace of the projector is seven, and the projector commutes with the action.

*Proof.* The rank of the projector is the dimension of its image, and a polynomial in the Casimir is invariant.

**Corollary.** The projector maps the matrix unit $E_{03}$ to itself, since the unit already lies in the carrier.

*Proof.* $E_{03}$ is a weight vector of weight three, and the weight-three space is inside the carrier.

**The reading.** The septet is the last eigenspace of the Casimir, and it is reached by projecting any matrix onto the eigenvalue twelve.

## The Special Elements

**Proposition.** The carrier contains the matrix unit $E_{03}$ of rank one, the element $E_{02}+E_{13}$ is not in the carrier while the element $E_{03}$ is, and the carrier realises the ranks one, three and four, the three being the rank of the generic point of its determinant hypersurface.

*Proof.* $E_{03}$ has weight three and belongs to the carrier; $E_{02}+E_{13}$ is the top weight vector of the quintet; the ranks are exhibited by $E_{03}$, by the generic point of the determinant hypersurface, and by the generic element.

**Corollary.** The determinant is not a function of the trace form on the carrier: the quadric $\operatorname{tr}(X^{2})=0$ carries the matrix unit $E_{03}$, with determinant zero, and also elements of rank four, one of which has $\operatorname{tr}(X^{2})=0$ and $\det X=14.1472+45.0994\,i$.

*Proof.* The first element is a matrix unit; the second was obtained from a random line in the carrier, solving $\operatorname{tr}(X^{2})=0$ for the parameter and computing the determinant, to machine precision.

**Corollary.** The carrier is spectrally the freest of the four: its two eigenvalue pairs are independent.

*Proof.* The spectrum is $\{\pm\alpha,\pm\beta\}$ with no relation between $\alpha$ and $\beta$; the determinant and the trace form are independent invariants.

**The reading.** The septet is the least rigid carrier, in contrast with the quintet, whose spectrum is a function of one invariant.

## The Boundary

**Against the parity article.** That article proves the splitting; this one studies the summand of label three.

**Against the Hermitian form article.** The positive-definite Hermitian form on the septet is computed there.

**Against the biquaternion row.** At order two there is no carrier of label three: the algebra is four-real-dimensional.

## The Septet and the Two Squares

**Proposition.** The symmetric square of the module is the sum $V_3\oplus V_1$ and the alternating square is the sum $V_2\oplus V_0$, so the carriers are distributed between the two squares according to the parity of the label.

*Proof.* The Clebsch–Gordan rule for $j=k=\tfrac32$ gives the labels $0,1,2,3$; the symmetry of the tensor $u\otimes v\pm v\otimes u$ under the exchange fixes which labels can occur in each square, and the even labels occur in the alternating square.

**Corollary.** The top carrier is the largest summand of the symmetric square, and it contains the highest weight vector of the whole algebra.

*Proof.* The label three is the largest label, and its weight string contains the weight three.

**Corollary.** The two squares together give the four carriers, and the dimensions add to $10+6=16$.

*Proof.* The dimensions $7+3$ and $5+1$.

**The reading.** The symmetry of the tensor square is the mechanism that distributes the spins, and the septet is the leading term of the symmetric part.

## The Note on Order Two

**The lower analogue.** At order two there is no carrier of label three, since the algebra has dimension four and the labels stop at one; the top of the chain below the septet is the triplet, and the symmetric square of the two-dimensional module is the sum of the triplet and the scalars.

**The comparison.** The septet is therefore the first carrier that exists only from order four on, and the reason is the length of the weight string: a carrier of label three needs a module whose label is at least three halves.

## The Check of the Weight String

**The endpoints.** The weight string of the septet runs from three to minus three, and the two endpoints are the matrix units $E_{03}$ and $E_{30}$; the string is symmetric and has no gaps, which is the statement that the carrier is the full symmetric power of the two-dimensional space.

**The centre of the string.** The middle weight is zero and its space is one-dimensional, spanned by the traceless combination of the diagonal units; the dimension one of the middle space is the statement that the multiplicity of the label zero inside the septet is one.

**The Casimir.** The Casimir eigenvalue twelve is the largest of the four, and it is the value $k(k+1)$ at $k=3$; the ordering of the eigenvalues $0,2,6,12$ is the ordering of the labels, and the septet is the last term.

## Summary

The carrier of label three is the orthogonal complement of the triplet in the symmetric square of the module, of complex dimension seven, with weight string $3,2,1,0,-1,-2,-3$ and Casimir eigenvalue twelve. Its projector is the Lagrange polynomial of the Casimir vanishing on $0,2,6$.

The carrier contains the matrix unit $E_{03}$, of rank one, and its determinant is independent of its trace form, so its spectrum is the freest of the four carriers.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $V_3\subset\operatorname{Sym}^{2}\mathbb{C}^{4}$ | the septet |
| $3,2,1,0,-1,-2,-3$ | its weights |
| $12$ | its Casimir eigenvalue |
| $E_{03}$ | its highest weight vector |

## Further Reading

- [The Parity Rule: $\operatorname{Sym}^{2}=V_3\oplus V_1$ and $\Lambda^{2}=V_2\oplus V_0$](the-parity-rule-the-two-squares-of-the-module-at-n-4.html), for the splitting.
- [The Spin-Three Carrier and the Hermitian Form at $n=4$](the-spin-three-carrier-and-the-hermitian-form-at-n-4.html), for the Hermitian form.
- [The Spin-Three Carrier and the Rank Strata at $n=4$](the-spin-three-carrier-and-the-rank-strata-at-n-4.html), for the ranks.
- [The Spin-Three Carrier and the Spectral Strata at $n=4$](the-spin-three-carrier-and-the-spectral-strata-at-n-4.html), for the spectra.
- [The Spin Group at $n=4$: the Principal Copy, $\operatorname{Sym}^3$ and the Kernel $\{\pm\mathrm I\}$](the-spin-group-at-n-4-the-principal-copy-and-its-kernel.html), for the copy.
