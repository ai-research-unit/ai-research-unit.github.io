
# __Lattices and the Quaternion Lattice__

## Introduction

A lattice is a free abelian group of finite rank together with a chosen embedding in a real vector space, so that a discrete geometry is available; equivalently, it is a free $\mathbb{Z}$-module of finite rank with a positive definite form on the real vector space it spans. The quaternions furnish the standard four-dimensional example: the integer quaternions form the Lipschitz lattice, and adjoining the half-integral element $\tfrac12(1+e_1+e_2+e_3)$ gives the Hurwitz lattice, which contains the Lipschitz lattice with index $2$. This article treats both strictly as free $\mathbb{Z}$-modules with rank, index, covolume and base change; the multiplicative structure of the quaternions, and the fact that these lattices are orders in a division algebra rather than merely sublattices, belongs to *Division Algebras*; it is used here only where the norm form carries it.

Throughout, a lattice is a free $\mathbb{Z}$-module $\Lambda$ of finite rank $n$ together with an $\mathbb{R}$-linear embedding $\Lambda \otimes_{\mathbb{Z}}\mathbb{R} \hookrightarrow \mathbb{R}^n$ and a positive definite form on $\mathbb{R}^n$; the base change $\Lambda \otimes_{\mathbb{Z}}\mathbb{R}$ is the real span of $\Lambda$. The extension and restriction of scalars of *Extension of Scalars* is used throughout, and the structure theory of finitely generated $\mathbb{Z}$-modules of *Finitely Generated Abelian Groups* supplies the index computations; both are articles of Part I, and the positive definite form that makes a lattice a quadratic space is the subject of the present category, so the article is placed here rather than with the module theory.

## Lattices as Free $\mathbb{Z}$-Modules

### Definition and Rank

**Definition.** A **lattice** is a free $\mathbb{Z}$-module $\Lambda$ of finite rank $n$; its **rank** is $n$. A **sublattice** is a subgroup $\Lambda' \subseteq \Lambda$ that is free of the same rank; it then has finite index. An **embedded lattice** is a lattice $\Lambda$ together with an injective linear map $\Lambda \otimes_{\mathbb{Z}}\mathbb{R} \to \mathbb{R}^n$ whose image spans, and a positive definite inner product on $\mathbb{R}^n$.

**Proposition.** Let $\Lambda' \subseteq \Lambda$ be sublattices of the same rank $n$, with $\mathbb{Z}$-bases $u_1,\dots,u_n$ and $v_1,\dots,v_n$. Write $v_j=\sum_i a_{ij}u_i$ with $a_{ij} \in \mathbb{Z}$; then $A=(a_{ij})$ is an integer matrix of nonzero determinant and

$$
[\Lambda:\Lambda']=|\det A| .
$$

*Proof.* By the structure theorem for finitely generated $\mathbb{Z}$-modules, the Smith normal form $\operatorname{diag}(d_1,\dots,d_n)$ of $A$ satisfies $\Lambda/\Lambda' \cong \bigoplus_i\mathbb{Z}/d_i\mathbb{Z}$, where the $d_i$ are the invariant factors, each positive because the rank is the same; the order of the quotient is $\prod_i d_i=|\det A|$, which is the index. $\square$

**Definition.** For an embedded lattice $\Lambda$ with a $\mathbb{Z}$-basis $v_1,\dots,v_n$, the **Gram matrix** is $G=(v_i \cdot v_j)$ and the **covolume** is $\operatorname{covol}(\Lambda)=\sqrt{\det G}$, the $n$-dimensional volume of the fundamental parallelepiped. For two sublattices of the same rank,

$$
[\Lambda:\Lambda']=\frac{\operatorname{covol}(\Lambda')}{\operatorname{covol}(\Lambda)} .
$$

*Proof.* The determinant of $A$ relates the two Gram matrices by $G'=A^{\mathsf{T}}GA$, so $\det G'=(\det A)^2\det G$ and the covolumes are in the ratio $|\det A|$, which is the index. $\square$

