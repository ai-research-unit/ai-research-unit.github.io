# __The Column Ideals of a Matrix Ring: One Idempotent and \(n-1\) Nilpotents__

## Introduction

Let \(D\) be a division ring, let \(n \geq 1\), and let \(A = M_n(D)\). The \(j\)-th **column ideal** of \(A\) is the left ideal \(L_j = AE_{jj}\) of the matrices supported in the \(j\)-th column. It is a minimal left ideal, and its corner-adapted basis has a fixed shape: **exactly one idempotent and \(n-1\) nilpotents**. For \(n = 2\) this reads one idempotent and one nilpotent, which is the shape of the biquaternion spinor space \(S = \mathbb{C}\{\tilde\Pi_+,\vec\Upsilon_2\} = \mathbb{B}\tilde\Pi_+\); the general statement removes any appearance of coincidence from that shape.

The count is forced by the **Peirce decomposition** and by nothing else. The matrix units \(E_{11},\dots,E_{nn}\) are a complete orthogonal family of idempotents, and relative to that family the column \(L_j\) splits into \(n\) one-dimensional corners. One of them is the **diagonal** corner \(E_{jj}L_j = E_{jj}AE_{jj}\), a copy of the division ring \(D\), and it contains the idempotent \(E_{jj}\), which is the identity of that corner. The other \(n-1\) are the **off-diagonal** corners \(E_{ii}AE_{jj}\) with \(i \neq j\), and each of them is **square-zero**: the product of any two of its elements is zero. A nonzero square-zero element is a nilpotent and not an idempotent, so an off-diagonal corner contains no nonzero idempotent at all. A basis of the column with one element per corner therefore has exactly one idempotent and \(n-1\) nilpotents, and \(n-1\) is nothing but the number of off-diagonal corners of a column.

Two cautions belong to the statement, and both are made precise below. The count is a count of **basis elements of the corner-adapted basis**, and not of the idempotents of the ideal: those form an affine family \(E_{jj} + N_j\) of dimension \(n-1\) over \(D\), and a basis of the column can even be chosen all of whose elements are idempotents (§*The Corner-Adapted Basis Is Not Every Basis*). And the count needs a division ring: over a ring with a proper nonzero ideal the column need not be minimal and the corner argument does not apply (§*Where the Count Does Not Apply*).

The matrix units, the classification of the left ideals of \(M_n(R)\) and the case \(n = 2\) are *Matrix Algebras*; the Peirce decomposition and its product rule are *Unital Algebras*, §*Idempotents and the Peirce Decomposition*; ideals, idempotents and nilpotents are *Rings*; and the biquaternion instance is *Ideals and Peirce Decomposition of the Biquaternion Algebra*.

## Matrix Units, Corners and the Column Ideal

### The Matrix Units

**Definition.** For \(1 \leq i, j \leq n\) let \(E_{ij}\) be the matrix with a single \(1\) in position \((i,j)\) and zeros elsewhere. The **matrix units** \(E_{ij}\) form a \(D\)-basis of \(A\), and their product is

$$
E_{ij}E_{kl} = \delta_{jk}\,E_{il}, \qquad E_{jj}^2 = E_{jj}, \qquad E_{ij}^2 = 0 \ \ (i \neq j), \qquad \sum_{i=1}^{n} E_{ii} = I .
$$

So each diagonal unit \(E_{jj}\) is an idempotent and each off-diagonal unit is square-zero, and \(\dim_D A = n^2\). The multiplication table, the centre and the units are those of *Matrix Algebras*, §*Matrix Units* and §*Ideals and Simplicity*; the units of a division ring and the vocabulary of ideals, idempotents and nilpotents are *Rings*.

### The Column Ideal

**Definition.** The \(j\)-th **column ideal** of \(A\) is

$$
L_j = AE_{jj} = \left\{\textstyle\sum_{i=1}^{n} x_{ij}E_{ij} : x_{ij} \in D\right\},
$$

the set of matrices whose only possibly nonzero entries lie in the \(j\)-th column.

