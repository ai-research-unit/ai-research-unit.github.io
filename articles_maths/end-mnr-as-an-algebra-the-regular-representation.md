# __$\operatorname{End}(M_n(\mathbb{R}))$ as an Algebra: the Regular Representation__

## Introduction

**The algebra of linear maps of $M_n(\mathbb{R})$ is an algebra of dimension $n^{4}$, and it contains two copies of $M_n(\mathbb{R})$ that commute: the left and the right multiplications.** The two copies meet in the scalars, their sum has dimension $2n^{2}-1$, and the products of their elements generate the whole algebra.

The article defines the two regular representations, proves that they commute and that each is injective, computes the dimension of their sum and the dimension of the algebra they generate, identifies the commutant of each with the other, states the double centraliser theorem in this case, and computes the trace and the determinant of a left multiplication. It assumes *The Matrix Algebra $M_n(\mathbb{R})$* for the algebra, its centre and its simplicity, and *The Ideals, the Centre and the Simplicity of $M_n(\mathbb{R})$* for the two-sided ideals.

## The Algebra of the Operators

**Definition.** $\operatorname{End}(M_n(\mathbb{R}))$ is the algebra of all linear maps $T:M_n(\mathbb{R})\to M_n(\mathbb{R})$, with the composition as product.

**Its dimension is $n^{4}$.** A linear map is determined by its values on a basis, and $M_n(\mathbb{R})$ has a basis of $n^{2}$ elements, each sent to an element of an $n^{2}$-dimensional space. So

$$
\dim\operatorname{End}(M_n(\mathbb{R}))=(n^{2})^{2}=n^{4}.
$$

**It is a matrix algebra in its own right.** Choose the basis $E_{11},E_{12},\dots,E_{nn}$ and stack the coordinates of $X$ into a column of length $n^{2}$; every linear map becomes an $n^{2}\times n^{2}$ matrix, and the algebra is $M_{n^{2}}(\mathbb{R})$.

**The product is composition.** For $S,T\in\operatorname{End}$, $(ST)(X)=S(T(X))$, and the unit is the identity map $\mathrm{id}$. The algebra is not commutative for $n\ge2$, since the operators of the next sections do not commute with arbitrary ones.

## The Left Multiplication

**Definition.** For $A\in M_n(\mathbb{R})$ put $L_A(X)=AX$.

**It is linear.** $L_A(\alpha X+\beta Y)=A(\alpha X+\beta Y)=\alpha AX+\beta AY$, by bilinearity of the matrix product.

**The map $A\mapsto L_A$ is injective.** If $L_A=0$ then $AX=0$ for every $X$, and taking $X=\mathrm{I}$ gives $A=0$. So the kernel of the map is zero and its image is a subspace of dimension $n^{2}$.

**It is an algebra homomorphism.** $L_AL_B(X)=A(BX)=(AB)X=L_{AB}(X)$ for every $X$, so

$$
L_AL_B=L_{AB}.
$$

Hence $A\mapsto L_A$ is an isomorphism from $M_n(\mathbb{R})$ onto its image. The image is a subalgebra of $\operatorname{End}$ isomorphic to $M_n(\mathbb{R})$, of dimension $n^{2}$.

**The image is not all of $\operatorname{End}$.** Its dimension $n^{2}$ is smaller than $n^{4}$ for $n\ge2$, so most operators are not left multiplications: an operator that mixes the columns of $X$ cannot be of the form $X\mapsto AX$.

**A characterisation.** An operator is a left multiplication exactly when it commutes with all right multiplications; that is the content of the commutant computation below.

## The Right Multiplication and the Opposite Algebra

**Definition.** For $B\in M_n(\mathbb{R})$ put $R_B(X)=XB$.

**It is linear and injective.** If $R_B=0$ then $XB=0$ for all $X$, and $X=\mathrm{I}$ gives $B=0$.

**It reverses the order of the product.** $R_BR_C(X)=(XC)B=X(CB)=R_{CB}(X)$, so

$$
R_BR_C=R_{CB}.
$$

The map is therefore not a homomorphism from $M_n(\mathbb{R})$ but from the opposite algebra $M_n(\mathbb{R})^{\mathrm{op}}$, which has the same elements and the product $B\cdot C=CB$. With that product, $B\mapsto R_B$ is an isomorphism onto its image, of dimension $n^{2}$.

