# __The Odd Rows: $M_3(\mathbb{C})$ and $M_5(\mathbb{C})$__

## Introduction

**The question.** The rows $n=3$ and $n=5$ differ from $n=2$ and $n=4$ in the parity of the module's label. What exactly changes, and what does it change?

**The answer in one line.** For odd $n$ the element $-\mathrm I$ acts trivially on $\operatorname{Sym}^{n-1}$, so the copy factors through $SO(3)$, every label in the picture is an integer, and no half-integer exists anywhere.

**Why the article is needed.** The rows $n=2$ and $n=4$ are the spinorial rows, and they are the ones the biquaternion series and its first generalisation treat. The rows $n=3$ and $n=5$ are tensorial, and their tables are short enough to write in full. Without them the reader has no example in which the half-integer is absent by construction, and the parity of $n$ looks like a technicality rather than a structural split.

**Boundaries.** The decomposition is *The Spin Decomposition of $M_n(\mathbb{C})$*; the labels are *Integer Labels on the Algebra, a Half-Integer on the Module: The Carrier Condition*; the even rows are *The Spin Content of $M_4(\mathbb{C})$*; the carrier tables are *The Carriers, the Closures and the Spin of $M_n(\mathbb{C})$*.

**Conventions.** $j=\tfrac{n-1}{2}$, so $j=1$ at $n=3$ and $j=2$ at $n=5$. The weights of the module are $-j,\dots,j$.

## The Parity

**Proposition.** The image of $-\mathrm I$ in the principal copy is $(-1)^{n-1}\mathrm I$. It is $+\mathrm I$ for odd $n$ and $-\mathrm I$ for even $n$.

*Proof.* $-\mathrm I=\exp(2\pi iJ_z)$ in $SU(2)$, and on $\operatorname{Sym}^{n-1}$ the element $J_z$ has eigenvalues $j,j-1,\dots,-j$, so the exponential acts by $\exp(2\pi i m)$ on the weight $m$. Every weight is a half-integer, so each exponential is $\pm1$, and the product of the signs is $(-1)^{2j}=(-1)^{n-1}$. $\square$

**The consequence for the group.** For odd $n$ the copy is a quotient of $SU(2)$ by $\{\pm\mathrm I\}$, hence is $SO(3)$, and the module is a representation of $SO(3)$: it is tensorial.

**The consequence for the labels.** Every weight of the module and of the algebra is an integer for odd $n$, hence every carrier label is an integer, hence the list of labels is the same list as the list of dimensions up to the shift by one.

**The check.** $\exp(2\pi iJ_z)$ equals $(-1)^{n-1}\mathrm I$ to $10^{-16}$ for $n=2,\dots,6$, computed from the weight diagonal.

## The Row $n=3$

**The carriers.** $M_3=V_2\oplus V_1\oplus V_0$, of dimensions $5+3+1=9$.

**The module.** $\mathbb{C}^3=V_1$: the defining module has spin one, an integer.

**The coincidence.** At $n=3$ the module's carrier and the adjoint carrier are the same, both $V_1$. The two roles that were distinct at $n=2$ and at $n=4$ coincide here, and they coincide for the same reason: the module has dimension three and the adjoint has dimension three.

**The weights.** The module has weights $-1,0,1$; the algebra has weights $-2,-1,0,1,2$ with multiplicities $1,2,3,2,1$.

**The Casimir.** The values are $0,2,6$ on $V_0,V_1,V_2$, and their sum with multiplicities is $1\cdot0+3\cdot2+5\cdot6=36$, which is $\tfrac{n^2(n^2-1)}{2}=\tfrac{9\cdot8}{2}=36$.

## The Row $n=5$

**The carriers.** $M_5=V_4\oplus V_3\oplus V_2\oplus V_1\oplus V_0$, of dimensions $9+7+5+3+1=25$.

**The module.** $\mathbb{C}^5=V_2$: the defining module has spin two.

