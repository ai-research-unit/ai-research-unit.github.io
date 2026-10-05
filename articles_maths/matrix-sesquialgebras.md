# __Matrix Sesquialgebras__

## Introduction

The complex matrices of a fixed order, with the conjugate transpose as their involution, are the standard example of a sesquialgebra, and the whole of the theory is read on them. The algebra $M_{n}(\mathbb{C})$ is associative with a unit, the conjugate transpose is a $\varsigma$-semilinear involution of order two for the conjugation $\varsigma(z)=\overline{z}$, and the resulting structure carries two products: the ordinary product $ST$, which is $\mathbb{C}$-bilinear, and the **sesquilinear product**

$$
S\star T=S\,T^{*} ,
$$

which is $\mathbb{C}$-linear in the first slot and conjugate-linear in the second. The elements selected by the involution are the **Hermitian** matrices $X^{*}=X$, the **skew-Hermitian** ones $X^{*}=-X$, and the **unitary** ones $U^{*}=U^{-1}$, and the trace functional $\tau(X)=\operatorname{tr}(X)$ is central and compatible with the involution, $\operatorname{tr}(X^{*})=\varsigma\bigl(\operatorname{tr}(X)\bigr)$, so that the pairing $\varphi(X,Y)=\operatorname{tr}(XY^{*})$ is the standard Hermitian form. The present article collects this structure, works the case $n=2$ on the Pauli basis, and identifies the resulting two-product structure with that of the biquaternion algebra, of which $M_{2}(\mathbb{C})$ is a matrix model.

The subject belongs to the applications of the sesquialgebras, in the group *Applications*, and it is the matrix instance that the whole operator theory of the category is computed on. The definition of the sesquialgebra, its involution, its units and its collapse at the identity are *Sesquialgebras*; the derived product, its parities and its one-sided reads are *The Sesquilinear Product*; the pairing, its two slots, its perfection and the trace $\tau$ that defines it are *The Sesquilinear Adjoint Operator*; the endomorphism algebra of a module with a form, of which this is the case $M=\mathbb{C}^{n}$, is *The Sesquilinear Structure of the Endomorphism Algebra*; the Hermitian elements and the positive ones are *Hermitian and Skew-Hermitian Elements* and *Hermitian Squares and the Algebraic Positive Cone*; and the four products of the biquaternion algebra, compared with the two here, are *The Four Biquaternion Complex Products* and *Comparison Between the Four Biquaternion Products*.

**The boundaries.** The Hermitian, skew-Hermitian and unitary **elements** of a general sesquialgebra are *Hermitian and Skew-Hermitian Elements*, *Units and the Unitary Elements* and *The Unitary Lie Algebra*; the matrix **groups** $U(n)$ and $SU(n)$ read with their structure are the subject of the matrix-group applications and are named and not developed here; the biquaternion algebra itself, its four products and its subalgebras, is *Biquaternions as a Sesquialgebra over $\mathbb{C}$*, *The Four Biquaternion Complex Products* and *Relations Between the Four Biquaternion Products*; and the algebra $M_{n}(\mathbb{C})$ as an algebra with an involution, without the sesquilinear product, is *The Endomorphism Algebra of a Module* and *Involutions of the Endomorphism Algebra*. This article stays inside Part I: no distance, no limit, no completeness.

Throughout, $n\ge 1$, $M_{n}(\mathbb{C})$ is the algebra of the complex square matrices of order $n$ with the ordinary product, the unit $I$, and the centre the scalar matrices $\mathbb{C}I$. The **involution** is the conjugate transpose, $X^{*}=\overline{X}^{T}$, and $\varsigma$ is the complex conjugation. The trace is $\tau(X)=\operatorname{tr}(X)=\sum_{i}X_{ii}$, the standard matrix units are $E_{ij}$, and $M_{n}(\mathbb{C})$ is a sesquialgebra over $\mathbb{C}$ with the base involution $\varsigma$ in the sense of *Sesquialgebras*.

## The Sesquialgebra of the Complex Matrices

### The Involution and its Laws

