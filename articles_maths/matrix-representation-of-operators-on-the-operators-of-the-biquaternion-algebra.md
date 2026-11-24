# __Matrix Representation of Operators on the Operators of the Biquaternion Algebra__

## Introduction

**The question.** The article *$M_4(\mathbb{C})$ Axis-Free Representation : Operators* assigns to every operator on the biquaternion algebra a $4\times4$ array, and sorts the operators into the general endomorphisms, the two one-sided copies and the two-sided products. This article runs the same sorting one level higher. An operator on the operator space is an element of $\operatorname{End}(\operatorname{End}(\mathbb{B}))$, it receives a $16\times16$ array in the sixteen words, and the three levels are read side by side.

**The answer in one line.** The sixteen words are an orthogonal basis of the operator space; an operator on that space is a $16\times16$ array; a two-sided one is the Kronecker product of two $4\times4$ arrays; the derivation $[K,\cdot]$ is the Kronecker difference of one array with itself; and the fifteen generators of $\mathfrak{su}(4)$ become fifteen arrays of order sixteen with the same split, the same grading and the same rotor.

**The three levels.** The three levels are the elements, the operators on them and the operators on the operators.

- At the level of the elements an array is a $4\times4$ matrix of a multiplication, and the sixteen words are themselves such arrays.
- At the level of the operators an array is a $4\times4$ matrix of an endomorphism of $\mathbb{B}$, and the space has sixteen complex dimensions.
- At the level of the operators on the operators an array is a $16\times16$ matrix of an endomorphism of that sixteen-dimensional space, and the space has two hundred and fifty-six complex dimensions.

**What the article proves.** Every operator on the operator space is a sum of at most sixteen two-sided products; the product itself is a Kronecker product; the least number of products is the rank of the $16\times16$ array; and the rank of the operator as a map is the product of the two ranks of its factors.

**Boundaries.** The level below is *$M_4(\mathbb{C})$ Axis-Free Representation : Operators*. The same fifteen generators read as operators rather than as arrays are *The Anti-Hermitian Derivations of the Operators of the Biquaternion Algebra as $\mathfrak{su}(4)$*, and the same fifteen read at the level of the algebra are *The Anti-Hermitian Derivations of $M_4(\mathbb{C})$ as $\mathfrak{su}(4)$*; §*The Generators in the Axis-Free Matrices $L$ and $R$* prints the six axis-free matrices $\ell_k$, $r_k$ whole and the nine products $iN_{jk}$, both bases being printed there, and §*The Fifteen as Arrays of Order Sixteen* restates the second of the two articles in the array language. The abstract two-sided family is *The Two-Sided Operators and the Segre Cone*, the length is *The Length and the Two Ranks*, and the algebra acting on itself is *$\operatorname{End}(\mathbb{B})$ as an Algebra: the Regular Representation*. The Hermitian pair is Part V and is not treated here.

**Conventions.** The basis of the algebra is
$$
\mathcal{E}=(e_t,\vec e_x,\vec e_y,\vec e_z),
$$
with $e_t$ the unit and
$$
\vec e_x^2=\vec e_y^2=\vec e_z^2=-e_t,\qquad
\vec e_x\vec e_y=\vec e_z,\quad
\vec e_y\vec e_z=\vec e_x,\quad
\vec e_z\vec e_x=\vec e_y,
$$
and the reverse products negated. Write $\mu,\nu,\rho,\sigma$ for the four indices and $L_\mu:=L_{\mathrm{axf},e_\mu}$, $R_\nu:=R_{\mathrm{axf},e_\nu}$ for the **axis-free matrices** of left and right multiplication in the basis $\mathcal{E}$, so that $L_\mu$ is the matrix of $X\mapsto e_\mu X$ and $R_\nu$ that of $X\mapsto Xe_\nu$. The short forms $\ell_k:=L_{\mathrm{axf},\vec e_k}$ and $r_k:=R_{\mathrm{axf},\vec e_k}$ are used for the six vector ones. The **words** are
$$
W_{\mu\nu}:=L_\mu R_\nu=T_{e_\mu,e_\nu},\qquad W_{\mu\nu}(X)=e_\mu Xe_\nu,
$$
sixteen of them, of order four. The matrix units of order four are $E_{ij}$, with $i,j\in\{1,2,3,4\}$ standing for $t,x,y,z$ in that order. The form on the operator space is
$$
\langle S,T\rangle=\operatorname{tr}\bigl(S^{*}T\bigr),
$$
and the form on the space of operators on operators is
$$
\langle\Phi,\Psi\rangle_{\mathcal{A}}=\operatorname{tr}\bigl(\Phi^{*}\Psi\bigr),
$$
with the adjoint taken with respect to the first form. The complex dimension is written $\dim_{\mathbb{C}}$, the rank of a matrix $\operatorname{rank}$, and the spectrum $\operatorname{spec}$.

## The Ladder of Levels

**The three spaces.** The algebra $\mathbb{B}$ has complex dimension four. Its endomorphism algebra $V:=\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ has complex dimension sixteen. The endomorphism algebra of that, $\mathcal{A}:=\operatorname{End}_{\mathbb{C}}(V)$, has complex dimension two hundred and fifty-six.

**The table.** The three levels differ in the object, in the dimension and in the order of the array that represents a member.

| level | the object | $\dim_{\mathbb{C}}$ | $\dim_{\mathbb{R}}$ | the array |
|---|---|---|---|---|
| elements | an element $Q$ of $\mathbb{B}$ | $4$ | $8$ | none; the element is a column |
| operators | $S\in V$ | $16$ | $32$ | $4\times4$ in the words $L_\mu$, $R_\nu$ |
| operators on operators | $\Phi\in\mathcal{A}$ | $256$ | $512$ | $16\times16$ in the sixteen words $W_{\mu\nu}$ |

**What the third level adds.** Two things, and nothing else. The first is size: an array of order sixteen has two hundred and fifty-six entries, and the product, the trace, the determinant and the spectrum of a two-sided operator follow the rules of the Kronecker product. The second is that the carrier now has an algebra structure of its own, so the operators on it include the regular representation, the derivations and the conjugations, and those three families have no counterpart at the level of the elements.

**The uniformity.** The construction is one construction. A basis of a space of dimension $n$ gives an array of order $n$ for every operator on that space: at the level below the space is $\mathbb{B}$, of dimension four, and the arrays are of order four; at this level the space is $V$, of dimension sixteen, and the arrays are of order sixteen.

## The Carrier and Its Basis

**The carrier.** The carrier of the derivation is the operator space $V=\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, of complex dimension sixteen. Its elements are the operators $S$, and they are the objects that the fifteen generators of $\mathfrak{su}(4)$ turn.

**Proposition (the sixteen words are an orthogonal basis).** The words $W_{\mu\nu}$ are a basis of $V$, and
$$
\langle W_{\mu\nu},W_{\rho\sigma}\rangle=\operatorname{tr}\bigl(W_{\mu\nu}^{\mathsf T}W_{\rho\sigma}\bigr)=4\,\delta_{\mu\rho}\delta_{\nu\sigma}.
$$

