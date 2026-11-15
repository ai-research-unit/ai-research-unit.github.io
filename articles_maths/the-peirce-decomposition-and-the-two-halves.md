# __The Peirce Decomposition and the Two Halves__

## Introduction

**The Peirce decomposition of $M_n(\mathbb{R})$ at a symmetric idempotent and the split into the symmetric and the antisymmetric halves are two decompositions of the same space, and they cross: each of the four corners splits into a symmetric part and an antisymmetric part, and the counts $r(r+1)/2$, $r(n-r)$ and the rest add up to the dimensions of the two halves.**

The article proves that the two decompositions are compatible exactly when the idempotent is symmetric, computes the intersection of each corner with each half, proves the dimension count in both directions, shows that the antisymmetric half contains no idempotent at all, and reads the crossing at $n=2$ through the biquaternion corners. It assumes *The Peirce Decomposition of $\operatorname{Sym}_n$ as a Jordan Algebra* for the Jordan version and *The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric* for the split. It defers the operator version of the crossing to *The Symmetric and Antisymmetric Parts of the Operator Space* and the idempotent variety to *The Space of Idempotents and the Flag Varieties*.

## The Two Splits of the Algebra

**The two decompositions are of different kinds.** The split

$$
M_n(\mathbb{R})=\operatorname{Sym}_n\oplus\operatorname{Skew}_n
$$

is the eigenspace decomposition of the involution $T:A\mapsto A^{\mathsf T}$, and it is a decomposition into two linear subspaces, of dimensions $n(n+1)/2$ and $n(n-1)/2$. The Peirce decomposition at an idempotent $E$ is

$$
M_n(\mathbb{R})=C_{++}\oplus C_{+-}\oplus C_{-+}\oplus C_{--},
$$

with $C_{++}=EM_nE$, $C_{+-}=EM_n(\mathrm{I}-E)$, $C_{-+}=(\mathrm{I}-E)M_nE$ and $C_{--}=(\mathrm{I}-E)M_n(\mathrm{I}-E)$, a decomposition into four subspaces which are also multiplication pieces: $C_{ij}C_{kl}\subseteq\delta_{jk}C_{il}$.

**The two decompositions commute exactly when the idempotent is symmetric.** The transpose carries $C_{ij}(E)$ to $C_{ji}(E^{\mathsf T})$, so it preserves the Peirce decomposition exactly when $E=E^{\mathsf T}$, that is when $E$ is an orthogonal projection. In that case each corner is stable under the transpose and splits into its symmetric and antisymmetric parts:

$$
C_{ij}=\big(C_{ij}\cap\operatorname{Sym}_n\big)\oplus\big(C_{ij}\cap\operatorname{Skew}_n\big)\qquad(i,j\in\{+,-\}).
$$

So the two decompositions are the commuting spectral decompositions of two involutions: the transpose $T$ and the Peirce reflection $2L_E-1$ on the corners.

**When the idempotent is not symmetric the decompositions do not commute.** For a general idempotent the transpose sends the corners of $E$ to the corners of $E^{\mathsf T}$, and the two decompositions are then in general position. So the compatibility of the article is the statement that the idempotents of the split — the orthogonal projections — are exactly the idempotents whose Peirce decomposition respects the split, and that is why the Peirce theory of the category is written with orthogonal projections.

**The common refinement has six parts.** With $E$ a symmetric idempotent of rank $r$ and $s=n-r$,

$$
M_n(\mathbb{R})=\big(C_{++}^{s}\oplus C_{++}^{a}\big)\oplus\big(C_{--}^{s}\oplus C_{--}^{a}\big)\oplus\big((C_{+-}\oplus C_{-+})^{s}\big)\oplus\big((C_{+-}\oplus C_{-+})^{a}\big),
$$

where the superscripts denote the symmetric and antisymmetric parts. The last two parts are written together because the transpose swaps $C_{+-}$ and $C_{-+}$, so neither corner alone is stable under it.

## A Symmetric Idempotent and Its Corners

**In blocks the two halving operations are visible at once.** Write a matrix in the two blocks of $E$:

$$
X=\begin{pmatrix}A&B\\ C&D\end{pmatrix},\qquad A\in M_r,\ D\in M_s,\ B\in M_{r\times s},\ C\in M_{s\times r}.
$$

The transpose acts by $A\mapsto A^{\mathsf T}$, $D\mapsto D^{\mathsf T}$ and $B\leftrightarrow C^{\mathsf T}$, and the Peirce projection to the corners reads off the four blocks. So the fixed space of the transpose consists of the symmetric $A$, the symmetric $D$ and the pairs $C=B^{\mathsf T}$, and the anti-fixed space consists of the antisymmetric $A$, the antisymmetric $D$ and the pairs $C=-B^{\mathsf T}$.

**Each diagonal corner splits into the symmetric and the antisymmetric matrices of its size.** Since $C_{++}=\{\begin{pmatrix}A&0\\0&0\end{pmatrix}\}\cong M_r$ and the transpose acts as the transpose of $A$,