**The two images are different.** $L_A$ acts on the left of every $X$ and $R_B$ on the right, and $L_A=R_B$ forces $A=B=\lambda\mathrm{I}$, as the next section shows.

**Both are copies of the same algebra.** $M_n(\mathbb{R})$ and $M_n(\mathbb{R})^{\mathrm{op}}$ are isomorphic through the transpose, $A\mapsto A^{\mathsf T}$, since $(AB)^{\mathsf T}=B^{\mathsf T}A^{\mathsf T}$. So the two images are abstractly the same algebra, sitting in $\operatorname{End}$ in two different ways.

## The Two Commute

**Theorem.** For all $A,B\in M_n(\mathbb{R})$,

$$
L_AR_B=R_BL_A .
$$

*Proof.* Both sides send $X$ to $AXB$: the left one applies $R_B$ first and then $L_A$, the right one the other way, and the matrix product is associative.

**The identity is the whole point of the construction.** It says that the two copies commute elementwise, so the pair $(A,B)$ defines a single operator $X\mapsto AXB$, and the sum $L_A+R_B$ is again an operator of a simple form.

**The pairs inside one family need not commute.** $L_A$ and $L_C$ commute only when $A$ and $C$ commute; it is the left family against the right family that always commutes.

**The commutator vanishes identically.** $[L_A,R_B]=0$ for all $A,B$, so the sum $L(M_n)+R(M_n)$ is a Lie subalgebra of $\operatorname{End}$ with the commutator.

## The Sum of the Two Copies

**Theorem.** $L(M_n(\mathbb{R}))\cap R(M_n(\mathbb{R}))=\{\lambda\,\mathrm{id}:\lambda\in\mathbb{R}\}$.

*Proof.* If $L_A=R_B$ then $AX=XB$ for all $X$. Taking $X=\mathrm{I}$ gives $A=B$. Then $AX=XA$ for all $X$, so $A$ is in the centre of $M_n(\mathbb{R})$, which is $\mathbb{R}\mathrm{I}$. Conversely $L_{\lambda\mathrm{I}}=R_{\lambda\mathrm{I}}=\lambda\,\mathrm{id}$.

**Corollary.** The sum has dimension

$$
n^{2}+n^{2}-1=2n^{2}-1,
$$

because the intersection is one-dimensional. At $n=2$ this is $7$ inside $\dim\operatorname{End}=16$; at $n=3$ it is $17$ inside $81$.

**The sum is a Lie subalgebra but not an associative one.** The bracket of two elements of the sum stays in the sum, since $[L_A,L_C]=L_{[A,C]}$, $[R_B,R_D]=R_{[B,D]}$ and $[L_A,R_B]=0$. The product does not: $L_AR_B$ is $X\mapsto AXB$, which is not of the form $LC+R_D$ in general, and its dimension count shows why, as the next section proves.

## The Products Generate the Whole Algebra

**Theorem.** Every operator is a sum of products $L_AR_B$; equivalently, the algebra generated by the two copies is $\operatorname{End}(M_n(\mathbb{R}))$.

*Proof.* For the matrix units, with $A=E_{il}$ and $B=E_{jl}$,

$$
E_{il}\,X\,E_{jl}=X_{lj}\,E_{il},
$$

because $XE_{jl}=\sum_kX_{kj}E_{kl}$ and $E_{il}E_{kl}=\delta_{lk}E_{il}$. So $L_{E_{il}}R_{E_{jl}}$ is the operator $X\mapsto X_{lj}E_{il}$, a map of rank one with image $\mathbb{R}E_{il}$ and kernel $\{X:X_{lj}=0\}$. As $(i,l)$ and $(j,l)$ range, these $n^{4}$ operators are the rank-one operators of a basis, hence a basis of $\operatorname{End}$.

**The count jumps from $2n^{2}-1$ to $n^{4}$.** The sum of the two copies misses almost everything; the products of the two copies miss nothing. Numerically the $n^{4}$ products span a space of dimension $n^{4}$: $16$ at $n=2$ and $81$ at $n=3$.