*Proof.* Two words whose nonzero positions differ are orthogonal, since no position carries two nonzero entries of the two, so every term of the trace vanishes. The sixteen words fall into four groups of four, one group for each possible support: the diagonal, and the three pairings of the four indices into two pairs. Within a group the four words differ only in the signs of the four positions, and the four sign vectors are pairwise orthogonal, which a check of the four groups settles. So distinct words are orthogonal, each word has norm four because it has four entries $\pm1$, and the sixteen independent elements of a space of dimension sixteen are a basis.

**Definition (the array).** The **array** of an operator $\Phi$ on the operator space is the $16\times16$ matrix of its values on the words,
$$
[\Phi]_{(\mu\nu),(\rho\sigma)}=\tfrac14\operatorname{tr}\bigl(W_{\mu\nu}^{\mathsf T}\,\Phi(W_{\rho\sigma})\bigr),
$$
so that $\Phi(W_{\rho\sigma})=\sum_{\mu\nu}[\Phi]_{(\mu\nu),(\rho\sigma)}W_{\mu\nu}$. The row index is the image and the column index the source.

**The reading.** The definition is the definition of a matrix in a basis, written with the Hilbert–Schmidt form because the words are orthogonal but not of unit norm. The factor $\tfrac14$ is the square of the norm of a word.

**Proposition (the words multiply to words up to sign).** For two words,
$$
W_{\mu\nu}W_{\rho\sigma}=\pm\,W_{\mu\rho,\,\nu\sigma},
$$
where $\mu\rho$ and $\nu\sigma$ are the products of the corresponding units, taken up to the sign of the multiplication table.

*Proof.* The left and the right multiplications commute, so $W_{\mu\nu}W_{\rho\sigma}=L_\mu L_\rho R_\nu R_\sigma$; the products of two units are units up to sign, by the multiplication table of $\mathbb{B}$.

**Corollary (the set of the words and their negatives is closed).** The product of any number of words is $\pm$ a word, and the identity is the word $W_{tt}=\mathrm{I}_4$.

*Proof.* Iterate the proposition. The identity is $L_tR_t$, and $e_te_t=e_t$.

**The change of basis from the matrix units.** The sixteen matrix units $E_{ij}$ are the second natural basis of $V$. Read the sixteen words in row-major order as the columns of a matrix $C$, so that $C=2P$ with
$$
P_{(\mu\nu),(ij)}=\tfrac12\,(W_{\mu\nu})_{ij}.
$$
The matrix $P$ is orthogonal,
$$
P^{\mathsf T}P=\mathrm{I}_{16},
$$
and it has four entries $\pm\tfrac12$ in each row and in each column.

*Proof.* The inner product of two columns of $P$ is $\tfrac14\operatorname{tr}(W_{\mu\nu}^{\mathsf T}W_{\rho\sigma})=\delta$, by the orthogonality of the words; a square matrix with orthonormal columns is orthogonal, and then its rows are orthonormal too, so each row has four entries $\pm\tfrac12$, since the entries are $0$ and $\pm\tfrac12$ and the row norm is one.

**Corollary (the two arrays of one operator).** For an operator $\Phi$ with array $[\Phi]_{E}$ in the matrix units and array $[\Phi]_{W}$ in the words,
$$
[\Phi]_{W}=C^{-1}[\Phi]_{E}\,C=P^{\mathsf T}[\Phi]_{E}P .
$$

*Proof.* The columns of $C$ are the coordinates of the words in the unit basis, so the array changes by $C^{-1}(\cdot)C$. Since $C=2P$ and $P$ is orthogonal, the two scalings cancel and the expression in $P$ is the same.

**Corollary (the invariants do not depend on the basis).** The trace, the determinant, the rank and the spectrum of an operator on the operator space are those of its array in either basis.

*Proof.* $P$ is invertible, so the two arrays are similar.

**The reading.** The word basis is the axis-free basis of the carrier: the same sixteen signed permutations that are the operators of the level below, now used as the basis of the space in which the operators of this level are written. The matrix units are the second basis, and the two are related by the orthogonal $P$.

## The Two-Sided Operators on the Operator Space

**Definition.** For two operators $A,B\in V$ the **two-sided operator on the operator space** is
$$
\Theta_{A,B}(S)=ASB .
$$
It extends the level-one operator $T_{a,b}(X)=aXb$, with the elements replaced by operators.

**Proposition (the Kronecker form).** In the matrix-unit basis of the carrier the array of $\Theta_{A,B}$ is the Kronecker product
$$
[\Theta_{A,B}]_{E}=A\otimes B^{\mathsf T},\qquad
\bigl(A\otimes B^{\mathsf T}\bigr)_{(ij),(kl)}=A_{ik}B_{lj}.
$$

*Proof.* Apply $\Theta_{A,B}$ to a matrix unit: $AE_{kl}B=\sum_{i,j}A_{ik}B_{lj}E_{ij}$, so the entry in row $(i,j)$ and column $(k,l)$ is $A_{ik}B_{lj}$, which is the entry of the Kronecker product.

**Corollary (the array in the words).** In the word basis,
$$
[\Theta_{A,B}]_{W}=P^{\mathsf T}\bigl(A\otimes B^{\mathsf T}\bigr)P .
$$

**Remark (the two Kronecker factors are the two axis-free families).** For $A=\ell_k=L_{\mathrm{axf},\vec e_k}$ the array of the left multiplier $\Lambda_{\ell_k}$ is $\ell_k\otimes\mathrm{I}_4$, and for $B=r_k=R_{\mathrm{axf},\vec e_k}$ the array of the right multiplier $\Rho_{r_k}$ is $\mathrm{I}_4\otimes r_k^{\mathsf T}$. So the two factors of the Kronecker product are the axis-free left matrix and the transposed axis-free right matrix, and the word $W_{\mu\nu}=L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},e_\nu}$ acts on the operator space with the array $L_{\mathrm{axf},e_\mu}\otimes R_{\mathrm{axf},e_\nu}^{\mathsf T}$.

*Proof.* The preceding corollary on the change of basis.

**Proposition (the invariants of a two-sided operator).** For two operators $A$ and $B$,
$$
\operatorname{tr}\Theta_{A,B}=\operatorname{tr}A\,\operatorname{tr}B,\qquad
\det\Theta_{A,B}=(\det A)^{4}(\det B)^{4},\qquad
\operatorname{rank}\Theta_{A,B}=\operatorname{rank}A\cdot\operatorname{rank}B,
$$
and the spectrum of $\Theta_{A,B}$ is the sixteen products $\alpha_i\beta_j$ of the eigenvalues of $A$ and of $B$.

*Proof.* The eigenvalues of a Kronecker product are the pairwise products, the trace is the sum of the products of the traces, the determinant of $A\otimes C$ of order $mn$ is $(\det A)^{m}(\det C)^{n}$, and the rank of a Kronecker product is the product of the ranks. The determinant of $B^{\mathsf T}$ is that of $B$, and the spectrum of $B^{\mathsf T}$ is that of $B$.

**Proposition (the composition law).** The two-sided operators compose by
$$
\Theta_{A,B}\,\Theta_{C,D}=\Theta_{AC,DB},
$$
the reversed order in the second factor.

*Proof.* $\Theta_{A,B}(\Theta_{C,D}(S))=A(CSD)B=(AC)S(DB)$.

**Corollary (the scaling and the cone).** The pair $(A,B)$ has thirty-two complex parameters, the scaling $(A,B)\mapsto(\lambda A,\lambda^{-1}B)$ leaves the operator alone, and the image of the pair is a cone of complex dimension thirty-one whose projective image is the Segre product $\mathbb{P}^{15}\times\mathbb{P}^{15}$.

