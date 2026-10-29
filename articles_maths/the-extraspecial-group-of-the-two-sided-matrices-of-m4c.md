# __The Extraspecial Group of the Two-Sided Matrices of $M_4(\mathbb{C})$__

## Introduction

The sixteen two-sided operators $T_{\mu\nu}=L_\mu R_\nu$ of *The Two-Sided Operators Method to Build $M_4(\mathbb{C})$*, together with their negatives, form a finite group of order $32$:

$$
G=\{\pm T_{\mu\nu}:\mu,\nu\in\{t,x,y,z\}\}.
$$

The group is the **central product of two quaternion groups**,

$$
G\cong Q_8\circ Q_8,
$$

the left multiplications giving one $Q_8$ and the right multiplications the other. It is an **extraspecial** group of order $2^{1+4}$: its centre is $\{\pm I\}$, its quotient $G/\{\pm I\}$ is the four-dimensional space $(\mathbb{Z}/2)^{4}$, and the commutator induces a nondegenerate alternating form on that space. The group has nineteen elements of order two, twelve of order four, seventeen conjugacy classes, and seventeen irreducible representations: sixteen of degree one and one of degree four, the defining representation on $\mathbb{C}^{4}$.

This article states the group, the two quaternion subgroups, the centre and the exponent, the extraspecial structure, the commutator form, the abelian subgroups, the conjugacy classes and the character count, and the comparison with the two-qubit Pauli group. The operators themselves are *The Operators of the Peirce Decomposition of $M_4(\mathbb{C})$* and *The Coefficient Matrix of a Two-Sided Operator: A Worked Computation*; the algebra they generate is *The Two-Sided Operators Method to Build $M_4(\mathbb{C})$*.

## The Group

**Definition.** Let $L_\mu$ and $R_\nu$ be the left and right multiplication operators on $\mathbb{B}\cong M_2(\mathbb{C})$ by the four biquaternion units, with $L_t=R_t=I$. The **group of the two-sided matrices** is

$$
G=\{\pm L_\mu R_\nu:\mu,\nu\in\{t,x,y,z\}\}.
$$

**Proposition.** $G$ has order $32$, and its elements are distinct up to sign: the sixteen products $T_{\mu\nu}$ are distinct, no one is the negative of another, and the two signs give thirty-two distinct matrices.

**Proof.** The sixteen $T_{\mu\nu}$ are a basis of $M_4(\mathbb{C})$ by the method article, so they are linearly independent and in particular distinct; $-T_{\mu\nu}=T_{\mu'\nu'}$ would be a linear dependence. The unit is $T_{tt}=I$, and $-I=T_{tt}$ is a distinct element.

**The product rule.** The product is read from the multiplication of the units:

$$
(L_\mu R_\nu)(L_{\mu'}R_{\nu'})=L_\mu L_{\mu'}\,R_\nu R_{\nu'}
$$

