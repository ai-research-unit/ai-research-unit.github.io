# __The Fine Decomposition against the Diagonal__

## Introduction

**Against the diagonal subalgebra the algebra splits into $n^{2}$ lines, one for each ordered pair of indices, and that is the finest decomposition of the category: the coarse split into two halves and the Peirce split into $n^{2}$ corners are both coarsenings of it.**

The article defines the diagonal subalgebra, grades the algebra by the characters of the diagonal torus, computes the weight of each matrix unit, counts the lines and the roots, and shows how the involution acts on the grading: it fixes the diagonal lines and pairs the two lines of a transposed pair, whose sum and difference are one symmetric and one skew line. It then identifies the Peirce lines of the coordinate flag with the weight lines, and the simple nilpotents of the frame with the simple root vectors. It assumes *The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric* and *The Two Halves over $\mathbb{C}$: Hermitian and Anti-Hermitian* for the splits, and *The Involutions over $\mathbb{R}$ and over $\mathbb{C}$* for the action of the involution. It defers the Peirce construction at a general flag to *The Peirce Decomposition in $n$ Dimensions* and the operator version to *The Symmetric and Antisymmetric Parts of the Operator Space*.

## The Diagonal Subalgebra

**The diagonal matrices form a commutative subalgebra of dimension $n$, and it is a maximal torus.** Write

$$
\mathfrak{h}=\Big\{\operatorname{diag}(t_1,\dots,t_n)\Big\},\qquad \dim\mathfrak{h}=n .
$$

The subalgebra is commutative and consists of semisimple elements. It is maximal among the commutative subalgebras: a matrix commuting with every diagonal matrix with distinct entries is itself diagonal, since $AE_{ii}=E_{ii}A$ forces the entries off the $i$-th column to vanish.

**The diagonal is the fixed set of the adjoint action of the torus, and the rest of the algebra is graded by its characters.** For $T=\operatorname{diag}(t_1,\dots,t_n)$ and $A$ a matrix, $(TAT^{-1})_{ij}=(t_i/t_j)A_{ij}$. So each matrix unit is an eigenvector of the conjugation action by the torus, with character

$$
T\cdot E_{ij}=\frac{t_i}{t_j}E_{ij},\qquad \chi_{ij}(T)=\frac{t_i}{t_j}.
$$

The characters are the **weights**, and they are the $n^{2}$ monomials $t_i/t_j$; $n$ of them are trivial, the diagonal ones, and the other $n(n-1)$ are nontrivial.

**The decomposition is a grading in the character group.** The character group of the torus is $\mathbb{Z}^{n}/\mathbb{Z}(1,\dots,1)$, of rank $n-1$, and

$$
M_n(\mathbb{C})=\bigoplus_{i,j=1}^{n}\mathbb{C}E_{ij},\qquad M^{(\alpha)}=\bigoplus_{\chi_{ij}=\alpha}\mathbb{C}E_{ij},
$$

with $\dim M^{(\alpha)}=1$ for the $n(n-1)$ nontrivial characters. In the language of the roots, $M^{(\alpha)}$ is a root space and $M^{(0)}=\mathfrak{h}$ is the Cartan subalgebra. Each root space is one-dimensional and is spanned by a single matrix unit.

## The Root System

**The roots are the $n(n-1)$ differences of the coordinate characters, and they form the system $A_{n-1}$.** Write $\epsilon_i$ for the character $t\mapsto t_i$ and $\alpha_{ij}=\epsilon_i-\epsilon_j$. Then

$$
\Phi=\{\alpha_{ij}: i\ne j\},\qquad |\Phi|=n(n-1),\qquad \Phi^{+}=\{\alpha_{ij}: i<j\},\qquad |\Phi^{+}|=\frac{n(n-1)}{2}.
$$

The roots are the weights of the adjoint action, and the root space of $\alpha_{ij}$ is $\mathbb{C}E_{ij}$. The system is irreducible of rank $n-1$, the Weyl group is the symmetric group $S_n$, and the positive roots are the ones with $i<j$ in the chosen order.

**The count is the dimension of the antisymmetric half.** The number of positive roots is $\binom{n}{2}=n(n-1)/2$, which is exactly the dimension of $\operatorname{Skew}_n$. At $n=2,3,4,5,6$ the counts of all roots are $2,6,12,20,30$, of positive roots $1,3,6,10,15$, and the last column is the dimension of the skew half. The coincidence is not numerical: the positive roots index the off-diagonal pairs, and each pair contributes one skew direction.

**The simple roots are the gaps between consecutive indices, and their vectors are the simple nilpotents.** Put $\alpha_k=\alpha_{k,k+1}$ for $k=1,\dots,n-1$. Then the simple roots are the $n-1$ elements

