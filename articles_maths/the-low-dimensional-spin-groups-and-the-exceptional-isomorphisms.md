
# __The Low-Dimensional Spin Groups and the Exceptional Isomorphisms__

## Introduction

The spin groups are defined uniformly, as the even versors of norm one, and for that reason they are not usually among the classical groups. In low dimension the uniformity breaks, and the spin groups coincide with groups that are classical for reasons of the classification of the root systems: the orthogonal Lie algebra of small rank is isomorphic to another classical Lie algebra, and the isomorphism lifts to the spin group. This article collects those coincidences, gives the algebra behind them, verifies the cases that can be verified by hand and quotes the rest, and identifies the point at which the coincidences stop.

The source of the phenomenon is the classification of the Dynkin diagrams. The diagrams of rank at most three satisfy the coincidences

$$
A_1\cong B_1\cong C_1,\qquad D_2\cong A_1\times A_1,\qquad B_2\cong C_2,\qquad A_3\cong D_3,
$$

and nothing further until the triality of $D_4$; the coincidences of the Lie algebras are exactly these, and the coincidences of the groups follow because the double cover is unique. The mechanical reason on the Clifford side is that the even part of the Clifford algebra of a definite space of dimension $n$ is the Clifford algebra of a definite space of dimension $n-1$ of the opposite sign, so that the even parts run through the low-dimensional table and land on a matrix algebra or on a sum of two, and the spin group is realised there.

The Clifford algebra, the $k$-vectors, the volume element, the even part and the basis theorem are from *The Clifford Algebra* and *Clifford Algebras in Finite Dimensions*; the reflection, the Clifford group, the norm $N(x)=x\bar x$, the versors, the spin group as the group of even versors of norm one and the double cover are from *The Clifford, Pin and Spin Groups* and *Versors, Rotors and the Sandwich Action*; the reflection groups and the unit groups of the quaternion algebras are from *Quaternion Rotations and Reflections* and *The Rotation and Reflection Groups in the Biquaternion Algebra*; the root systems and the classification of the Dynkin diagrams are from *Root Systems and Classification*; the spinor modules and their dimensions are from *Spin Representations and Clifford Modules* and *Spin Representations of the Orthogonal Lie Algebra*; the Lorentzian realisations are from *The Biquaternion Algebra as a Clifford Algebra*. Nothing owned by those entries is re-derived. The field is $\mathbb{R}$ unless a complexification is named, and the signature is positive definite unless stated otherwise.

## The Even Parts and the Low-Dimensional Table

### The Even Part of a Definite Clifford Algebra

**Theorem.** For the positive definite form on $\mathbb{R}^n$ there is an isomorphism of algebras

$$
\mathrm{Cl}^0_{n,0}\cong\mathrm{Cl}_{0,n-1},
$$

the even part of the Clifford algebra of the positive definite space of dimension $n$ being the Clifford algebra of the negative definite space of dimension $n-1$.

**Proof.** Let $e_1,\ldots,e_n$ be an orthonormal basis with $e_i^2=1$. The products $e_ie_n$ for $i<n$ are even, they satisfy $(e_ie_n)^2=-1$ and $(e_ie_n)(e_je_n)+(e_je_n)(e_ie_n)=0$ for $i\neq j$, by the Clifford relations; so the subalgebra they generate is a Clifford algebra of $n-1$ generators of square $-1$, and it is contained in the even part, of the same dimension $2^{n-1}$, hence equal to it. $\square$

**Corollary (the table of even parts).** By the low-dimensional table of *Clifford Algebras in Finite Dimensions*,

| $n$ | $\mathrm{Cl}^0_{n,0}$ | $\dim SO(n)$ | $n$ | $\mathrm{Cl}^0_{n,0}$ | $\dim SO(n)$ |
|---|---|---|---|---|---|
| $2$ | $\mathbb{C}$ | $1$ | $5$ | $M_2(\mathbb{H})$ | $10$ |
| $3$ | $\mathbb{H}$ | $3$ | $6$ | $M_4(\mathbb{C})$ | $15$ |
| $4$ | $\mathbb{H}\oplus\mathbb{H}$ | $6$ | $7$ | $M_8(\mathbb{R})$ | $21$ |

