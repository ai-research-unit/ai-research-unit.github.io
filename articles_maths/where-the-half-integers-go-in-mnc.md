# __Where the Half-Integers Go in $M_n(\mathbb{C})$__

## Introduction

**The question.** The biquaternion algebra carries the labels $0$, $\tfrac12$ and $1$. Under the principal copy at general $n$, which labels does the algebra carry, and where does the half-integer go?

**The answer in one line.** The algebra carries the integer labels $0,1,\dots,n-1$ at every $n$; the half-integer $j=\tfrac{n-1}{2}$ is the label of the module $\mathbb{C}^n$, which is not a subspace of the algebra except when $j$ happens to be an integer.

**Why the article is needed.** This is the point at which $n=2$ habits do the most damage. At $n=2$ the module has label $\tfrac12$, the algebra has labels $0$ and $1$, and the three numbers together look like the spectrum of one object. At $n=4$ the module has label $\tfrac32$ and the algebra has labels $0,1,2,3$; a reader who imports the $n=2$ picture looks for spin $\tfrac32$ inside $M_4$ and does not find it, and then doubts the decomposition.

**Boundaries.** The decomposition is *The Spin Decomposition of $M_n(\mathbb{C})$*; the carrier of spin zero is *The Spin-Zero Carrier of $M_n(\mathbb{C})$*; the carrier of spin one is *The Spin-One Carrier of $M_n(\mathbb{C})$*; the case $n=4$ in four readings is *The Spin Content of $M_4(\mathbb{C})$*. The biquaternion originals are *The Spin-Half Bispinor Spaces* and *From the Spin to the Carriers and the Closures*.

**Conventions.** $j=\tfrac{n-1}{2}$; the module is $\mathbb{C}^n\cong V_j$; the algebra is $M_n\cong\bigoplus_{k=0}^{n-1}V_k$ under conjugation. $V_s\cong V_t$ if and only if $s=t$.

## The Two Objects

**The module.** $\mathbb{C}^n=V_j$, of dimension $2j+1=n$, with weights $-j,-j+1,\dots,j$, which are half-integers when $n$ is even and integers when $n$ is odd.

**The algebra.** $M_n=\bigoplus_{k=0}^{n-1}V_k$, with $k$ an integer, at every $n$.

**The arithmetic of the two labels.** The algebra's labels are differences of the module's weights, $d=m_a-m_b$, and the difference of two numbers that are both half-integers, or both integers, is an integer. Hence the algebra's labels are integers whether the module's label is or not.

**The consequence.** The half-integer cannot appear in the algebra as a weight difference. It can appear only as the label of a carrier, and the carriers have integer labels by the theorem.

## Is the Module Inside the Algebra?

**Proposition.** The module's carrier $V_j$ occurs as a summand of $M_n$ if and only if $j\in\{0,1,\dots,n-1\}$, that is if and only if $n$ is odd.

*Proof.* The summands of $M_n$ are $V_k$ with $0\le k\le n-1$. Since $V_j\cong V_k$ only for $j=k$, the carrier $V_j$ occurs exactly when $j$ is one of those integers. With $j=\tfrac{n-1}{2}$ this is $0\le\tfrac{n-1}{2}\le n-1$, which holds for every $n\ge1$, together with the integrality of $j$, which holds exactly for odd $n$. $\square$

**The table.**

| $n$ | $j$ | $j$ integral | $V_j\subseteq M_n$ | module weights |
|---|---|---|---|---|
| $2$ | $\tfrac12$ | no | no | $\pm\tfrac12$ |
| $3$ | $1$ | yes | yes, $V_1$ | $-1,0,1$ |
| $4$ | $\tfrac32$ | no | no | $\pm\tfrac12,\pm\tfrac32$ |
| $5$ | $2$ | yes | yes, $V_2$ | $-2,\dots,2$ |
| $6$ | $\tfrac52$ | no | no | $\pm\tfrac12,\dots,\pm\tfrac52$ |

**The reading.** For odd $n$ the module's spin is an integer and the module's carrier is one of the algebra's carriers; the question "where is the half-integer" does not arise. For even $n$ the module's spin is a half-integer and no carrier of the algebra has that label.

**The precise negative statement.** For even $n$ there is no subspace of $M_n$ that is isomorphic to $\mathbb{C}^n$ as a module for the principal copy. The module is the space on which the algebra acts, not a part of it.

## Why the Biquaternion Case Looks Different

**The real form.** At $n=2$ the module is $\mathbb{C}^2=V_{1/2}$, and the algebra is $M_2\cong V_1\oplus V_0$. The biquaternion series reads both through a real structure: the algebra over $\mathbb{R}$ has the four-dimensional space $\mathbb{B}$, and the spinor plane and the bispinor space are real subspaces of it, and they are visible inside the algebra because the algebra is only four-real-dimensional.