**Definition.** The **conjugate transpose** of $X\in M_{n}(\mathbb{C})$ is the matrix $X^{*}$ with $(X^{*})_{ij}=\overline{X_{ji}}$.

**Theorem (the involution).** For all $X,Y\in M_{n}(\mathbb{C})$ and all $\lambda\in\mathbb{C}$,

$$
(XY)^{*}=Y^{*}X^{*},\qquad (X^{*})^{*}=X,\qquad (\lambda X)^{*}=\overline{\lambda}\,X^{*},\qquad I^{*}=I ,
$$

so $X\mapsto X^{*}$ is a $\varsigma$-semilinear anti-automorphism of order two of $M_{n}(\mathbb{C})$, and $M_{n}(\mathbb{C})$ is a sesquialgebra over $\mathbb{C}$.

**Proof.** The first is the transpose of a product, $(XY)^{T}=Y^{T}X^{T}$, followed by the entrywise conjugation, which is multiplicative; the second is the same pair of operations in reverse, each of order two; the third is $\overline{\lambda X}^{T}=\overline{\lambda}\,\overline{X}^{T}$; and the fourth is that $I$ has real entries on the diagonal and zeroes elsewhere. The four laws are those of a $\varsigma$-semilinear involution with $I^{*}=I$. $\square$

**Theorem (the trace under the involution).** The trace is central and compatible,

$$
\operatorname{tr}(XY)=\operatorname{tr}(YX),\qquad \operatorname{tr}(X^{*})=\varsigma\bigl(\operatorname{tr}(X)\bigr) .
$$

**Proof.** The first is $\sum_{i}(XY)_{ii}=\sum_{i}\sum_{k}X_{ik}Y_{ki}=\sum_{k}\sum_{i}Y_{ki}X_{ik}=\sum_{k}(YX)_{kk}$. The second is $\operatorname{tr}(X^{*})=\sum_{i}\overline{X_{ii}}=\overline{\sum_{i}X_{ii}}$. $\square$

### The Pairing

**Definition.** The **pairing** of the sesquialgebra is

$$
\varphi(X,Y)=\operatorname{tr}(XY^{*}) .
$$

**Proposition (the pairing is Hermitian and perfect).** The pairing is $\mathbb{C}$-linear in the first slot and $\varsigma$-semilinear in the second, it is sesqui-symmetric, $\varphi(Y,X)=\varsigma\bigl(\varphi(X,Y)\bigr)$, and it is perfect: for the matrix units,

$$
\varphi(X,E_{ij}^{*})=X_{ij} ,
$$

so a matrix is recovered from its pairings against the matrix units, and the map $X\mapsto\varphi(X,\,\cdot\,)$ is a bijection.

**Proof.** The semilinearity in the second slot is the compatibility of the trace with the involution; the sesqui-symmetry is $\operatorname{tr}(YX^{*})=\varsigma\bigl(\operatorname{tr}(XY^{*})\bigr)$ by $\operatorname{tr}(Z^{*})=\varsigma(\operatorname{tr}Z)$ applied to $Z=YX^{*}=(XY^{*})^{*}$. For the perfection, $\varphi(X,E_{ij}^{*})=\operatorname{tr}(XE_{ji})$, since $(E_{ij})^{*}=E_{ji}$ and the conjugation is entrywise; the matrix $XE_{ji}$ has the $j$-th column of $X$ in its $i$-th column and zeroes elsewhere, so its trace is $X_{ij}$. $\square$

**Remark (the coefficient reading).** The pairing computes in the entries,

$$
\varphi(X,Y)=\operatorname{tr}(XY^{*})=\sum_{i,j}X_{ij}\,\overline{Y_{ij}} ,
$$

which is the standard Hermitian form on the $n^{2}$ complex coordinates $X_{ij}$, written with the correct order of the two slots.

### The Two Products

**Theorem (the parities of the two products).** The ordinary product $ST$ is $\mathbb{C}$-bilinear in the two slots; the sesquilinear product $S\star T=ST^{*}$ is $\mathbb{C}$-linear in the first slot and $\varsigma$-semilinear in the second,