**The position of the module's carrier.** $V_2$ is the middle carrier of the five. It is neither the adjoint nor the top: the adjoint is $V_1$ and the top is $V_4$.

**The weights.** The module has weights $-2,-1,0,1,2$; the algebra has the differences, with multiplicities $1,2,3,4,5,4,3,2,1$.

**The Casimir.** The values are $0,2,6,12,20$, and the weighted sum is $1\cdot0+3\cdot2+5\cdot6+7\cdot12+9\cdot20=300=\tfrac{25\cdot24}{2}$.

## The Even Rows for Contrast

**The row $n=2$.** $M_2=V_1\oplus V_0=3+1=4$, module $V_{1/2}$: the module's carrier is not a summand of the algebra, and $-\mathrm I$ acts by $-1$.

**The row $n=4$.** $M_4=V_3\oplus V_2\oplus V_1\oplus V_0=7+5+3+1=16$, module $V_{3/2}$: again the module's carrier is absent, and $-\mathrm I$ acts by $-1$.

**The row $n=6$.** $M_6=V_5\oplus\dots\oplus V_0=11+9+7+5+3+1=36$, module $V_{5/2}$.

**The pattern.** For even $n$ the module's label is a half-integer, $-\mathrm I$ acts by $-1$, the copy is faithful, and the module is spinorial. For odd $n$ the label is an integer, $-\mathrm I$ acts trivially, the copy factors through $SO(3)$, and the module is tensorial.

## What the Odd Rows Show

**No half-integer anywhere.** In the odd rows every weight, every label and every Casimir value is an integer. A reader who has seen only $n=2$ and $n=4$ may believe the half-integer is intrinsic to the construction; the odd rows show that it is a parity phenomenon.

**The module inside the algebra.** For odd $n$ the module's carrier $V_j$ is a summand of $M_n$: $V_1$ at $n=3$, $V_2$ at $n=5$. The module and the algebra share a carrier type exactly in the odd rows.

**The absent phenomenon.** There is no "$-\mathrm I$ acts by $-1$" statement, no double cover, and no spinorial module. The price is that the top carrier is even: the top label is $n-1$, which is even for odd $n$.

**The reading.** Parity of $n$ decides between the tensorial and the spinorial picture, and it decides it at the level of the group, before any label is assigned.

## The Finite Check

Computed for $n=2,\dots,6$: $\exp(2\pi iJ_z)=(-1)^{n-1}\mathrm I$ with residual below $10^{-15}$.

The carrier dimensions were read from the Casimir eigenspaces: $1,3,5$ at $n=3$ and $1,3,5,7,9$ at $n=5$, summing to $9$ and $25$. The Casimir values are $0,2,6$ and $0,2,6,12,20$, and the weighted sums are $36$ and $300$, equal to $\tfrac{n^2(n^2-1)}{2}$ in both cases.

The weight multiplicities were computed from $\operatorname{ad}_{J_z}$: at $n=3$ they are $1,2,3,2,1$ and at $n=5$ they are $1,2,3,4,5,4,3,2,1$, matching $n-\lvert d\rvert$.

## The Casimir Table for the Odd Rows

| $n$ | values | multiplicities | weighted sum |
|---|---|---|---|
| $3$ | $0,2,6$ | $1,3,5$ | $36$ |
| $5$ | $0,2,6,12,20$ | $1,3,5,7,9$ | $300$ |

**The parity of the values.** For odd $n$ every label is an integer, so every Casimir value $k(k+1)$ is even. For even $n$ the module's label is a half-integer, and the values $\tfrac34,\tfrac{15}{4},\dots$ of the module never appear in the algebra.

**The reading.** The Casimir values of the algebra are even integers at every $n$; the half-integer labels show up only as the fraction $\tfrac34$-type values of the module, which the algebra does not contain.

## What the Odd Rows Cannot Show

**The absence.** No spinorial module, no double cover, and no element acting by $-1$ on the module.

**The price.** The top carrier has even spin $n-1$, so the algebra's spin is never half-integer in the odd rows, and the module's carrier is a summand.