$$
\dim\big(C_{++}\cap\operatorname{Sym}_n\big)=\frac{r(r+1)}{2},\qquad \dim\big(C_{++}\cap\operatorname{Skew}_n\big)=\frac{r(r-1)}{2},
$$

and the same with $s$ for $C_{--}$. The two dimensions add to $r^{2}$, and at $r=1$ the second is zero: the one-dimensional corner $C_{++}$ is spanned by the idempotent, which is symmetric.

**The two mixed corners are exchanged by the transpose, and their sum splits evenly.** Since $C_{+-}=\{\begin{pmatrix}0&B\\0&0\end{pmatrix}\}$ and $C_{-+}=\{\begin{pmatrix}0&0\\ C&0\end{pmatrix}\}$ with $C=B^{\mathsf T}$ under the transpose,

$$
\big(C_{+-}\oplus C_{-+}\big)\cap\operatorname{Sym}_n=\Big\{\begin{pmatrix}0&B\\B^{\mathsf T}&0\end{pmatrix}\Big\},\qquad \big(C_{+-}\oplus C_{-+}\big)\cap\operatorname{Skew}_n=\Big\{\begin{pmatrix}0&B\\-B^{\mathsf T}&0\end{pmatrix}\Big\},
$$

both of dimension $rs$. So the mixed part of the algebra splits into two halves of equal dimension, one symmetric and one antisymmetric, and neither is a corner.

**The mixed symmetric part is the Jordan middle space.** The symmetric mixed elements are exactly the space $J_{1/2}$ of *The Peirce Decomposition of $\operatorname{Sym}_n$ as a Jordan Algebra*, of dimension $rs$. So the Jordan decomposition of the symmetric half is the collection of the symmetric parts of the four corners, with the two mixed corners merged, and the antisymmetric half has no Jordan structure at all.

## The Count of Dimensions

**The symmetric half is the sum of three of the pieces.** Adding the symmetric parts,

$$
\dim\operatorname{Sym}_n=\frac{r(r+1)}{2}+\frac{s(s+1)}{2}+rs=\frac{n(n+1)}{2},
$$

which holds identically in $r$ and $s$; at $n=5$ and $r=1,2,3,4$ the three summands are $(1,10,4)$, $(3,6,6)$, $(6,3,6)$ and $(10,1,4)$, each adding to $15$.

**The antisymmetric half is the sum of the other three.** Adding the antisymmetric parts,

$$
\dim\operatorname{Skew}_n=\frac{r(r-1)}{2}+\frac{s(s-1)}{2}+rs=\frac{n(n-1)}{2},
$$

which at $n=5$ gives $(0,6,4)$, $(1,3,6)$, $(3,1,6)$ and $(6,0,4)$, of sums $10,10,10,10$. So the two halves are the two halves of the same six pieces, and the crossing of the two decompositions is a $2\times2$ grid of dimensions.

**The grid is symmetric under $E\mapsto\mathrm{I}-E$.** The exchange $r\leftrightarrow s$ leaves both totals unchanged and swaps the two diagonal corners, so the picture at rank $r$ and at rank $n-r$ is the same picture with the two corners exchanged. That is the dimension form of the statement that the two decompositions are dual to each other.

**The corner dimensions are $r^{2}$, $rs$, $sr$ and $s^{2}$, and the halves cut each corner in half up to one.** The diagonal corners are cut into a triangular part and a strictly triangular part, of dimensions $r(r+1)/2$ and $r(r-1)/2$; the mixed pair is cut into two equal parts of dimension $rs$. So the crossing is as even as it can be, and the only asymmetry is the triangular one on the diagonal.

## No Idempotents in the Antisymmetric Half

**An antisymmetric idempotent is zero.** If $K\in\operatorname{Skew}_n$ and $K^{2}=K$, then

$$
\operatorname{tr}(K)=\operatorname{tr}(K^{2})=-\operatorname{tr}(KK^{\mathsf T})=-\|K\|^{2}\le0,
$$

and also $\operatorname{tr}(K)=0$ because $K$ is antisymmetric. Hence $\|K\|=0$ and $K=0$. So

$$
\operatorname{Skew}_n\cap\{\text{idempotents}\}=\{0\},
$$

which is the sharpest statement of the asymmetry of the two halves: one half contains all the idempotents of the algebra, the other none.

**The Peirce decomposition of an antisymmetric element is therefore not a decomposition by idempotents of its own half.** Every idempotent lies in the symmetric half, so the Peirce theory of the algebra is a theory of the symmetric half. The antisymmetric half appears in the theory only as the set of directions on which the corners act, and its elements are the nilpotent-like directions of the algebra.

**The square of an antisymmetric matrix is symmetric and negative semidefinite.** For $K\in\operatorname{Skew}_n$,

$$
(K^{2})^{\mathsf T}=K^{2},\qquad K^{2}=-K^{\mathsf T}K\preceq0,
$$

