# __The Two-Parameter Gauge of $M_3(\mathbb{C})$__

## Introduction

A frame of $M_{3}(\mathbb{C})$ has three diagonal idempotents and six off-diagonal units. The idempotents are fixed by the root; the off-diagonal units are fixed only up to rescalings that preserve the matrix-unit table. The rescalings are

$$
E_{ij}\longmapsto\frac{t_{i}}{t_{j}}E_{ij},\qquad t_{i}\in\mathbb{C}^{\times},
$$

and the common scalar of the three $t_{i}$ acts trivially, so the effective group is $(\mathbb{C}^{\times})^{2}$. Its two parameters are $\lambda_{1}=t_{1}/t_{2}$ and $\lambda_{2}=t_{2}/t_{3}$; the third ratio is the product $\lambda_{1}\lambda_{2}$, and there is no third independent scalar. The idempotents do not depend on $\lambda_{1},\lambda_{2}$.

This article reads the gauge on the Peirce coordinates, identifies the gauge-invariant combinations of the off-diagonal entries, proves that the Peirce table is unchanged, compares the two-parameter gauge with the single $\lambda$ of the biquaternion algebra, and separates the gauge from the global phase of a quantum state. The frame and the simple nilpotents are *The Frame, the Simple Nilpotents and the Gauge of $M_3(\mathbb{C})$*; the Peirce decomposition is *The Peirce Decomposition of $M_{3}(\mathbb{C})$*; the corner is *The $M_{2}$ Corner of $M_{3}(\mathbb{C})$*.

## The Gauge on the Peirce Coordinates

**The frame change.** Let $E_{ij}$ be a normalized frame, $E_{ij}E_{kl}=\delta_{jk}E_{il}$, $E_{ii}=P_{i}$. For $t_{1},t_{2},t_{3}\in\mathbb{C}^{\times}$ put

$$
E_{ij}'=\frac{t_{i}}{t_{j}}E_{ij}.
$$

Then $E_{ij}'E_{kl}'=\delta_{jk}E_{il}'$ and $E_{ii}'=E_{ii}$, so the $E_{ij}'$ are again a normalized frame with the same diagonal idempotents. The map $E_{ij}\mapsto E_{ij}'$ is the gauge transformation of *The Frame, the Simple Nilpotents and the Gauge of $M_3(\mathbb{C})$*, with $E_{ij}'=D E_{ij}D^{-1}$ for $D=\operatorname{diag}(t_{1},t_{2},t_{3})$.

**The coordinates.** Write an element as

$$
A=\sum_{i,j}\alpha_{ij}E_{ij}=\sum_{i,j}\alpha_{ij}'E_{ij}'.
$$

Since $E_{ij}'=(t_{i}/t_{j})E_{ij}$, the two coordinate arrays are related by

$$
\alpha_{ij}'=\frac{t_{j}}{t_{i}}\alpha_{ij}.
$$

The diagonal coordinates are invariant,

$$
\alpha_{11}'=\alpha_{11},\qquad \alpha_{22}'=\alpha_{22},\qquad \alpha_{33}'=\alpha_{33},
$$

and the off-diagonal ones transform by the six weights

$$
\alpha_{12}'=\lambda_{1}^{-1}\alpha_{12},\quad
\alpha_{23}'=\lambda_{2}^{-1}\alpha_{23},\quad
\alpha_{13}'=(\lambda_{1}\lambda_{2})^{-1}\alpha_{13},
$$

$$
\alpha_{21}'=\lambda_{1}\alpha_{21},\quad
\alpha_{32}'=\lambda_{2}\alpha_{32},\quad
\alpha_{31}'=\lambda_{1}\lambda_{2}\alpha_{31},
$$

where $\lambda_{1}=t_{1}/t_{2}$ and $\lambda_{2}=t_{2}/t_{3}$. The pattern is the root system $A_{2}$: the units $E_{12},E_{23},E_{13}$ carry the positive weights $1,1,2$ and the units $E_{21},E_{32},E_{31}$ carry the negative weights $-1,-1,-2$, with the composite $E_{13}$ carrying the sum $1+1=2$. The coordinates transform by the inverse weights, as the formulas above show.

**Worked example.** Take

$$
A=\begin{pmatrix}1&2&3\\4&5&6\\7&8&9\end{pmatrix}
$$

in the standard frame, and $\lambda_{1}=2$, $\lambda_{2}=3$, so $D=\operatorname{diag}(6,3,1)$. The coordinates become