*Proof.* The scaling is read from the definition; the stabiliser is trivial at every pair of nonzero operators, so the orbits are lines and the image has dimension $32-1=31$; the projective image of the decomposable tensors of $M_4\otimes M_4$ is the product of the two projective spaces.

**Proposition (the 256 arrays are signed permutations of order sixteen).** For two words $A=W_{\alpha\beta}$ and $B=W_{\gamma\delta}$ the array $[\Theta_{A,B}]_{W}$ has exactly sixteen nonzero entries, one in each row and in each column, all of them $\pm1$.

*Proof.* The entry in row $(\mu\nu)$ and column $(\rho\sigma)$ is $\tfrac14\operatorname{tr}(W_{\mu\nu}^{\mathsf T}W_{\alpha\beta}W_{\rho\sigma}W_{\gamma\delta})$. The product $W_{\alpha\beta}W_{\rho\sigma}W_{\gamma\delta}$ is, up to sign, a single word, by the closure of the words; and a word pairs with itself to the trace four and with every other word to zero. So for each column $(\rho,\sigma)$ there is exactly one row, and the entry there is $\pm1$; a square matrix with one nonzero in each column has one in each row.

**The reading.** At the level below the sixteen words act on the four basis elements of the algebra, and the arrays of the units are the signed permutations of order four. At this level the same sixteen words act on the sixteen words, and the arrays of the products of two of them are the signed permutations of order sixteen. The pattern of the level is repeated with four replaced by sixteen.

## The One-Sided Copies and the Regular Representation

**Definition (the left and the right copies).** Write
$$
\Lambda_A(S)=AS,\qquad \Rho_B(S)=SB,
$$
so that $\Lambda_A=\Theta_{A,\mathrm{I}}$ and $\Rho_B=\Theta_{\mathrm{I},B}$.

**Proposition (each copy is of dimension sixteen).** The maps $A\mapsto\Lambda_A$ and $B\mapsto\Rho_B$ are injective, so their images are two subspaces of $\mathcal{A}$ of complex dimension sixteen.

*Proof.* $\Lambda_A$ applied to the identity gives $A$, so $\Lambda_A=0$ forces $A=0$; likewise $\Rho_B$ applied to the identity gives $B$.

**Proposition (the intersection is the scalars).** $\Lambda_A=\Rho_B$ exactly when $A=B=\lambda\mathrm{I}_4$.

*Proof.* Evaluate at the identity: $A=B$. Then $AS=SA$ for every operator $S$, so $A$ commutes with the whole matrix algebra and is a scalar.

**Corollary (the two-sided complement is of dimension 225).** The sum of the two copies has complex dimension $16+16-1=31$, and its complement in the two hundred and fifty-six has dimension $225$.

*Proof.* The sum of two subspaces of dimensions sixteen and sixteen with an intersection of dimension one.

**Proposition (the splitting of the two hundred and fifty-six).** Write $\mathfrak{sl}_4$ for the traceless operators, of complex dimension fifteen. Then, in the identification $\mathcal{A}=V\otimes V$ of the Kronecker form,
$$
\mathcal{A}=\bigl(\mathfrak{sl}_4\otimes\mathfrak{sl}_4\bigr)\oplus\bigl(\mathfrak{sl}_4\otimes\mathrm{I}\bigr)\oplus\bigl(\mathrm{I}\otimes\mathfrak{sl}_4\bigr)\oplus\bigl(\mathrm{I}\otimes\mathrm{I}\bigr),
$$
of dimensions $225+15+15+1$. The left copy is the sum of the second summand and the scalar line, and the right copy the sum of the third and the scalar line.

*Proof.* The decomposition $V=\mathfrak{sl}_4\oplus\mathbb{C}\mathrm{I}$ of a matrix algebra into its traceless part and its centre, multiplied out.

**Corollary (which operators are genuinely two-sided).** The complement of the one-sided copies is exactly the set of the two-sided operators with both factors traceless.

*Proof.* The trace of $A$ is the coefficient of $\mathrm{I}$ in the first factor and the trace of $B$ that in the second; the complement is the product of the two traceless parts.

**The reading against the level below.** The level below splits its sixteen as $4+4-1+9$, with the one-sided copies of dimension four and a complement of dimension nine. This level splits its two hundred and fifty-six as $16+16-1+225$, with the same shape and one number changed: nine becomes $15^{2}=225$. The complement is the square of the traceless space, so the genuinely two-sided operators are the products of two traceless ones.

**Proposition (the double centraliser).** The commutant of the left copy in $\mathcal{A}$ is the right copy, and conversely, so each family is the centraliser of the other.

*Proof.* Let $\Phi$ commute with every $\Lambda_A$. Then $\Phi(AS)=A\Phi(S)$ for all $A$ and $S$, and the choice $A=S$ with $S$ replaced by the identity gives $\Phi(S)=S\,\Phi(\mathrm{I})$. So $\Phi=\Rho_B$ with $B=\Phi(\mathrm{I})$. The converse is the commutation $L_AR_B=R_BL_A$.

## The Derivations and the Fifteen

**Definition.** For an operator $K\in V$ the **inner derivation** is
$$
\mathrm{ad}_K(S)=KS-SK,
$$
and it is $\Lambda_K-\Rho_K$.

**Proposition (it is a derivation and its adjoint).** $\mathrm{ad}_K(ST)=\mathrm{ad}_K(S)T+S\,\mathrm{ad}_K(T)$, and $(\mathrm{ad}_K)^{*}=\mathrm{ad}_{K^{*}}$ for the form of the operator space, so $\mathrm{ad}_K$ is anti-Hermitian exactly when $K$ is.

*Proof.* The Leibniz rule is associativity; the adjoint is the cyclic invariance of the trace, $\operatorname{tr}((KS-SK)^{*}T)=\operatorname{tr}(S^{*}(K^{*}T-TK^{*}))$.

**Proposition (the array).** In the matrix-unit basis of the carrier the array of $\mathrm{ad}_K$ is the Kronecker difference
$$
[\mathrm{ad}_K]_{E}=K\otimes\mathrm{I}_4-\mathrm{I}_4\otimes K^{\mathsf T}.
$$

*Proof.* The first term is the array of $\Lambda_K$ and the second that of $\Rho_K$, by the Kronecker form of the two-sided operator.

**Corollary (the kernel, the rank and the spectrum).** Let $m_1,\dots,m_r$ be the multiplicities of the distinct eigenvalues $\kappa_1,\dots,\kappa_r$ of $K$. Then the kernel of $\mathrm{ad}_K$ is the centraliser of $K$ in $V$, of complex dimension $\sum_i m_i^{2}$; the rank is $16-\sum_i m_i^{2}$; and the spectrum is the sixteen differences $\kappa_i-\kappa_j$.

*Proof.* $KS=SK$ exactly when $S$ preserves each eigenspace of $K$, so the centraliser is the algebra of block-diagonal operators in the eigenbasis, of dimension $\sum m_i^{2}$. The spectrum is the spectrum of a Kronecker difference, and the rank is the number of nonzero differences.

