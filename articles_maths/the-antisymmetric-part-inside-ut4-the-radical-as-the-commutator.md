# __The Antisymmetric Part inside $UT_4$: the Radical as the Commutator__

## Introduction

**Inside the Borel $\mathfrak{b}=\mathfrak{h}\oplus\mathfrak{n}_+$ the radical of the trace form is $\mathfrak{n}_+$, of dimension $6$, and it is also the derived algebra $[\mathfrak{b},\mathfrak{b}]$; but the antisymmetric matrices inside $\mathfrak{b}$ are only the zero matrix, so the identification is between the radical and the commutator, not between the radical and $\operatorname{Skew}_4$.**

The article computes the restricted form, proves that an antisymmetric upper triangular matrix is zero, proves $[\mathfrak{b},\mathfrak{b}]=\mathfrak{n}_+$ and that the radical is $\mathfrak{n}_+$, and then states exactly what the coincidence means: $\mathfrak{n}_+$ is the totally isotropic part of the Borel, the place where the form is alternating, and it is a six-dimensional subspace that is not the antisymmetric half.

It assumes *The Triangular Decomposition $h\oplus n_+\oplus n_-$ of $M_4(\mathbb{C})$* and *$UT_4$ as the Complement of the Antisymmetric Part*. The case $n=2$ is *The Antisymmetric Part inside $UT_2$: the Radical as the Commutator*; the form itself is *The Trace Form and Its Signature on the Two Halves of $M_4(\mathbb{C})$*; the Killing form of the same algebra is *The Killing Form, Its Radical and the Triangular Case*.

## The Restricted Form

**Definition.** $\beta(X,Y)=\operatorname{tr}(XY)$ restricted to $\mathfrak{b}$, the upper triangular matrices including the diagonal of dimension $10$.

**Proposition.** $\beta(E_{ij},X)=X_{ji}$ for every unit $E_{ij}$ and every $X$.

**Proof.** $\operatorname{tr}(E_{ij}X)=\sum_p(E_{ij}X)_{pp}$, and $(E_{ij}X)_{pp}=\delta_{pj}X_{ip}$, so the sum is $X_{ji}$.

**Corollary.** For $X\in\mathfrak{b}$ and $i<j$, $\beta(E_{ij},X)=X_{ji}=0$; and $\beta(E_{ii},X)=X_{ii}$.

**Proof.** The entry $X_{ji}$ with $j>i$ is below the diagonal and vanishes; the diagonal entry is read directly.

**Theorem.** The radical of $\beta$ restricted to $\mathfrak{b}$ is $\mathfrak{n}_+$, of dimension $6$.

**Proof.** By the corollary every strictly upper unit pairs to zero with every element of $\mathfrak{b}$, so $\mathfrak{n}_+\subset\operatorname{rad}$. Conversely if $X\in\mathfrak{b}$ pairs to zero with every $E_{ii}$, then $X_{ii}=0$ for all $i$, so $X\in\mathfrak{n}_+$. Hence the radical is exactly $\mathfrak{n}_+$.

**Corollary.** On $\mathfrak{b}$ the form has rank $4$, and on the diagonal it is the standard positive definite form $\sum h_ih_i'$.

**Proof.** The rank is the dimension minus the radical, $10-6=4$, and the diagonal part is $\sum_i h_ih_i'$ since $\operatorname{tr}(E_{ii}E_{jj})=\delta_{ij}$.