$$
\alpha_{12}'=\frac{2}{2}=1,\quad
\alpha_{23}'=\frac{6}{3}=2,\quad
\alpha_{13}'=\frac{3}{6}=\frac12,
$$

$$
\alpha_{21}'=4\cdot2=8,\quad
\alpha_{32}'=8\cdot3=24,\quad
\alpha_{31}'=7\cdot6=42,
$$

while the diagonal $1,5,9$ is unchanged. The gauge is not a symmetry of the array of numbers; it is a change of the frame in which the array is read. The element $A$ itself is fixed.

**The inverse reading.** If instead one keeps the standard frame and conjugates the element, $A\mapsto DAD^{-1}$, the entries become

$$
(DAD^{-1})_{ij}=\frac{t_{i}}{t_{j}}a_{ij}=\lambda_{ij}a_{ij},
$$

which is the inverse of the transformation of the coordinates. The two readings are the two sides of the same change of frame: the frame is rescaled, or the element is conjugated. The gauge-invariant statements below are the same in either reading.

## The Gauge-Invariant Combinations

**The diagonal is invariant.** The three numbers $\alpha_{11},\alpha_{22},\alpha_{33}$ are unchanged. They are the values of the three idempotents on $A$:

$$
P_{i}AP_{i}=\alpha_{ii}P_{i}.
$$

The trace is $\alpha_{11}+\alpha_{22}+\alpha_{33}$, so it is invariant; the determinant is the determinant of the coordinate array, so it is invariant as well.

**The opposite-pair products are invariant.** The three products

$$
\alpha_{12}\alpha_{21},\qquad \alpha_{23}\alpha_{32},\qquad \alpha_{13}\alpha_{31}
$$

are unchanged by the gauge:

$$
\alpha_{12}'\alpha_{21}'=\frac{\alpha_{12}}{\lambda_{1}}\cdot\lambda_{1}\alpha_{21}=\alpha_{12}\alpha_{21},
$$

and similarly for the other two pairs. These are the **coherence entries** of the Peirce coordinates: for each pair of opposite lines, the product of the two coordinates is a gauge-invariant number. The product is the coefficient of $P_{i}$ in the square of the off-diagonal part, and it is the natural pairing of the line with its dual.

**The oriented three-cycles are invariant.** The products

$$
\alpha_{12}\alpha_{23}\alpha_{31},\qquad \alpha_{21}\alpha_{32}\alpha_{13}
$$

are also invariant:

$$
\alpha_{12}'\alpha_{23}'\alpha_{31}'=\frac{\alpha_{12}}{\lambda_{1}}\cdot\frac{\alpha_{23}}{\lambda_{2}}\cdot\lambda_{1}\lambda_{2}\alpha_{31}=\alpha_{12}\alpha_{23}\alpha_{31},
$$

and the other cycle is its opposite. The two cycles are the two orientations of the triangle $1\to2\to3\to1$; their product is the product of the three opposite-pair invariants.

**The invariant ring.** The gauge group $(\mathbb{C}^{\times})^{2}$ acts on the six off-diagonal coordinates with the six weights $\pm1,\pm1,\pm2$. The four invariant combinations

$$
\alpha_{12}\alpha_{21},\quad
\alpha_{23}\alpha_{32},\quad
\alpha_{13}\alpha_{31},\quad
\alpha_{12}\alpha_{23}\alpha_{31}
$$

generate the invariant ring; the second three-cycle is

$$
\alpha_{21}\alpha_{32}\alpha_{13}
=\frac{(\alpha_{12}\alpha_{21})(\alpha_{23}\alpha_{32})(\alpha_{13}\alpha_{31})}{\alpha_{12}\alpha_{23}\alpha_{31}}.
$$

The diagonal coordinates are additional invariants, independent of the gauge. The count of the off-diagonal invariants is $6-2=4$, matching the four generators; the ring has relations among them, but the four numbers are the gauge-invariant content of the six off-diagonal entries.

**The invariants are the data of the element.** Two coordinate arrays related by the gauge describe the same element $A$ in two frames. The invariants are the functions of $A$ that do not depend on the frame: the diagonal values, the three opposite-pair products and the two three-cycles. The off-diagonal entries themselves are not invariant, and no individual off-diagonal entry has a gauge-independent meaning.

## The Peirce Table Is Unchanged