$$
(\lambda S)\star T=\lambda\,(S\star T),\qquad S\star(\lambda T)=\varsigma(\lambda)\,(S\star T) ,
$$

and it is the derived product of the sesquialgebra $M_{n}(\mathbb{C})$ with its conjugate transpose. The unit $I$ is a right unit for $\star$, $T\star I=T$, and a two-sided unit only for the Hermitian matrices, where $I\star T=T^{*}=T$.

**Proof.** The bilinearity of the ordinary product is the $\mathbb{C}$-algebra structure. For the sesquilinear product, the first parity is the linearity of the product in the first slot and the second is $S\star(\lambda T)=S\,\varsigma(\lambda)T^{*}=\varsigma(\lambda)(S\star T)$. The unit laws are $T\star I=T\,I^{*}=T$ for every $T$, so $I$ is a right unit, and $I\star T=I\,T^{*}=T^{*}$, which is $T$ exactly for $T^{*}=T$. $\square$

**Remark (the sesquilinear product is not associative).** The product $\star$ is not associative: $(S\star T)\star U=ST^{*}U^{*}$ while $S\star(T\star U)=S\,U\,T^{*}$, and the two agree exactly when $T^{*}U^{*}=UT^{*}$. This is the matrix form of the general fact that the derived product of a sesquialgebra is the product of the algebra with the involution and not the product of the algebra, so the associativity of $M_{n}(\mathbb{C})$ is the associativity of $ST$ and not of $S\star T$.

## Hermitian, Skew-Hermitian and Unitary Matrices

### Hermitian and Skew-Hermitian

**Definition.** A matrix $X$ is **Hermitian** when $X^{*}=X$ and **skew-Hermitian** when $X^{*}=-X$. Both classes are closed under real linear combinations, and each is a real form of the complex space $M_{n}(\mathbb{C})$.

**Theorem (the decomposition).** Every matrix is the sum of a Hermitian and a skew-Hermitian matrix, in one way,

$$
X=\tfrac{1}{2}(X+X^{*})+\tfrac{1}{2}(X-X^{*}) ,
$$

and the two parts are Hermitian and skew-Hermitian respectively.

**Proof.** The two parts are $\tfrac12(X+X^{*})$ and $\tfrac12(X-X^{*})$, whose adjoints are themselves and their negatives because $(X^{*})^{*}=X$. If $X=H+K$ with $H$ Hermitian and $K$ skew-Hermitian then $X^{*}=H-K$, so $H=\tfrac12(X+X^{*})$ and $K=\tfrac12(X-X^{*})$, which is uniqueness. $\square$

**Remark (the real form of the Hermitian matrices).** A matrix is Hermitian exactly when its diagonal entries are real and its entries satisfy $X_{ij}=\overline{X_{ji}}$; the conjugated entries off the diagonal are therefore free, and the Hermitian matrices are a real form of $M_{n}(\mathbb{C})$ spanned by $n$ real diagonal entries and $\tfrac{n(n-1)}{2}$ complex off-diagonal entries, which is $n+n(n-1)=n^{2}$ real parameters.

### Unitary Matrices

**Definition.** A matrix $U$ is **unitary** when $U^{*}=U^{-1}$, equivalently $U^{*}U=UU^{*}=I$.

**Theorem (the unitary group).** The unitary matrices form a group under the product, and $|\det U|=1$; the unitary matrices of determinant one form a subgroup.

**Proof.** If $U,V$ are unitary then $(UV)^{*}UV=V^{*}U^{*}UV=V^{*}V=I$, so the product is unitary; $I$ is unitary; and $U^{*}=U^{-1}$ is unitary because $(U^{*})^{*}=U$. For the determinant, $\det(U^{*})=\overline{\det U}$ and $\det(U^{*}U)=\det I=1$, so $|\det U|^{2}=1$. $\square$