**Proposition (the fifteen).** The operators $K$ with $K^{*}=-K$ and $\operatorname{tr}K=0$ form a real vector space of dimension fifteen, and the map $K\mapsto\mathrm{ad}_K$ is injective on it.

*Proof.* Sixteen real parameters for an anti-Hermitian operator of order four, one equation for the trace; the kernel of the map is the scalars, and the only scalar among the traceless operators is zero.

**Proposition (the split at order sixteen).** The fifteen arrays split as six real antisymmetric and nine purely imaginary symmetric arrays of order sixteen.

*Proof.* For $K$ real antisymmetric, $(K\otimes\mathrm{I}-\mathrm{I}\otimes K^{\mathsf T})^{\mathsf T}=K^{\mathsf T}\otimes\mathrm{I}-\mathrm{I}\otimes K=-(K\otimes\mathrm{I}-\mathrm{I}\otimes K^{\mathsf T})$, so the array is real and antisymmetric; for $K=iS$ with $S$ real symmetric, the array is $i(S\otimes\mathrm{I}-\mathrm{I}\otimes S)$, which is imaginary and symmetric.

**The table of the three shapes.** Every array is anti-Hermitian and of trace zero. The spectrum and the rank depend on the generator.

| the generator | its spectrum | the spectrum of its array | the rank |
|---|---|---|---|
| the fifteen of the words basis, $K^{2}=-\mathrm{I}_4$ | $i,i,-i,-i$ | $0^{8},(\pm2i)^{4}$ | $8$ |
| the fourteen of the plane basis other than $iD$ | $0,0,\pm i$ | $0^{6},(\pm i)^{4},\pm2i$ | $10$ |
| the sum $iD$ | $-3i,i,i,i$ | $0^{10},(\pm4i)^{3}$ | $6$ |

**The reading of the table.** The rank is the number of ordered pairs of positions whose eigenvalues differ, so it measures how far the generator is from a multiple of the identity. The uniform value $8$ is the value of an involution, where every eigenvalue appears twice; the value $10$ is the value of a plane array, where two eigenvalues vanish and two survive at multiplicity one; and the value $6$ is the value of $iD$, of multiplicities $1,3$, the largest degeneracy among the fifteen, which no involution reaches. The two lists of the fifteen are printed in the next section.

**Corollary (the square of the derivation of an involution).** For $K^{2}=-\mathrm{I}_4$,
$$
\Bigl(\tfrac12\,\mathrm{ad}_K\Bigr)^{2}=-P,
$$
with $P$ the projection onto the eight-dimensional image of $\mathrm{ad}_K$. So $\tfrac12\mathrm{ad}_K$ is a complex structure on the image, and the image is the orthogonal complement of the commutant.

*Proof.* The eigenvalues of the array are $0$ and $\pm2i$, so those of its square are $0$ and $-4$, and $\operatorname{rank}\mathrm{ad}_K=8$; a diagonalisable operator with the eigenvalues $0$ and $-4$ satisfies $(\mathrm{ad}_K)^{2}=-4P$ with $P$ the spectral projection of the nonzero part.

**Theorem (the rotor).** For $U=e^{\theta K}\in\mathrm{SU}(4)$,
$$
e^{\theta\,\mathrm{ad}_K}=\mathrm{Ad}_U,\qquad
\bigl[\mathrm{Ad}_U\bigr]_{E}=U\otimes\bar U,
$$
and $\mathrm{Ad}_U$ is unitary for the form of the operator space, of determinant one.

*Proof.* The exponential of a commutator is the conjugation by the exponential; the array of the conjugation is the Kronecker product of the array with its conjugate; the eigenvalues of $U\otimes\bar U$ are the products $\upsilon_i\bar\upsilon_j$ of modulus one, and the determinant is $(\det U)^{4}(\det\bar U)^{4}=1$.

**Proposition (the trace form on the fifteen).** For two traceless operators $X$ and $Y$,
$$
\langle\mathrm{ad}_X,\mathrm{ad}_Y\rangle_{\mathcal{A}}=8\,\langle X,Y\rangle .
$$

*Proof.* Expanding the Kronecker difference, the two diagonal terms are $4\operatorname{tr}(X^{*}Y)$ each, one from the left factors and one from the right; the two cross terms carry the factor $\operatorname{tr}X$ or $\operatorname{tr}Y$ and vanish on traceless factors. The sum is $8\operatorname{tr}(X^{*}Y)$.

**The ladder.** The counts of the level are:
$$
512\ \longrightarrow\ 256\ \longrightarrow\ 30\ \longrightarrow\ 15,
$$
five hundred and twelve real dimensions of endomorphisms of the operator space, two hundred and fifty-six of anti-Hermitian ones, thirty of derivations, and fifteen of anti-Hermitian derivations.

*Proof.* The space $\mathcal{A}$ of complex dimension $256$ has real dimension $512$. An anti-Hermitian operator on it is a matrix of order sixteen with $\Phi^{*}=-\Phi$: the sixteen diagonal entries are purely imaginary and the one hundred and twenty off-diagonal pairs are conjugate, so the count is $16+2\cdot120=256$. The derivations of a full matrix algebra are the inner ones, $\mathrm{ad}_K$ with $K$ of order four, of complex dimension fifteen and real dimension thirty; the anti-Hermitian ones among them are the fifteen real dimensions of $\mathfrak{su}(4)$.

## The Generators in the Axis-Free Matrices $L$ and $R$

**What this frame is.** The regular matrices of left and right multiplication in the coefficient basis, with the columns equal to the products of the basis units. No frame of $\mathbb{C}^2$ is chosen and no sign of $\sigma_k$ is fixed, so this is where the frame of this article is read. Write
$$
\ell_k:=L_{\mathrm{axf},\vec e_k},\qquad r_k:=R_{\mathrm{axf},\vec e_k},
$$
so that $\ell_k$ is the array of $X\mapsto\vec e_kX$ and $r_k$ that of $X\mapsto X\vec e_k$. The same six arrays are printed in [Matrix Representations and Conventions](matrix-representations-conventions.html), §*The Left Family* and §*The Right Family*, in [$M_4(\mathbb{C})$ Axis-Free Representation : Operators](m4c-axis-free-representation-operators.html), §*The Four Left Matrices* and §*The Four Right Matrices*, and in [The Anti-Hermitian Derivations of $M_2(\mathbb{C})$ as $\mathfrak{su}(2)$](the-anti-hermitian-derivations-of-m2c-as-su2.html), §*The Axis-Free Representation, $4\times4$*. The four articles print one and the same six arrays, entry for entry.

**The three left matrices.** Left multiplication by the three vector units, printed whole:

$$
\ell_x=L_{\mathrm{axf},\vec e_x}=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix}
$$

$$
\ell_y=L_{\mathrm{axf},\vec e_y}=\begin{pmatrix}0&0&-1&0\\0&0&0&1\\1&0&0&0\\0&-1&0&0\end{pmatrix}
$$

$$
\ell_z=L_{\mathrm{axf},\vec e_z}=\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&1&0&0\\1&0&0&0\end{pmatrix}
$$

**The three right matrices.** Right multiplication by the same three units, the same construction with the order of the factors exchanged:

$$
r_x=R_{\mathrm{axf},\vec e_x}=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&1\\0&0&-1&0\end{pmatrix}
$$