### Base Change

**Proposition.** Let $\Lambda$ be a lattice of rank $n$. Then $\Lambda \otimes_{\mathbb{Z}}\mathbb{R} \cong \mathbb{R}^n$ as $\mathbb{R}$-modules, and for any ring homomorphism $\mathbb{Z} \to R$ the base change $\Lambda \otimes_{\mathbb{Z}}R$ is a free $R$-module of rank $n$. In particular rank is preserved by base change from $\mathbb{Z}$ to $\mathbb{R}$, to $\mathbb{C}$ or to $\mathbb{Z}/m\mathbb{Z}$.

*Proof.* This is the statement $R \otimes_{\mathbb{Z}}\mathbb{Z}^n \cong R^n$ of the companion article on extension of scalars, applied to $\Lambda \cong \mathbb{Z}^n$. $\square$

## The Quaternion Lattice

### The Lipschitz Lattice

**Definition.** The algebra of quaternions is $\mathbb{H}=\mathbb{R} \oplus \mathbb{R}e_1 \oplus \mathbb{R}e_2 \oplus \mathbb{R}e_3$ with $e_k^2=-1$ and $e_ie_j=\varepsilon_{ijk}e_k$ for $(i,j,k)$ a cyclic permutation of $(1,2,3)$. The **Lipschitz lattice** is the free abelian group

$$
\mathbb{H}(\mathbb{Z})=\mathbb{Z} \oplus \mathbb{Z}e_1 \oplus \mathbb{Z}e_2 \oplus \mathbb{Z}e_3 \subseteq \mathbb{H},
$$

of rank $4$ over $\mathbb{Z}$, with the standard basis $1,e_1,e_2,e_3$.

**Proposition.** (i) As a $\mathbb{Z}$-module, $\mathbb{H}(\mathbb{Z}) \cong \mathbb{Z}^4$, and its base change is the module of the algebra: $\mathbb{H}(\mathbb{Z}) \otimes_{\mathbb{Z}}\mathbb{R} \cong \mathbb{H}$ as $\mathbb{R}$-modules, of dimension $4$; more generally $\mathbb{H}(\mathbb{Z}) \otimes_{\mathbb{Z}}\mathbb{C} \cong \mathbb{B}$ as $\mathbb{C}$-modules, of complex dimension $4$.

(ii) The **norm** $N(x)=x\bar x$ of $x=a_0+a_1e_1+a_2e_2+a_3e_3$ is $N(x)=a_0^2+a_1^2+a_2^2+a_3^2$, an integer for $x \in \mathbb{H}(\mathbb{Z})$; the polar form is $(x,y)=\operatorname{Sc}(x\bar y)=a_0b_0+a_1b_1+a_2b_2+a_3b_3$, the Euclidean inner product of the coefficient vectors.

(iii) The Gram matrix of the standard basis is the identity, so $\operatorname{covol}(\mathbb{H}(\mathbb{Z}))=1$, and $\mathbb{H}(\mathbb{Z})$ is self-dual for the form $(x,y)=\operatorname{Sc}(x\bar y)$.

*Proof.* (i) The first statement is the definition and the base-change proposition. For the second, $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}=\mathbb{B}$ is the biquaternion algebra, of real dimension $8$, hence of complex dimension $4$; the module statement is immediate from $R\otimes_{\mathbb{Z}}\mathbb{Z}^4 \cong R^4$. (ii) Expanding $x\bar x$ with $\bar x=a_0-a_1e_1-a_2e_2-a_3e_3$, the cross terms cancel and the squares contribute $a_i^2$ because $e_i^2=-1$; the scalar part of $x\bar y$ is the stated dot product. (iii) With the standard basis, $(e_i,e_j)=\delta_{ij}$ and $(1,1)=1$, so $G=I$. Self-duality: $y \in \mathbb{H}(\mathbb{Z})^*$ means $\operatorname{Sc}(x\bar y) \in \mathbb{Z}$ for all $x \in \mathbb{H}(\mathbb{Z})$; taking $x \in \{1,e_1,e_2,e_3\}$ gives the coordinates of $y$ integral, so $y \in \mathbb{H}(\mathbb{Z})$. $\square$