**Remark (comparison with the sesquialgebra).** The group is $U(n)$, and it is the group $U(A)$ of the unitary elements of the sesquialgebra $M_{n}(\mathbb{C})$; the skew-Hermitian matrices are its Lie algebra in the sense of *The Unitary Lie Algebra*, and the Hermitian matrices are the $i$-multiple of the skew-Hermitian ones, which is the matrix form of the relation between the two classes.

## The Case $n=2$ and the Biquaternions

### The Pauli Basis

**Definition.** The **Pauli matrices** are

$$
\sigma_{1}=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad \sigma_{2}=\begin{pmatrix}0&-i\\ i&0\end{pmatrix},\qquad \sigma_{3}=\begin{pmatrix}1&0\\0&-1\end{pmatrix} .
$$

**Theorem (the multiplication table).** With $I$ the unit, the Pauli matrices satisfy

$$
\sigma_{j}^{2}=I,\qquad \sigma_{j}\sigma_{k}=-\sigma_{k}\sigma_{j}\ (j\ne k),\qquad \sigma_{1}\sigma_{2}=i\sigma_{3},\quad \sigma_{2}\sigma_{3}=i\sigma_{1},\quad \sigma_{3}\sigma_{1}=i\sigma_{2} .
$$

**Proof.** The three squares are the direct products $\sigma_{1}^{2}=\sigma_{2}^{2}=\sigma_{3}^{2}=I$. The anticommutation and the cyclic products are the three products computed in order: $\sigma_{1}\sigma_{2}=\begin{pmatrix}i&0\\0&-i\end{pmatrix}=i\sigma_{3}$, and the other two follow by the cyclic permutation of the indices. $\square$

**Remark.** The Pauli matrices are Hermitian, they have trace zero, and together with $I$ they span the real space of the Hermitian matrices of order two.

### Hermitian and Unitary Matrices of Order Two

**Proposition (the Hermitian matrices).** Every Hermitian matrix of order two is

$$
X=aI+b\,\sigma_{1}+c\,\sigma_{2}+d\,\sigma_{3},\qquad a,b,c,d\in\mathbb{R} ,
$$

and the four parameters are exactly the $2^{2}=4$ real parameters of the Hermitian matrix.

**Proof.** A Hermitian matrix has the form $\begin{pmatrix}a_{1}&z\\ \overline{z}&a_{2}\end{pmatrix}$ with $a_{1},a_{2}$ real and $z$ complex, and the display is that matrix with $a=\tfrac12(a_{1}+a_{2})$, $d=\tfrac12(a_{1}-a_{2})$, $b=\operatorname{Re}z$, $c=-\operatorname{Im}z$. The correspondence of the four real parameters with the four matrix entries is a bijection. $\square$

**Proposition (the unitary matrices and the unit quaternions).** The unitary matrices of order two with determinant one are exactly the composites $aI+bi\,\sigma_{3}+ci\,\sigma_{2}+di\,\sigma_{1}$ with $a^{2}+b^{2}+c^{2}+d^{2}=1$, and they correspond to the unit quaternions.

**Proof.** Such a matrix has the shape $\begin{pmatrix}\alpha&\beta\\-\overline{\beta}&\overline{\alpha}\end{pmatrix}$ with $|\alpha|^{2}+|\beta|^{2}=1$, which is unimodular and unitary; conversely a unimodular unitary matrix of order two has this shape, since its two columns are perpendicular and each of modulus one. Writing $\alpha=a+bi$, $\beta=c+di$ gives the display with $a^{2}+b^{2}+c^{2}+d^{2}=1$, which is the unit sphere of the quaternions. $\square$

### The Identification with the Biquaternion Algebra

**Theorem (the matrix model).** The biquaternion algebra $\mathbb{B}=\mathbb{H}\otimes_{\mathbb{R}}\mathbb{C}$ is isomorphic to $M_{2}(\mathbb{C})$ as a $\mathbb{C}$-algebra, by the assignment

$$
i\longmapsto i\,\sigma_{3},\qquad j\longmapsto i\,\sigma_{2},\qquad k\longmapsto i\,\sigma_{1} ,
$$

under which the relations $i^{2}=j^{2}=k^{2}=-1$, $ij=k$, $jk=i$, $ki=j$ of the quaternions hold.