**Proof.** Immediate from the theorem and the values $\mathrm{Cl}_{0,1}=\mathbb{C}$, $\mathrm{Cl}_{0,2}=\mathbb{H}$, $\mathrm{Cl}_{0,3}=\mathbb{H}\oplus\mathbb{H}$, $\mathrm{Cl}_{0,4}=M_2(\mathbb{H})$, $\mathrm{Cl}_{0,5}=M_4(\mathbb{C})$, $\mathrm{Cl}_{0,6}=M_8(\mathbb{R})$ of the cited table; the last column is $n(n-1)/2$. $\square$

The spin group is the group of even versors of norm one inside this algebra, so the table is the list of the algebras in which the low-dimensional spin groups live.

## Two, Three and Four Dimensions

### The Spin Group in Two Dimensions

**Theorem.** $\mathrm{Spin}(2)\cong U(1)$, and the double cover $\mathrm{Spin}(2)\to SO(2)$ is the squaring map of the circle, of kernel $\{\pm1\}$, so that the two groups are isomorphic as abstract groups while the covering is still two-to-one.

**Proof.** By the table $\mathrm{Cl}^0_{2,0}\cong\mathbb{C}$, with the generator $e_1e_2$ of square $-1$; an element $x=a+be_1e_2$ has norm $N(x)=a^2+b^2$, so the even versors of norm one are the elements of the unit circle, which is $U(1)$. The rotation group of the plane is a circle as well, and the map of the covering is written in the two circles as $z\mapsto z^2$: the rotor of parameter $\theta/2$ produces the rotation through $\theta$, as in *Versors, Rotors and the Sandwich Action*, so the covering wraps once around the rotations as the rotor wraps twice. $\square$

**Remark.** The case of the plane is the one in which the two groups are abstractly isomorphic, $\mathrm{Spin}(2)\cong SO(2)\cong U(1)$, even though the covering map is not an isomorphism but the squaring of the circle; it is also the case in which the spinor module is one-dimensional: the weights are $\pm\tfrac12$, which for $n=2$ is the pair of weights of the one-dimensional complex module of $U(1)$ with the half-integral charge. The covering is two-to-one for every $n\ge2$; what is special about the plane is only that the two groups are abstractly the same circle, so that the kernel $\{\pm1\}$ is realised inside the group and the covering is the self-map $z\mapsto z^2$ rather than a map between different groups.

### The Spin Group in Three Dimensions

**Theorem.** $\mathrm{Spin}(3)\cong Sp(1)\cong SU(2)$, the group of unit quaternions.

**Proof.** By the table $\mathrm{Cl}^0_{3,0}\cong\mathbb{H}$. Write $i=e_2e_3$, $j=e_3e_1$, $k=e_1e_2$, so that $i^2=j^2=k^2=-1$ and $ij=-ji=-k$, this labelling being the orientation-reversing one of *Versors, Rotors and the Sandwich Action*; the even part is thus a copy of $\mathbb{H}$, and an even element $x=a+bi+cj+dk$ has norm $N(x)=x\bar x=a^2+b^2+c^2+d^2$, the square of the Euclidean norm of the coefficient vector. The even versors of norm one are therefore the elements of $\mathbb{H}$ of unit norm, which is $Sp(1)$; the identification with $SU(2)$ is the standard one, in which $i,j,k$ are sent to the Pauli matrices multiplied by $-i$. $\square$

**Corollary.** The double cover $\mathrm{Spin}(3)\to SO(3)$ is the quotient of the unit quaternions by $\{\pm1\}$, and the spinor module is the defining two-dimensional complex representation of $SU(2)$.

**Proof.** The double cover and its kernel are from *The Clifford, Pin and Spin Groups*; the module is the defining representation because the weights of the spinor module are $\pm\tfrac12$, as in *Spin Representations of the Orthogonal Lie Algebra*, and the defining representation of $SU(2)$ has exactly those weights. $\square$

### The Spin Group in Four Dimensions

**Theorem.** $\mathrm{Spin}(4)\cong Sp(1)\times Sp(1)$.