**Theorem.** The gauge transformation preserves the Peirce lines, the Peirce table, the multiplication rule and the idempotents. It changes only the choice of the normalized matrix units inside the lines.

**Proof.** The lines are $A_{ij}=P_{i}M_{3}P_{j}$, defined by the idempotents, and the idempotents are fixed. The matrix units $E_{ij}$ and $E_{ij}'$ both lie in $A_{ij}$ and are both nonzero, so they differ by a scalar, which is $t_{i}/t_{j}$. The multiplication rule

$$
E_{ij}E_{kl}=\delta_{jk}E_{il}
$$

is preserved by the rescaling:

$$
E_{ij}'E_{kl}'=\frac{t_{i}}{t_{j}}\frac{t_{k}}{t_{l}}E_{ij}E_{kl}
=\delta_{jk}\frac{t_{i}}{t_{l}}E_{il}=\delta_{jk}E_{il}'.
$$

The structure constants of the algebra in the frame are the numbers $1$ and $0$ of this table, and they are unchanged. The gauge is exactly the freedom of choosing the normalized frame; it is not a change of the multiplication.

**The table in coordinates.** The product of two elements is

$$
AB=\sum_{i,j}\Bigl(\sum_{m}\alpha_{im}\beta_{mj}\Bigr)E_{ij}
=\sum_{i,j}\Bigl(\sum_{m}\alpha_{im}'\beta_{mj}'\Bigr)E_{ij}',
$$

because the coordinate arrays multiply by the same matrix product in either frame. The gauge is a change of basis of the coordinate space that preserves the matrix multiplication; it is the conjugation $\alpha'=T^{-1}\alpha T$ with $T=\operatorname{diag}(t_{1},t_{2},t_{3})$. Indeed $\alpha'_{ij}=(t_{j}/t_{i})\alpha_{ij}$. The product is preserved because conjugation by $T$ is an algebra automorphism of the array algebra. This is the coordinate form of the frame change.

**The gauge is an automorphism of the coordinate algebra.** The map $\alpha\mapsto T^{-1}\alpha T$ is an automorphism of $M_{3}(\mathbb{C})$; it is inner, given by the diagonal matrix $T$. The gauge group is the image of the diagonal torus in $PGL_{3}$, and its action on the coordinates is the adjoint action. The frame change and the coordinate conjugation are the same inner automorphism read in two ways.

## The Count and the Cocycle

**The gauge group.** The parameters $t_{1},t_{2},t_{3}$ and $ct_{1},ct_{2},ct_{3}$ give the same rescaling, so the effective group is

$$
(\mathbb{C}^{\times})^{3}/\mathbb{C}^{\times}\cong(\mathbb{C}^{\times})^{2},
$$

of complex dimension two. The two parameters are

$$
\lambda_{1}=\frac{t_{1}}{t_{2}},\qquad \lambda_{2}=\frac{t_{2}}{t_{3}},
\qquad
\frac{t_{1}}{t_{3}}=\lambda_{1}\lambda_{2}.
$$

The third ratio is not independent. If a rescaling $E_{ij}\mapsto\lambda_{ij}E_{ij}$ preserves the frame, the cocycle

$$
\lambda_{ij}\lambda_{jk}=\lambda_{ik},\qquad \lambda_{ii}=1,\qquad \lambda_{ji}=\lambda_{ij}^{-1}
$$

forces $\lambda_{ij}=t_{i}/t_{j}$ for $t_{i}=\lambda_{i0}$, so the solution space is exactly the two-parameter torus. In particular $\lambda_{13}=\lambda_{12}\lambda_{23}$: the composite carries the product.

**The count of the frame.** The frame has dimension $8$, the root orbit dimension $6$, and the gauge dimension $2$:

$$
8=6+2.
$$

The frame is a point of $PGL_{3}$, the root is a point of $PGL_{3}/T$, and the gauge is the torus $T\cong(\mathbb{C}^{\times})^{2}$. The count is the orbit-stabiliser count of *The Frame, the Simple Nilpotents and the Gauge of $M_3(\mathbb{C})$*.

**The composite is forced.** The simple nilpotents $E_{12},E_{23}$ carry $\lambda_{1},\lambda_{2}$; the composite $E_{13}=E_{12}E_{23}$ carries $\lambda_{1}\lambda_{2}$. There is no independent scalar $\lambda_{3}$ on $E_{13}$: the cocycle would fail unless $\lambda_{3}=\lambda_{1}\lambda_{2}$. The same holds for the opposite composite $E_{31}=E_{32}E_{21}$, which carries $\lambda_{1}^{-1}\lambda_{2}^{-1}$.