$$
r_y=R_{\mathrm{axf},\vec e_y}=\begin{pmatrix}0&0&-1&0\\0&0&0&-1\\1&0&0&0\\0&1&0&0\end{pmatrix}
$$

$$
r_z=R_{\mathrm{axf},\vec e_z}=\begin{pmatrix}0&0&0&-1\\0&0&1&0\\0&-1&0&0\\1&0&0&0\end{pmatrix}
$$

**The six are $G_1$ to $G_6$.** The first six of the fifteen generators are these six arrays, taken whole. The fourth column names each of them again in the Peirce frame of the $M_2(\mathbb{C})$ article, through the identity of the next paragraph.

| generator | axis-free array $L$, $R$ | the half, in the Peirce frame | symmetry | square |
|---|---|---|---|---|
| $G_1$ | $\ell_x=L_{\mathrm{axf},\vec e_x}$ | $\mathrm{I}_2\otimes g_x$ | real antisymmetric | $-\mathrm{I}_4$ |
| $G_2$ | $\ell_y=L_{\mathrm{axf},\vec e_y}$ | $\mathrm{I}_2\otimes g_y$ | real antisymmetric | $-\mathrm{I}_4$ |
| $G_3$ | $\ell_z=L_{\mathrm{axf},\vec e_z}$ | $\mathrm{I}_2\otimes g_z$ | real antisymmetric | $-\mathrm{I}_4$ |
| $G_4$ | $r_x=R_{\mathrm{axf},\vec e_x}$ | $g_x^{\mathsf T}\otimes\mathrm{I}_2$ | real antisymmetric | $-\mathrm{I}_4$ |
| $G_5$ | $r_y=R_{\mathrm{axf},\vec e_y}$ | $g_y^{\mathsf T}\otimes\mathrm{I}_2$ | real antisymmetric | $-\mathrm{I}_4$ |
| $G_6$ | $r_z=R_{\mathrm{axf},\vec e_z}$ | $g_z^{\mathsf T}\otimes\mathrm{I}_2$ | real antisymmetric | $-\mathrm{I}_4$ |

**The same six in the Peirce frame.** Write $g_k:=\tfrac12\mathsf{M}_2(\vec e_k)$ for the three generators that the $M_2(\mathbb{C})$ article names $G_k$, and let $S$ be the matrix whose columns are the four preimages of the matrix units in the coefficient basis. Then
$$
\tfrac12S^{-1}\ell_kS=\mathrm{I}_2\otimes g_k,\qquad \tfrac12S^{-1}r_kS=g_k^{\mathsf T}\otimes\mathrm{I}_2,
$$
so the half of each axis-free array is one block in the Peirce frame: $\mathrm{I}_2\otimes g_k$ for the left family and $g_k^{\mathsf T}\otimes\mathrm{I}_2$ for the right one. The transposition in the second is the reversal of the order of a product. The two families are the two commuting copies of $\mathfrak{su}(2)$ inside $\mathfrak{so}(4)$.

**The two families against each other.** Each of the six is a quarter turn of two coordinate planes. They agree wherever the two laws agree, and they differ exactly where right multiplication carries a unit to the negative of where left multiplication carries it: the difference $\ell_k-r_k$ has exactly two nonzero entries, $+2$ and $-2$.

| | $\ell_x,\ell_y,\ell_z$ | $r_x,r_y,r_z$ |
|---|---|---|
| trace | $0$ | $0$ |
| determinant | $1$ | $1$ |
| square | $-\mathrm{I}_4$ | $-\mathrm{I}_4$ |
| transpose | $-\ell_k$ | $-r_k$ |
| the planes turned | $(e_t,\vec e_x)$ with $(e_y,\vec e_z)$, cyclically | the same two planes |
| fixed | none | none |

**The six are a basis of $\mathfrak{so}(4)$.** Each is real and antisymmetric, so each lies in $\mathfrak{so}(4)$, and the six are linearly independent, so they span it: rank six in the sixteen-dimensional space. The halves $\tfrac12(\ell_k-r_k)$ and $\tfrac12(\ell_k+r_k)$ split that six as $\mathfrak{su}(2)\oplus\mathfrak{su}(2)$.

**The generator there is the half, here the whole.** The article on $M_2(\mathbb{C})$ takes its three generators to be $\tfrac12\ell_k$ and its three derivations to be $\tfrac12(\ell_k-r_k)$, the six halved arrays satisfying the same brackets with the structure constant $1$ instead of $2$. This article keeps the six whole and undifferenced: each of them is one of the fifteen generators at order four, and each acts here as the generator of a derivation of the operator space, whose array of order sixteen is the Kronecker difference of the next section.

**The nine products.** The nine remaining generators are $i$ times a product of one left array with one right one. Write $N_{jk}:=\ell_jr_k$; each row of $\ell_j$ carries a single entry, so each row of the product is $\pm$ one row of $r_k$.

$$
G_{7}=iN_{xx}=i\,\ell_x r_x=\begin{pmatrix}-i&0&0&0\\0&-i&0&0\\0&0&i&0\\0&0&0&i\end{pmatrix}
$$

$$
G_{8}=iN_{xy}=i\,\ell_x r_y=\begin{pmatrix}0&0&0&i\\0&0&-i&0\\0&-i&0&0\\i&0&0&0\end{pmatrix}
$$

$$
G_{9}=iN_{xz}=i\,\ell_x r_z=\begin{pmatrix}0&0&-i&0\\0&0&0&-i\\-i&0&0&0\\0&-i&0&0\end{pmatrix}
$$

$$
G_{10}=iN_{yx}=i\,\ell_y r_x=\begin{pmatrix}0&0&0&-i\\0&0&-i&0\\0&-i&0&0\\-i&0&0&0\end{pmatrix}
$$

$$
G_{11}=iN_{yy}=i\,\ell_y r_y=\begin{pmatrix}-i&0&0&0\\0&i&0&0\\0&0&-i&0\\0&0&0&i\end{pmatrix}
$$

$$
G_{12}=iN_{yz}=i\,\ell_y r_z=\begin{pmatrix}0&i&0&0\\i&0&0&0\\0&0&0&-i\\0&0&-i&0\end{pmatrix}
$$

$$
G_{13}=iN_{zx}=i\,\ell_z r_x=\begin{pmatrix}0&0&i&0\\0&0&0&-i\\i&0&0&0\\0&-i&0&0\end{pmatrix}
$$

$$
G_{14}=iN_{zy}=i\,\ell_z r_y=\begin{pmatrix}0&-i&0&0\\-i&0&0&0\\0&0&0&-i\\0&0&-i&0\end{pmatrix}
$$

$$
G_{15}=iN_{zz}=i\,\ell_z r_z=\begin{pmatrix}-i&0&0&0\\0&i&0&0\\0&0&i&0\\0&0&0&-i\end{pmatrix}
$$

**One product, worked.** The entries of $G_8$ follow row by row from $\ell_x$ and $r_y$. The rows of $\ell_x$ are $-e_x^{\mathsf T}$, $e_t^{\mathsf T}$, $-e_z^{\mathsf T}$, $e_y^{\mathsf T}$, so the rows of the product are
$$
-(0,0,0,-1),\qquad (0,0,-1,0),\qquad -(0,1,0,0),\qquad (1,0,0,0),
$$
which is the array at $G_8$ with the factor $i$ removed.