so the square lands in the symmetric half, in the negative part of the cone. So a rotation composes with itself into a stretch, which is the algebraic statement of *The Exponential of the Antisymmetric Part: One-Parameter Rotations*, and the Peirce decomposition sees it as a map from the antisymmetric half into the negative part of the symmetric half.

**The two halves are therefore of different algebraic types.** One half carries the idempotents, the Jordan product and the cone; the other carries the nilpotent-like directions, the brackets and the rotations. The crossing of the two decompositions is the exact bookkeeping of that difference, corner by corner.

## The Case $n=2$

**At $n=2$ with $r=1$ the six pieces are all one-dimensional.** The corners are

$$
C_{++}=\mathbb{R}\tilde\Pi_+,\qquad C_{--}=\mathbb{R}\tilde\Pi_-,\qquad C_{+-}=\mathbb{R}u,\qquad C_{-+}=\mathbb{R}v,
$$

with $u$ and $v$ the two companion nilpotents, and the four dimensions add to $4=n^{2}$. The symmetric parts are $\mathbb{R}\tilde\Pi_+$, $\mathbb{R}\tilde\Pi_-$, $\mathbb{R}(u+v)$ and the antisymmetric part is $\mathbb{R}(u-v)$, which is one-dimensional and is the rotation line.

**The identification of the symmetric part is the Pauli computation.** With $\tilde\Pi_\pm=\tfrac12(\mathrm{I}\pm\sigma_3)$ and the nilpotents proportional to $\sigma_1\pm i\sigma_2$,

$$
u+v\propto\sigma_1\ \text{(symmetric)},\qquad u-v\propto i\sigma_2\ \text{(antisymmetric)},
$$

so the two mixed corners produce the symmetric mixing and the antisymmetric difference, and the whole algebra is $\operatorname{Sym}_2\oplus\operatorname{Skew}_2$ with dimensions $3+1$. The computation confirms that $u+v$ is symmetric and $u-v$ is antisymmetric when the frame is normalised so that $v=u^{\mathsf T}$ and $uv=\tilde\Pi_+$.

**The biquaternion frame is the common refinement.** The four corners $\mathbb{B}_{++}$, $\mathbb{B}_{+-}$, $\mathbb{B}_{-+}$ and $\mathbb{B}_{--}$ are the four Peirce pieces, and the split into halves collects them as $\mathbb{B}_{++}\oplus\mathbb{B}_{--}\oplus(\mathbb{B}_{+-}\oplus\mathbb{B}_{-+})^{s}$ against $(\mathbb{B}_{+-}\oplus\mathbb{B}_{-+})^{a}$. So the biquaternion Peirce basis and the symmetric-antisymmetric split are the two decompositions of the article, and their crossing is the four-term count of the frame.

## Summary

The Peirce decomposition at a symmetric idempotent and the split into the symmetric and antisymmetric halves commute, and their common refinement has six pieces: the symmetric and antisymmetric parts of the two diagonal corners, of dimensions $r(r\pm1)/2$ and $s(s\pm1)/2$, and the symmetric and antisymmetric parts of the two mixed corners, each of dimension $rs$. The symmetric parts add to $n(n+1)/2$ and the antisymmetric parts to $n(n-1)/2$, and the crossing is symmetric under $E\mapsto\mathrm{I}-E$. The antisymmetric half contains no idempotent, since an antisymmetric idempotent has $\operatorname{tr}K=\operatorname{tr}K^{2}=-\|K\|^{2}\le0$ and vanishes, so all Peirce theory of the algebra lives in the symmetric half.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $C_{++}=EM_nE$, $C_{+-}=EM_n(\mathrm{I}-E)$ | the four Peirce corners |
| $C_{ij}\cap\operatorname{Sym}_n$, $C_{ij}\cap\operatorname{Skew}_n$ | the crossing of the two decompositions |
| $r(r+1)/2$, $r(r-1)/2$ | the symmetric and antisymmetric parts of a diagonal corner |
| $rs$ | the dimension of each half of the mixed part |
| $\operatorname{Skew}_n\cap\{\text{idempotents}\}=\{0\}$ | the absence of idempotents in the antisymmetric half |
| $K^{2}=-K^{\mathsf T}K\preceq0$ | the square of an antisymmetric matrix |
| $u+v$, $u-v$ | the symmetric and antisymmetric combinations of the companion nilpotents |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for Peirce decompositions and the multiplication rules of the corners.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the symmetric part of the Peirce decomposition.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for orthogonal projections and the block form of the transpose.
- [The Peirce Decomposition of $\operatorname{Sym}_n$ as a Jordan Algebra](the-peirce-decomposition-of-sym-n-as-a-jordan-algebra.html), for the Jordan decomposition that the mixed symmetric part carries.
- [The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric](the-two-halves-over-r-symmetric-and-antisymmetric.html), for the split that the corners cross.
- [The Peirce Decomposition in $n$ Dimensions](the-peirce-decomposition-in-n-dimensions.html), for the four corners and their multiplication rules.