**The two parameters are the simple roots.** In the character lattice of the torus, the weights of $E_{12}$ and $E_{23}$ are the two simple roots $\alpha_{1},\alpha_{2}$ of $A_{2}$, and the weight of $E_{13}$ is the highest root $\alpha_{1}+\alpha_{2}$. The gauge parameters $\lambda_{1},\lambda_{2}$ are the values of the two simple roots; the composite value is their product. The gauge is the maximal torus of $PGL_{3}$, and the root system is the $A_{2}$ of *The Frame, the Simple Nilpotents and the Gauge of $M_3(\mathbb{C})$*.

## The Comparison with the Biquaternion Single $\lambda$

**In $M_{2}(\mathbb{C})$ the frame has one gauge parameter, not two.**

For the biquaternion algebra $\mathbb{B}\cong M_{2}(\mathbb{C})$, the frame is $E_{11},E_{22},E_{12},E_{21}$, and the gauge is

$$
E_{12}\longmapsto\mu E_{12},\qquad E_{21}\longmapsto\mu^{-1}E_{21},\qquad \mu\in\mathbb{C}^{\times}.
$$

The effective group is $(\mathbb{C}^{\times})^{2}/\mathbb{C}^{\times}\cong\mathbb{C}^{\times}$, of dimension one. The single parameter $\mu$ is the analogue of the product $\lambda_{1}\lambda_{2}$ of the $M_{3}$ gauge, but in $M_{2}$ there is no simple-root decomposition into two steps: the root system is $A_{1}$, with one node, and the one off-diagonal pair carries the one weight $\mu$.

**The comparison.**

- **$M_{2}$:** one idempotent pair, one off-diagonal pair, one gauge parameter $\mu$, one invariant $\alpha_{12}\alpha_{21}$.
- **$M_{3}$:** three idempotents, three off-diagonal pairs, two gauge parameters $\lambda_{1},\lambda_{2}$, and the composite pair carries $\lambda_{1}\lambda_{2}$.
- **The pattern:** for $M_{n}(\mathbb{C})$ the gauge is $(\mathbb{C}^{\times})^{n-1}$; the count is the number of simple roots of $A_{n-1}$, which is $n-1$. The biquaternion case is $n=2$, one parameter; the $M_{3}$ case is $n=3$, two parameters.

**The single $\lambda$ of $\mathbb{B}$ is not a third parameter of $M_{3}$.** The biquaternion $\mu$ and the $M_{3}$ pair $(\lambda_{1},\lambda_{2})$ are the gauge groups of two different frames. In $M_{3}$ the composite carries the product; in $M_{2}$ there is no composite. The two-parameter gauge of $M_{3}$ reduces to the one-parameter gauge of $M_{2}$ only after a degeneration in which one of the two simple nilpotents is set to zero; the remaining parameter is then the single $\lambda$ of the biquaternion corner. This degeneration is the subject of *The $M_{2}$ Corner of $M_{3}(\mathbb{C})$*.

## The Gauge Is Not a Physical Phase

**The gauge is an algebraic redundancy of the frame; the global phase is a redundancy of a vector.**

The gauge group $(\mathbb{C}^{\times})^{2}$ acts on the frame by $E_{ij}\mapsto(t_{i}/t_{j})E_{ij}$. It fixes the idempotents, the root, the spectrum, the trace, the determinant and the characteristic polynomial. It is a change of the matrix units, not a change of the element. A physical global phase $e^{i\theta}$ acts on a vector $\psi\in\mathbb{C}^{3}$ by $\psi\mapsto e^{i\theta}\psi$; it is a one-parameter group $U(1)$, and it does not act on the frame in the same way. The two groups act on different spaces and have different dimensions.

**The gauge is complex.** The parameters $t_{i}$ are nonzero complex numbers, not phases. The gauge rescales the off-diagonal entries by complex numbers, including their moduli. The compact real form of the gauge is $U(1)^{2}$, the group of relative phases of the three lines; the diagonal factor $U(1)$ of $U(1)^{3}$ acts trivially on the frame ratios $t_{i}/t_{j}$ and is divided out. This diagonal factor is the algebraic analogue of the global phase of a vector, but it is not the same action: the global phase multiplies a vector of $\mathbb{C}^{3}$, while the diagonal frame rescaling multiplies the matrix units. The two are distinct one-parameter groups acting on different spaces, and the article does not identify them.

