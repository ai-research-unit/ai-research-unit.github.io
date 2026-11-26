# __The Lengths of the Standard Endomorphisms of the Biquaternion Algebra: One, Two, Three and Four in $M_2(\mathbb{C})$__

## Introduction

**The question.** The length of an endomorphism is the least number of two-sided products $X\mapsto AXB$ whose sum it is, and it is the rank of the coefficient array. This article computes that number for every standard operator of the display: the products, the sums of a left and a right actor, the diagonal scalings, the reflections, the transpositions and the permutations of the four units.

**Why it is the same statement.** This is the in-depth matrix reading of [The Lengths of the Standard Endomorphisms of the Biquaternion Algebra: One, Two, Three and Four](the-lengths-of-the-standard-endomorphisms-of-the-biquaternion-algebra.html). The source computes the array of each named operator in the basis of products of the units; the display computes the same arrays as $4\times4$ Kronecker products and reads the same ranks. The statements are the same statements, and only the writing is new.

**What the article proves.** In this order. The array rule is recalled in one display. The length-one class is the class of products, and it includes the identity, both one-sided families, the Hermitian pair, the adjoint action, the complex structure and the Peirce corners. A sum of a left and a right actor has length two unless a multiplier is central, and this covers the commutator, the Jordan product and the sums of corners. The diagonal scalings obey a closed rule: their array is diagonal and its four entries are the signed averages of the eigenvalue vector. The reflections, the coordinate projections, the odd permutations and the generic operator have length four, and the even permutations have length one. The length is not a function of the operator rank.

**What the article does not do.** It does not prove the length theorem, which is [The Length of an Endomorphism of the Biquaternion Algebra: Four Two-Sided Products in $M_2(\mathbb{C})$](the-length-of-an-endomorphism-of-the-biquaternion-algebra-in-m2c.html); it does not treat the singular decomposition, which is [The SVD Decomposition of Endomorphisms of the Biquaternion Algebra in $M_2(\mathbb{C})$](the-svd-decomposition-of-endomorphisms-of-the-biquaternion-algebra-in-m2c.html); and it does not treat the transpose as a rule, which is [The Transposition of the Two Sides in $M_2(\mathbb{C})$](the-transposition-of-the-two-sides-in-m2c.html).

**Conventions.** The display is $\mathsf M_2(\tilde Q)=Q_t\mathrm I_2-i(Q_x\sigma_1+Q_y\sigma_2+Q_z\sigma_3)$, with $N(\tilde Q)=\det A$. The units are $E_t=\mathrm I_2$, $E_x=-i\sigma_1$, $E_y=-i\sigma_2$, $E_z=-i\sigma_3$. The products are $T_{\mu\nu}(X)=E_\mu XE_\nu$, and the coefficient array is $c(M)_{\mu\nu}=\tfrac14\operatorname{tr}(T_{\mu\nu}^{\dagger}M)$. The arrays are those of the axis-free frame, by the canonical privilege of [The Axis-Free $4\times4$ Representation : Operators](m4c-axis-free-representation-operators.html); the Pauli arrays are a translation.

**Boundaries.** The cone of products and its geometry are [Operators Acting on Two Sides in $M_2(\mathbb{C})$](operators-acting-on-two-sides-in-m2c.html). The Hermitian pair is [The Hermitian Pair of Operators Acting on Two Sides in $M_2(\mathbb{C})$](the-hermitian-pair-of-operators-acting-on-two-sides-in-m2c.html). The derivation as a Sylvester operator belongs to the Sylvester article of the category. The $n=2$ spine is [The One-Sided Operators at $n=2$](the-one-sided-operators-at-n-2.html) and [The Two-Sided Operators and the Segre Cone at $n=2$](the-two-sided-operators-and-the-segre-cone-at-n-2.html), and the display is [$M_2(\mathbb{C})$ Pauli Representation : Operators](m2c-pauli-representation-operators.html).

**Letters.** $D_a$ is the diagonal scaling with coordinate vector $a=(a_t,a_x,a_y,a_z)$, and $b=(b_t,b_x,b_y,b_z)$ are its four signed averages. $c_A$ is the coefficient vector of an element. $P_1,P_2$ are the two complementary diagonal idempotents of $M_2(\mathbb{C})$.

## The Array Rule