The name is exact: \(L_j\) is a left ideal, because \(A \cdot L_j \subseteq AE_{jj} = L_j\), and it is not a right ideal for \(n \geq 2\), because \(E_{ij}E_{jk} = E_{ik}\) carries the matrix unit \(E_{ij}\) of column \(j\) into column \(k \neq j\). The left ideals of \(M_n(k)\) over a field are exactly the sets of matrices whose columns lie in a fixed subspace, and the minimal ones are the columns, the set \(L_j = I_{V_j}\) with \(V_j = De_j\) in that article's notation; that classification is *Matrix Algebras*, §*Ideals and Simplicity*; the regular module is the direct sum \(\bigoplus_j L_j\) of the \(n\) columns, whose rank and length are *Direct Sums, Free Modules and Rank*.

### The Corners of the Algebra

The family \(E_{11},\dots,E_{nn}\) is complete and pairwise orthogonal, \(E_{ii}E_{kk} = \delta_{ik}E_{ii}\) and \(\sum_i E_{ii} = I\). The **Peirce decomposition** of \(A\) with respect to it is the direct sum of the \(n^2\) **corners**

$$
A = \bigoplus_{i,k=1}^{n} E_{ii}AE_{kk}, \qquad (E_{ii}AE_{kk})(E_{ll}AE_{mm}) \subseteq \delta_{kl}\,E_{ii}AE_{mm},
$$

the corners being the **Peirce spaces**. A corner \(E_{ii}AE_{kk}\) is a subalgebra with identity \(E_{ii}\) when \(i = k\), called **diagonal**, and only a bimodule over the two diagonal corners when \(i \neq k\), called **off-diagonal**. The decomposition, the directness and the product rule are *Unital Algebras*, §*Idempotents and the Peirce Decomposition*.

**Proposition (the corners are one-dimensional).** For all \(i, k\),

$$
E_{ii}AE_{kk} = DE_{ik} .
$$

*Proof.* Writing \(X = \sum_{p,q}x_{pq}E_{pq}\), the product of the two outer units is \(E_{ii}XE_{kk} = \sum_{p,q}x_{pq}E_{ii}E_{pq}E_{kk} = x_{ik}E_{ik}\), since \(E_{ii}E_{pq} = \delta_{ip}E_{iq}\) and \(E_{iq}E_{kk} = \delta_{qk}E_{ik}\). So a corner consists of the left multiples of one matrix unit by elements of \(D\).

## The Corner Decomposition of a Column

### The Column as a Sum of Its Corners

The column is cut by the same family, and the cut is the sum of its corners inside the column:

$$
L_j = AE_{jj} = \left(\sum_{i=1}^{n} E_{ii}\right) A E_{jj} = \bigoplus_{i=1}^{n} E_{ii}AE_{jj},
$$

using \(\sum_i E_{ii} = I\) and the directness of the Peirce decomposition. By §*The Corners of the Algebra* each summand is the line \(DE_{ij}\), so

$$
L_j = \bigoplus_{i=1}^{n} DE_{ij},
$$

a left \(D\)-module of dimension \(n\). The summand \(E_{jj}AE_{jj} = DE_{jj}\) is the **diagonal corner of the column**, and the \(n-1\) summands \(E_{ii}AE_{jj} = DE_{ij}\) with \(i \neq j\) are the **off-diagonal corners of the column**.

### The Diagonal Corner

**Proposition.** \(E_{jj}AE_{jj} = DE_{jj}\) is a division ring isomorphic to \(D\), with identity \(E_{jj}\).