**Proof.** By the table $\mathrm{Cl}^0_{4,0}\cong\mathbb{H}\oplus\mathbb{H}$, an isomorphism of algebras. An even element is a pair $(q_1,q_2)$ of quaternions, its Clifford conjugate is the pair $(\bar q_1,\bar q_2)$, and the product $x\bar x=(N(q_1),N(q_2))$ is a scalar of the algebra only when the two components agree, that is when $N(q_1)=N(q_2)$; for an element of the Clifford group this must be so, and the norm-one condition then reads $N(q_1)=N(q_2)=1$, which is $Sp(1)\times Sp(1)$. The count of dimensions confirms it: $3+3=6=\dim SO(4)$. $\square$

**Corollary.** The double cover $\mathrm{Spin}(4)\to SO(4)$ is the quotient of $Sp(1)\times Sp(1)$ by the diagonal $\{\pm1\}$, the two factors acting on the two half-spinor modules of dimension two each, and the Spin representation is the pair of defining representations.

**Proof.** The half-spinor modules are the two minimal left ideals of the even part, which is a direct sum of two matrix algebras over $\mathbb{H}$; each factor acts on its own ideal. The two-sided quaternionic description of the rotations of $\mathbb{R}^4$ is in *The Rotation and Reflection Groups in the Biquaternion Algebra*. $\square$

**Remark.** The decomposition of the even part is the reason the rotations of four-dimensional space factor as a product of two three-dimensional rotations, and the reason the two half-spinor modules are of dimension two: the volume element is even and central with $\omega^2=1$, its two eigenspaces are the two summands, and each summand is a copy of the quaternions.

## Five and Six Dimensions

### The Spin Group in Five Dimensions

**Theorem.** $\mathrm{Spin}(5)\cong Sp(2)$, the compact symplectic group of rank two, and the spinor module of dimension four is the defining quaternionic representation of $Sp(2)$ on $\mathbb{H}^2$.

**Proof.** By the table $\mathrm{Cl}^0_{5,0}\cong M_2(\mathbb{H})$, so the spin group is the group of norm-one units of the quaternionic matrix algebra $M_2(\mathbb{H})$, that is the group of $2\times2$ matrices over $\mathbb{H}$ with $x\bar x=1$. That group is the compact symplectic group $Sp(2)$, of dimension $10$, and the dimension of $SO(5)$ is $10$, so the two agree; the spinor module is the natural module $\mathbb{H}^2$ of the matrices, of real dimension four, and the weights of the spinor module of *Spin Representations of the Orthogonal Lie Algebra* are the four vectors $\tfrac12(\pm\epsilon_1\pm\epsilon_2)$, which are the weights of the defining representation of $Sp(2)$. $\square$

**Remark.** The isomorphism reflects the coincidence of Dynkin diagrams $B_2\cong C_2$, that is $\mathfrak{so}(5,\mathbb{C})\cong\mathfrak{sp}(2,\mathbb{C})$, recorded in *Root Systems and Classification*. The representation theory is the same on both sides: the spinor module of $\mathfrak{so}(5)$ is the defining module of $\mathfrak{sp}(2)$, which is self-dual.

### The Spin Group in Six Dimensions

**Theorem.** $\mathrm{Spin}(6)\cong SU(4)$, and the two half-spinor modules are the defining representation of $SU(4)$ and its dual.

**Proof.** By the table $\mathrm{Cl}^0_{6,0}\cong M_4(\mathbb{C})$; the spin group acts on the spinor module $\mathbb{C}^4$ through this algebra, preserving the Hermitian form that the Clifford norm defines on the module, and the volume element provides the complex structure, so the image lies in $U(4)$; the determinant of the image is one, because the spin group is perfect and has no nontrivial homomorphism to an abelian group, so the image lies in $SU(4)$, of dimension $15$, equal to the dimension of $SO(6)$. The two half-spinor modules are the eigenspaces of the volume element, of dimension four each, and they are the defining representation $4$ and its dual $\bar4$ of $SU(4)$. $\square$