**Remark.** The norm form is multiplicative, $N(xy)=N(x)N(y)$, because $\overline{xy}=\bar y\bar x$; this is the algebra-level statement used by the four-square theorem, and it is mentioned only to explain why the norm is the natural form on these lattices.

### The Hurwitz Lattice

**Definition.** Let $\omega=\tfrac12(1+e_1+e_2+e_3)$. The **Hurwitz lattice** is

$$
\mathbb{H}'(\mathbb{Z})=\mathbb{Z} \oplus \mathbb{Z}e_1 \oplus \mathbb{Z}e_2 \oplus \mathbb{Z}e_3 \oplus \mathbb{Z}\omega ,
$$

the subgroup generated by $\mathbb{H}(\mathbb{Z})$ and $\omega$.

**Proposition.** (i) $\mathbb{H}'(\mathbb{Z})$ is free of rank $4$ with basis $\omega,e_1,e_2,e_3$, and it contains $\mathbb{H}(\mathbb{Z})$ as a sublattice of index $2$; the quotient $\mathbb{H}'(\mathbb{Z})/\mathbb{H}(\mathbb{Z}) \cong \mathbb{Z}/2\mathbb{Z}$.

(ii) The norm is integer-valued on $\mathbb{H}'(\mathbb{Z})$: every element of $\mathbb{H}'(\mathbb{Z})$ has coordinates $b_0,b_1,b_2,b_3$ in $\tfrac12\mathbb{Z}$ that are either all integers or all odd half-integers, and then $N(y)=\sum_ib_i^2$ is an integer, since a square of an odd half-integer contributes $\tfrac14$ of an odd square and four such contributions sum to an integer.

(iii) The Gram matrix of the basis $\omega,e_1,e_2,e_3$ for the polar form $(x,y)=\operatorname{Sc}(x\bar y)$ is

$$
G'=\begin{pmatrix}1&\tfrac12&\tfrac12&\tfrac12\\ \tfrac12&1&0&0\\ \tfrac12&0&1&0\\ \tfrac12&0&0&1\end{pmatrix}, \qquad \det G'=\tfrac14,
$$