*Proof.* By §*The Corners of the Algebra* the corner is \(DE_{jj}\), and \(D \to DE_{jj}\), \(d \mapsto dE_{jj}\), is a ring isomorphism: it is additive and bijective by definition of the line, it is multiplicative because \((dE_{jj})(d'E_{jj}) = dd'E_{jj}\), and it sends \(1\) to \(E_{jj}\). So the corner is a copy of the division ring \(D\).

The element \(E_{jj}\) is therefore the identity of the diagonal corner of the column, and it is the idempotent of the column's corner decomposition.

### The Off-Diagonal Corners Are Square-Zero

**Lemma (off-diagonal corners are square-zero).** Let \(e, f\) be orthogonal idempotents and let \(x = fae\) be an element of the off-diagonal corner \(fAe\). Then \(x^2 = 0\).

*Proof.* \(x^2 = (fae)(fae) = fa(ef)ae = 0\), because \(ef = 0\).

The lemma is the product rule of the Peirce decomposition read at an off-diagonal pair: for \(i \neq j\) one has \((E_{ii}AE_{jj})^2 \subseteq E_{ii}A(E_{jj}E_{ii})AE_{jj} = 0\).

**Corollary.** Every element of an off-diagonal corner of the column is square-zero, and hence a nilpotent; and an off-diagonal corner contains no nonzero idempotent.

*Proof.* The corner is \(DE_{ij}\) with \(i \neq j\) by §*The Corners of the Algebra*, and \((dE_{ij})^2 = d^2E_{ij}^2 = 0\) for every \(d\), since \(E_{ij}^2 = 0\) when \(i \neq j\). A nonzero square-zero element \(x\) satisfies \(x^2 = 0 \neq x\), so it is not idempotent.

The *normalisation* of the basis element is irrelevant here: every nonzero element of an off-diagonal corner is square-zero, not merely the matrix unit \(E_{ij}\) itself. This will matter in §*The Count*.

### The Column Is a Minimal Left Ideal

**Proposition.** Every nonzero element of \(L_j\) generates \(L_j\) as a left ideal, so \(L_j\) is a minimal left ideal of \(A\).

*Proof.* Let \(0 \neq x = \sum_i x_{ij}E_{ij} \in L_j\) and choose \(i_0\) with \(x_{i_0j} \neq 0\), possible because \(D\) has no zero divisors. For every \(i\),

$$
E_{ii_0}x = \sum_{k} x_{kj}E_{ii_0}E_{kj} = x_{i_0j}E_{ij},
$$

using \(E_{ii_0}E_{kj} = \delta_{i_0k}E_{ij}\). So every matrix unit \(E_{ij}\) of the column lies in the left ideal generated by \(x\), and with them every element of \(L_j\); since also \(x \in L_j\), that ideal is \(L_j\). A nonzero left ideal contained in \(L_j\) contains a nonzero \(x\) and therefore equals \(L_j\), so \(L_j\) has no nonzero proper left submodule and is minimal.

## The Count

### The Theorem

A \(D\)-basis \((x_1,\dots,x_n)\) of \(L_j\) is **corner-adapted** when its \(i\)-th element lies in the \(i\)-th corner of the column,

$$
x_i \in E_{ii}L_j = E_{ii}AE_{jj} = DE_{ij} \qquad (1 \leq i \leq n).
$$

**Theorem (one idempotent and \(n-1\) nilpotents).** Let \((x_1,\dots,x_n)\) be a corner-adapted basis of \(L_j\), so that \(x_i = c_iE_{ij}\) with \(0 \neq c_i \in D\). Then:

**(a)** for every \(i \neq j\) the element \(x_i = c_iE_{ij}\) is square-zero, hence a nilpotent, whatever the nonzero scalar \(c_i\);

**(b)** the diagonal element \(x_j = c_jE_{jj}\) is idempotent if and only if \(c_j = 1\), that is, if and only if it is normalised to the identity \(E_{jj}\) of the corner;

**(c)** in particular the **matrix-unit basis** \((E_{1j},\dots,E_{nj})\), the corner-adapted basis with \(c_i = 1\) for every \(i\), consists of exactly one idempotent, \(E_{jj}\), and \(n-1\) nilpotents, the off-diagonal units \(E_{ij}\).

*Proof.* (a) is the corollary of §*The Off-Diagonal Corners Are Square-Zero*, which holds for every nonzero scalar. (b) \((c_jE_{jj})^2 = c_j^2E_{jj}\) equals \(c_jE_{jj}\) exactly when \(c_j^2 = c_j\), and in a division ring the nonzero solutions are \(c_j = 1\). (c) Combine (a) and (b) with the fact that \(E_{jj}^2 = E_{jj}\) and that a corner-adapted basis has one element per corner, of which \(n-1\) are off-diagonal.

So the shape of the statement is invariant to the off-diagonal normalisation and needs the diagonal normalisation: the \(n-1\) off-diagonal basis elements are nilpotents as they stand, and the diagonal basis element is the idempotent exactly when it is the corner's identity.

### Why the Count Is Forced

The count is not a property of this or that basis element; it is the arithmetic of the column's corners. The Peirce decomposition of \(L_j\) has

- **one** diagonal corner, a copy of the division ring \(D\), whose identity \(E_{jj}\) is an idempotent;
- **\(n-1\)** off-diagonal corners, each square-zero, hence each devoid of nonzero idempotents.

A corner-adapted basis takes one element from each corner, so its \(n-1\) off-diagonal elements are nilpotents and at most one element, the diagonal one, can be idempotent; for the matrix-unit basis that element is \(E_{jj}\), and it is the only idempotent of that basis. Equivalently:

$$
1 \;(\text{diagonal corner}) \;+\; (n-1) \;(\text{off-diagonal corners}) \;=\; n \;=\; \dim_D L_j ,
$$

where \(n\) is also the length of the regular module over \(A\), the number of its simple summands \(A = \bigoplus_j L_j\). The number \(n-1\) is thus not a numerical accident but the number of off-diagonal corners of a column.

### The Nilpotents of the Column

The nilpotents of \(L_j\) are exactly the elements of its off-diagonal part, and each of them is square-zero. Let

$$
N_j = \bigoplus_{i \neq j} DE_{ij} \subseteq L_j
$$

be the **off-diagonal part** of the column, of dimension \(n-1\).

**Proposition.** For \(x = \sum_i x_{ij}E_{ij} \in L_j\) and every \(m \geq 1\), the coefficient of \(E_{ij}\) in \(x^m\) is \(x_{ij}x_{jj}^{m-1}\); consequently:

**(a)** \(x^2 = 0\) if and only if \(x_{jj} = 0\), that is, if and only if \(x \in N_j\) (the element \(0\) included);

**(b)** the nilpotent elements of \(L_j\) are exactly the elements of \(N_j\), and each of them is square-zero;

**(c)** \(N_j^2 = 0\).

*Proof.* Write \(x^m = \sum_i c_i^{(m)}E_{ij}\). From \((uv)_{ij} = u_{ij}v_{jj}\) for \(u, v \in L_j\), which follows because \(u_{im}\) vanishes unless \(m = j\) in the sum \((uv)_{ij} = \sum_m u_{im}v_{mj}\), the recursion \(c_i^{(m+1)} = c_i^{(m)}x_{jj}\) with \(c_i^{(1)} = x_{ij}\) gives \(c_i^{(m)} = x_{ij}x_{jj}^{m-1}\). (a) For \(m = 2\): \(x^2 = 0\) means \(x_{ij}x_{jj} = 0\) for every \(i\). If \(x_{jj} = 0\) this holds; if \(x_{jj} \neq 0\) then \(x_{ij} = 0\) for every \(i\), since \(D\) has no zero divisors, so \(x = 0\). (b) By (a), a nonzero \(x\) with \(x_{jj} = 0\) has \(x^2 = 0\), so it is nilpotent; and if \(x_{jj} \neq 0\) then every power has coefficient \(x_{ij}x_{jj}^{m-1}\), which vanishes for no \(m\) when some \(x_{ij} \neq 0\), so no power of a nonzero such \(x\) is zero. (c) Apply (a) to every element of \(N_j\).

**Corollary (the diagonal coefficient is a ring homomorphism).** The map

$$
\pi : L_j \to D, \qquad \pi(x) = x_{jj},
$$

is a surjective ring homomorphism with kernel \(N_j\) and \(\pi(E_{jj}) = 1\), so \(L_j/N_j \cong D\) and \(N_j\) is a square-zero two-sided ideal of \(L_j\), viewed as a ring under the inherited product. That ring has right identity \(E_{jj}\), since \(xE_{jj} = x\) for every \(x \in L_j\), and it has no two-sided identity for \(n \geq 2\), since \(E_{jj}x = x_{jj}E_{jj}\) fails to be \(x\) as soon as the diagonal coefficient of \(x\) is not \(1\).

*Proof.* The map is additive and \(\pi(xy) = (xy)_{jj} = x_{jj}y_{jj} = \pi(x)\pi(y)\), and \(\pi(E_{jj}) = 1\). Its kernel is the set of column elements with vanishing diagonal coefficient, which is \(N_j\) by definition.

### The Idempotents of the Column

The idempotents of \(L_j\) are not the single element \(E_{jj}\); they are an affine family.

**Proposition.** An element \(x \in L_j\) is idempotent if and only if \(x = 0\) or \(x = E_{jj} + \nu\) for some \(\nu \in N_j\). Equivalently, the idempotents of the column are the origin together with the affine space \(E_{jj} + N_j\), of dimension \(n-1\) over \(D\).

*Proof.* Let \(x = \sum_i x_{ij}E_{ij}\) satisfy \(x^2 = x\). By §*The Nilpotents of the Column* the coefficient of \(E_{ij}\) in \(x^2\) is \(x_{ij}x_{jj}\), so the equation reads \(x_{ij}x_{jj} = x_{ij}\) for every \(i\), and for \(i = j\), \(x_{jj}^2 = x_{jj}\), so \(x_{jj} \in \{0,1\}\) because \(D\) is a division ring. If \(x_{jj} = 0\) then \(x_{ij}x_{jj} = 0 = x_{ij}\) for every \(i\), so \(x = 0\). If \(x_{jj} = 1\) then \(x = E_{jj} + \nu\) with \(\nu = x - E_{jj} \in N_j\). Conversely, for \(\nu \in N_j\) one has \(E_{jj}\nu = \nu_{jj}E_{jj} = 0\), \(\nu E_{jj} = \nu\) and \(\nu^2 = 0\), so \((E_{jj}+\nu)^2 = E_{jj} + \nu\).

The family \(E_{jj} + N_j\) is a translate of the nilpotent subspace, so the idempotents of the column are as numerous as the elements of \(N_j \cong D^{n-1}\); in the biquaternion case \(n = 2\) they are the idempotents \(\tilde\Pi_+ + c\vec\Upsilon_2\) with \(c \in \mathbb{C}\).

### The Corner-Adapted Basis Is Not Every Basis

The count of §*The Theorem* is a statement about corner-adapted bases, and it should not be read as a statement about every basis of the column. Because the idempotents form the affine family \(E_{jj}+N_j\), a basis can be chosen from that family alone.

**Proposition (an idempotent basis).** For \(n \geq 2\) the \(n\) elements

$$
E_{jj}, \qquad E_{jj} + E_{ij} \quad (i \neq j),
$$

are idempotent and form a \(D\)-basis of \(L_j\). So a basis of the column can consist entirely of idempotents.

*Proof.* Each \(E_{ij}\) with \(i \neq j\) lies in \(N_j\), so \(E_{jj}+E_{ij}\) is idempotent by §*The Idempotents of the Column*. The \(n\) elements are linearly independent: their coefficients in the basis \((E_{1j},\dots,E_{nj})\) are the rows of the matrix that is the identity except that its \(j\)-th column is filled with ones, whose determinant is \(1\). So they are a basis.

So "one idempotent and \(n-1\) nilpotents" is a statement about the **corner-adapted** basis, the basis with one element per Peirce corner, and it is that basis which the physical spinor statements use: the biquaternion spinor space is presented on \((\tilde\Pi_+,\vec\Upsilon_2)\), not on \((\tilde\Pi_+, \tilde\Pi_+ + \vec\Upsilon_2)\). What the theorem asserts is that the \(n-1\) off-diagonal elements of a corner-adapted basis are nilpotents for every normalisation, and that such a basis never has two idempotents, having exactly one, namely \(E_{jj}\), when its diagonal element is the identity of its corner.

## The Counts Tabulated

### One Column

The corners of a column, with what each contributes. Every entry is a count of basis elements of the corner-adapted basis.

| corner of the column | number | contents | the basis element |
|---|---|---|---|
| diagonal \(E_{jj}AE_{jj} = DE_{jj}\) | \(1\) | a copy of the division ring \(D\); the identity \(E_{jj}\) | one idempotent, \(E_{jj}\) |
| off-diagonal \(E_{ii}AE_{jj} = DE_{ij}\), \(i \neq j\) | \(n-1\) | a square-zero line | one nilpotent, \(E_{ij}\) |

### The Whole Algebra

The same bookkeeping for the whole matrix ring reads as follows.

| corners of \(A = M_n(D)\) | number | contents |
|---|---|---|
| diagonal \(E_{ii}AE_{ii} = DE_{ii}\) | \(n\) | copies of the division ring \(D\); the idempotents \(E_{ii}\), a complete orthogonal family |
| off-diagonal \(E_{ii}AE_{kk} = DE_{ik}\), \(i \neq k\) | \(n(n-1)\) | square-zero lines; the nilpotents \(E_{ik}\) |

The two counts add up: \(n + n(n-1) = n^2 = \dim_D A\). Per column the count is \(1 + (n-1) = n\), the dimension of the column and the length of the regular module over \(A\). The \(n\) diagonal corners carry the \(n\) matrix-unit idempotents of the complete orthogonal family; the \(n(n-1)\) off-diagonal corners carry the \(n(n-1)\) matrix-unit nilpotents \(E_{ik}\) with \(i \neq k\). The biquaternion case \(n = 2\) has \(2\) diagonal corners and \(2\) off-diagonal corners, the off-diagonal ones being spanned by the nilpotents \(\vec\Upsilon_1\) and \(\vec\Upsilon_2\).

### The Case \(n = 2\) and the Biquaternion Instance

For \(n = 2\) a column has one diagonal corner and one off-diagonal corner, so the count is one idempotent and one nilpotent, the smallest case in which both kinds occur. The four corners of \(M_2(k)\) over a field and the multiplication of the units are *Matrix Algebras*, §*The Case \(n = 2\)*.

The corpus's worked instance is the biquaternion algebra \(\mathbb{B} \cong M_2(\mathbb{C})\), with \(D = \mathbb{C}\) and \(n = 2\). The first column is the spinor space

$$
S = \mathbb{B}\tilde\Pi_+ = \mathbb{C}\{\tilde\Pi_+,\vec\Upsilon_2\},
$$

with \(\tilde\Pi_+ = \tfrac12(e_0+ie_3)\) the idempotent of the diagonal corner and \(\vec\Upsilon_2 = \tfrac12(ie_1+e_2)\) the square-zero generator of the off-diagonal corner; the second column is the complement \(\mathbb{B}\tilde\Pi_- = \mathbb{C}\{\vec\Upsilon_1,\tilde\Pi_-\}\), the mirror case. The root \(ie_3\) of \(+1\), \((ie_3)^2=e_0\), carries the two associated idempotents \(\tilde\Pi_+\) and \(\tilde\Pi_-\). The idempotents of \(S\) are \(\tilde\Pi_+ + c\vec\Upsilon_2\) with \(c \in \mathbb{C}\), by §*The Idempotents of the Column*. The ideals, the Peirce corners and the two multiplication tables are *Ideals and Peirce Decomposition of the Biquaternion Algebra*; the two minimal left ideals as the spinor space and its complement are *The Spinor Space as a Module and as a Hilbert Space* and *The Complementary Space of the Spinor Space and Its Physical Meaning*.

## Where the Count Does Not Apply

**The coefficient ring must be a division ring.** The corner \(E_{ii}AE_{kk} = DE_{ik}\) is one-dimensional only because \(D\) is a division ring, and with it the corner argument. Over a ring \(R\) with a proper nonzero ideal \(I\), the column \(M_n(R)E_{jj}\) is not minimal: the set

$$
M_n(I)E_{jj} = \left\{\textstyle\sum_i x_{ij}E_{ij} : x_{ij} \in I\right\}
$$

is a nonzero left ideal of \(M_n(R)\) strictly contained in \(M_n(R)E_{jj}\), since \(E_{jj} \notin M_n(I)E_{jj}\). For \(R = \mathbb{Z}\) and \(I = 2\mathbb{Z}\) it is the left ideal of the matrices whose first column has even entries and whose other columns vanish. So the one-plus-\((n-1)\) count is a theorem about a matrix ring over a division ring, equivalently about a simple artinian ring, and not about a matrix ring over an arbitrary coefficient ring.

**The count is of a corner-adapted basis.** It is not a count of the idempotents of the column, which form the affine family \(E_{jj}+N_j\) of §*The Idempotents of the Column*, and it is not a count of the ideals of the column, which is the single minimal ideal \(L_j\). The number \(n-1\) counts corners, not elements of a set of idempotents.

**A trap on the scalar side.** For \(D\) noncommutative the matrix ring carries two scalar structures and \(dE_{ik} \neq E_{ik}d\) in general; the article reads every corner as a set of **left** multiples, \(E_{ii}AE_{kk} = DE_{ik}\), and every coefficient \(x_{ij}\) as a left coefficient. For a field \(D = k\) the two sides coincide and the trap disappears, and the corpus's instances have \(D = \mathbb{C}\). The general division-ring statement is kept because the coefficient ring of a simple artinian algebra is a division ring (Wedderburn–Artin), and the count transports to that generality unchanged.

**Only the diagonal idempotent persists under renormalisation.** The off-diagonal nilpotency of §*The Theorem*(a) is insensitive to the choice of basis element in its corner, but the diagonal idempotency needs the normalisation \(c_j = 1\); the general basis element \(c_jE_{jj}\) of the diagonal corner is idempotent only for \(c_j = 1\). A reader who scales the diagonal basis element loses the idempotent and gets a corner-adapted basis with no idempotents at all.

## Worked Verification



- **Corners.** Every corner product \(E_{ii}AE_{jj}\) is the line \(\mathbb{C}E_{ij}\), and \(AE_{jj}\) is the direct sum of its \(n\) corners.
- **Square-zero.** Every element of every off-diagonal corner satisfies \(x^2 = 0\), for \(n = 2,3,4,5\).
- **Minimality.** For every nonzero \(x \in L_j\), and \(i_0\) chosen with \(x_{i_0j} \neq 0\), one has \(E_{ii_0}x = x_{i_0j}E_{ij}\), so that \(Ax = L_j\); the column has no nonzero proper left submodule.
- **Powers and nilpotents.** The \(E_{ij}\)-coefficient of \(x^m\) is \(x_{ij}x_{jj}^{m-1}\) for \(m \le 4\); \(x\) is nilpotent exactly when \(x_{jj} = 0\); and \(N_j^2 = 0\).
- **Idempotents.** \(E_{jj}+\nu\) is idempotent for every \(\nu \in N_j\), and \(E_{jj}\), \(E_{jj}+E_{ij}\) (\(i \neq j\)) are \(n\) idempotents forming a basis of the column.
- **Biquaternion instance.** \(\tilde\Pi_+^2 = \tilde\Pi_+\), \(\vec\Upsilon_2^2 = 0\) and \(\tilde\Pi_+ + c\vec\Upsilon_2\) idempotent for \(100\) values of \(c \in \mathbb{C}\).
- **Boundary.** Over \(R = \mathbb{Z}\) with \(I = 2\mathbb{Z}\) and \(n = 2\), the set \(M_2(I)E_{11}\) is preserved by left multiplication and excludes \(E_{11}\), so it is a proper nonzero left ideal of \(M_2(\mathbb{Z})E_{11}\).

## Summary

In the matrix ring \(A = M_n(D)\) over a division ring \(D\), the \(j\)-th column ideal \(L_j = AE_{jj} = \bigoplus_i DE_{ij}\) is a minimal left ideal of dimension \(n\), and its corner-adapted basis, the basis with one element per Peirce corner, has exactly **one idempotent and \(n-1\) nilpotents**. The count is forced by the corner structure of the column: the diagonal corner \(E_{jj}AE_{jj} = DE_{jj}\) is a copy of the division ring \(D\) and contains the idempotent \(E_{jj}\), the identity of that corner, while each of the \(n-1\) off-diagonal corners \(E_{ii}AE_{jj} = DE_{ij}\) is square-zero by \((fae)^2 = fa(ef)ae = 0\), so it contains no nonzero idempotent and all its nonzero elements are nilpotents. Hence \(1 + (n-1) = n\), and \(n-1\) is the number of off-diagonal corners of a column, not a numerical accident.

The matrix-unit basis \((E_{1j},\dots,E_{nj})\) realises the count, and the shape is stable in the off-diagonal corners under any normalisation, while the diagonal element is idempotent exactly when it is the corner's identity \(E_{jj}\). The nilpotents of the column are exactly the elements of its off-diagonal part \(N_j\), each square-zero, and \(N_j\) is the kernel of the ring homomorphism \(\pi(x) = x_{jj}\) from the column to \(D\), with \(\pi(E_{jj}) = 1\), so the column is an extension of \(D\) by a square-zero ideal. The idempotents, by contrast, are not the single \(E_{jj}\): they are the affine family \(E_{jj}+N_j\), and a basis of the column can be chosen all of whose elements are idempotents. The count needs a division ring: over a ring with a proper nonzero ideal the column is not minimal, and the corner argument fails. For \(n = 2\) the count is one idempotent and one nilpotent, which is the shape of the biquaternion spinor space \(S = \mathbb{B}\tilde\Pi_+ = \mathbb{C}\{\tilde\Pi_+,\vec\Upsilon_2\}\).

## Summary of Notation

| Symbol | Meaning |
|---|---|
| \(D\), \(n\), \(A = M_n(D)\) | A division ring, an integer \(n \geq 1\), and the matrix ring |
| \(E_{ij}\) | The matrix units, \(E_{ij}E_{kl} = \delta_{jk}E_{il}\) |
| \(E_{jj}\), \(E_{ij}\) (\(i \neq j\)) | The diagonal idempotents and the off-diagonal square-zero units |
| \(L_j = AE_{jj}\) | The \(j\)-th column ideal, a minimal left ideal of dimension \(n\) |
| \(E_{ii}AE_{kk} = DE_{ik}\) | The Peirce corners of the algebra, one-dimensional over \(D\) |
| \(E_{jj}AE_{jj} = DE_{jj}\) | The diagonal corner of the column, a division ring \(\cong D\) |
| \(E_{ii}AE_{jj} = DE_{ij}\), \(i \neq j\) | The \(n-1\) off-diagonal corners of the column, square-zero |
| \(N_j = \bigoplus_{i\neq j} DE_{ij}\) | The off-diagonal part of the column, \(\dim_D N_j = n-1\), \(N_j^2 = 0\) |
| \(\pi(x) = x_{jj}\) | The diagonal-coefficient homomorphism \(L_j \to D\), kernel \(N_j\) |
| \(E_{jj} + N_j\) | The affine family of idempotents of the column |
| Corner-adapted basis | A basis of \(L_j\) with one element in each corner |
| \(\mathbb{B} \cong M_2(\mathbb{C})\) | The biquaternion instance, \(n = 2\), \(D = \mathbb{C}\) |
| \(S = \mathbb{B}\tilde\Pi_+ = \mathbb{C}\{\tilde\Pi_+,\vec\Upsilon_2\}\) | The spinor space, the first column: one idempotent, one nilpotent |

## Further Reading

- The corpus articles named in the text: *Matrix Algebras* (matrix units, the left ideals \(I_V\), the regular module, the case \(n = 2\)); *Unital Algebras*, §*Idempotents and the Peirce Decomposition* (the Peirce decomposition and its product rule); *Rings* (ideals, idempotents and nilpotents as vocabulary); *Direct Sums, Free Modules and Rank* (summands, rank and the length of the regular module); *Ideals and Peirce Decomposition of the Biquaternion Algebra* and *Idempotents of the General Plain Algebra* (the biquaternion instance); *The Spinor Space as a Module and as a Hilbert Space* and *The Complementary Space of the Spinor Space and Its Physical Meaning* (the two minimal left ideals of the biquaternion algebra).
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for idempotents, the Peirce decomposition, matrix units and the structure of matrix rings over division rings.
- Nathan Jacobson, *Structure of Rings* (American Mathematical Society, 1956), for the corner structure of a simple artinian ring and the minimal one-sided ideals.
- William Fulton and Joe Harris, *Representation Theory: A First Course* (Springer, 1991), for the simple module of \(M_n(\mathbb{C})\) and the decomposition of the regular module into \(n\) copies of it.