**Why half-integers appear there.** The real algebra $\mathbb{B}$ acts on itself by left multiplication, and the left ideal $\mathbb{B}\tilde\Pi_{\mathrm{id},+}$ is a real subspace of the algebra isomorphic to the spinor module. So at $n=2$ the module *is* a subspace of the algebra over $\mathbb{R}$: the left ideals are inside the algebra.

**The general-$n$ statement.** For $n\ge3$ no left ideal of $M_n$ is a minimal carrier of the principal copy: the minimal left ideals are the spaces $M_nP$ for a rank-one idempotent $P$, of complex dimension $n$, and their module structure is the defining module, not a subspace of the carrier list.

*Proof.* $M_nP$ consists of the matrices whose image lies in the line $\operatorname{im}P$, so it is the space of all matrices with that image; under left multiplication it is the defining module. Its dimension is $n$, and its isomorphism type as a principal-copy module is $V_j$, which occurs in the carrier list only for odd $n$. $\square$

**The honest conclusion.** The biquaternion spin-half space is a left ideal of a four-dimensional real algebra. The general-$n$ object of the same shape is the left ideal $M_nP$, of complex dimension $n$, and it carries the label $j$ — which is a half-integer exactly when $n$ is even, and then it is not a summand of the algebra. The label lives on the ideal, and the ideal is not a carrier of the algebra.

## Where Half-Integers Do Appear in the Algebra

**Other groups.** Under a group other than the principal copy the algebra can carry half-integer labels. At $n=4$, with the block reading on $\mathbb{C}^2\oplus\mathbb{C}^2$ and the group $SU(2)\times SU(2)$, the two off-diagonal corners carry two copies of $(\tfrac12,\tfrac12)$; the diagonal content of the whole algebra in that reading is $4V_1\oplus4V_0$, with no half-integer, but the pair labels $\tfrac12$ are visible in the corners.

**The lesson.** A half-integer label in the algebra is a statement about a group action, and the group must be named. Under the principal copy the answer is always "integers only".

**The exception that is not one.** The label $\tfrac12$ at $n=2$ is the principal copy's module label, and it is visible in the algebra only because the algebra happens to be four-real-dimensional and the left ideal is a real subspace. It is not a half-integer carrier of $M_2$.

## What Not to Import

**The wrong claim.** "The algebra $M_4$ has spin content $\tfrac32 + \tfrac12 + \dots$ because the module has label $\tfrac32$." False: the algebra's labels are $0,1,2,3$, and $\tfrac32$ is not among them.

**The wrong claim.** "The spin-half carrier of $M_2$ generalises to a spin-half carrier of $M_n$." False: at even $n$ there is no carrier of label $\tfrac{n-1}{2}$; at odd $n$ the label is an integer.

**The right claim.** "The module has label $j$ and the algebra has labels $0$ to $n-1$; the algebra's top label is $2j$." True at every $n$, and it is the whole of the general statement.

## The Finite Check

Computed for $n=2,3,4,5$: the Casimir $-\sum_i\operatorname{ad}_{J_i}^2$ (the $J_i$ anti-Hermitian) has the eigenvalues $k(k+1)$ with $k=0,\dots,n-1$, all even integers, and the eigenspace dimensions are $2k+1$; no half-integer eigenvalue occurs.

The module's weights were computed from $J_z=\operatorname{diag}(j,j-1,\dots,-j)$: they are $\pm\tfrac12$ at $n=2$, $-1,0,1$ at $n=3$, $\pm\tfrac12,\pm\tfrac32$ at $n=4$, $-2,\dots,2$ at $n=5$. The differences $m_a-m_b$ are integers in every case, with multiplicity $n-\lvert d\rvert$.

The left ideal was checked at $n=2,3,4,5$: for a rank-one idempotent $P$ the space $\{XP\}$ has dimension $n$ and is invariant under left multiplication, confirming that the module of the ideal is the defining module and not a carrier of the algebra.

## The Four Lists at $n=4$

| group | carrier list | module labels |
|---|---|---|
| principal $SU(2)$ | $7+5+3+1$ | the module $V_{3/2}$, not a summand |
| full $U(4)$ | $1+15$ | the defining module, not a summand |
| factorised on $\mathbb{C}^2\otimes\mathbb{C}^2$ | $9+3+3+1$ | $(\tfrac12,\tfrac12)$, a pair of half-integers |
| block on $S_+\oplus S_-$ | $8+3+3+2$ | two copies of $(\tfrac12,\tfrac12)$ plus $(1,0)\oplus(0,1)$ |