**One display.** For an endomorphism $M$ of $M_2(\mathbb{C})$,
$$
c(M)_{\mu\nu}=\tfrac14\operatorname{tr}\bigl(T_{\mu\nu}^{\dagger}M\bigr),\qquad \ell(M)=\operatorname{rank}c(M),
$$
and the array of a product is an outer product,
$$
c\bigl(L_AR_B\bigr)_{\mu\nu}=c_{A,\mu}c_{B,\nu}.
$$

**The reading.** A product has length one whatever its operator rank, and a sum of $k$ products has an array of rank at most $k$. Every length below is the rank of one of these arrays.

**The frame.** The arrays are written in the basis of products of the units in the order $(t,x,y,z)$. A change of basis acts on the two slots by invertible factors and preserves the rank, so the lengths are frame-free.

## Length One: The Products

**The class.**

| operator | definition | array | operator rank |
|---|---|---|---|
| the identity | $X\mapsto X$ | $c_{\mathrm I}c_{\mathrm I}^{\mathsf T}$ | $4$ |
| a left actor | $X\mapsto AX$ | $\mathrm I_2\otimes A=c_Ac_{\mathrm I}^{\mathsf T}$ | $0,2,4$ |
| a right actor | $X\mapsto XB$ | $B^{\mathsf T}\otimes\mathrm I_2=c_{\mathrm I}c_B^{\mathsf T}$ | $0,2,4$ |
| a product | $X\mapsto AXB$ | $c_Ac_B^{\mathsf T}$ | $0,1,2,4$ |
| the Hermitian pair | $X\mapsto AXA^{\dagger}$ | $c_Ac_{A^{\dagger}}^{\mathsf T}$ | $0,1,4$ |
| the adjoint action | $X\mapsto AXA^{-1}$ | $c_Ac_{A^{-1}}^{\mathsf T}$ | $4$ |
| the complex structure | $X\mapsto iX$ | $c_{i\mathrm I}c_{\mathrm I}^{\mathsf T}$ | $4$ |
| a Peirce corner | $X\mapsto P_iXP_j$ | $c_{P_i}c_{P_j}^{\mathsf T}$ | $0,1$ |
| a one-sided Peirce projection | $X\mapsto XP_j$ | $c_{\mathrm I}c_{P_j}^{\mathsf T}$ | $0,2$ |

**Why every row is one.** Each row is a product, and the array of a product is an outer product of rank one unless a multiplier vanishes. The Hermitian pair is a product because its second slot is the fixed matrix $A^{\dagger}$; the star is applied to the parameter and not to the variable, so the operator is complex-linear.

**The adjoint action and the frame group.** $\mathrm{Ad}_A$ has an array of rank one and operator rank four. The two numbers answer different questions, and length one does not imply invertibility. The Peirce frame group, the rescaling $E_{ij}\mapsto(t_i/t_j)E_{ij}$, is conjugation by $t_1P_1+t_2P_2$, which is the one-parameter diagonal torus inside the adjoint action.

**The corner maps.** With $P_1=\operatorname{diag}(1,0)$ and $P_2=\operatorname{diag}(0,1)$, the corner map $X\mapsto P_iXP_j$ reads one entry of the matrix and is a projection of rank one. It is a single product, and the four corners sum to the identity, also of length one.

**Length one is not invertibility.** A product of two rank-one matrices has operator rank one and length one, while the quaternion conjugation is invertible and has length four.

## Length Two: One Left and One Right

**The proposition.** For $A,B$ with $L_A+R_B\neq0$, the length of $X\mapsto AX+XB$ is two unless $A$ or $B$ is central, in which case it is one.

*Proof.* The array is $c_Ac_{\mathrm I}^{\mathsf T}+c_{\mathrm I}c_B^{\mathsf T}$, of rank one exactly when $c_A$ is proportional to $c_{\mathrm I}$ or $c_B$ is, that is when $A$ or $B$ is a scalar. The numerical rank on random non-central pairs is two.

**The commutator.** $\operatorname{ad}_A(X)=AX-XA$ has the array $c_Ac_{\mathrm I}^{\mathsf T}-c_{\mathrm I}c_A^{\mathsf T}$, of rank two for non-central $A$, with residual $10^{-16}$ and rank two exactly. Its operator rank is two, and the derivations of $M_2(\mathbb{C})$ are inner, so this form runs over every derivation.

**The Jordan product.** $\tfrac12(AX+XA)$ has the same length, two, for non-central $A$.