**The reading.** A reader who wants to see the half-integer mechanism must go to $n=4$; a reader who wants to see its absence has $n=3$ and $n=5$.

## The Two Rows in One Line

**The row $n=3$.** $M_3=V_2\oplus V_1\oplus V_0=5+3+1$, module $V_1$, group $SO(3)$.

**The row $n=5$.** $M_5=V_4\oplus V_3\oplus V_2\oplus V_1\oplus V_0=9+7+5+3+1$, module $V_2$, group $SO(3)$.

**The pattern.** The top carrier is $V_{n-1}$, the module is $V_{(n-1)/2}$, and the module's carrier sits in the middle of the list.

**The reading.** The odd rows are the rows in which the whole picture is a picture of $SO(3)$ representations, and the module is one of the carriers.

## The Two Actions

**At $n=3$.** The module $\mathbb{C}^3$ is the vector representation of $SO(3)$, and the algebra is $V_2\oplus V_1\oplus V_0$, the traceless symmetric plus the adjoint plus the scalars.

**At $n=5$.** The module $\mathbb{C}^5$ is the spin-two representation of $SO(3)$, and the algebra runs from spin four down to spin zero.

**The reading.** In both rows the module is one of the carriers, and the highest carrier is twice the module's label.

## The Module as a Carrier

**The statement.** For odd $n$ the module's carrier $V_j$ is a summand of the algebra, so the module is a direct summand of the algebra as a module.

**The consequence.** The module is visible from inside the algebra at odd $n$ and from outside at even $n$.

**The reading.** The difference between the odd and even rows is the difference between a module that sits inside the algebra and one that does not.

## The Reading of the Two Rows

**The summary line.** $M_3$ has three carriers and $M_5$ has five, and in both cases the module is one of them.

**The contrast with $M_4$.** $M_4$ has four carriers and the module $V_{3/2}$ is not among them, so one of the four rows of the family behaves differently from the other three at the level of the module.

**The reading.** The odd rows are the rows in which the algebra and the module live in the same list.

## Summary

For odd $n$ the principal copy factors through $SO(3)$, every label is an integer, and the module's carrier is a summand of the algebra. The rows $n=3$ and $n=5$ have carrier lists $5+3+1$ and $9+7+5+3+1$, module labels $1$ and $2$, and Casimir spectra $0,2,6$ and $0,2,6,12,20$. The even rows have half-integer module labels, the faithful copy, and no module carrier inside the algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(-1)^{n-1}$ | the image of $-\mathrm I$ in the principal copy |
| $5+3+1$ | the carrier dimensions at $n=3$ |
| $9+7+5+3+1$ | the carrier dimensions at $n=5$ |
| $V_1$, $V_2$ | the module's carriers at $n=3$, $n=5$ |
| $36$, $300$ | the weighted Casimir sums, equal to $\tfrac{n^2(n^2-1)}{2}$ |

## Further Reading
- [The Spin Decomposition of $M_n(\mathbb{C})$: $n$ Carriers, One for Each Spin from $0$ to $n-1$](the-spin-decomposition-of-mnc.html), for the general theorem.
- [Integer Labels on the Algebra, a Half-Integer on the Module: The Carrier Condition](integer-labels-on-the-algebra-a-half-integer-on-the-module.html), for the parity argument in full.
- [The Spin Content of $M_4(\mathbb{C})$](the-spin-content-of-m4c.html), for the even row $n=4$.
- [The $SU(2)$ of $M_n(\mathbb{C})$ Acting on $n^2$ Dimensions](the-su2-of-mnc-acting-on-n-squared-dimensions.html), for the real action.
- [The Carriers, the Closures and the Spin of $M_n(\mathbb{C})$](the-carriers-the-closures-and-the-spin-of-mnc.html), for the counts.
- [The Spin-One Carrier of $M_n(\mathbb{C})$: the Three-Dimensional $V_1$](the-spin-one-carrier-of-mnc.html), for the carrier that is the module at $n=3$.