because left and right multiplications commute. The left product $L_\mu L_{\mu'}$ is $\pm L_{\mu''}$ and the right product is $\pm R_{\nu''}$, with the signs fixed by the orientation convention of the units. Hence the product is $\pm T_{\mu''\nu''}$, and $G$ is closed under products and inverses.

## The Two Quaternion Subgroups

**Proposition.** The sets

$$
Q_L=\{\pm L_\mu:\mu\in\{t,x,y,z\}\},\qquad
Q_R=\{\pm R_\nu:\nu\in\{t,x,y,z\}\}
$$

are subgroups isomorphic to the quaternion group $Q_8$.

**Proof.** The left multiplications satisfy $L_x^{2}=L_y^{2}=L_z^{2}=-I$ and $L_xL_y=-L_yL_x$; with $L_z=L_xL_y$ up to the orientation sign, the eight elements $\{\pm I,\pm L_x,\pm L_y,\pm L_z\}$ are the quaternion group: one element of order two, six of order four, and the multiplication of $Q_8$. The same holds on the right. $\square$

**The central product.** The two subgroups commute elementwise,

$$
L_\mu R_\nu=R_\nu L_\mu,
$$

because left and right multiplication commute in an associative algebra, and they meet in

$$
Q_L\cap Q_R=\{\pm I\}.
$$

**Theorem.**

$$
G=Q_L\,Q_R\cong Q_8\circ Q_8,\qquad |G|=\frac{8\cdot8}{2}=32.
$$

**Proof.** Every element of $G$ is a product of an element of $Q_L$ and an element of $Q_R$ by definition. The product map $Q_L\times Q_R\to G$ is surjective; its kernel is the pairs $(x,x^{-1})$ with $x\in Q_L\cap Q_R=\{\pm I\}$, of order $2$. Hence $|G|=64/2=32$, and $G$ is the central product, the quotient of $Q_8\times Q_8$ by the diagonal central subgroup of order two.

**The commutator.** The two factors do not commute as abstract groups inside $Q_8\times Q_8$; their images in the central product commute because the identification is central. The commutator of a left and a right element is

$$
[L_\mu,R_\nu]=L_\mu R_\nu L_\mu^{-1}R_\nu^{-1}=I,
$$

and the nontrivial commutators come from within each $Q_8$: $[L_x,L_y]=-I$ and $[R_x,R_y]=-I$.

## The Centre and the Exponent

**Proposition.** The centre of $G$ is $\{\pm I\}$.

**Proof.** An element $L_\mu R_\nu$ commutes with every $L_\alpha$ exactly when $L_\mu$ commutes with $L_\alpha$ for every $\alpha$, which forces $\mu=t$; and it commutes with every $R_\beta$ exactly when $\nu=t$. Hence the central elements are $\pm L_tR_t=\pm I$. $\square$

**Proposition.** The exponent of $G$ is $4$: every element has order at most four, and some have order four.

**Proof.** For $g=L_\mu R_\nu$,

$$
g^{2}=L_\mu^{2}R_\nu^{2}=\pm I,
$$

because each unit squares to $\pm I$; hence $g^{4}=I$. The elements $L_x$ and $R_x$ have order four, because their squares are $-I\ne I$. $\square$

**The order count.** The elements of order two are $-I$ and the eighteen products $L_\mu R_\nu$ with both $\mu\ne t$ and $\nu\ne t$, taken with both signs: $2+18=20$ elements satisfy $g^{2}=I$, of which nineteen have order exactly two. The remaining twelve elements, with exactly one index equal to $t$, have order four.

| Order | Number of elements |
|---|---|
| $1$ | $1$ |
| $2$ | $19$ |
| $4$ | $12$ |
| total | $32$ |

## The Extraspecial Structure

**Proposition.** $G/\{\pm I\}\cong(\mathbb{Z}/2)^{4}$.

**Proof.** The quotient has order $16$. Its elements are the classes of $L_\mu R_\nu$; the class of $L_\mu R_\nu$ has order two because its square is $\pm I$, and the quotient is abelian because the commutator of any two elements lies in $\{\pm I\}$. A group of order $16$ and exponent two is $(\mathbb{Z}/2)^{4}$. $\square$

**Theorem.** $G$ is extraspecial of order $2^{1+4}$: its centre has order $2$, its quotient by the centre is elementary abelian of order $16$, and its derived subgroup is the centre.

**Proof.** The centre is $\{\pm I\}$ and the quotient is elementary abelian, which is the definition. The derived subgroup is contained in the centre because the quotient is abelian, and contains $-I$ because $[L_x,L_y]=-I$; hence $G'=\{\pm I\}$. $\square$

**The commutator form.** Define

$$
b(x\{\pm I\},y\{\pm I\})=[x,y]\in\{\pm I\}\cong\mathbb{F}_2.
$$

**Proposition.** $b$ is a well-defined alternating bilinear form on $G/\{\pm I\}$, and it is nondegenerate.

**Proof.** The commutator depends only on the classes because the centre is central, and it is alternating because $[x,x]=I$; bilinearity is the identity $[xy,z]=[x,z]\,[y,z]$ in a class-two group. If $x\{\pm I\}$ is in the radical, then $[x,y]=I$ for all $y$, so $x$ is central and the class is the identity. $\square$

**The type.** The nondegenerate alternating form on a four-dimensional symplectic space over $\mathbb{F}_2$ has a symplectic basis $e_1,f_1,e_2,f_2$ with $b(e_i,f_i)=1$ and all other pairings zero; the group is the extraspecial group of that form, of order $2^{1+4}$.

## The Abelian Subgroups

**Proposition.** The subgroup $\langle L_x,R_x\rangle$ is abelian of order $8$, isomorphic to $\mathbb{Z}/4\times\mathbb{Z}/2$.

**Proof.** $L_x$ and $R_x$ commute, $L_x$ has order four, and $L_xR_x$ has order two, because $(L_xR_x)^{2}=L_x^{2}R_x^{2}=(-I)(-I)=I$. Every element of the subgroup is $L_x^{a}(L_xR_x)^{b}$ with $a\in\{0,1,2,3\}$ and $b\in\{0,1\}$, and these eight elements are distinct; the subgroup is abelian of order $8$, isomorphic to $\mathbb{Z}/4\times\mathbb{Z}/2$. $\square$

**The maximal abelian subgroups.** Every abelian subgroup $A$ has $A\cap\{\pm I\}$ of order at most two, and its image in $G/\{\pm I\}$ is a totally isotropic subspace for the commutator form, of dimension at most two. Hence $|A|\le 2\cdot4=8$, and the bound is attained. The maximal abelian subgroups are therefore the inverse images of the maximal totally isotropic planes of $G/\{\pm I\}$, of order $8$.

**The count.** A maximal totally isotropic plane in a four-dimensional symplectic space over $\mathbb{F}_2$ has $3$ nonzero vectors, and there are $15$ nonzero vectors; the number of such planes is $15\cdot 6/(3\cdot 2)=15$. The group has fifteen maximal abelian subgroups, matching the fifteen non-central conjugacy classes below.

## The Conjugacy Classes and the Representations

**Proposition.** $G$ has seventeen conjugacy classes: the two central classes $\{I\}$ and $\{-I\}$, and fifteen classes of size two.

**Proof.** A non-central element has centraliser of order $16$: the centraliser is the inverse image in $G$ of the orthogonal complement of its class under the commutator form, a three-dimensional subspace of $G/\{\pm I\}$, of order $8$; together with the centre this gives $16$. The class therefore has $32/16=2$ elements. There are $30$ non-central elements, hence $15$ classes of size two. $\square$

**Theorem.** $G$ has seventeen irreducible complex representations: sixteen of degree one and one of degree four, the defining representation on $\mathbb{C}^{4}$.

**Proof.** The number of irreducible representations equals the number of conjugacy classes, seventeen. The sixteen characters of the abelian quotient $G/\{\pm I\}\cong(\mathbb{Z}/2)^{4}$ are sixteen representations of degree one. The sum of the squares of the degrees is $|G|=32$, so the remaining representation has degree $d$ with $d^{2}=32-16=16$, that is, $d=4$. The defining representation is irreducible: the algebra generated by $G$ is $M_4(\mathbb{C})$, because the sixteen $T_{\mu\nu}$ are a basis, so its commutant is $\mathbb{C}I$ and the module $\mathbb{C}^{4}$ is simple. $\square$

**The character table.** The sixteen linear characters take values $\pm1$ on the classes of $L_\mu R_\nu$; the degree-four character is the trace of the defining representation: $\chi(I)=4$, $\chi(-I)=-4$, $\chi(L_\mu R_\nu)=0$ for $\mu,\nu\ne t$, and $\chi(L_\mu)=0$, $\chi(R_\nu)=0$ for the elements of order four, whose trace vanishes because their eigenvalues are $\pm i$ in pairs.

**The Schrödinger representation.** The uniqueness of the degree-four representation is the Stone–von Neumann theorem for the Heisenberg group over $\mathbb{F}_2$: the extraspecial group is the Heisenberg group of the symplectic form, and it has a unique irreducible representation of dimension $2^{2}=4$ on which the centre acts by $-1$.

## The Pauli Comparison

**The two-qubit Pauli group.** The Pauli group of two qubits is

$$
P_2=\{i^{k}P_1\otimes P_2:k\in\mathbb{Z}/4,\ P_j\in\{I,X,Y,Z\}\},
$$

of order $64$, with centre $\{\pm I,\pm iI\}\cong\mathbb{Z}/4$ of order four. The quotient by the centre is $(\mathbb{Z}/2)^{4}$. The commutator pairing takes values in $\{\pm I\}\subset Z(P_2)$ and is nondegenerate on $P_2/Z(P_2)$; the quotient by the smaller subgroup $\{\pm I\}$ is elementary abelian of order $32$.

**The difference.** $G$ and $P_2$ are not isomorphic, although both are built on the same symplectic space. $G$ has order $32$, centre of order $2$ and $G'=\{\pm I\}$; it is extraspecial and nonabelian. $P_2$ has order $64$ and centre $\mathbb{Z}/4$; its quotient by $\{\pm I\}$ is elementary abelian of order $32$, so $P_2$ is not extraspecial. The two share the symplectic space $(\mathbb{Z}/2)^{4}$ of the quotient by the centre, but the kernels of the central extensions differ: $\mathbb{Z}/2$ for $G$ and $\mathbb{Z}/4$ for $P_2$. The group of the two-sided matrices is therefore not the two-qubit Pauli group; it is the extraspecial double cover of the four-dimensional symplectic space over $\mathbb{F}_2$.

**The physical interpretation.** The nineteen elements of order two are the reflections of the two-sided frame; the twelve elements of order four are the quarter turns; the unique four-dimensional representation is the carrier of the algebra. The Clifford frame of *The Gamma Frame and the Complexified Dirac Algebra of $M_4(\mathbb{C})$* is a different set of generators of the same algebra, and the comparison of $G$ with the Pauli group is the discrete side of the comparison of the two frames.

## Summary

The thirty-two matrices $\pm T_{\mu\nu}$ form a group $G$ of order $32$, the central product $Q_8\circ Q_8$ of the left and right quaternion subgroups. Its centre is $\{\pm I\}$, its exponent is $4$, it has nineteen elements of order two and twelve of order four, seventeen conjugacy classes, and seventeen irreducible representations: sixteen of degree one and one of degree four. The quotient $G/\{\pm I\}$ is $(\mathbb{Z}/2)^{4}$ with a nondegenerate alternating commutator form, so $G$ is extraspecial of order $2^{1+4}$; its maximal abelian subgroups have order $8$ and are fifteen in number. The group is not the two-qubit Pauli group: $G$ is nonabelian extraspecial of order $32$ with $G'=\{\pm I\}$, while the two-qubit Pauli group modulo $\{\pm I\}$ is elementary abelian of order $32$.

| Quantity | Value |
|---|---|
| $|G|$ | $32$ |
| Structure | $Q_8\circ Q_8$ |
| Centre | $\{\pm I\}$, order $2$ |
| Exponent | $4$ |
| Elements of order $2$ | $19$ |
| Elements of order $4$ | $12$ |
| $G/\{\pm I\}$ | $(\mathbb{Z}/2)^{4}$ |
| Derived subgroup | $\{\pm I\}$ |
| Conjugacy classes | $17$ |
| Irreducible representations | $16$ of degree $1$, $1$ of degree $4$ |
| Maximal abelian subgroups | $15$, of order $8$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T_{\mu\nu}=L_\mu R_\nu$ | the two-sided operator of the pair $(\mu,\nu)$ |
| $G$ | the group $\{\pm T_{\mu\nu}\}$ |
| $Q_L,Q_R$ | the quaternion subgroups $\{\pm L_\mu\}$ and $\{\pm R_\nu\}$ |
| $b$ | the commutator form on $G/\{\pm I\}$ |
| $P_2$ | the two-qubit Pauli group |
| $Q_8\circ Q_8$ | the central product of two quaternion groups |

## Further Reading

- [The Two-Sided Operators Method to Build $M_4(\mathbb{C})$](the-two-sided-operators-method-to-build-m4c.html), for the sixteen operators and their product rule.
- [The Operators of the Peirce Decomposition of $M_4(\mathbb{C})$](the-operators-of-the-peirce-decomposition-of-m4c.html), for the left, right and sandwich operators.
- [The Coefficient Matrix of a Two-Sided Operator: A Worked Computation](the-coefficient-matrix-of-a-two-sided-operator-a-worked-computation.html), for the explicit matrices.
- [The Kronecker Factorisation $M_4(\mathbb{C})\cong M_2(\mathbb{C})\otimes M_2(\mathbb{C})$](the-kronecker-factorisation-of-m4c.html), for the two commuting factors.
- [The Gamma Frame and the Complexified Dirac Algebra of $M_4(\mathbb{C})$](the-gamma-frame-and-the-complexified-dirac-algebra-of-m4c.html), for the Clifford frame.
- Daniel Gorenstein, *Finite Groups* (Harper and Row, 1968), for extraspecial groups and their representations.
- I. Martin Isaacs, *Character Theory of Finite Groups* (Dover, 1994), for the character count and the degrees.