**The sums of corners.** $X\mapsto P_1XP_1+P_2XP_2$ has the array $E_{11}+E_{22}$, of rank two, so its length is two. The sum of three corners has the array $E_{11}+E_{12}+E_{21}$, of rank two, so its length is two although its operator rank is three.

**The class is a space.** The map $(A,B)\mapsto L_A+R_B$ is linear with a one-dimensional kernel spanned by $(\mathrm I_2,-\mathrm I_2)$, so the class is a seven-dimensional subspace of the sixteen-dimensional ambient, and its length-one members are the two faces where a multiplier is central.

## The Diagonal Scalings

**The family.** For a coordinate vector $a$, let
$$
D_a(X)=\sum_\mu a_\mu x_\mu E_\mu,\qquad X=\sum_\mu x_\mu E_\mu .
$$
The identity is $D_{(1,1,1,1)}$, the quaternion conjugation is $D_{(1,-1,-1,-1)}$, the projection onto the coordinate line $\mathbb{C}E_\mu$ is $D_{\mathbf e_\mu}$, and the truncation to a set $S$ is $D_{\mathbf 1_S}$.

**Theorem (the array of a scaling).** The array of $D_a$ is diagonal, with the entries
$$
b_t=\tfrac14(a_t+a_x+a_y+a_z),\quad
b_x=\tfrac14(-a_t-a_x+a_y+a_z),\quad
b_y=\tfrac14(-a_t+a_x-a_y+a_z),\quad
b_z=\tfrac14(-a_t+a_x+a_y-a_z),
$$
and $\ell(D_a)$ is the number of nonzero entries. The residual of the array identity on random $a$ is $2\cdot10^{-16}$.

*Proof.* The four diagonal products $T_{\mu\mu}$ have the eigenvalue vectors $v_t=(1,1,1,1)$, $v_x=(-1,-1,1,1)$, $v_y=(-1,1,-1,1)$, $v_z=(-1,1,1,-1)$, pairwise orthogonal with squared norm four. Expanding $a$ in this orthogonal basis gives $D_a=\tfrac14\sum_\mu(v_\mu\cdot a)T_{\mu\mu}$, and the array of $T_{\mu\mu}$ is the unit array $E_{\mu\mu}$.

**The named cases.**

| operator | $a$ | $b$ | length |
|---|---|---|---|
| the identity | $(1,1,1,1)$ | $(1,0,0,0)$ | $1$ |
| the quaternion conjugation | $(1,-1,-1,-1)$ | $-\tfrac12(1,1,1,1)$ | $4$ |
| the sign flip of $\vec e_y$, the transpose | $(1,1,-1,1)$ | $\tfrac12(1,-1,1,-1)$ | $4$ |
| the projection onto $\mathbb{C}e_t$ | $(1,0,0,0)$ | $\tfrac14(1,-1,-1,-1)$ | $4$ |
| the truncation to $\{t,x\}$ | $(1,1,0,0)$ | $\tfrac12(1,-1,0,0)$ | $2$ |
| the truncation to $\{t,x,y\}$ | $(1,1,1,0)$ | $\tfrac14(3,-1,-1,1)$ | $4$ |
| $D_{(1,2,3,4)}$ | $(1,2,3,4)$ | $(\tfrac52,1,\tfrac12,0)$ | $3$ |
| $D_{(1,2,3,5)}$ | $(1,2,3,5)$ | $(\tfrac{11}4,\tfrac54,\tfrac34,-\tfrac14)$ | $4$ |

**The short scalings.** A scaling has length one exactly when three of its four averages vanish, and those vectors are the four rays of $v_\mu$, that is the four diagonal products. Every other scaling has length two, three or four.

**Where three comes from.** $\ell(D_a)=3$ is the vanishing of exactly one average, a hyperplane in $a$. The vector $(1,2,3,4)$ lies on $b_z=0$, since $-1+2+3-4=0$.

**The eigenvalues do not give the length.** $(1,2,3,4)$ has four distinct nonzero eigenvalues and length three; the conjugation has two eigenvalues and length four.

**The truncations.** A truncation to $k$ coordinates has length $4,2,4,1$ for $k=1,2,3,4$, for every choice of the set.

## Length Four: The Reflections

**The criterion.** An operator has length four exactly when $\det c(M)\neq0$, since length at most three is the single condition $\det c=0$. The length-four operators are the complement of a hypersurface.