$$
\alpha_1,\dots,\alpha_{n-1},\qquad \mathbb{C}E_{k,k+1}=M^{(\alpha_k)},
$$

and the matrix units $E_{k,k+1}$ are exactly the simple nilpotents $N_k$ of *The Frame, the Simple Nilpotents and the Gauge of $M_n(\mathbb{C})$*. Every other root vector is a product of consecutive simple ones, which is the root-system form of the statement that every unit of the frame is a product of simple nilpotents. The number $n-1$ of simple roots is the number of simple nilpotents and the number of parameters of the gauge.

## The Refinement of the Two Halves

**The involution acts on the grading by reversing the weight.** The transpose sends $E_{ij}$ to $E_{ji}$, so it sends the weight $\alpha_{ij}$ to $\alpha_{ji}=-\alpha_{ij}$. A weight line is therefore fixed by the involution exactly when its weight is zero, that is on the diagonal, and the other lines are exchanged in pairs.

**Each transposed pair splits into a symmetric line and a skew line.** For $i<j$ put

$$
S_{ij}=E_{ij}+E_{ji},\qquad K_{ij}=E_{ij}-E_{ji}.
$$

Then $S_{ij}^{\mathsf T}=S_{ij}$ and $K_{ij}^{\mathsf T}=-K_{ij}$, and the two-dimensional space $\mathbb{C}E_{ij}\oplus\mathbb{C}E_{ji}$ is the direct sum of the two lines. Hence

$$
\operatorname{Sym}_n=\mathfrak{h}\oplus\bigoplus_{i<j}\mathbb{C}S_{ij},\qquad
\operatorname{Skew}_n=\bigoplus_{i<j}\mathbb{C}K_{ij},
$$

of dimensions $n+\tfrac{n(n-1)}{2}=\tfrac{n(n+1)}{2}$ and $\tfrac{n(n-1)}{2}$. The two halves are the coarse split, and this is the fine form of it: the symmetric half is the diagonal plus one line from each pair, and the skew half is the other line from each pair.

**The coarse split loses the weight and keeps the parity.** A vector in $\operatorname{Sym}_n$ or in $\operatorname{Skew}_n$ is a sum of pieces of many weights, so the two halves are not graded pieces: they are the fixed and the anti-fixed sets of an involution which acts on the grading. The correct picture is a $\mathbb{Z}$-grading by weight together with a $\mathbb{Z}/2$-grading by the involution, and the four multiplication tables of the next articles are the interaction of the two.

**The complex case refines the complex halves the same way.** Over $\mathbb{C}$ the diagonal contributes its real part only, of real dimension $n$, and each transposed pair contributes one complex line,

$$
\operatorname{Herm}_n=\{\text{real diagonal}\}\oplus\bigoplus_{i<j}\mathbb{C}(E_{ij}+E_{ji}),
$$

of real dimension $n+2\cdot\tfrac{n(n-1)}{2}=n^{2}$, and the anti-Hermitian half is $i$ times it. The counting is the one of *The Two Halves over $\mathbb{C}$: Hermitian and Anti-Hermitian*, read pair by pair: the transpose splits each pair into two real lines, the conjugate transpose into two complex ones.

## The Peirce Lines as Weight Lines

**Against the coordinate flag the Peirce decomposition is the weight decomposition.** Take the coordinate family $P_k=E_{kk}$, with lines $V_k=\mathbb{C}e_k$. Then

$$
A_{kl}=P_kM_nP_l=\mathbb{C}E_{kl}=M^{(\epsilon_k-\epsilon_l)},
$$

so the $n^{2}$ Peirce lines are the $n^{2}$ weight lines, and the Peirce coordinates of a matrix are its entries. The Peirce decomposition of *The Peirce Decomposition in $n$ Dimensions* is therefore the general-flag version of the grading, and the grading is the case of the coordinate flag.

**The comparison with a general flag is the comparison of two gradings.** For a general family $P_1,\dots,P_n$ the lines $A_{kl}$ are still $n^{2}$ and one-dimensional, but the diagonal torus of the frame is not the coordinate torus: the two decompositions coincide only when the flag is the coordinate one. What is invariant is the count, $n$ diagonal lines and $n(n-1)$ off-diagonal lines, and the product rule $A_{kl}A_{pq}\subseteq\delta_{lp}A_{kq}$ which the grading satisfies as $M^{(\alpha)}M^{(\beta)}\subseteq M^{(\alpha+\beta)}$.