**The fifteen, listed once.** The fifteen traceless words are $\ell_x,\ell_y,\ell_z$, $r_x,r_y,r_z$ and the nine $iN_{jk}$, the six with one index $t$ and the nine with none:
$$
\ell_x,\ \ell_y,\ \ell_z,\ r_x,\ r_y,\ r_z,\quad iN_{xx},\ iN_{xy},\ iN_{xz},\ iN_{yx},\ iN_{yy},\ iN_{yz},\ iN_{zx},\ iN_{zy},\ iN_{zz}.
$$
The factor $i$ makes the nine anti-Hermitian, since each of the nine products is a real symmetric signed permutation. Every array of order sixteen in this article is computed from one of these fifteen by the Kronecker difference.

**The plane basis.** With the rows and the columns in the order $t,x,y,z$, the twelve off-diagonal arrays are
$$
A_{jk}=E_{jk}-E_{kj},\qquad iS_{jk}=i\bigl(E_{jk}+E_{kj}\bigr),
$$
six real antisymmetric and six imaginary symmetric, and the three diagonals are
$$
iD=i\bigl(W_{xx}+W_{yy}+W_{zz}\bigr),\qquad
d_2=\tfrac i2\bigl(W_{yy}-W_{xx}\bigr),\qquad
d_3=\tfrac i2\bigl(W_{zz}-W_{yy}\bigr).
$$

$$
A_{tx}=\begin{pmatrix}0&1&0&0\\-1&0&0&0\\0&0&0&0\\0&0&0&0\end{pmatrix}
$$

$$
A_{ty}=\begin{pmatrix}0&0&1&0\\0&0&0&0\\-1&0&0&0\\0&0&0&0\end{pmatrix}
$$

$$
A_{tz}=\begin{pmatrix}0&0&0&1\\0&0&0&0\\0&0&0&0\\-1&0&0&0\end{pmatrix}
$$

$$
A_{xy}=\begin{pmatrix}0&0&0&0\\0&0&1&0\\0&-1&0&0\\0&0&0&0\end{pmatrix}
$$

$$
A_{xz}=\begin{pmatrix}0&0&0&0\\0&0&0&1\\0&0&0&0\\0&-1&0&0\end{pmatrix}
$$

$$
A_{yz}=\begin{pmatrix}0&0&0&0\\0&0&0&0\\0&0&0&1\\0&0&-1&0\end{pmatrix}
$$

$$
iS_{tx}=\begin{pmatrix}0&i&0&0\\i&0&0&0\\0&0&0&0\\0&0&0&0\end{pmatrix}
$$

$$
iS_{ty}=\begin{pmatrix}0&0&i&0\\0&0&0&0\\i&0&0&0\\0&0&0&0\end{pmatrix}
$$

$$
iS_{tz}=\begin{pmatrix}0&0&0&i\\0&0&0&0\\0&0&0&0\\i&0&0&0\end{pmatrix}
$$

$$
iS_{xy}=\begin{pmatrix}0&0&0&0\\0&0&i&0\\0&i&0&0\\0&0&0&0\end{pmatrix}
$$

$$
iS_{xz}=\begin{pmatrix}0&0&0&0\\0&0&0&i\\0&0&0&0\\0&i&0&0\end{pmatrix}
$$

$$
iS_{yz}=\begin{pmatrix}0&0&0&0\\0&0&0&0\\0&0&0&i\\0&0&i&0\end{pmatrix}
$$

$$
iD=\begin{pmatrix}-3i&0&0&0\\0&i&0&0\\0&0&i&0\\0&0&0&i\end{pmatrix}
$$

$$
d_2=\begin{pmatrix}0&0&0&0\\0&i&0&0\\0&0&-i&0\\0&0&0&0\end{pmatrix}
$$

$$
d_3=\begin{pmatrix}0&0&0&0\\0&0&0&0\\0&0&i&0\\0&0&0&-i\end{pmatrix}
$$

**The two lists agree on three arrays and differ on twelve.** For $(a,b,c)$ a cyclic order of $(x,y,z)$,
$$
\tfrac12\bigl(\ell_a+r_a\bigr)=-A_{ta},\qquad \tfrac12\bigl(\ell_a-r_a\bigr)=-A_{bc},
$$
so the six real arrays are the half-sum and the half-difference of the three pairs $\ell_a,r_a$. The six imaginary ones are read from the three pairs of products, for example
$$
\tfrac12\bigl(iN_{xy}+iN_{yx}\bigr)=-iS_{xy},\qquad
\tfrac12\bigl(iN_{xy}-iN_{yx}\bigr)=iS_{tz}.
$$
The three diagonals are the three diagonal words recombined, $iD=G_7+G_{11}+G_{15}$.

**The trace form is not the same in the two.** In the words basis $\operatorname{tr}(G_a^{*}G_b)=4\delta_{ab}$. In the plane basis the square norms are $2$ on fourteen arrays and $12$ on $iD$, and $\operatorname{tr}(d_2^{*}d_3)=-1$. Every factor $4$ and every factor $8$ in this article refers to the words basis.

**The spectra are not the same in the two.** The fifteen of the words basis all square to $-\mathrm{I}_4$ and have the eigenvalues $i,i,-i,-i$; in the plane basis the fourteen arrays other than $iD$ have $0,0,\pm i$, and $iD$ has $-3i,i,i,i$. That is the source of the three shapes of the table above.

## The Fifteen as Arrays of Order Sixteen

**What this section does.** *The Anti-Hermitian Derivations of $M_4(\mathbb{C})$ as $\mathfrak{su}(4)$* states its results at the level of the algebra: fifteen generators, one involution, one spectrum, one rotor, one grading, two bases. Each of those statements is a statement about the fifteen $16\times16$ arrays of this level, and the table gives the translation.

| the statement at the level of the algebra | the statement as arrays of order sixteen |
|---|---|
| the generators are anti-Hermitian and traceless | each array is anti-Hermitian for $\langle\cdot,\cdot\rangle_{\mathcal{A}}$ and of trace zero |
| the split $6+9$ | six real antisymmetric arrays, nine imaginary symmetric ones |
| $K^{2}=-\mathrm{I}_4$ for each of the fifteen of the words basis | the array spectrum is $0^{8},(\pm2i)^{4}$ and $(\tfrac12\mathrm{ad}_K)^{2}=-P$ on the image |
| the derivation spectrum $0^{8},(\pm2i)^{4}$ | the sixteen differences of the eigenvalues, repeated by multiplicity |
| the trace form $4\delta_{ab}$ | the form on the fifteen arrays is $8\delta_{ab}$, in the words basis |
| the rotor $\cos\theta\,\mathrm{I}_4+\sin\theta\,K$ | the rotor $U\otimes\bar U$, of order sixteen, unitary and of determinant one |
| the grading of the six and the nine | the bracket of a real antisymmetric array with an imaginary symmetric one is imaginary symmetric, and so on |
| the two bases of the fifteen | two similarity classes of arrays, one for each basis of the generators |

**The first row, in detail.** The two conditions on an operator $K$ of order four are the two conditions on its array of order sixteen. The anti-Hermitian condition is preserved because the words are an orthogonal basis: the array of the adjoint is the conjugate transpose of the array of the operator, in either basis, since $P$ is real. The trace condition is preserved because the trace of the array is the trace of the operator.