**Remark.** The isomorphism reflects the coincidence $D_3\cong A_3$, that is $\mathfrak{so}(6,\mathbb{C})\cong\mathfrak{sl}(4,\mathbb{C})$, and the two half-spinors correspond to the two ends of the Dynkin diagram of $A_3$, which is the reason they are dual to one another: the diagram has an outer automorphism, and it interchanges the two modules. In the language of the next section, the diagram of $D_3$ is the diagram of $A_3$ relabelled, and the chiral splitting of the spinor module is the splitting of the defining representation of the linear algebra from its dual.

## The Real Forms

The same coincidences hold for the real forms, where they are the classical isomorphisms between the groups of the Lorentzian and split signatures.

**Theorem.** With the conventions and the identifications of *The Biquaternion Algebra as a Clifford Algebra* and *The Rotation and Reflection Groups in the Biquaternion Algebra*,

$$
\mathrm{Spin}(1,2)\cong SL(2,\mathbb{R}),\qquad \mathrm{Spin}(1,3)\cong SL(2,\mathbb{C}),
$$

$$
\mathrm{Spin}(2,2)\cong SL(2,\mathbb{R})\times SL(2,\mathbb{R}),\qquad \mathrm{Spin}(3,3)\cong SL(4,\mathbb{R}),\qquad \mathrm{Spin}(4,2)\cong SU(2,2).
$$

**Proof.** Each is a standard isomorphism of the real forms, of the same kind as those of the preceding sections and reflecting the same diagram coincidences; the Lorentzian case $\mathrm{Spin}(1,3)\cong SL(2,\mathbb{C})$ is realised inside the biquaternion algebra in *Spinors and the Biquaternion Spinor Module* and *The Rotation and Reflection Groups in the Biquaternion Algebra*, where the double cover $SL(2,\mathbb{C})\to SO^+(1,3)$ is described. The dimensions agree in each case: $3=3$, $6=6$, $6=6$, $15=15$ and $15=15$. The remaining isomorphisms of real forms are tabulated in the literature cited below. $\square$

**Remark.** The conformal case deserves the separate mention it receives in the list: $\mathrm{Spin}(4,2)\cong SU(2,2)$ is the spin group of the quadratic space in which the conformal group of four-dimensional Minkowski space is linearised, which is the conformal model of *The Conformal Model of Euclidean Space* read in the Lorentzian signature. The isomorphism is the reason the conformal group of space-time is a classical group of low rank.

## The End of the Coincidences

**Theorem.** For $n\ge7$ the spin group $\mathrm{Spin}(n)$ is not isomorphic to a classical group of the same dimension, apart from the accidental isomorphisms of the real forms; and the first structure of the exceptional kind in the spin groups occurs at $n=8$, where the diagram $D_4$ has an outer automorphism group of order three, which permutes its three eight-dimensional representations.

**Proof.** The classification of the Dynkin diagrams has no coincidences among $B_m$, $C_m$ and $D_m$ beyond those listed for rank at most three, by *Root Systems and Classification*; the spin groups of higher rank are therefore not classical, their Lie algebras being of type $B_m$ or $D_m$ with $m\ge4$; for $\mathrm{Spin}(7)$ the even part is $M_8(\mathbb{R})$, and the group of norm-one even versors in it has dimension $21$, which is the dimension of $SO(7)$ and of no classical group of smaller rank. The case $n=8$ is the subject of *Triality and Spin(8)*. $\square$

**Remark.** The non-classical character of $\mathrm{Spin}(7)$ has a visible algebraic cause: the even part is the full matrix algebra $M_8(\mathbb{R})$, so the spin group sits inside a matrix algebra for which no classical group of dimension $21$ is available, unlike the cases $n=5$ and $n=6$, where the even part is a matrix algebra over a division algebra whose automorphism group provides the classical group of the right dimension. The list of coincidences is thus exhausted at $n=6$, and $D_4$ supplies a symmetry of a different kind.

## Summary

The even part of the Clifford algebra of the positive definite space of dimension $n$ is the Clifford algebra of the negative definite space of dimension $n-1$, $\mathrm{Cl}^0_{n,0}\cong\mathrm{Cl}_{0,n-1}$, and the low-dimensional table therefore reads