**The totally isotropic part.** $\mathfrak{n}_+$ is totally isotropic: $\beta(N,N')=0$ for all $N,N'\in\mathfrak{n}_+$.

**Proof.** The product of two strictly upper triangular matrices is strictly upper triangular, hence has zero diagonal, hence zero trace.

## The Antisymmetric Matrices inside the Borel

**Proposition.** $\operatorname{Skew}_4\cap\mathfrak{b}=0$.

**Proof.** Let $K\in\mathfrak{b}$ be antisymmetric. Its diagonal entries satisfy $k_{ii}=-k_{ii}$, so they vanish. Its entries above the diagonal vanish by triangularity, and its entries below vanish by antisymmetry. Hence $K=0$.

**Corollary.** The antisymmetric part inside $UT_4$ is the zero subspace, and every nonzero antisymmetric matrix has a nonzero entry strictly below the diagonal.

**Proof.** The first is the proposition; the second is its contrapositive, read entry by entry.

**Corollary.** $\operatorname{Skew}_4\oplus\mathfrak{b}=M_4$, and the map sending an antisymmetric matrix to its $\mathfrak{b}$-component along $\mathfrak{n}_-$ is injective, its image being the six-dimensional space of strict upper parts.

**Proof.** The dimensions are $6+10=16$ with zero intersection. An antisymmetric matrix has zero diagonal, so its $\mathfrak{b}$-component is its strict upper part, and an antisymmetric matrix whose strict upper part vanishes is its own negative transpose with zeros above the diagonal, hence zero.

**What this rules out.** The claim "the antisymmetric part inside the Borel is its nilradical" is false as a statement about matrices: the nilradical $\mathfrak{n}_+$ consists of strictly **upper** triangular matrices, none of which is antisymmetric except zero. The two spaces are disjoint, and they even have zero intersection.

**Proof.** A strictly upper triangular matrix has a nonzero entry above the diagonal and its transpose is not its negative; if it were antisymmetric it would be zero by the proposition.

## The Radical Is the Commutator

**Theorem.** $[\mathfrak{b},\mathfrak{b}]=\mathfrak{n}_+$.

**Proof.** The quotient $\mathfrak{b}/\mathfrak{n}_+\cong\mathfrak{h}$ is abelian, so the derived algebra lies in $\mathfrak{n}_+$. Conversely $[E_{ii},E_{ij}]=E_{ij}$ for $i\neq j$, since $E_{ij}E_{ii}=0$, so every strictly upper unit is a commutator; the six units span $\mathfrak{n}_+$.

**Corollary.** $\mathfrak{n}_+$ is a nilpotent ideal of dimension $6$, and $\mathfrak{b}$ is solvable of derived length two.

**Proof.** $\mathfrak{n}_+^{4}=0$ by the strictly upper triangular argument, and the second derived algebra is $[\mathfrak{n}_+,\mathfrak{n}_+]\subset\mathfrak{n}_+$; since $\mathfrak{b}/\mathfrak{n}_+$ is abelian and $\mathfrak{n}_+$ is nilpotent, $\mathfrak{b}$ is solvable, and it is not abelian, so the derived length is exactly two.

**Corollary.** The radical of $\beta$ on $\mathfrak{b}$ equals the derived algebra, and both are $\mathfrak{n}_+$.

**Proof.** The two theorems identify the same subspace.

**The invariance reading.** $\beta([X,Y],Z)=\beta(X,[Y,Z])$ for all $X,Y,Z\in\mathfrak{b}$, so the radical is an ideal and the derived algebra lies in it.

**Proof.** The invariance identity of the trace form, $\operatorname{tr}([X,Y]Z)=\operatorname{tr}(X[Y,Z])$, and the radical of an invariant form is an ideal.

**Corollary.** The form descends to the quotient $\mathfrak{b}/\mathfrak{n}_+\cong\mathfrak{h}$, where it is positive definite.

**Proof.** The radical is exactly the kernel of the descended form, and on the diagonal the form is $\sum h_ih_i'$.

## Two Sixes, One Subspace

**Proposition.** $\dim\mathfrak{n}_+=6=\dim\operatorname{Skew}_4$, and $\mathfrak{n}_+\cap\operatorname{Skew}_4=0$.

**Proof.** The first is the count of pairs $i<j$; the second is the proposition of the previous section.

**Corollary.** The two six-dimensional spaces are complementary inside the twelve-dimensional off-diagonal part, and each is totally isotropic or totally non-isotropic in a different sense: $\mathfrak{n}_+$ is isotropic for $\beta$, while $\operatorname{Skew}_4$ is negative definite for it.

**Proof.** $\mathfrak{n}_+$ is isotropic by the trace argument; on $\operatorname{Skew}_4$ the form is $-2\sum_{i<j}k_{ij}^{2}$, negative definite; the sum has dimension $12$ and both lie in the off-diagonal part.

**The measurement that separates them.** $\beta(N,N)=0$ for $N\in\mathfrak{n}_+$ and $\beta(K,K)<0$ for $K\in\operatorname{Skew}_4$ nonzero; the two spaces are therefore distinguished by the sign of the form and not by the dimension.

**Proof.** The two displayed computations.

**Why the coincidence of the dimensions is not an accident of counting.** The number $\binom{4}{2}=6$ counts the pairs $i<j$, and it counts them twice: once as the units of $\mathfrak{n}_+$ and once as the units $E_{ij}-E_{ji}$ of $\operatorname{Skew}_4$. The two uses of the same count are the two ways of attaching a number to an unordered pair, as an ordered upper entry or as a difference of two entries.

**Proof.** Both spaces have one basis element per unordered pair, indexed by the same set.

## What the Title's Claim Means

**The true statement.** The antisymmetric part inside the Borel, in the sense of the antisymmetric matrices it contains, is zero. The radical of the trace form on the Borel is $\mathfrak{n}_+$, and it coincides with the derived algebra. The two statements are different and both are proved above.

**Proof.** The first is $\operatorname{Skew}_4\cap\mathfrak{b}=0$, the second is the computation of the radical and of the commutator.

**Why the two are easily confused.** In the whole algebra the antisymmetric half is the negative definite part of the form, so "the part where the form is negative" and "the antisymmetric part" name the same subspace. Inside the Borel the form degenerates, its radical is six-dimensional, and the radical is isotropic — the opposite sign — so the identification breaks down at exactly the place where the form stops being nondegenerate.

**Proof.** On $\operatorname{Skew}_4$ the form is negative definite; on the radical it is identically zero; the two properties cannot hold on the same nonzero subspace.

**What survives of the analogy.** The radical is still the "alternating" part in the sense that the form restricts to zero on it, and it is still a Lie ideal, and it is still the piece that the quotient kills. Those three properties are the ones the antisymmetric half has in the whole algebra, and they are the ones that carry over.

**Proof.** The radical of an invariant form is an ideal, the restriction to it vanishes, and the quotient is the nondegenerate part.

## Summary

Inside the Borel of dimension $10$ the trace form has radical $\mathfrak{n}_+$ of dimension $6$ and rank $4$, positive definite on the diagonal quotient. The derived algebra is also $\mathfrak{n}_+$, so the radical and the commutator are one subspace, and both are read from the same six units.

The antisymmetric matrices inside the Borel are only zero, so the antisymmetric half is not the radical and the two spaces are disjoint; they share the dimension $6$ because both are indexed by the unordered pairs of indices.

The title's identification holds for the radical and the commutator and fails for the antisymmetric matrices. The reason is the degeneration of the form: on the whole algebra the negative definite part and the antisymmetric part coincide, and inside the Borel the form's radical is isotropic, which is the opposite sign. What carries over is that the radical is an ideal, that the form vanishes on it, and that the quotient is the nondegenerate part.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathfrak{b}=\mathfrak{h}\oplus\mathfrak{n}_+$ | the Borel, dimension $10$ |
| $\mathfrak{n}_+$ | strictly upper triangular, dimension $6$, the radical |
| $[\mathfrak{b},\mathfrak{b}]$ | the derived algebra, equal to $\mathfrak{n}_+$ |
| $\operatorname{Skew}_4$ | the antisymmetric half, with $\operatorname{Skew}_4\cap\mathfrak{b}=0$ |
| $\beta(X,Y)=\operatorname{tr}(XY)$ | the restricted trace form |
| $\mathfrak{h}$ | the diagonal, the nondegenerate quotient |

## Further Reading

- James E. Humphreys, *Introduction to Lie Algebras and Representation Theory* (Springer, 1972), for solvable algebras, radicals and derived series.
- [The Triangular Decomposition $h\oplus n_+\oplus n_-$ of $M_4(\mathbb{C})$](the-triangular-decomposition-h-n-plus-n-minus-of-m4c.html), for the Borel and its derived algebra.
- [The Killing Form, Its Radical and the Triangular Case](the-killing-form-its-radical-and-the-triangular-case.html), for the same radical computed for the Killing form.
- [$UT_4$ as the Complement of the Antisymmetric Part](ut4-as-the-complement-of-the-antisymmetric-part.html), for the disjointness of the two six-dimensional spaces.
- [The Antisymmetric Part inside $UT_2$: the Radical as the Commutator](the-antisymmetric-part-inside-ut2-the-radical-as-the-commutator.html), for the case at order two.