so $\operatorname{covol}(\mathbb{H}'(\mathbb{Z}))=\tfrac12$ and the index relation $\operatorname{covol}(\mathbb{H})/\operatorname{covol}(\mathbb{H}')=2$ recovers $[\mathbb{H}':\mathbb{H}]=2$.

*Proof.* (i) Every element is $u+t\omega$ with $u \in \mathbb{H}(\mathbb{Z})$ and $t \in \mathbb{Z}$; writing $u=a_0+a_1e_1+a_2e_2+a_3e_3$, the coefficients of $u+t\omega$ are $a_0+t/2$ and $a_i+t/2$. The map $\mathbb{H}'(\mathbb{Z}) \to \mathbb{Z}/2$ sending $u+t\omega$ to $t \bmod 2$ is a surjection with kernel $\mathbb{H}(\mathbb{Z})$, so the quotient is $\mathbb{Z}/2$ and the index is $2$; the elements $\omega,e_1,e_2,e_3$ are visibly independent over $\mathbb{Z}$, so the rank is $4$ and the index formula gives $|\det(\text{inclusion})|=2$, whose Smith normal form is $\operatorname{diag}(1,1,1,2)$.

(ii) The coordinates of $y$ satisfy $y=\sum a_ie_i$ with $e_0=1$; if $t$ is even the coefficients $a_i+t/2$ are integers and the sum of their squares is an integer; if $t$ is odd they are all odd half-integers $c_i/2$ with $c_i$ odd, and $\sum_i(c_i/2)^2=\tfrac14\sum_ic_i^2$ is an integer because each odd square is $1 \bmod 8$ and the sum of four of them is $4 \bmod 8$, making $\sum_ic_i^2$ divisible by $4$.

(iii) $(e_i,e_j)=\delta_{ij}$ and $(e_i,\omega)=-\operatorname{Sc}(e_i\omega)$. Since $\omega e_1=\tfrac12(e_1-1+e_2-e_3)$ has scalar part $-\tfrac12$, one gets $(\omega,e_1)=\tfrac12$, and similarly for $e_2,e_3$; $(\omega,\omega)=N(\omega)=1$. A block determinant gives $\det G'=\det I_3\cdot\bigl(1-\tfrac14(1,1,1)I_3^{-1}(1,1,1)^{\mathsf{T}}\bigr)=1-\tfrac34=\tfrac14$, using the block formula for a partitioned matrix. Hence $\operatorname{covol}=\tfrac12$, and the covolume ratio is $2$. $\square$

The two lattices are both integral for the norm form, and the half-integral element $\omega$ has integral norm $1$; the sublattice relation between them is index $2$, and the duality computation inverts this index.

## Sublattices, Index and Duality

**Proposition.** (i) There is no lattice strictly between $\mathbb{H}(\mathbb{Z})$ and $\mathbb{H}'(\mathbb{Z})$; equivalently the quotient $\mathbb{H}'(\mathbb{Z})/\mathbb{H}(\mathbb{Z}) \cong \mathbb{Z}/2\mathbb{Z}$ has prime order.

(ii) For the form $(x,y)=\operatorname{Sc}(x\bar y)$ the Lipschitz lattice is self-dual, $\mathbb{H}(\mathbb{Z})^*=\mathbb{H}(\mathbb{Z})$, while the dual of the Hurwitz lattice is

$$
\mathbb{H}'(\mathbb{Z})^*=\{y \in \mathbb{H}(\mathbb{Z}): y_0+y_1+y_2+y_3 \equiv 0 \pmod 2\},
$$

a sublattice of $\mathbb{H}(\mathbb{Z})$ of index $2$ and covolume $2$; thus $\mathbb{H}'(\mathbb{Z})$ is not self-dual and $[\mathbb{H}'(\mathbb{Z}):\mathbb{H}'(\mathbb{Z})^*]=4$.

(iii) The lattice $\tfrac12\mathbb{H}(\mathbb{Z})$ contains $\mathbb{H}'(\mathbb{Z})$ with index $8$ and covolume $\tfrac1{16}$.

*Proof.* (i) A lattice $M$ with $\mathbb{H} \subsetneq M \subseteq \mathbb{H}'$ has quotient $M/\mathbb{H}$ a nonzero subgroup of $\mathbb{H}'/\mathbb{H} \cong \mathbb{Z}/2$, hence equal to the whole of it, so $M=\mathbb{H}'$. (ii) The self-duality of $\mathbb{H}$ was shown. For $\mathbb{H}'$ with basis $\omega,e_1,e_2,e_3$, a vector $y$ lies in the dual exactly when $y \cdot e_i \in \mathbb{Z}$ for $i=1,2,3$, forcing $y_1,y_2,y_3 \in \mathbb{Z}$, and $y \cdot \omega=\tfrac12(y_0+y_1+y_2+y_3) \in \mathbb{Z}$, forcing $y_0 \in \mathbb{Z}$ with $y_0+y_1+y_2+y_3$ even; this is the displayed sublattice. Its index in $\mathbb{H}(\mathbb{Z})$ is $2$, since it is the kernel of the surjection $\mathbb{H}(\mathbb{Z}) \to \mathbb{Z}/2$, $y \mapsto y_0+y_1+y_2+y_3$. Duality inverts covolume, so $\operatorname{covol}((\mathbb{H}')^*)=1/\operatorname{covol}(\mathbb{H}')=2$, and $[\mathbb{H}':(\mathbb{H}')^*]=\operatorname{covol}((\mathbb{H}')^*)/\operatorname{covol}(\mathbb{H}')=4$, consistent with the chain $(\mathbb{H}')^* \subset \mathbb{H} \subset \mathbb{H}'$ of successive index $2$. (iii) The covolume of $\tfrac12\mathbb{H}$ is $2^{-4}=\tfrac1{16}$, so the index is $\operatorname{covol}(\mathbb{H}')/\operatorname{covol}(\tfrac12\mathbb{H})=(\tfrac12)/(\tfrac1{16})=8$. $\square$

**Remark.** Duality for a form inverts index and covolume: the dual of a sublattice of index $m$ in a unimodular lattice has index $m$ and lies on the other side, and a sublattice containing the unimodular one has a dual contained in it. Here $\mathbb{H}$ is unimodular, so $\mathbb{H}'$ of index $2$ has $(\mathbb{H}')^*$ of index $2$ inside $\mathbb{H}$, and the chain $(\mathbb{H}')^* \subset \mathbb{H} \subset \mathbb{H}'$ has successive indices $2,2$.

## Base Change and Dimension

**Proposition.** The ranks and dimensions of the lattices over their various base rings are:

| Lattice | over $\mathbb{Z}$ | over $\mathbb{R}$ | over $\mathbb{C}$ |
|---|---|---|---|
| $\mathbb{H}(\mathbb{Z})$ | rank $4$ | $\dim_{\mathbb{R}}\mathbb{H}=4$ | $\dim_{\mathbb{C}}\mathbb{B}=4$ |
| $\mathbb{H}'(\mathbb{Z})$ | rank $4$ | $\dim_{\mathbb{R}}\mathbb{H}=4$ | $\dim_{\mathbb{C}}\mathbb{B}=4$ |

Both lattices span the same real vector space $\mathbb{H}$, since $\omega=\tfrac12(1+e_1+e_2+e_3)$ is an $\mathbb{R}$-linear combination of the standard basis, and both complexify to $\mathbb{B}$; the base change forgets the index and remembers only the rank, because $\mathbb{R} \otimes_{\mathbb{Z}}\mathbb{H}(\mathbb{Z}) \cong \mathbb{R} \otimes_{\mathbb{Z}}\mathbb{H}'(\mathbb{Z}) \cong \mathbb{H}$ and $\mathbb{Q} \otimes_{\mathbb{Z}}\mathbb{H}(\mathbb{Z}) \cong \mathbb{Q} \otimes_{\mathbb{Z}}\mathbb{H}'(\mathbb{Z}) \cong \mathbb{H}(\mathbb{Q})=\mathbb{Q} \oplus \mathbb{Q}e_1 \oplus \mathbb{Q}e_2 \oplus \mathbb{Q}e_3$.

*Proof.* The dimensions are the base-change proposition: $\mathbb{Z}^4 \otimes_{\mathbb{Z}}R \cong R^4$ for $R=\mathbb{R},\mathbb{C},\mathbb{Q}$, and $\dim_{\mathbb{R}}\mathbb{H}=4$, $\dim_{\mathbb{C}}\mathbb{B}=4$; the two lattices have the same real span because they have the same rank and both lie in $\mathbb{H}$. $\square$

**Remark.** This is the module-level content of the quaternion lattice: rank, index, covolume, duality, and base change recovering real and complex vector spaces of the same rank. The product, the norm's multiplicativity, the maximality of the Hurwitz order and the resulting arithmetic of sums of four squares are algebra-level statements, and they belong to the companion category.

## Summary

A lattice is a free $\mathbb{Z}$-module of finite rank, embedded in a real vector space with a positive definite form; a sublattice of the same rank has finite index equal to the absolute value of the determinant of the change-of-basis matrix, and for embedded lattices the index is the ratio of covolumes, where the covolume is the square root of the determinant of the Gram matrix. Base change along $\mathbb{Z} \to R$ sends a lattice of rank $n$ to the free $R$-module of rank $n$, so rank is preserved by extension of scalars to $\mathbb{R}$, to $\mathbb{C}$ or to $\mathbb{Q}$.

The Lipschitz lattice $\mathbb{H}(\mathbb{Z})=\mathbb{Z} \oplus \mathbb{Z}e_1 \oplus \mathbb{Z}e_2 \oplus \mathbb{Z}e_3$ is free of rank $4$, base changes to $\mathbb{H}=\mathbb{H}(\mathbb{Z})\otimes_{\mathbb{Z}}\mathbb{R}$ and to the biquaternions $\mathbb{B}=\mathbb{H}(\mathbb{Z})\otimes_{\mathbb{Z}}\mathbb{C}$ at the module level, carries the integer-valued norm $N(x)=a_0^2+a_1^2+a_2^2+a_3^2$ with polar form the Euclidean dot product, has Gram matrix the identity and covolume $1$, and is self-dual. The Hurwitz lattice $\mathbb{H}'(\mathbb{Z})=\mathbb{H}(\mathbb{Z}) \oplus \mathbb{Z}\omega$ with $\omega=\tfrac12(1+e_1+e_2+e_3)$ is free of rank $4$ on the basis $\omega,e_1,e_2,e_3$, contains the Lipschitz lattice with index $2$ and covolume $\tfrac12$, and has an integer-valued norm; its Gram determinant is $\tfrac14$, and the index and covolume computations agree. The Lipschitz lattice is a maximal proper sublattice of the Hurwitz lattice, the two have the same real and complex spans, and the further multiplicative and arithmetic structure of these orders is treated in the companion category.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Lambda$, $\Lambda'$ | lattices, free $\mathbb{Z}$-modules |
| $n$ | rank of a lattice |
| $[\Lambda:\Lambda']$ | index of a sublattice |
| $A=(a_{ij})$ | change-of-basis matrix |
| $G=(v_i\cdot v_j)$ | Gram matrix |
| $\operatorname{covol}(\Lambda)=\sqrt{\det G}$ | covolume |
| $\Lambda^*$ | dual lattice with respect to a form |
| $\mathbb{H}(\mathbb{Z})$ | Lipschitz lattice, rank $4$ |
| $\mathbb{H}'(\mathbb{Z})$ | Hurwitz lattice, rank $4$ |
| $\omega=\tfrac12(1+e_1+e_2+e_3)$ | half-integral generator |
| $N(x)=x\bar x$ | norm form, $a_0^2+a_1^2+a_2^2+a_3^2$ |
| $(x,y)=\operatorname{Sc}(x\bar y)$ | polar form, Euclidean dot product |
| $e_0=1,e_1,e_2,e_3$ | quaternion basis, $e_k^2=-1$ |
| $\mathbb{H}$, $\mathbb{B}$ | quaternions and biquaternions |
| $R$ | base ring for extension of scalars |



## Further Reading

- John H. Conway and Neil J. A. Sloane, *Sphere Packings, Lattices and Groups* (Springer, 3rd ed. 1999), for lattices, covolumes and the quaternionic examples.
- John Voight, *Quaternion Algebras* (Springer, 2021), for orders, the Lipschitz and Hurwitz orders, and their arithmetic.
- Marie-France Vignéras, *Arithmétique des algèbres de quaternions* (Springer, 1980), for maximal orders and norms.
- Jean-Pierre Serre, *A Course in Arithmetic* (Springer, 1973), for the four-square theorem and the theta series of these lattices.
- Henri Cohen, *A Course in Computational Algebraic Number Theory* (Springer, 1993), for lattice algorithms and covolume computations.
- Martin Eichler, *Quadratische Formen und orthogonale Gruppen* (Springer, 1952), for integral quadratic forms on lattices.