**The second row, in detail.** The split is the level-one split seen through the Kronecker difference. A real antisymmetric $K$ gives a real array, because both factors of the Kronecker difference are real; an imaginary symmetric one gives an imaginary array; and the transposition rule of the proposition above separates the two.

**The third row, in detail.** The involution $K^{2}=-\mathrm{I}_4$, which holds on the words basis, does not survive as an involution of the array: the array of the derivation squares to $-4$ on its image and to zero on the commutant. What survives is the pair of eigenvalues $0$ and $-4$, and the complex structure $\tfrac12\mathrm{ad}_K$ on the image. The spectral reading is the honest one: the derivation of an involution is not an involution, and the eight zero eigenvalues are the commutant.

**The fourth row, in detail.** The uniform spectrum of the level of the algebra is the statement that every generator has the eigenvalues $i,i,-i,-i$, and the array's spectrum is the sixteen differences of those four numbers, which is $0$ eight times and $\pm2i$ four times each. The uniformity is a property of the fifteen of the words basis; a generator of the plane basis breaks it, as the table of the three shapes records. The two statements are the same statement, read at the two levels of the two bases.

**The fifth row, in detail.** The trace form of the fifteen is $4\delta_{ab}$; the form on the corresponding arrays is $8\delta_{ab}$, by the factor of the proposition above. The factor eight is twice the four of the norm of a word: the two terms of the Kronecker difference contribute four each.

**The sixth row, in detail.** The rotor of the level of the algebra is a polynomial of degree one in $K$. The rotor of this level is the Kronecker product of that polynomial with its conjugate,
$$
\bigl(\cos\theta\,\mathrm{I}_4+\sin\theta\,K\bigr)\otimes\bigl(\cos\theta\,\mathrm{I}_4+\sin\theta\,\bar K\bigr),
$$
which is a polynomial of degree two in the Kronecker products of $K$ with itself. The compact form $\cos\theta\,\mathrm{I}_{16}+\sin\theta\,K$ is lost, exactly as the plane basis of the level below loses the compact form of the rotor.

**The seventh row, in detail.** The grading is a statement about the brackets of the generators, and it is transported to the arrays by the identity $[\mathrm{ad}_X,\mathrm{ad}_Y]=\mathrm{ad}_{[X,Y]}$. The bracket of two real antisymmetric arrays is a real antisymmetric array; the bracket of a real antisymmetric one with an imaginary symmetric one is imaginary symmetric; and the bracket of two imaginary symmetric ones is real antisymmetric. The array computation and the generator computation agree entry by entry, because the map $\mathrm{ad}$ is a Lie algebra isomorphism onto its image.

**The eighth row, in detail.** The two bases of the fifteen are two bases of the generator space, and each gives a different similarity class of arrays. The change of basis of the generators is a $15\times15$ matrix; the change of the arrays is the conjugation by the corresponding element of $\mathrm{GL}_{16}$. The invariants of the array, its spectrum and its rank, are the same in the two; the entries are not.

**The reading of the section.** The article at the level of the algebra is about fifteen matrices of order four. This level turns each of them into an operator of order sixteen, and every proposition of that article becomes a proposition about the array of order sixteen of that operator: the split into real and imaginary, the rank, the spectrum, the rotor, the form and the grading. Nothing is added to the mathematics; the arrays of order sixteen are the same fifteen objects written in the basis in which the derivations act.

## One Operator, Three Arrays

**The operator.** The example is the derivation of the sum $iD=i(W_{xx}+W_{yy}+W_{zz})=\operatorname{diag}(-3i,i,i,i)$, the generator whose image is the six planes through the $t$ line.

**In the matrix units.** The array is the Kronecker difference, which is diagonal because $iD$ is diagonal. The sixteen entries, in row-major order with the semicolons between the four rows of the $4\times4$ grid, are
$$
[\mathrm{ad}_{iD}]_{E}=\operatorname{diag}\bigl(0,-4i,-4i,-4i;\ 4i,0,0,0;\ 4i,0,0,0;\ 4i,0,0,0\bigr),
$$
the differences $\kappa_\mu-\kappa_\nu$ of the four diagonal entries $-3i,i,i,i$.

**In the words.** The array is the diagonal one conjugated by $P$. It has twenty-four nonzero entries, all of them $\pm2i$: the twelve off-diagonal rows are the words of the six pairs, and each of those rows lands on the two words of the pair on the complementary planes.

**In the planes.** In the basis
$$
\mathrm{I}_4,\ A_{tx},\ iS_{tx},\ A_{ty},\ iS_{ty},\ A_{tz},\ iS_{tz},\ A_{xy},\ iS_{xy},\ A_{xz},\ iS_{xz},\ A_{yz},\ iS_{yz},\ iD,\ d_2,\ d_3
$$
of the carrier, the array is block diagonal, with three copies of one block and zeros elsewhere:
$$
[\mathrm{ad}_{iD}]_{\mathrm{plane}}=\operatorname{diag}\bigl(0,\ J,\ J,\ J,\ 0_6,\ 0_3\bigr),\qquad
J=\begin{pmatrix}0&4\\-4&0\end{pmatrix}.
$$

*Proof.* On the first triple of planes, $[\mathrm{iD},A_{ta}]=-4\,iS_{ta}$ and $[\mathrm{iD},iS_{ta}]=4\,A_{ta}$; on the second triple and on the three diagonals the bracket vanishes; and the identity is fixed.

**The reading of the example.** One operator, three arrays, one spectrum $\{0^{10},(\pm4i)^{3}\}$ and one rank six. The matrix-unit array displays the spectrum; the plane array displays the image, which is the three planes through $t$ and nothing else; the word array is the axis-free form, and it is the array in which the other fifteen generators are also written. A reader who wants the spectrum reads the diagonal array, a reader who wants the geometry reads the plane array, and a reader who wants the integral structure reads the array in the words.

## The Ranks and the Length

**Proposition (the rank of a product operator).** For two operators $A$ and $B$ of order four, the rank of $\Theta_{A,B}$ as a map of the operator space is $\operatorname{rank}A\cdot\operatorname{rank}B$, so the possible ranks are $0$ and the nine products of two numbers of $\{1,2,3,4\}$.

*Proof.* The rank of a Kronecker product, and the ranks of $A$ and of $B$ ranging over the five values $0,1,2,3,4$; the nonzero products are $1,2,3,4,6,8,9,12,16$.

**The reading.** At the level below an operator of the biquaternion algebra has rank four or zero, because the algebra is a division algebra, and a two-sided operator has rank four over the invertible pairs. At this level the factors are operators, whose ranks are the ten of a matrix of order four, and the rank of the product is the product. The rank stratifies the product operators into nine nonzero values, against the two of the level below.

**Proposition (the length).** Every operator on the operator space is a sum of two-sided products, and the least number of them is the rank of its $16\times16$ array. So the length takes the values $1$ to $16$ and is a property of the array alone.

*Proof.* An expansion $\Phi=\sum_k\Theta_{A_k,B_k}$ is an expansion of the array as $\sum_k A_k\otimes B_k^{\mathsf T}$, and the least number of terms in such an expansion of a tensor in $M_4\otimes M_4$ is the rank of the matricised tensor, which is the array itself.

**Corollary (the two invariants measure different things).** A single product has length one and rank $\operatorname{rank}A\cdot\operatorname{rank}B$, which runs over the nine nonzero values; so the length does not determine the rank. The identity has length one and rank sixteen, and a product of two projections of rank two has length one and rank four.