$$
\mathrm{Cl}^0_{2,0}\cong\mathbb{C},\quad \mathrm{Cl}^0_{3,0}\cong\mathbb{H},\quad \mathrm{Cl}^0_{4,0}\cong\mathbb{H}\oplus\mathbb{H},\quad \mathrm{Cl}^0_{5,0}\cong M_2(\mathbb{H}),\quad \mathrm{Cl}^0_{6,0}\cong M_4(\mathbb{C}),\quad \mathrm{Cl}^0_{7,0}\cong M_8(\mathbb{R}).
$$

The spin group is the group of even versors of norm one inside that algebra, and in the first four cases the algebra is one whose norm-one part is a classical group. The resulting isomorphisms are

$$
\mathrm{Spin}(2)\cong U(1),\quad \mathrm{Spin}(3)\cong Sp(1)\cong SU(2),\quad \mathrm{Spin}(4)\cong Sp(1)\times Sp(1),
$$

$$
\mathrm{Spin}(5)\cong Sp(2),\qquad \mathrm{Spin}(6)\cong SU(4),
$$

with the dimensions $1$, $3$, $6$, $10$ and $15$ matching those of $SO(2)$ to $SO(6)$, and with the spinor modules matching the defining modules of the classical groups: the two-dimensional defining module of $SU(2)$ in three dimensions, the pair of two-dimensional half-spinors in four, the four-dimensional defining module of $Sp(2)$ in five, and the defining module $4$ of $SU(4)$ together with its dual in six. The real forms satisfy $\mathrm{Spin}(1,2)\cong SL(2,\mathbb{R})$, $\mathrm{Spin}(1,3)\cong SL(2,\mathbb{C})$, $\mathrm{Spin}(2,2)\cong SL(2,\mathbb{R})\times SL(2,\mathbb{R})$, $\mathrm{Spin}(3,3)\cong SL(4,\mathbb{R})$ and $\mathrm{Spin}(4,2)\cong SU(2,2)$, the last being the linearisation of the conformal group of Minkowski space.

The source of all of these is the coincidence of Dynkin diagrams of small rank, $A_1\cong B_1\cong C_1$, $D_2\cong A_1\times A_1$, $B_2\cong C_2$ and $A_3\cong D_3$; the coincidences stop there, so $\mathrm{Spin}(7)$ and the higher spin groups are not classical, and the first exceptional structure in the sequence is the triality of $D_4$ at $n=8$, where an outer automorphism of order three permutes the vector representation and the two half-spinors.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{Cl}^0_{n,0}\cong\mathrm{Cl}_{0,n-1}$ | Even part of a definite Clifford algebra |
| $Sp(1)$ | Unit quaternions, $=SU(2)$ |
| $Sp(2)$ | Compact symplectic group of rank two |
| $U(1)$, $SU(2)$, $SU(4)$ | The unitary groups of the low-dimensional cases |
| $SL(2,\mathbb{R})$, $SL(2,\mathbb{C})$, $SL(4,\mathbb{R})$ | The real forms of the low-dimensional cases |
| $SU(2,2)$ | The real form isomorphic to $\mathrm{Spin}(4,2)$ |
| $B_m$, $C_m$, $D_m$ | Orthogonal odd, symplectic and orthogonal even types |
| $\omega$ | Volume element, central in the even part |
| $1$, $3$, $6$, $10$, $15$, $21$, $28$ | The dimensions $\dim SO(n)$ for $n=2,\ldots,8$ |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the table of the Clifford algebras of low dimension and the identification of the spin groups.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the even parts, the norm-one groups and the classical isomorphisms.
- John Conway and Derek Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the quaternionic identifications $\mathrm{Spin}(3)\cong Sp(1)$, $\mathrm{Spin}(4)\cong Sp(1)\times Sp(1)$ and the octonionic $\mathrm{Spin}(8)$.
- Nicolas Bourbaki, *Lie Groups and Lie Algebras, Chapters 4–6* (Springer, 2002), for the classification of the Dynkin diagrams and the coincidences of small rank.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the spin representations and the low-dimensional isomorphisms of the spin groups.