**The algebra is a tensor product.** The map $M_n(\mathbb{R})\otimes M_n(\mathbb{R})^{\mathrm{op}}\to\operatorname{End}(M_n(\mathbb{R}))$, $A\otimes B\mapsto L_AR_B$, is an algebra homomorphism, since $(A\otimes B)(C\otimes D)\mapsto L_{AC}R_{DB}$ matches $AC\otimes DB$. Both sides have dimension $n^{4}$, and the source is simple, so the map is an isomorphism:

$$
\operatorname{End}(M_n(\mathbb{R}))\cong M_n(\mathbb{R})\otimes M_n(\mathbb{R})^{\mathrm{op}}\cong M_{n^{2}}(\mathbb{R}).
$$

**In coordinates the isomorphism is the Kronecker product.** With columns stacked, $[L_A]=\mathrm{I}\otimes A$ and $[R_B]=B^{\mathsf T}\otimes\mathrm{I}$, and the products $B^{\mathsf T}\otimes A$ span all of $M_{n^{2}}(\mathbb{R})$.

## The Commutant and the Double Centraliser

**Theorem.** The commutant of $L(M_n)$ in $\operatorname{End}$ is $R(M_n)$, and the commutant of $R(M_n)$ is $L(M_n)$.

*Proof.* Let $T$ commute with every $L_A$ and put $B=T(\mathrm{I})$. For every $X$, $T(X)=T(L_X\mathrm{I})=L_XT(\mathrm{I})=XB=R_B(X)$, so $T=R_B$. Conversely every $R_B$ commutes with every $L_A$ by the identity of the previous section. The same argument with the roles exchanged gives the second statement.

**The commutant has dimension $n^{2}$.** Numerically the space of operators commuting with all left multiplications has dimension $4$ at $n=2$ and $9$ at $n=3$, which is $n^{2}$ in both cases.

**Theorem (double centraliser).** The bicommutant of $L(M_n)$ is $L(M_n)$.

*Proof.* The commutant of $L(M_n)$ is $R(M_n)$, and the commutant of $R(M_n)$ is $L(M_n)$.

**The theorem is the finite-dimensional case of a general statement.** For a faithful module $M$ over an algebra $R$, the endomorphisms of $M$ that commute with the action of $R$ form $\operatorname{End}_R(M)$, and the endomorphisms commuting with those give back $R$ when $R$ is simple. Here $R=M_n(\mathbb{R})$ acts on itself by left multiplication, $\operatorname{End}_R(M_n)$ is the opposite algebra acting by right multiplication, and the double centraliser of $M_n$ in $\operatorname{End}(M_n)$ is $M_n$ again.

**The two theorems differ.** The sum of the two copies has dimension $2n^{2}-1$; the algebra they generate is everything; and the commutant of either copy is the other. The first count measures a subspace, the second an algebra, and the third an operation.

## The Trace and the Determinant

**Theorem.** For every $A\in M_n(\mathbb{R})$,

$$
\operatorname{tr}L_A=n\operatorname{tr}A,\qquad \det L_A=(\det A)^{n}.
$$

*Proof.* In the column-stacking basis $[L_A]=\mathrm{I}_n\otimes A$, the Kronecker product of the identity with $A$. The eigenvalues of a Kronecker product are the products of the eigenvalues, so the eigenvalues of $L_A$ are the eigenvalues of $A$, each repeated $n$ times. Summing and multiplying,

$$
\operatorname{tr}L_A=n\sum_i\lambda_i,\qquad \det L_A=\Big(\prod_i\lambda_i\Big)^{n}.
$$

Both identities are polynomial in the entries, so they hold over $\mathbb{R}$ as soon as they hold over $\mathbb{C}$, where the eigenvalues exist.

**The eigenvalues of $L_A$ are the eigenvalues of $A$ with multiplicity $n$.** This is the spectral reading of the Kronecker form, and it gives the rank at once: the rank of $L_A$ is $n$ times the rank of $A$, and the kernel has dimension $n(n-\operatorname{rk}A)$.

**The determinant identity is the reason $\mathrm{GL}_n$ acts on the whole algebra.** If $A$ is invertible then $\det L_A=(\det A)^{n}\ne0$, so $L_A$ is invertible, with inverse $L_{A^{-1}}$; the map $A\mapsto L_A$ embeds $\mathrm{GL}_n(\mathbb{R})$ into $\mathrm{GL}_{n^{2}}(\mathbb{R})$, and its image is the group of invertible left multiplications.