**The grading is the sharpest form of the statement that the algebra is a direct sum of lines.** No decomposition of $M_n(\mathbb{C})$ has more than $n^{2}$ summands of dimension one, and the weight decomposition attains the bound. The coarse split has two summands, the split by a rank-$p$ idempotent has four, and the Peirce split at a complete family has $n^{2}$.

## The Case $n=2$

**At $n=2$ the grading has $4$ lines, $2$ roots and $1$ positive root.** The weights are $1,t_1/t_2,t_2/t_1,1$ on the lines $\mathbb{C}E_{11},\mathbb{C}E_{12},\mathbb{C}E_{21},\mathbb{C}E_{22}$, and the pair $E_{12},E_{21}$ splits into

$$
S=\sigma_1=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad K=E_{12}-E_{21}=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
$$

a symmetric and a skew line. The one positive root is $\alpha_{12}$, its vector is the simple nilpotent $N_1=E_{12}$, and the count $n-1=1$ is the number of gauge parameters.

**The biquaternion frame is the grading plus the gauge.** The idempotents $\tilde\Pi_\pm$ are the two diagonal weight lines, the companion nilpotents $\vec\Upsilon_{+-}$ and $\vec\Upsilon_{-+}$ are the two off-diagonal weight lines, and the freedom of a frame is the freedom of choosing a vector in each line, which is the gauge $(\mathbb{C}^{\times})^{n-1}$ of *The Frame, the Simple Nilpotents and the Gauge of $M_n(\mathbb{C})$*. At $n=2$ that is one complex parameter, the reciprocal rescaling of the two nilpotents.

## Summary

The diagonal subalgebra $\mathfrak{h}$ has dimension $n$ and is a maximal torus; the conjugation action of the torus grades the algebra into $n^{2}$ one-dimensional weight lines, $n$ of weight zero and $n(n-1)$ of nontrivial weight. The weights are the roots of the system $A_{n-1}$, $n(n-1)$ in number with $n(n-1)/2$ positive, and the positive roots index the off-diagonal pairs. The simple roots correspond to the simple nilpotents $E_{k,k+1}$, $n-1$ of them, and every other unit is a product of consecutive simple ones. The transpose reverses the weight and splits each transposed pair into a symmetric line $E_{ij}+E_{ji}$ and a skew line $E_{ij}-E_{ji}$, which gives the two halves as a coarsening: $\operatorname{Sym}_n=\mathfrak{h}\oplus\bigoplus_{i<j}\mathbb{C}S_{ij}$ and $\operatorname{Skew}_n=\bigoplus_{i<j}\mathbb{C}K_{ij}$. Against the coordinate flag the Peirce lines are the weight lines, and no decomposition has more than $n^{2}$ one-dimensional summands.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathfrak{h}$ | the diagonal subalgebra, of dimension $n$ |
| $T=\operatorname{diag}(t_1,\dots,t_n)$ | an element of the diagonal torus |
| $\chi_{ij}(T)=t_i/t_j$ | the weight of the line $\mathbb{C}E_{ij}$ |
| $M^{(\alpha)}$ | the weight space of the character $\alpha$ |
| $\alpha_{ij}=\epsilon_i-\epsilon_j$ | a root, with $\epsilon_i$ the character $t\mapsto t_i$ |
| $\Phi^{+}$ | the positive roots $\alpha_{ij}$ with $i<j$, $n(n-1)/2$ of them |
| $S_{ij}=E_{ij}+E_{ji}$ | the symmetric line of a transposed pair |
| $K_{ij}=E_{ij}-E_{ji}$ | the skew line of a transposed pair |
| $A_{kl}=P_kM_nP_l$ | the Peirce line, equal to $\mathbb{C}E_{kl}$ at the coordinate flag |

## Further Reading

- James E. Humphreys, *Introduction to Lie Algebras and Representation Theory* (Springer, 1972), for the root system $A_{n-1}$, the simple roots and the root spaces.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the diagonal subalgebra, the maximal torus and the conjugation action.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the fine decomposition of an algebra into lines and the coordinate form of Peirce.
- [The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric](the-two-halves-over-r-symmetric-and-antisymmetric.html), for the split that this grading refines.
- [The Two Halves over $\mathbb{C}$: Hermitian and Anti-Hermitian](the-two-halves-over-c-hermitian-and-skew-hermitian.html), for the complex version of the refinement.
- [The Frame, the Simple Nilpotents and the Gauge of $M_n(\mathbb{C})$](the-frame-the-simple-nilpotents-and-the-gauge-of-mnc.html), for the simple nilpotents as simple root vectors.
- [The Peirce Decomposition in $n$ Dimensions](the-peirce-decomposition-in-n-dimensions.html), for the general-flag version of the grading.