**The quaternion conjugation.** The complex-linear map $X\mapsto\operatorname{tr}(X)\mathrm I_2-X$ is $D_{(1,-1,-1,-1)}$, of length four, and
$$
\operatorname{tr}(X)\mathrm I_2-X=-\tfrac12\sum_{\mu}T_{\mu\mu},
$$
so its array is $-\tfrac12\mathrm I_4$. The two readings agree because the four diagonal products are the four entries of the array.

**The sign flips.** A sign flip of one imaginary coordinate is $D_{(1,1,-1,1)}$ for $\vec e_y$, of length four, and the same for $\vec e_x$ and $\vec e_z$. The flip of all three is the conjugation, also of length four.

**The transposes.** The transpose of the display fixes $E_t,E_x,E_z$ and negates $E_y$, so it is the sign flip of $\vec e_y$, of length four, with the array $\tfrac12\operatorname{diag}(1,-1,1,-1)$.

**The coordinate projections.** The projection onto the line $\mathbb{C}E_\mu$ is $D_{\mathbf e_\mu}$, of length four, for every $\mu$ including $\mu=t$.

**The permutations, and the parity that decides.** A permutation of the four units is a linear map fixing the coordinate vector, and its array has determinant $\pm\tfrac1{16}$.

No product has operator determinant $-1$. The determinant of a product is
$$
\det\bigl(L_AR_B\bigr)=\det\bigl(B^{\mathsf T}\otimes A\bigr)=\bigl(\det A\,\det B\bigr)^{2},
$$
verified to $7\cdot10^{-16}$ on random pairs, so it is a square. An odd permutation has determinant $-1$ and is therefore not a product.

**The odd permutations.** One representative of each conjugacy class of odd permutations suffices:
$$
\tfrac12\begin{pmatrix}1&0&0&0\\0&-1&0&0\\0&0&0&-1\\0&0&-1&0\end{pmatrix}\quad(y\ z),\qquad
\tfrac12\begin{pmatrix}0&0&-1&0\\0&0&0&-1\\0&-1&0&0\\1&0&0&0\end{pmatrix}\quad(t\ z\ x\ y),
$$
both of rank four, both computed exactly.

**The even permutations.** Two factorisations, each a lookup in the multiplication table, generate the alternating group. With $\epsilon=\tfrac12(\mathrm I_2+E_x+E_y+E_z)$,
$$
(x\ y\ z)=L_\epsilon R_{\epsilon^{-1}},\qquad (t\ x)(y\ z)=-L_{E_z}R_{E_y},
$$
verified to $10^{-16}$ and $8\cdot10^{-17}$. The first has the rank-one array $\tfrac14\mathbf 1\,\mathbf u^{\mathsf T}$ with $\mathbf u=(1,-1,-1,-1)$, the second the rank-one array with the single entry $-1$ in the row $z$ and the column $y$.

**The count.** The twelve even permutations have length one and the twelve odd ones have length four. The six transpositions are the odd ones of order two.

**The generic operator.** A generic endomorphism has length four, a generic product has length one, and a generic sum of a left and a right actor has length two.

## The Same Rank, Three Lengths

**The table.**

| operator | operator rank | length |
|---|---|---|
| the corner $X\mapsto P_1XP_1$ | $1$ | $1$ |
| the truncation to one coordinate | $1$ | $4$ |
| the Peirce projection $X\mapsto XP_1$ | $2$ | $1$ |
| the truncation to two coordinates | $2$ | $2$ |
| the sum of three corners | $3$ | $2$ |
| the truncation to three coordinates | $3$ | $4$ |
| the identity | $4$ | $1$ |

**Two rank-one projections of lengths one and four.** The corner map onto the Peirce line is a single product; the coordinate projection onto $\mathbb{C}E_t$ is $D_{\mathbf e_t}$, of length four. Both are idempotent and both have rank one; the difference is the shape of the array.

**The truncations.** The pattern is $4,2,4,1$ for ranks one to four, read from the four signed averages of the indicator vector.

**A sum of two long operators can be short.** The truncation to $\{t,x\}$ is the sum of the truncations to $\{t\}$ and to $\{x\}$, and its length is two while each summand has length four.

**The corners.** Each corner has length one, a partial sum of two or three corners has length two, and the sum of all four is the identity, of length one.

## The Strata and the Named Operators

**The strata.** The operators of length at most $r$ are the arrays of rank at most $r$, of complex dimension $8r-r^{2}$, so the ladder is $0,7,12,15,16$.