**The same for the right.** $\operatorname{tr}R_B=n\operatorname{tr}B$ and $\det R_B=(\det B)^{n}$, by the same computation with $[R_B]=B^{\mathsf T}\otimes\mathrm{I}$ and the eigenvalues of $B^{\mathsf T}$ equal to those of $B$.

## The Numerical Check

**The invariants.** At $n=2$ a random $A$ gives $\operatorname{tr}L_A=5.719598$ and $2\operatorname{tr}A=5.719598$; at $n=3$ the two values are $5.129450$. The determinants agree as well: $3.224486$ against $(\det A)^{2}$ at $n=2$, and $-0.464772$ against $(\det A)^{3}$ at $n=3$. The eigenvalues of $L_A$ form the spectrum of $A$ with each value repeated $n$ times, to machine precision.

**The dimensions.** The sum $L(M)+R(M)$ has dimension $7$ at $n=2$ and $17$ at $n=3$, against $2n^{2}-1=7$ and $17$. The products $L_AR_B$ span $16$ and $81$ dimensions, against $n^{4}$. The commutant of the left copy has dimension $4$ and $9$, against $n^{2}$.

**The rank.** For a rank-two $3\times3$ matrix, $L_A$ has rank $6=3\cdot2$, and its kernel has dimension $3=3(3-2)$, with three zero eigenvalues.

## Summary

The algebra $\operatorname{End}(M_n(\mathbb{R}))$ has dimension $n^{4}$ and is $M_{n^{2}}(\mathbb{R})$ in a basis. The left multiplications $L_A(X)=AX$ form a subalgebra isomorphic to $M_n(\mathbb{R})$, the right multiplications $R_B(X)=XB$ form a subalgebra isomorphic to the opposite algebra, and the two commute elementwise, $L_AR_B=R_BL_A$. Their intersection is the line of scalar maps, so their sum has dimension $2n^{2}-1$, and yet the products $L_AR_B$ span the whole algebra: $\operatorname{End}(M_n(\mathbb{R}))\cong M_n(\mathbb{R})\otimes M_n(\mathbb{R})^{\mathrm{op}}$, of dimension $n^{4}$. The commutant of either copy is the other, and the bicommutant of either is itself, which is the double centraliser theorem in this case. Finally $\operatorname{tr}L_A=n\operatorname{tr}A$ and $\det L_A=(\det A)^{n}$, because the eigenvalues of $L_A$ are those of $A$ with multiplicity $n$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{End}(M_n(\mathbb{R}))$ | The algebra of linear maps, of dimension $n^{4}$ |
| $L_A(X)=AX$ | The left multiplication by $A$ |
| $R_B(X)=XB$ | The right multiplication by $B$ |
| $M_n(\mathbb{R})^{\mathrm{op}}$ | The opposite algebra, with product $B\cdot C=CB$ |
| $L(M_n)$, $R(M_n)$ | The two copies inside $\operatorname{End}$ |
| $2n^{2}-1$ | The dimension of their sum |
| $n^{4}$ | The dimension of the algebra they generate |
| $[L_A]=\mathrm{I}\otimes A$ | The matrix of $L_A$ in the column-stacking basis |
| $[R_B]=B^{\mathsf T}\otimes\mathrm{I}$ | The matrix of $R_B$ in the same basis |

## Further Reading

- Paul Richard Halmos, *Finite-Dimensional Vector Spaces* (Springer, 1974), for the regular representation and the double centraliser.
- Roger A. Horn and Charles R. Johnson, *Topics in Matrix Analysis* (Cambridge, 1991), for Kronecker products and the spectra of $A\otimes B$.
- [The Matrix Algebra $M_n(\mathbb{R})$](the-matrix-algebra-mnr.html), for the algebra, its centre and its dimension.
- [The Ideals, the Centre and the Simplicity of $M_n(\mathbb{R})$](the-ideals-the-centre-and-the-simplicity-of-mnr.html), for the simplicity used in the tensor argument.
- [The One-Sided Operators](the-one-sided-operators-over-r.html), for the rank, the spectrum and the adjoint of $L_A$ and $R_B$.