**The observation.** In every list the algebra's own labels are integers. The half-integers occur only as the pair $(\tfrac12,\tfrac12)$, never as a single half-integer label.

**The reading.** A single half-integer in the algebra would be a state of half-integer total spin. At $n=4$ there is none, and the factorised reading explains why: the two half-integers come in a pair, and the pair has integer total spin.

## Why the Module Is Not a Subspace

**The dimensions.** The module has complex dimension $n$ and the algebra has complex dimension $n^2$; the carrier list of the algebra has $n$ summands of dimensions $1,3,\dots,2n-1$.

**The labels.** The module's label $j=\tfrac{n-1}{2}$ is half-integral for even $n$, and no summand of the algebra has that label, because the algebra's labels are $0,1,\dots,n-1$.

**The conclusion.** For even $n$ the module is not isomorphic to any submodule of the algebra, so the module does not occur as a submodule of the algebra at all.

**The reading.** At $n=4$ the module is a two-dimensional complex space of spin $\tfrac32$, and the algebra has carriers of spins $0,1,2,3$; there is no $\tfrac32$ anywhere in the algebra, and no subspace of the algebra carries it.

## What a Half-Integer Carrier Would Require

**The requirement.** A half-integer carrier of the algebra would be a summand $V_{k/2}$ with $k$ odd, hence a summand of even dimension $2\cdot\tfrac{k}{2}+1=k+1$ with $k$ odd.

**The obstruction.** The decomposition is multiplicity-free with labels $0,1,\dots,n-1$, so no summand of that kind exists. A half-integer subspace that is not a summand is not a carrier, and it is not invariant.

**The reading.** The half-integer would have to be introduced by a different group action, and at $n=4$ the only place it can appear is a pair of labels coming from a product of two half-integer factors.

## The Rule

**The rule.** In the algebra, integer labels only. Half-integer labels occur in the module, and in the algebra only as pairs coming from a product of two half-integer factors.

**The reason.** The algebra's labels are the differences of the module's weights, and the difference of two half-integers is an integer.

**The reading.** The rule is the article in one line, and it holds at every $n$: the parity of the labels is inherited from the parity of $n$, and the differences forget it.

## The Counterexample That Is Not One

**The apparent counterexample.** At $n=4$ the block reading exhibits the labels $(\tfrac12,\tfrac12)$, and a reader may take them as half-integer labels of the algebra.

**The correction.** The pair has integer total label $\tfrac12+\tfrac12=1$, and the algebra's carrier $V_1$ is the corresponding summand. The half-integers are the two factors, not the label.

**The reading.** A half-integer label is a property of a single factor of a product group, and the principal copy has only one factor.

## The Count

**The numbers.** At $n=4$ the carriers have dimensions $7,5,3,1$ and the module has dimension $2$. No summand has dimension $2$.

## Summary

Under the principal copy the algebra carries the integer labels $0$ to $n-1$ at every $n$, and the module carries $j=\tfrac{n-1}{2}$, which is a half-integer for even $n$. The module's carrier is a summand of the algebra exactly when $n$ is odd. The biquaternion spin-half space is a left ideal of a real four-dimensional algebra, and its general analogue is the left ideal $M_nP$ of complex dimension $n$, which carries the label $j$ without being a carrier of the algebra. Half-integer labels inside the algebra require a different group, and the group must be named.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $j=\tfrac{n-1}{2}$ | the label of the module |
| $0,\dots,n-1$ | the labels of the algebra |
| $V_j\subseteq M_n$ | holds exactly for odd $n$ |
| $M_nP$ | the minimal left ideal, of complex dimension $n$ |
| $(\tfrac12,\tfrac12)$ | the pair label in the chiral corners at $n=4$ |

## Further Reading
- [The Spin Decomposition of $M_n(\mathbb{C})$: $n$ Carriers, One for Each Spin from $0$ to $n-1$](the-spin-decomposition-of-mnc.html), for the integer labels.
- [The Spin Content of $M_4(\mathbb{C})$](the-spin-content-of-m4c.html), for the four readings at $n=4$.
- [The Spin-Half Bispinor Spaces](the-spin-half-bispinor-spaces.html), for the case $n=2$.
- [The Spin-Zero Carrier of $M_n(\mathbb{C})$: the Scalars](the-spin-zero-carrier-of-mnc.html), for the label $0$.
- [The Spin-One Carrier of $M_n(\mathbb{C})$: the Three-Dimensional $V_1$](the-spin-one-carrier-of-mnc.html), for the label $1$.
- [The Odd Rows: $M_3(\mathbb{C})$ and $M_5(\mathbb{C})$](the-odd-rows-m3-and-m5.html), for the rows with no half-integer at all.