**Proof.** The three images are the matrices $i\sigma_{3}$, $i\sigma_{2}$, $i\sigma_{1}$; their squares are $-I$ because $\sigma_{j}^{2}=I$, and the three products are $i\sigma_{3}\cdot i\sigma_{2}=-\sigma_{3}\sigma_{2}=i\sigma_{1}$, $i\sigma_{2}\cdot i\sigma_{1}=-\sigma_{2}\sigma_{1}=i\sigma_{3}$ and $i\sigma_{1}\cdot i\sigma_{3}=-\sigma_{1}\sigma_{3}=i\sigma_{2}$, by the multiplication table above, which is $ij=k$, $jk=i$, $ki=j$. So the assignment extends to a homomorphism $\mathbb{B}\to M_{2}(\mathbb{C})$ of $\mathbb{C}$-algebras, which is an isomorphism because the images are linearly independent and the two algebras have the same complex rank, namely four. $\square$

**Proposition (the involution and the two products).** Under the isomorphism the conjugate transpose of $M_{2}(\mathbb{C})$ is the quaternionic conjugation extended to $\mathbb{B}$, sending $i,j,k$ to their negatives; and the two products correspond, the ordinary product $ST$ to the complex bilinear product of $\mathbb{B}$ and the sesquilinear product $S\star T=ST^{*}$ to the complex sesquilinear product $\tilde P\tilde Q^{*}$.

**Proof.** The conjugate transpose of the image of a quaternion $a+bi+cj+dk$ is the image of $a-bi-cj-dk$: the images of $i,j,k$ are the matrices $i\sigma_{3}$, $i\sigma_{2}$, $i\sigma_{1}$, and the conjugate transpose of $i\sigma_{1}$ is $-i\sigma_{1}$ because $\sigma_{1}$ is real symmetric while of $i\sigma_{2}$ and $i\sigma_{3}$ is the negative because those are skew-Hermitian; so the involution on $M_{2}(\mathbb{C})$ restricts to the quaternionic conjugation and extends to it on the complexification. The two product statements are then the definition of the two products on each side. $\square$

**Remark (the place of the four products).** The biquaternion algebra carries four products, and exactly two of them are $\mathbb{C}$-bilinear and exactly two are sesquilinear for the base conjugation, the split recorded in *Comparison Between the Four Biquaternion Products*; the ordinary and the sesquilinear product of this article are the matrix reads of the complex bilinear and the complex sesquilinear members of that family, which is why $M_{2}(\mathbb{C})$ is the model in which the biquaternion structure is computed.

## The General Case

For general $n$ the structure is the same and the tabulation is shorter. The Hermitian matrices $X^{*}=X$ form a real form of $M_{n}(\mathbb{C})$ with $n^{2}$ real parameters, on which the pairing $\varphi(X,Y)=\operatorname{tr}(XY^{*})$ is the standard Hermitian form, and the skew-Hermitian matrices are its $i$-multiple. The unitary matrices form the group $U(n)$, the determinant has modulus one, and the matrices of determinant one form the subgroup $SU(n)$, which in the case $n=2$ is the unit quaternions read through the matrix model above. The endomorphism algebra of the biquaternion algebra as a complex space is the case $n=4$, $\operatorname{End}_{\mathbb{C}}(\mathbb{B})\cong M_{4}(\mathbb{C})$, so the case $n=4$ of this article is the sesquilinear structure of the biquaternion algebra read on its coordinates, and the case $n=2$ is the biquaternion algebra itself.

## Summary

The complex matrices $M_{n}(\mathbb{C})$ with the conjugate transpose form the standard sesquialgebra over $\mathbb{C}$: the involution is $\varsigma$-semilinear of order two, $(XY)^{*}=Y^{*}X^{*}$ and $(\lambda X)^{*}=\overline{\lambda}\,X^{*}$; the trace is central and compatible, $\operatorname{tr}(X^{*})=\varsigma(\operatorname{tr}X)$; and the pairing $\varphi(X,Y)=\operatorname{tr}(XY^{*})=\sum_{i,j}X_{ij}\overline{Y_{ij}}$ is the standard Hermitian form, perfect on the $n^{2}$ coordinates.