*Proof.* The first sentence is the two propositions; the identity is $\Theta_{\mathrm{I},\mathrm{I}}$ and a projection of rank two has, as a factor, the rank two.

**The reading.** The two invariants measure different things, as at the level below. The length measures the tensor and the array; the rank measures the map. The first is between one and sixteen and the second between zero and sixteen, and the two agree neither in general nor at the identity.

## Summary

The operator space $V=\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ has complex dimension sixteen and the sixteen words $W_{\mu\nu}=L_\mu R_\nu$ are an orthogonal basis of it, with $\langle W_{\mu\nu},W_{\rho\sigma}\rangle=4\delta$. An operator on the operator space is an element of $\mathcal{A}=\operatorname{End}_{\mathbb{C}}(V)$ of complex dimension two hundred and fifty-six, and its array is a $16\times16$ matrix in the words. The change of basis from the matrix units is the orthogonal $P$, with $P_{(\mu\nu),(ij)}=\tfrac12(W_{\mu\nu})_{ij}$.

The two-sided operator $\Theta_{A,B}(S)=ASB$ has the Kronecker array $A\otimes B^{\mathsf T}$ in the matrix units and its similarity by $P$ in the words. Its trace is $\operatorname{tr}A\operatorname{tr}B$, its determinant $(\det A)^{4}(\det B)^{4}$, its rank $\operatorname{rank}A\cdot\operatorname{rank}B$, and its spectrum the sixteen products of the eigenvalues of the two factors. The composition law is $\Theta_{A,B}\Theta_{C,D}=\Theta_{AC,DB}$; the pairs form a cone of complex dimension thirty-one; and the products of two words are the $256$ signed permutations of order sixteen.

The left and the right copies are of dimension sixteen with the scalars in common, so their sum is of dimension thirty-one, and the complement of dimension $225$ is the product of the two traceless spaces. The derivation $\mathrm{ad}_K$ has the array $K\otimes\mathrm{I}_4-\mathrm{I}_4\otimes K^{\mathsf T}$, kernel the centraliser of $K$ of dimension $\sum m_i^{2}$, rank $16-\sum m_i^{2}$ and spectrum the sixteen differences; the fifteen generators of $\mathfrak{su}(4)$ give fifteen anti-Hermitian traceless arrays of order sixteen, six real antisymmetric and nine imaginary symmetric, with the ranks $8$, $10$ and $6$ of the three shapes; the rotor is $U\otimes\bar U$; and the form on the fifteen arrays is $8$ times the form on the fifteen generators in the words basis.

The ladder is $512\to256\to30\to15$. Every operator on the operator space is a sum of at most sixteen two-sided products, the least number being the rank of its array, and the derivation of the sum $iD$ is one operator with three arrays, one per basis: the diagonal one of the matrix units, the twenty-four-entry one of the words, and the three-block one of the planes.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra, of complex dimension four |
| $V$ | the operator space $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, of complex dimension sixteen |
| $\mathcal{A}$ | the space of operators on operators, $\operatorname{End}_{\mathbb{C}}(V)$, of complex dimension two hundred and fifty-six |
| $L_\mu$, $R_\nu$ | the axis-free matrices $L_{\mathrm{axf},e_\mu}$ and $R_{\mathrm{axf},e_\nu}$ of left and right multiplication |
| $\ell_k$, $r_k$ | the axis-free matrices $L_{\mathrm{axf},\vec e_k}$ and $R_{\mathrm{axf},\vec e_k}$, the first six generators, printed whole |
| $g_k$ | the generator $\tfrac12\mathsf{M}_2(\vec e_k)$ of the $M_2(\mathbb{C})$ article, which names it $G_k$ |
| $N_{jk}$ | the product $\ell_jr_k$, a real symmetric signed permutation |
| $W_{\mu\nu}$ | the word $L_\mu R_\nu=T_{e_\mu,e_\nu}$ |
| $E_{ij}$ | the matrix unit of order four, $i,j$ standing for $t,x,y,z$ |
| $P$ | the orthogonal change of basis, $P_{(\mu\nu),(ij)}=\tfrac12(W_{\mu\nu})_{ij}$ |
| $[\Phi]_{W}$, $[\Phi]_{E}$ | the array of $\Phi$ in the words and in the matrix units |
| $\Theta_{A,B}$ | the two-sided operator $S\mapsto ASB$ |
| $\Lambda_A$, $\Rho_B$ | the left and the right multipliers $S\mapsto AS$ and $S\mapsto SB$ |
| $\mathrm{ad}_K$ | the derivation $S\mapsto KS-SK$ |
| $\langle S,T\rangle$ | the form $\operatorname{tr}(S^{*}T)$ on $V$ |
| $\langle\Phi,\Psi\rangle_{\mathcal{A}}$ | the form $\operatorname{tr}(\Phi^{*}\Psi)$ on $\mathcal{A}$ |
| $G_a$, $a=1,\dots,15$ | the fifteen generators in the words basis |
| $A_{jk}$, $iS_{jk}$ | the twelve off-diagonal generators of the plane basis |
| $iD$, $d_2$, $d_3$ | the three diagonal generators of the plane basis |
| $K\otimes L$ | the Kronecker product of two matrices of order four |
| $\mathfrak{sl}_4$ | the traceless operators, of complex dimension fifteen |
| $\operatorname{rank}$, $\operatorname{spec}$ | the rank of a matrix, the spectrum of an operator |

## Further Reading

- [$M_4(\mathbb{C})$ Axis-Free Representation : Operators](m4c-axis-free-representation-operators.html), for the level below: the one-sided copies, the sixteen products and the coefficient matrix.
- [The Anti-Hermitian Derivations of $M_4(\mathbb{C})$ as $\mathfrak{su}(4)$](the-anti-hermitian-derivations-of-m4c-as-su4.html), for the fifteen generators at the level of the algebra, the grading and the two bases.
- [The Anti-Hermitian Derivations of the Operators of the Biquaternion Algebra as $\mathfrak{su}(4)$](the-anti-hermitian-derivations-of-the-operators-of-the-biquaternion-algebra-as-su4.html), for the same fifteen read as operators on the algebra.
- [$\operatorname{End}(\mathbb{B})$ as an Algebra: the Regular Representation](end-b-as-an-algebra-the-regular-representation.html), for the two-sided products and the law $T_{a,b}T_{c,d}=T_{ac,db}$.
- [The Two-Sided Operators and the Segre Cone](the-two-sided-operators-and-the-segre-cone.html), for the cone of the products and its projective image.
- [The Length and the Two Ranks](the-length-and-the-two-ranks.html), for the minimal number of products at the level below.
- [Matrix Representations and Conventions](matrix-representations-conventions.html), for the axis-free matrices $L_{\mathrm{axf}}$ and $R_{\mathrm{axf}}$ the words are built from.
- [The Anti-Hermitian Derivations of $M_2(\mathbb{C})$ as $\mathfrak{su}(2)$](the-anti-hermitian-derivations-of-m2c-as-su2.html), for the same six axis-free matrices printed whole, in the frame that fixes no sign of $\sigma_k$, and for the halves $\tfrac12\ell_k$ and $\tfrac12(\ell_k-r_k)$ that are its generators.