**The gauge does not change the state.** A density matrix $\rho$ written in the frame has off-diagonal entries that rescale under the gauge; the diagonal entries and the products of opposite coherences are invariant. The physical state is the element $\rho$, not its coordinate array; the gauge is the freedom of the frame in which the array is written. The global phase of a pure state is the freedom of the vector, not of the frame. The two freedoms are distinct, and the article keeps them distinct.

## Summary

The gauge of the $M_{3}$ frame is

$$
\boxed{\;E_{ij}\longmapsto\frac{t_{i}}{t_{j}}E_{ij},\qquad
(t_{1},t_{2},t_{3})\in(\mathbb{C}^{\times})^{3}/\mathbb{C}^{\times}\cong(\mathbb{C}^{\times})^{2},\;}
$$

with the two parameters

$$
\lambda_{1}=\frac{t_{1}}{t_{2}},\qquad \lambda_{2}=\frac{t_{2}}{t_{3}},\qquad \lambda_{3}=\lambda_{1}\lambda_{2}.
$$

It fixes the idempotents, the root, the trace, the determinant and the spectrum. On the Peirce coordinates it acts by $\alpha_{ij}\mapsto(t_{j}/t_{i})\alpha_{ij}$; the diagonal entries and the products $\alpha_{12}\alpha_{21}$, $\alpha_{23}\alpha_{32}$, $\alpha_{13}\alpha_{31}$ and the three-cycles are invariant. The Peirce table and the multiplication rule are unchanged: the gauge is the freedom of the normalized frame, not a change of the algebra.

| Quantity | Value for $M_{3}(\mathbb{C})$ |
|---|---|
| Gauge group | $(\mathbb{C}^{\times})^{2}$ |
| Parameters | $\lambda_{1},\lambda_{2}$ |
| Composite rescaling | $\lambda_{1}\lambda_{2}$ |
| Third independent scalar | none |
| Idempotents depending on the gauge | none |
| Frame dimension | $8$ |
| Root orbit dimension | $6$ |
| Gauge dimension | $2$ |
| Biquaternion gauge | one parameter $\mu$ |

The single $\lambda$ of the biquaternion algebra is the $n=2$ case of the pattern $(\mathbb{C}^{\times})^{n-1}$; the $M_{3}$ case has two parameters because the root system $A_{2}$ has two simple roots. The gauge is not the global phase of a quantum state: it is a complex two-parameter redundancy of the frame, whose compact form is $U(1)^{2}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $t_{i}$ | the three gauge parameters, modulo a common scalar |
| $\lambda_{1}=t_{1}/t_{2}$ | the gauge parameter on $E_{12}$ |
| $\lambda_{2}=t_{2}/t_{3}$ | the gauge parameter on $E_{23}$ |
| $\lambda_{3}=\lambda_{1}\lambda_{2}$ | the forced parameter on $E_{13}$ |
| $\alpha_{ij}$ | the Peirce coordinates |
| $\alpha_{ij}'$ | the coordinates after the gauge |
| $\mu$ | the single gauge parameter of the biquaternion frame |

## Further Reading

- [The Frame, the Simple Nilpotents and the Gauge of $M_3(\mathbb{C})$](the-frame-the-simple-nilpotents-and-the-gauge-of-m3c.html), for the frame, the nilpotents and the cocycle.
- [The Peirce Decomposition of $M_3(\mathbb{C})$](the-peirce-decomposition-of-m3c.html), for the Peirce coordinates and the table.
- [The $M_2$ Corner of $M_3(\mathbb{C})$](the-m2-corner-of-m3c.html), for the biquaternion corner and its single parameter.
- [Roots of Unity and the Lagrange Idempotents of $M_3(\mathbb{C})$](roots-of-unity-and-the-lagrange-idempotents-of-m3c.html), for the root and the idempotents that the gauge fixes.
- [The Peirce Decomposition of the Biquaternion Algebra](the-peirce-decomposition-of-the-biquaternion-algebra.html), for the single $\mu$ of the biquaternion frame.
- [The Involution and the Hermitian Structure of $M_3(\mathbb{C})$](the-involution-and-the-hermitian-structure-of-m3c.html), for the compact real form and the global phase.