The structure carries two products: the ordinary product $ST$, which is $\mathbb{C}$-bilinear and associative, and the sesquilinear product $S\star T=ST^{*}$, the derived product of the sesquialgebra, which is $\mathbb{C}$-linear in the first slot and conjugate-linear in the second, has $I$ as a right unit, and is not associative. The elements singled out by the involution are the Hermitian and skew-Hermitian matrices, one the $i$-multiple of the other and together a decomposition $X=\tfrac12(X+X^{*})+\tfrac12(X-X^{*})$ of every matrix, and the unitary matrices, a group with the determinant of modulus one.

The case $n=2$ is worked on the Pauli basis $\sigma_{1},\sigma_{2},\sigma_{3}$: the Hermitian matrices are $aI+b\sigma_{1}+c\sigma_{2}+d\sigma_{3}$ with real parameters, the unimodular unitary matrices are the unit quaternions, and the isomorphism $\mathbb{B}=\mathbb{H}\otimes_{\mathbb{R}}\mathbb{C}\cong M_{2}(\mathbb{C})$ by $i\mapsto i\sigma_{3}$, $j\mapsto i\sigma_{2}$, $k\mapsto i\sigma_{1}$ carries the conjugate transpose to the quaternionic conjugation and the two products to two of the four biquaternion products. For general $n$ the Hermitian form has $n^{2}$ real parameters, the unitary matrices are $U(n)$, and the case $n=4$ is $\operatorname{End}_{\mathbb{C}}(\mathbb{B})\cong M_{4}(\mathbb{C})$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $X^{*}=\overline{X}^{T}$ | the conjugate transpose, the involution |
| $\varsigma(z)=\overline{z}$ | the base involution, the complex conjugation |
| $\operatorname{tr}(X)=\sum_{i}X_{ii}$ | the trace, central and compatible |
| $\varphi(X,Y)=\operatorname{tr}(XY^{*})$ | the pairing, the standard Hermitian form |
| $S\star T=ST^{*}$ | the sesquilinear product, the derived product |
| $X^{*}=X$ / $X^{*}=-X$ | Hermitian / skew-Hermitian matrices |
| $X=\tfrac12(X+X^{*})+\tfrac12(X-X^{*})$ | the Hermitian–skew decomposition |
| $U^{*}=U^{-1}$, $\lvert\det U\rvert=1$ | unitary matrices, the group $U(n)$ |
| $\sigma_{1},\sigma_{2},\sigma_{3}$ | the Pauli matrices |
| $aI+b\sigma_{1}+c\sigma_{2}+d\sigma_{3}$ | the Hermitian matrices of order two |
| $\mathbb{B}\cong M_{2}(\mathbb{C})$, $i\mapsto i\sigma_{3}$, $j\mapsto i\sigma_{2}$, $k\mapsto i\sigma_{1}$ | the biquaternion matrix model |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis*, 2nd ed. (Cambridge University Press, 2013), for the Hermitian, skew-Hermitian and unitary matrices, the Schur and spectral theorems and the unitary group.
- F. R. Gantmacher, *The Theory of Matrices*, vol. 1 (Chelsea, 1959), for the trace, the matrix units and the canonical forms of the complex matrices.
- Kenneth Hoffman and Ray Kunze, *Linear Algebra*, 2nd ed. (Prentice-Hall, 1971), for the sesquilinear and Hermitian forms, the adjoint of a linear transformation and the unitary group of a form.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for the quaternions, the Pauli matrices and the identification of the quaternion algebra with the complex matrices of order two.
- The companion articles of this series: *Sesquialgebras*, *The Sesquilinear Product*, *The Sesquilinear Structure of the Endomorphism Algebra*, *Hermitian and Skew-Hermitian Elements*, *Units and the Unitary Elements*, *The Unitary Lie Algebra*, *The Four Biquaternion Complex Products* and *Comparison Between the Four Biquaternion Products*.