| $r$ | the named operators of length exactly $r$ |
|---|---|
| $0$ | the zero operator |
| $1$ | the identity, $L_A$, $R_B$, $L_AR_B$, the Hermitian pair, $\mathrm{Ad}_A$, $i\,\cdot$, the Peirce corners, the even permutations |
| $2$ | $L_A+R_B$, the derivations, the Jordan products, the sums of two and of three corners, the truncations to two coordinates |
| $3$ | the diagonal scalings with exactly one vanishing average, such as $D_{(1,2,3,4)}$ |
| $4$ | the quaternion conjugation, the sign flips, the odd permutations, the transpose, the coordinate projections, the truncations to one and to three coordinates, the generic operator |

**The classes are not the strata.** The length-one stratum is the cone of products of dimension seven, and the products with two invertible multipliers are its open dense part.

**The unlisted operators.** The matrix adjoint $A\mapsto A^{\dagger}$ is conjugate-linear and has no length in this sense; it belongs to the antilinear family $\{T_{\mu\nu}J\}$.

## Where $n=2$ Differs

**The array.** At $n=2$ every array is $4\times4$ and the four averages are four numbers. At order $n$ the array is $n^2\times n^2$, the diagonal scalings have $n^2$ averages, and the truncation pattern has $n^2+1$ values.

**The parity argument.** The determinant of a product is $\det(B^{\mathsf T}\otimes A)=(\det A\det B)^{n}$ at order $n$; at $n=2$ it is a square, which is what makes the parity argument work. At odd $n$ it is a cube and the argument is different.

**The $\pm1$ determinant.** At $n=2$ the operator determinant of a product is a square, so $\det=-1$ is out of reach and the odd permutations must have length four. That exact numerical coincidence is a property of the size two.

**Nothing else differs.** The length-one class, the length-two criterion, the rule for the diagonal scalings and the length four on the complement of the hypersurface hold at every order.

## Summary

The length of every standard operator of the display is the rank of its coefficient array. A product has length one whatever its operator rank, and the class includes the identity, both one-sided actors, the Hermitian pair, the adjoint action, the complex structure, the corner maps and the even permutations of the units.

A sum of a left and a right actor has length two unless a multiplier is central, and this covers the commutator $AX-XA$, the Jordan product, and the sums of two and of three corners, the last with operator rank three.

A diagonal scaling has a diagonal array whose four entries are the signed averages of its coordinate vector, and its length is the number of nonzero averages. The identity is the only scaling of length one apart from the three other diagonal products; $D_{(1,2,3,4)}$ has length three on the hyperplane $b_z=0$; the conjugation, the transpositions, the coordinate projections and the truncations to one and to three coordinates have length four.

The length is not a function of the operator rank: the two rank-one projections have lengths one and four, the truncations of ranks one to four have lengths $4,2,4,1$, and a sum of two operators of length four can have length two. The parity of a permutation of the units decides its length, because a product has a square operator determinant and an odd permutation has determinant $-1$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $c(M)$ | the coefficient array in the sixteen products |
| $\ell(M)$ | the length, the least number of products |
| $D_a$ | the diagonal scaling with coordinate vector $a$ |
| $b_t,b_x,b_y,b_z$ | the four signed averages of $a$ |
| $P_1,P_2$ | the two complementary diagonal idempotents |
| $T_{\mu\nu}$ | $L_{E_\mu}R_{E_\nu}$ |

## Further Reading

- [The Lengths of the Standard Endomorphisms of the Biquaternion Algebra: One, Two, Three and Four](the-lengths-of-the-standard-endomorphisms-of-the-biquaternion-algebra.html), for the source tables and the parity argument.
- [The Length of an Endomorphism of the Biquaternion Algebra: Four Two-Sided Products in $M_2(\mathbb{C})$](the-length-of-an-endomorphism-of-the-biquaternion-algebra-in-m2c.html), for the theorem that the length is the array rank.
- [Operators Acting on Two Sides in $M_2(\mathbb{C})$](operators-acting-on-two-sides-in-m2c.html), for the cone of products.
- [The Transposition of the Two Sides in $M_2(\mathbb{C})$](the-transposition-of-the-two-sides-in-m2c.html), for the transpose as the sign flip of $\vec e_y$.
- [The Length and the Two Ranks at $n=2$](the-length-and-the-two-ranks-at-n-2.html), for the same counts in the regular representation.
