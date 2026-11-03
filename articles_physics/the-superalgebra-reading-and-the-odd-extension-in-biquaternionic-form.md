# __The Superalgebra Reading and the Odd Extension in Biquaternionic Form__

## Introduction

The biquaternion algebra is the even part of the graded Clifford algebra, $\mathbb{B}=\mathrm{Cl}^0_{1,3}$, and the graded commutator $[a,b]_{\mathrm{gr}}=ab-(-1)^{\lvert a\rvert\lvert b\rvert}ba$ makes the ambient algebra a Lie superalgebra whose even part is the algebra of the series. That structure is built from the product and the parity, and the article develops it with the supercharge, the odd extension and the boundary between what the algebra supplies and what it imports.

A superalgebra used by physics does not carry only a bracket; it carries an **adjoint**, the operation that turns a state into a dual state and an operator into its Hermitian conjugate, and it is the adjoint that makes the Hamiltonian Hermitian and the probabilities real. The odd sector is reached through the star, the Hermitian conjugation $X^{*}$ of the element, and not through a second parameter; on an operator the same structure appears as the dagger of the corpus's operator conventions, $(L_a)^{\dagger}=L_{a^{*}}$, one mark for each of the two layers. The object of the article is the interaction of the two: a $\mathbb{Z}/2$-graded algebra with a parity-preserving anti-involution, and the sign it puts on the graded bracket.

Three statements carry the interpretation. The first is that the star is an **even anti-involution** of the superalgebra, $(ab)^{*}=b^{*}a^{*}$ with $\lvert a^{*}\rvert=\lvert a\rvert$; it is the structure the corpus's own physics uses, since the biquaternionic supercharge is paired with its star — written there with the dagger of the operators, $\{\mathcal{Q},\mathcal{Q}^{\dagger}\}=H$ — in *Supersymmetric Quantum Physics in the Biquaternion Framework*. The second is that the adjoint **reverses the graded bracket** up to the parity sign,

$$
\bigl([a,b]_{\mathrm{gr}}\bigr)^{*}=-(-1)^{\lvert a\rvert\lvert b\rvert}\,\bigl[a^{*},b^{*}\bigr]_{\mathrm{gr}},
$$

so it reverses a commutator and preserves an anticommutator, the reason being that the order reversal of the adjoint and the Koszul sign of the bracket multiply, and cancel exactly on an odd-odd pair. The third is that this is a statement about the *convention*: the Koszul-signed rule of a super-* would make the star an anti-automorphism of the bracket without the extra sign, and the corpus's star does not obey that rule; the two conventions are distinguished by a check on two generators, and the article records which one the physics uses — and why it has to be that one: on the other convention the square of a Hermitian odd element is anti-Hermitian, so the Hamiltonian would be imaginary.

The body is written in **cells**: an operator is a two-sided multiplication $L_{a}R_{b}$, $\psi\mapsto a\psi b$, its adjoint is the cell $(L_{a}R_{b})^{\dagger}=L_{a^{*}}R_{b^{*}}$, and the odd generator acts by the left multiplication $L_{u}$ by a single vector. The matrix frame is those same cells written as letters; it is collected in *The Gamma Formulation*, which is the only section of the article where that frame appears, and it is there that the two Dirac equations the corpus carries — the one-sided chiral pair and the two-sided cell equation — are kept apart.

The graded bracket, the parity table, the Lie-superalgebra statement and the odd extension are restated here in the form the physics uses; the parity interpretation of the ambient algebra and the sectors are *The Grading, Fermion Parity and the Two Sectors in Biquaternionic Form*; the supercharge pair and the chirality grading are *Supersymmetric Quantum Physics in the Biquaternion Framework*; the Grassmann envelope is *Grassmann Coherent States in Biquaternionic Form* and *BRST Symmetry in Biquaternionic Form*; the commutator bracket and the trace-free part are *Symmetric and Antisymmetric Decomposition of the Four General Products*; the one-mode parity is *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*. Nothing owned by those articles is re-derived.

## The Graded Algebra and Its Parity

**Definition.** On a $\mathbb{Z}/2$-graded algebra $A=A^0\oplus A^1$ the **graded commutator** is

$$
[a,b]_{\mathrm{gr}}=ab-(-1)^{\lvert a\rvert\lvert b\rvert}ba ,
$$

the two parities read modulo two. It is the commutator on an even or a mixed pair and the anticommutator on two odd elements, and it satisfies the graded Jacobi identity, making a Lie superalgebra of the graded algebra with the graded commutator as bracket.

**Proposition (the parity of the bracket).** For homogeneous $a,b$ the bracket is even,

$$
\bigl\lvert[a,b]_{\mathrm{gr}}\bigr\rvert=\lvert a\rvert+\lvert b\rvert \pmod 2 ,
$$

so the bracket of two odd elements is even, the bracket of an even and an odd element is odd, and the bracket of two even elements is even. On the ambient Clifford algebra,

$$
[\mathbb{B},\mathbb{B}]\subseteq\mathbb{B},\qquad
[\mathbb{B},\mathrm{Cl}^1]\subseteq\mathrm{Cl}^1,\qquad
\{\mathrm{Cl}^1,\mathrm{Cl}^1\}\subseteq\mathbb{B}.
$$

**Proof.** A product of $i$ and of $j$ frame vectors is a sum of terms of grades $i+j$, $i+j-2$, $\dots$, all of the same parity $i+j$; so the product of an even and an even element is even, of an even and an odd element is odd, and of two odd elements is even, which gives the three inclusions. The bracket is the commutator unless both elements are odd, in which case it is the anticommutator, and the parity of a commutator or an anticommutator is the sum of the parities.

**The grades and their parity.** The ambient algebra is filtered by the number of vector factors, and the parity is that number reduced modulo two; the filtration is not a grading, because a product of two vectors is a scalar plus a bivector. The table gives the five grades with a basis, the dimension and the part of the ambient algebra that each occupies. The superscript of $\mathrm{Cl}^i$ is the **parity** and not the grade: $\mathrm{Cl}^0=\mathbb{B}$ collects the grades $0$, $2$ and $4$, and $\mathrm{Cl}^1$ collects the grades $1$ and $3$.

| Grade | A basis | Dimension | Parity | Part |
|---|---|---|---|---|
| $0$ | $1$ | $1$ | even | $\mathbb{B}$ |
| $1$ | $v_\mu$ | $4$ | odd | $\mathrm{Cl}^1$ |
| $2$ | $v_\mu v_\nu$, $\mu<\nu$ | $6$ | even | $\mathbb{B}$ |
| $3$ | $v_\mu v_\nu v_\rho$ | $4$ | odd | $\mathrm{Cl}^1$ |
| $4$ | $\omega=v_0v_1v_2v_3$ | $1$ | even | $\mathbb{B}$ |

The even part has dimension $1+6+1=8$ and the odd part $4+4=8$; the odd slot is therefore the sum of the vector and the trivector grades, and it is not a single grade. The Clifford relations are $\{v_\mu,v_\nu\}=2g_{\mu\nu}e_t$ with $g=(+1,-1,-1,-1)$, so $v_0^2=e_t$ and $v_k^2=-e_t$.

**Remark (the even part is the Lie algebra of the framework).** The restriction of the graded bracket to $\mathbb{B}$ is the ordinary commutator, that is the Lie algebra of *Symmetric and Antisymmetric Decomposition of the Four General Products*, whose trace-free part is the Lorentz algebra. The odd slot is a module over the even part and not a second Lie algebra: the bracket of two odd elements is even, exactly as the bracket of two reflections is a rotation.

## The Module and the Cells

The operators of the article are the two-sided multiplications of the algebra on itself, and every one of them is written as a cell rather than as a matrix.

**Definition.** For $\psi\in\mathbb{B}$ and $a,b\in\mathbb{B}$,

$$
L_a\psi=a\psi,\qquad R_b\psi=\psi b,\qquad L_aR_b\,\psi=a\psi b ,
$$

and the composition rule is

$$
L_aR_b\,L_cR_d=L_{ac}R_{db},
$$

the right multipliers composing in reverse order. The two-sided action is the reason for the reversal: the element $d$ acts first, and the element $b$ acts on the result.

**Proposition (the cells span the operators).** The sixteen cells $L_{a}R_{b}$, with $a$ and $b$ ranging over a basis $\{e_t,\vec e_x,\vec e_y,\vec e_z\}$ of $\mathbb{B}$, are a basis of $\mathrm{End}_{\mathbb{C}}(\mathbb{B})$, and a general $\mathbb{C}$-linear operator is a finite sum of cells, of at most four of them.

**Proof.** Both spaces have complex dimension sixteen, and the cells are linearly independent: $L_aR_b$ is the tensor $a\otimes b^{\mathrm{opp}}$ under the identification $\mathrm{End}_{\mathbb{C}}(\mathbb{B})\cong\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}$. A sum of $k$ pure tensors is a tensor of rank at most $k$, and the rank of a tensor in a four-dimensional factor is at most four.

**Proposition (the adjoint of a cell).** With the Hermitian form of the corpus,

$$
\langle s,t\rangle_{*}=\mathrm{Sc}\bigl(s\,t^{*}\bigr),
\qquad
\langle s,s\rangle_{*}=\lvert s_t\rvert^{2}+\lvert s_x\rvert^{2}+\lvert s_y\rvert^{2}+\lvert s_z\rvert^{2}>0 ,
$$

the adjoint of a cell is a cell,

$$
\boxed{\;(L_aR_b)^{\dagger}=L_{a^{*}}R_{b^{*}}\;},
$$

and the cell is Hermitian, $(L_aR_b)^{\dagger}=L_aR_b$, exactly when

$$
a^{*}=\lambda a,\qquad b^{*}=\lambda^{-1}b,\qquad \lvert\lambda\rvert=1 ,
$$

which is wider than the case of two Hermitian multipliers. The rescaling $L_{\mu a}R_{b/\mu}=L_aR_b$ carries $\lambda$ to $\lambda\bar\mu/\mu=\lambda\mu^{-2}$ for $\lvert\mu\rvert=1$, and $\mu^{2}=\pm\lambda$ gives the two signs, so the condition says that the two multipliers can be chosen **simultaneously** Hermitian or simultaneously anti-Hermitian; that is the case the frame uses, and a cell such as $L_aR_b$ with $a^{*}=ia$ and $b^{*}=-ib$ is Hermitian without either multiplier being so.

*Proof.* For $\psi\in\mathbb{B}$ one has $\langle a\psi b,t\rangle_{*}=\mathrm{Sc}\bigl(a\psi b\,t^{*}\bigr)=\mathrm{Sc}\bigl(\psi\,bt^{*}a\bigr)=\bigl\langle\psi,a^{*}tb^{*}\bigr\rangle_{*}$, the middle step by the cyclicity of the scalar part, $\mathrm{Sc}(xyz)=\mathrm{Sc}(zxy)$, and the last because $(a^{*}tb^{*})^{*}=b\,t^{*}a$. The form is Hermitian and positive definite by the display, the star being the Hermitian conjugation of the algebra, so the operator $L_{a^{*}}R_{b^{*}}$ is the adjoint of $L_aR_b$.

**Definition (the odd unit).** Fix a non-isotropic vector $u$ of the frame, $u^2=q(u)e_t$. The odd part of the ambient algebra is the free module of rank one

$$
\mathrm{Cl}^1=\mathbb{B}u,
$$

and an odd element is $su$ with $s$ even. The odd slot is generated by one cell: $L_u$ carries the even part into the odd part, and the operator of an odd element is $L_{su}=L_sL_u$, the fixed odd cell preceded by an even one.

**Remark (two properties of the odd unit).** Since $u$ is a vector, $u^{*}=-u$ under the star of §*The Adjoint of the Graded Bracket*; and $L_u$ is an odd operator, because it maps the even part to the odd part. Both statements are used below. The star is an anti-automorphism, so that $(su)^{*}=u^{*}s^{*}$ and not $s^{*}u^{*}$.

## The Adjoint of the Graded Bracket

**Proposition (the star is an even anti-involution of the superalgebra).** The Hermitian conjugation satisfies

$$
\boxed{\;(ab)^{*}=b^{*}a^{*},\qquad (a^{*})^{*}=a,\qquad \lvert a^{*}\rvert=\lvert a\rvert\;}
$$

so it is an anti-automorphism of the graded algebra and it preserves the grading; it is $\mathbb{C}$-antilinear. This is the star on the elements; the dagger is the adjoint of the corresponding operators, $(L_a)^{\dagger}=L_{a^{*}}$ and, on the cells, $(L_aR_b)^{\dagger}=L_{a^{*}}R_{b^{*}}$, so that the two markings name one structure in the two layers.

*Proof.* The reversion reverses the order of the factors, the grade involution acts on the degree and not on the order, and the coefficient conjugation is a $\mathbb{C}$-antilinear automorphism acting on the coefficients only; the composite therefore reverses the order and preserves the degree, so it is an anti-automorphism, involutive and even. On the algebra this is the Hermitian conjugation $\tilde{Q}^{*}=\overline{\tilde{Q}^{\natural}}$ of the corpus.

**Proposition (the adjoint reverses a commutator and preserves an anticommutator).** For homogeneous $a,b$,

$$
\boxed{\;\bigl([a,b]_{\mathrm{gr}}\bigr)^{*}=-(-1)^{\lvert a\rvert\lvert b\rvert}\,\bigl[a^{*},b^{*}\bigr]_{\mathrm{gr}}\;},
$$

that is

$$
\bigl([a,b]_{\mathrm{gr}}\bigr)^{*}=
\begin{cases}
-\,\bigl[a^{*},b^{*}\bigr]_{\mathrm{gr}}, & a,b\ \text{not both odd},\\[2pt]
+\,\bigl[a^{*},b^{*}\bigr]_{\mathrm{gr}}, & a,b\ \text{both odd}.
\end{cases}
$$

*Proof.* Apply the anti-automorphism to the definition: $\bigl([a,b]_{\mathrm{gr}}\bigr)^{*}=(ab)^{*}-(-1)^{\lvert a\rvert\lvert b\rvert}(ba)^{*}=b^{*}a^{*}-(-1)^{\lvert a\rvert\lvert b\rvert}a^{*}b^{*}$. Since $\lvert a^{*}\rvert=\lvert a\rvert$ and $\lvert b^{*}\rvert=\lvert b\rvert$, the same exponent occurs in $\bigl[a^{*},b^{*}\bigr]_{\mathrm{gr}}=a^{*}b^{*}-(-1)^{\lvert a\rvert\lvert b\rvert}b^{*}a^{*}$, and the two expressions differ by the factor $-(-1)^{\lvert a\rvert\lvert b\rvert}$; for $a,b$ both odd the factor is $+1$, and otherwise it is $-1$. The identity was checked on the sixteen basis elements of the ambient algebra, hence on all $256$ of their products, and separately on the four frame vectors $v_\mu$ and on the products of two of them, for all four parity pairs.

**Remark (the same rule in cells).** In the two-sided operators the statement is the one of §*The Module and the Cells*, $(L_aR_b)^{\dagger}=L_{a^{*}}R_{b^{*}}$, and it is consistent with the element rule because $(ab)^{*}=b^{*}a^{*}$ and $L$ is a homomorphism: $L_{(ab)^{*}}=L_{b^{*}a^{*}}=L_{b^{*}}L_{a^{*}}$, the two left multiplications composing in the order opposite to the reversed product. A cell preserves the parity when its two multipliers have the same parity and flips it when they differ, and the star preserves the parity of each multiplier, so the adjoint preserves the parity of the cell.

**Remark (why the two behave differently).** The adjoint reverses the order of the two factors, and the graded bracket distinguishes the two orders by the sign $(-1)^{\lvert a\rvert\lvert b\rvert}$ exactly in the odd-odd case, where the bracket is symmetric: a symmetric bracket is preserved by the reversal, an antisymmetric one is negated. The statement is therefore not an accident of the Clifford algebra but the interaction of two signs, the order reversal of the adjoint and the Koszul sign of the bracket. On the even part, where the bracket is the Lie bracket of the framework, the rule reads $\bigl([a,b]\bigr)^{*}=-\bigl[a^{*},b^{*}\bigr]$, so the bracket of two anti-Hermitian elements is anti-Hermitian: the anti-Hermitian part is a Lie subalgebra, the compact form of the framework, while the Hermitian generators enter it with the conventional factor $i$.

**Remark (the Koszul-signed convention and what the star is not).** A superalgebra is often equipped with a super-* satisfying the Koszul-signed rule $(\xi\eta)^{*}=(-1)^{\lvert\xi\rvert\lvert\eta\rvert}\eta^{*}\xi^{*}$. For such a structure the bracket-adjoint identity reads $\bigl([a,b]_{\mathrm{gr}}\bigr)^{*}=-\bigl[a^{*},b^{*}\bigr]_{\mathrm{gr}}$ without the extra parity sign. The star of the corpus is **not** of that kind: on two generators $v_0,v_1$, both odd, one has

$$
(v_0v_1)^{*}=v_1^{*}v_0^{*}=(-v_1)(-v_0)=v_1v_0=-v_0v_1 ,
$$

while the Koszul-signed expression would be $(-1)^{1\cdot1}v_1^{*}v_0^{*}=-v_1v_0=+v_0v_1$; the two minus signs of the anti-Hermitian generators cancel in each expression, so the two results differ by the Koszul sign alone: both rules reverse the order of the factors, and only the plain one reverses it without an extra sign. The corpus's star is the plain anti-involution, and the factor $(-1)^{\lvert a\rvert\lvert b\rvert}$ in the bracket identity is the price of it. A reader importing the super-* convention from the supersymmetry literature must choose which of the two signs his own star obeys, and the two are not the same map.

**Remark (why the physics forces the plain rule).** The choice is not aesthetic. Take a supercharge that is Hermitian, $\mathcal{Q}^{*}=\mathcal{Q}$, as the Hamiltonian's Hermiticity requires of the operator that squares to it, and compute its graded square under the two rules. Under the plain rule $(ab)^{*}=b^{*}a^{*}$ one finds $\{\mathcal{Q},\mathcal{Q}\}^{*}=2\mathcal{Q}\mathcal{Q}^{*}=\{\mathcal{Q},\mathcal{Q}^{*}\}$, which is Hermitian: the Hamiltonian is real. Under the Koszul-signed rule, $(\mathcal{Q}\mathcal{Q})^{*}=(-1)^{1\cdot1}\mathcal{Q}^{*}\mathcal{Q}^{*}=-\mathcal{Q}^{2}$, so the square of a Hermitian odd element is **anti-Hermitian** and its spectrum imaginary. A superalgebra whose odd generator squares to the Hamiltonian therefore cannot carry the signed rule; the corpus's plain star is the one the physics selects, and the parity sign in the bracket identity above is what that selection costs.

## Supercharges, the Adjoint and the Odd Generators

**Definition.** A **supercharge** is an odd element $\mathcal{Q}$ whose square is even and central, and the physics pairs it in two ways, which are not the same display.

**(i) The square.** The anticommutator of the element with itself is its square,

$$
\{\mathcal{Q},\mathcal{Q}\}=2\mathcal{Q}^{2}=2H,\qquad [\mathcal{Q},H]_{\mathrm{gr}}=0 ,
$$

so that the square is a bosonic element commuting with $\mathcal{Q}$, and it is Hermitian as well when $\mathcal{Q}$ is, since $(\mathcal{Q}^{2})^{*}=(\mathcal{Q}^{*})^{2}$. This needs $\mathcal{Q}^{2}\neq0$. In the Clifford parity it is the relation of the ambient algebra, where the square of a frame vector is central, $v_\mu^{2}=g_{\mu\mu}e_t$; in the chirality grading of the supersymmetry article the odd object is the gradient, and its square is the central scalar, $\tilde\nabla\tilde\nabla^{\natural}=\Box$, which is the $H$ of that reading.

**(ii) The star.** In the Hermitian interpretation the physical pairing is the one with the **star** rather than with the element itself,

$$
\boxed{\;\{\mathcal{Q},\mathcal{Q}^{*}\}=2H'\;}
$$

with $H'$ the Hamiltonian of that reading; it is the convention of *Supersymmetric Quantum Physics in the Biquaternion Framework*, $\{\mathcal{Q},\mathcal{Q}^{\dagger}\}=H$, $\mathcal{Q}^{2}=(\mathcal{Q}^{\dagger})^{2}=0$. There it is the *nilpotent* realisation that is in play: the supercharge is strictly triangular, its square vanishes, and the Hamiltonian is not a square at all but the off-diagonal product $AA^{\dagger}$, which is why the first display would give $H=0$ and the second does not.

The two agree when $\mathcal{Q}^{*}=\mathcal{Q}$. They also agree, **at zero**, on one family, and it is worth naming because it shows what the agreement is not. Let $\omega=v_0v_1v_2v_3$ be the pseudoscalar, with $\omega^{2}=-1$, and put

$$
B=v\,(1-i\omega)=v+i\omega v .
$$

A vector changes sign under the star and a trivector does not, so $v$ is anti-Hermitian and $i\omega v$ is anti-Hermitian as well: $B^{*}=-B$. Its square is

$$
B^{2}=q(v)\,e_t\,(1+i\omega)(1-i\omega)=q(v)\,e_t\,(1-i^{2}\omega^{2})=0 ,
$$

because $i^{2}=-1$ and $\omega^{2}=-1$ give $i^{2}\omega^{2}=+1$. On such an element both pairings vanish, so their agreement there carries no Hamiltonian. Apart from that vanishing family the agreement forces $\mathcal{Q}^{*}=\mathcal{Q}$: it makes $\mathcal{Q}^{2}$ Hermitian and $(\mathcal{Q}-\mathcal{Q}^{*})^{2}=0$, and a search over the odd slot returns no element on which the two are equal and nonzero. Outside that family, for an odd element that is not Hermitian, the two differ, and on a vector they differ by a sign,

$$
\{u,u\}=2q(u)e_t,\qquad \{u,u^{*}\}=-2q(u)e_t ,
$$

because $u^{*}=-u$. The factor $i$ that repairs the anti-Hermitian $u$ into the Hermitian $iu$ multiplies the square by $i^{2}=-1$, and then $\{iu,iu\}=-2q(u)e_t=\{\,iu,(iu)^{*}\}$: the two displays are reconciled by one factor of $i^{2}=-1$, and it is the same sign that the Hermitian repair of the framework's gradient carries.

**Proposition (the starred pairing is Hermitian and even).** If $\mathcal{Q}$ is odd then $\mathcal{Q}^{*}$ is odd and

$$
\{\mathcal{Q},\mathcal{Q}^{*}\}=\mathcal{Q}\mathcal{Q}^{*}+\mathcal{Q}^{*}\mathcal{Q}
$$

is even and Hermitian, $\{\mathcal{Q},\mathcal{Q}^{*}\}^{*}=\{\mathcal{Q},\mathcal{Q}^{*}\}$; a supercharge is never an element of $\mathbb{B}$.

*Proof.* The star preserves the parity, so $\mathcal{Q}^{*}$ is odd and the product of two odd elements is even; the anticommutator of two elements and the star of a product give $\{\mathcal{Q},\mathcal{Q}^{*}\}^{*}=(\mathcal{Q}\mathcal{Q}^{*}+\mathcal{Q}^{*}\mathcal{Q})^{*}=\mathcal{Q}\mathcal{Q}^{*}+\mathcal{Q}^{*}\mathcal{Q}$ by the anti-automorphism property. Since $\mathbb{B}=\mathrm{Cl}^0$ contains no odd element, no supercharge is an element of the algebra.

**Remark (the operator of a supercharge).** The supersymmetry article writes the pairing with a dagger, $\{\mathcal{Q},\mathcal{Q}^{\dagger}\}=H$, because its $\mathcal{Q}$ is an operator on $\Delta$; the element of the odd slot is what that operator multiplies by, and the two markings are one structure, $L_{\mathcal{Q}^{\dagger}}=(L_{\mathcal{Q}})^{\dagger}=L_{\mathcal{Q}^{*}}$. Read as an operator on the module, the supercharge is the left multiplication $L_{\mathcal{Q}}$, and its adjoint is the left multiplication by the star, $L_{\mathcal{Q}}^{\dagger}=L_{\mathcal{Q}^{*}}$. The pairing of the operator with its adjoint is therefore the left multiplication by the pairing of the elements,

$$
L_{\mathcal{Q}}L_{\mathcal{Q}^{*}}+L_{\mathcal{Q}^{*}}L_{\mathcal{Q}}=L_{\{\mathcal{Q},\mathcal{Q}^{*}\}},
$$

with no sign and no order correction, because $L$ is a homomorphism and the two factors are odd, so that their graded bracket is already the anticommutator. This is the precise sense in which the superalgebra of the article is an algebra of cells.

**Remark (why the adjoint and not the inverse).** The Hamiltonian of the framework must be Hermitian, and its spectrum real, and the pairing $\{\mathcal{Q},\mathcal{Q}^{*}\}$ is Hermitian automatically because the star is an involution and the two odd factors reverse in it; a pairing built with the inverse, $\{\mathcal{Q},\mathcal{Q}^{-1}\}$, has no reason to be. This is the physical content of the Hermitian reading of the odd sector: the operator that pairs the two chiralities is the adjoint of the supercharge and not its inverse, and the corpus's own supersymmetric realisation of the mass pair is written with the dagger for that reason. The star is the inverse only up to a central scalar and the coefficient conjugation, $X^{*}=\sigma(\langle X\rangle_{\natural})\sigma(X)^{-1}$, so on the unit slice of the real quaternions the two coincide and elsewhere they differ by a scalar; the bracket structure below is insensitive to it, which is the honest scope of the distinction.

**Remark (the supercharge in the module).** The odd slot is the rank-one module $\mathrm{Cl}^1=\mathbb{B}u$ for a non-isotropic vector $u$ ($u^2=q(u)e_t$, $q$ the quadratic form), so an odd element is $\mathcal{Q}=su$ with $s$ even. By the anti-automorphism property, and because a vector is anti-Hermitian, its adjoint is

$$
\mathcal{Q}^{*}=(su)^{*}=u^{*}s^{*}=-u\,s^{*},
$$

an odd element again, and

$$
\mathcal{Q}\,\mathcal{Q}^{*}=s\,u\,(-u)\,s^{*}=-q(u)\,s\,s^{*},
$$

an even and Hermitian element, the first half of the pairing of the supercharge with its star. The product $u^2=q(u)e_t$ is central, so no commutation is needed in this line. The pairing itself is

$$
\{\mathcal{Q},\mathcal{Q}^{*}\}=-q(u)\,s\,s^{*}-u\,s^{*}s\,u ,
$$

and the second term collapses to $-q(u)s^{*}s$ when $s$ has a definite $u$-parity, $us=\pm su$; the standard case is $s$ commuting with $u$, for instance a product of an even number of vectors orthogonal to $u$, and then

$$
\{\mathcal{Q},\mathcal{Q}^{*}\}=-q(u)\bigl(s\,s^{*}+s^{*}s\bigr).
$$

The condition is not cosmetic. Split the even element $s^{*}s=w_{+}+w_{-}$ by the $u$-parity, $uw_{\pm}=\pm w_{\pm}u$; then $u\,s^{*}s\,u=q(u)(w_{+}-w_{-})$, so a part of $u$-parity $-1$ in $s^{*}s$ enters the second term with the opposite sign. The pairing remains even and Hermitian, as the proposition above proves, but it is the symmetric expression only when $w_{-}=0$. For a spacelike $u$ the factor $-q(u)$ is $+1$, and the pairing is the manifestly positive $ss^{*}+s^{*}s$, which is the form the Hamiltonian takes in the one-mode case.

## What Must Be Adjoined

Two constructions in the series adjoin the missing odd sector, and in the Hermitian interpretation each has to be compatible with the star.

**The Grassmann envelope.** The odd generators can be made to carry anticommuting coefficients by tensoring with a Grassmann algebra, the construction of *Grassmann Coherent States in Biquaternionic Form*; *BRST Symmetry in Biquaternionic Form* uses the same envelope for the ghosts and records as an **open question** whether a biquaternionic envelope can be found that is natural rather than imported. In the Hermitian interpretation the question acquires a second clause: the envelope must carry an involution compatible with the star of the algebra, since a Berezin integral and a Hilbert structure must be defined on the same object. The Grassmann algebra does carry one — the coefficient conjugation extended to the odd coefficients — and that is the envelope the physics uses; what is open is its naturality, not its existence.

**One fermionic mode, natively.** The one piece of fermionic structure that the algebra does host is a single fermionic mode: the creation and annihilation operators of one mode are elements of the algebra, the parity is the element $(-1)^F=i\vec e_z$ of the informational sector, and the algebra's own graded structure therefore carries the finite one-mode case without any extension. The element is Hermitian, $(i\vec e_z)^{*}=(-i)(-\vec e_z)=i\vec e_z$, and it squares to the identity,

$$
(-1)^F(-1)^F=i^2\,\vec e_z^2=(-1)(-e_t)=e_t ,
$$

by $i^2=-1$ and $\vec e_z^2=-e_t$, so it is a parity operator of a $*$-unitary theory, $(-1)^F\in\mathbb{M}_+$. The parity of a field, the product of the element over the modes, $\prod_{\text{modes}}(i\vec e_z)$, is not an element of the algebra.

**Remark (the count of what is adjoined).** One odd generator, and its products with the even elements, exhaust the odd slot: the extension is not "one more algebra" but one more generator, and the rule odd $\times$ odd $=$ even that it brings with it.

## One Graded Algebra, Not Two

**Proposition.** With one odd unit $u$ one has $\mathrm{Cl}_{1,3}=\mathbb{B}\oplus\mathbb{B}u$, every supercharge is a $\mathbb{B}$-multiple of $u$, and the odd slot carries the Hermitian form induced by the module structure, $\langle su,tu\rangle_{*}=-q(u)\langle s,t\rangle_{*}$ and $\langle s,tu\rangle_{*}=0$ for even $s,t$, with $\langle s,t\rangle_{*}=\mathrm{Sc}(st^{*})$.

**Proof.** The decomposition is the rank-two module statement of *The Grading, Fermion Parity and the Two Sectors in Biquaternionic Form*, and an odd element is $su$ with $s$ even. For the form, $(tu)^{*}=u^{*}t^{*}=-u\,t^{*}$, so

$$
\langle su,tu\rangle_{*}=\mathrm{Sc}\bigl(su\,(tu)^{*}\bigr)=-\mathrm{Sc}\bigl(s\,u^{2}\,t^{*}\bigr)=-q(u)\,\mathrm{Sc}\bigl(st^{*}\bigr)=-q(u)\langle s,t\rangle_{*} ,
$$

the third step dropping the two central minus signs of $u^{2}$ and using $u^{2}=q(u)e_t$, which is central and may be moved past $s$. The orthogonality is the vanishing of the scalar part of an odd element, since $s\,(tu)^{*}=-sut^{*}$ is odd for even $s,t$. The elementwise identity without the scalar part is false — a vector need not commute with an even element — and the claim is made only for the form.

**Remark (the sign of the odd form).** The factor $-q(u)$ is $+1$ for a spacelike odd unit, $q(u)=-1$, and $-1$ for a timelike one, $q(u)=+1$. The odd slot therefore carries the form of $\mathbb{B}$ itself for a spacelike $u$ and its negative for a timelike one, and the two choices are isometric up to sign; the sign is a property of the chosen odd unit and not of the superalgebra.

**Remark (why this is the answer to the "two copies" question).** A superalgebra needs an even part, an odd part, the graded bracket between them and the adjoint; it does not need two algebras. The pair $(\mathbb{B},\mathbb{B})$ of two independent copies has no bracket $\{\cdot,\cdot\}\to\mathbb{B}$ between the copies, no grading and no adjoint pairing across them, so it is not a superalgebra. The single graded algebra $\mathrm{Cl}_{1,3}=\mathbb{B}\oplus\mathbb{B}u$ has all of them, and the biquaternion algebra is its even part.

## Honest Limits

- **The algebra is not a superalgebra by itself.** With the Clifford parity the algebra is entirely even; with the chirality $L/R$ splitting the two minimal left ideals give a $\mathbb{Z}/2$ of the module structure and not of the algebra. The statement that "the biquaternion algebra is a superalgebra" needs the ambient algebra or an explicit further grading, and this article does not make it.
- **The supercharge is imported.** The odd generator is not an element of $\mathbb{B}$; the Grassmann envelope or the odd slot of the Clifford algebra is required, and the naturality of that envelope is open in the BRST article.
- **The parity of a field is external.** $(-1)^F$ is an element of the algebra for one mode and a product over modes, hence outside it, for a field.
- **The star of the envelope is a convention.** The corpus defines the star on the algebra; the extension used here, $X^{*}=\sigma(\alpha(X^{r}))$ with $\sigma$ the coefficient conjugation, is the Clifford conjugation of the maths corpus, and it agrees with the algebra's star on the even part through the identification of the frame with the cells. The reversion is the other natural anti-involution of the envelope, and the bracket-adjoint identity holds for it as well, because it is a property of any parity-preserving anti-involution; only the identification of the involution with the physical adjoint depends on the choice, and the reversion is not the adjoint of the spinor form.
- **The symmetric pairing is conditional.** The formula $\{\mathcal{Q},\mathcal{Q}^{*}\}=-q(u)(ss^{*}+s^{*}s)$ is claimed exactly when $s^{*}s$ has no part of $u$-parity $-1$ — in particular for an even $s$ of definite $u$-parity — and not in general, where the second term is $-u\,s^{*}s\,u$; what holds always is that the pairing is even and Hermitian.
- **The two pairings coincide only for a Hermitian supercharge.** For a non-Hermitian odd element they are two different elements, and they coincide only on the nilpotent family $v(1-i\omega)$, where both vanish; a Hamiltonian read from the pair needs $\mathcal{Q}^{*}=\mathcal{Q}$.
- **Nothing here is a measure or an integral.** The Grassmann and Berezin constructions are cited from their articles and are not used; the article is algebra, grading and adjointness.
- **No supersymmetry algebra is claimed to be contained in $\mathbb{B}$.** The super-Poincaré algebra, if it is to be written, is written on an extension; the corpus's supersymmetry article states which superalgebra its construction realizes, and this article adds the general boundary and the Hermitian structure, not a second claim.

## The Gamma Formulation

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra. They are the frame cells of the body written as letters, and this section is the only place in the article where they appear: every section above is written in cells.

Here $L_a$ and $R_b$ are the left and right multiplications of §*The Module and the Cells*, and $c(M)$ is the coefficient matrix of $M$ in the basis of the sixteen products.

$$
\begin{aligned}
\gamma_0 &= iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}, &\gamma_1 &= iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\\[2pt]
\gamma_2 &= iL_{e_y}R_{\vec e_y}^{\mathrm{pau}}, &\gamma_3 &= iL_{e_z}R_{\vec e_y}^{\mathrm{pau}},\\[2pt]
\gamma_5 &= -iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}.
\end{aligned}
$$

The four $\gamma_\mu$ are the images of the frame vectors $v_\mu$ in the representation, and $\gamma_5$ is not a fifth frame vector but the image of their product, the pseudoscalar: $\gamma_5=i\omega$ with $\omega=\gamma_0\gamma_1\gamma_2\gamma_3$. The squares follow from $(L_aR_b)^2=L_{a^2}R_{b^2}$ and $\vec e_k^2=-e_t$,

$$
\gamma_0^2=i^2L_{e_t}^{\mathrm{pau}}R_{\vec e_x^{2}}^{\mathrm{pau}}=i^2L_{e_t}^{\mathrm{pau}}R_{-e_t}^{\mathrm{pau}}=L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}=I_4,\qquad
\gamma_k^2=i^2L_{\vec e_k^{2}}^{\mathrm{pau}}R_{\vec e_y^{2}}^{\mathrm{pau}}=i^2L_{-e_t}^{\mathrm{pau}}R_{-e_t}^{\mathrm{pau}}=-I_4 .
$$

Each square is the product of $i^{2}=-1$ with one minus for every spacelike multiplier: one such multiplier for $\gamma_0$, two for each $\gamma_k$. The products are $(-1)(-1)=+1$ and $(-1)(-1)(-1)=-1$, which is the metric sign. So the four carry the metric $g=\operatorname{diag}(+1,-1,-1,-1)$, and

$$
\{\gamma_\mu,\gamma_\nu\}=2g_{\mu\nu}I_4,\qquad
\{\gamma_\mu,\gamma_5\}=0,\qquad
\gamma_5^2=I_4 .
$$

**The fifth gamma.** The product $\gamma_0\gamma_1\gamma_2\gamma_3$ is computed in cells, and the factors of $i$ are reduced first: the four cells carry $i^4=(i^2)^2=+1$, so the two factors of $i^2=-1$ cancel. The left multipliers multiply in order, $e_t\vec e_x\vec e_y\vec e_z=\vec e_z^2=-e_t$, and the right multipliers compose in reverse, $\vec e_y\vec e_y\vec e_y\vec e_x=\vec e_y^3\vec e_x=-\vec e_y\vec e_x=\vec e_z$. The product is therefore

$$
\gamma_0\gamma_1\gamma_2\gamma_3=-L_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}=-R_{\vec e_z}^{\mathrm{pau}},
$$

and the single $i$ of the definition gives $\gamma_5=i\gamma_0\gamma_1\gamma_2\gamma_3=-iR_{\vec e_z}^{\mathrm{pau}}=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$. The cell $\Gamma:=-iR_{\vec e_z}^{\mathrm{pau}}$ is the chirality cell of the module, and in this frame $\gamma_5=\Gamma$.

**The central grading and the cell.** The cell $\gamma_5$ is the representative on the Dirac module of an object that is not an element of the algebra. The central grading is $\chi=i\tilde\Xi_{\mathrm{ad}}$, with $\tilde\Xi_{\mathrm{ad}}$ the central root of $-e_t$ in the complexification, so that

$$
\chi^2=i^2\,\tilde\Xi_{\mathrm{ad}}^2=(-1)(-e_t)=e_t ,
$$

by $i^2=-1$; $\chi$ is also the difference $e_+-e_-$ of the two central idempotents $e_\pm=\tfrac12(e_t\pm\chi)$. The sign $\chi$ is central and lies outside $\mathbb{B}_{\mathbb{R}}$, and $\gamma_5$ represents it on the module; it is not its definition, and the two must not be identified.

**The two Dirac equations.** The corpus carries two forms of one dynamics, and they are kept apart by where the second chirality slot sits. In units $\hbar=c=1$, with the biquaternionic gradient $\tilde\nabla=e_t\partial/\partial Q_t+\sum_k\vec e_k\partial/\partial Q_k$ and its conjugate $\tilde\nabla^{\natural}$, the **one-sided** form is the chiral pair

$$
\tilde\nabla\tilde\Psi_R=m\tilde\Psi_L,\qquad
\tilde\nabla^{\natural}\tilde\Psi_L=m\tilde\Psi_R ,
$$

two fields, both equations acting from the left, the chirality carried by the two fields and exchanged by $\natural$. The **two-sided** form writes a single field and puts the second slot on the right of the algebra element,

$$
\left(i\frac{\partial}{\partial t'}+D_3\right)F-m\,i\,\overline{F}\,\vec e_z=0,
\qquad
D_3=\sum_k\vec e_k\frac{\partial}{\partial Q_k},
$$

with the derivative acting from the left, the bar the antilinear entry, and $\vec e_z$ multiplying from the right after the conjugation. Since $i\partial/\partial t'=-\partial/\partial Q_t$ in these units, the free part is $-\tilde\nabla^{\natural}$, and the equation reads

$$
\tilde\nabla^{\natural}F=m\left(-i\overline{F}\,\vec e_z\right),
$$

which is the second member of the pair with its left field read as $-i\overline{F}\,\vec e_z$: a conjugation and the fixed direction $\vec e_z$. That right-hand factor is the chirality cell, since $-i\overline{F}\,\vec e_z=\Gamma\,\overline{F}$ with $\Gamma=-iR_{\vec e_z}^{\mathrm{pau}}=\gamma_5$, so the mass of the two-sided equation is carried by the cell that names the chirality — the two-sided counterpart of the off-diagonal mass of the one-sided pair, and the reason the mass is chirality-odd here as it is off-diagonal there. The two forms are one operator read from two sides, and the dictionary between them is that of *The Dirac Equation in Biquaternionic Form*. In the language of this article the one-sided pair is the superalgebra's own statement in the chirality grading of the supersymmetry article, where the gradient is the odd element and its conjugate is the odd element of the conjugate module, the two paired off-diagonally by the mass; the two-sided equation is instead the cell $L_{\tilde\nabla^{\natural}}$ with the chirality carried on the right: what the one-sided form holds in a second field, the two-sided form holds in the side of the action.

**The cells and the cone.** A single product is a pure tensor. Writing $c(M)$ for the coefficient matrix of $M$ in the basis of the sixteen products, the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$. The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

## Summary

A **superalgebra** is a $\mathbb{Z}/2$-graded algebra with the grading as part of its structure, and on it the graded commutator $[a,b]_{\mathrm{gr}}=ab-(-1)^{\lvert a\rvert\lvert b\rvert}ba$ is the commutator for even or mixed pairs and the anticommutator for two odd elements. The biquaternion algebra is the **even part** of the graded Clifford algebra, $\mathbb{B}=\mathrm{Cl}^0_{1,3}$, so it is not by itself a superalgebra, and it must not be conflated with the chirality grading of the supersymmetry article or with the sector splitting by the star.

The body is written in **cells**, $L_a\psi=a\psi$ and $R_b\psi=\psi b$ with $L_aR_bL_cR_d=L_{ac}R_{db}$, and the adjoint of a cell is the cell $(L_aR_b)^{\dagger}=L_{a^{*}}R_{b^{*}}$ for the Hermitian form $\langle s,t\rangle_{*}=\mathrm{Sc}(st^{*})$. The odd slot is $\mathrm{Cl}^1=\mathbb{B}u$ for a non-isotropic vector $u$, an odd element is $\mathcal{Q}=su$, and its operator is $L_{\mathcal{Q}}=L_sL_u$.

Read on the **elements** with the star, the superalgebra carries an even anti-involution, $(ab)^{*}=b^{*}a^{*}$ with $\lvert a^{*}\rvert=\lvert a\rvert$, and the star of the graded bracket is

$$
\bigl([a,b]_{\mathrm{gr}}\bigr)^{*}=-(-1)^{\lvert a\rvert\lvert b\rvert}\bigl[a^{*},b^{*}\bigr]_{\mathrm{gr}},
$$

so it reverses a commutator and preserves an anticommutator: the star reverses the order of the factors, and only the odd-odd, symmetric case is even under the reversal. The Koszul-signed super-* convention would give the cleaner rule without the parity sign, and the corpus's star is not of that convention; the two are distinguished on two generators, and the physics selects the plain one, because under the signed rule the square of a Hermitian odd element is anti-Hermitian and the Hamiltonian would be imaginary.

A **supercharge** is an odd element, paired either with **itself**, $\{\mathcal{Q},\mathcal{Q}\}=2\mathcal{Q}^{2}=2H$, which is the Clifford square and needs $\mathcal{Q}^{2}\neq0$, or with its **star**, $\{\mathcal{Q},\mathcal{Q}^{*}\}=2H'$, which is the nilpotent pairing of the corpus's supersymmetric quantum physics and is Hermitian and even because the star is an involution. The two agree for a Hermitian supercharge and are reconciled by $i^{2}=-1$ otherwise. In the module $\mathrm{Cl}^1=\mathbb{B}u$ a supercharge is $\mathcal{Q}=su$ with adjoint $\mathcal{Q}^{*}=-us^{*}$ and $\mathcal{Q}\mathcal{Q}^{*}=-q(u)ss^{*}$, an even element; the symmetric form $\{\mathcal{Q},\mathcal{Q}^{*}\}=-q(u)(ss^{*}+s^{*}s)$ holds when $s$ has a definite $u$-parity, and only the evenness and the Hermiticity hold in general. The odd extension is one generator, not a second algebra, and the odd slot carries the algebra's own Hermitian form, $-q(u)\langle s,t\rangle_{*}$, which is the form of $\mathbb{B}$ for a spacelike $u$ and its negative for a timelike one.

The matrix frame is the frame of cells written as letters, and it is confined to *The Gamma Formulation*: the five cells, their squares fixed by $i^2=-1$, the central sign $\chi=i\tilde\Xi_{\mathrm{ad}}$ with $\chi^2=e_t$, and the two Dirac equations — the one-sided chiral pair, whose chirality sits in the two fields, and the two-sided cell equation, whose chirality sits in the side of the action.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A=A^0\oplus A^1$ | A $\mathbb{Z}/2$-graded algebra, a superalgebra |
| $\lvert a\rvert\in\{0,1\}$ | The parity of a homogeneous element |
| $[a,b]_{\mathrm{gr}}=ab-(-1)^{\lvert a\rvert\lvert b\rvert}ba$ | Graded commutator; anticommutator for two odd elements |
| graded Jacobi identity | The super-Jacobi identity of a Lie superalgebra |
| $\mathrm{Cl}_{1,3}=\mathbb{B}\oplus\mathrm{Cl}^1$ | Lie superalgebra, even part the biquaternion algebra |
| $u$, $q(u)$, $v_\mu$ | The odd unit, its quadratic form and the Clifford frame vectors: $\mathrm{Cl}^1=\mathbb{B}u$, $u^2=q(u)e_t$, $v_0^2=e_t$, $v_k^2=-e_t$ |
| $L_a\psi=a\psi$, $R_b\psi=\psi b$, $L_aR_b\psi=a\psi b$ | The cells; every $\mathbb{C}$-linear operator is a sum of at most four |
| $L_aR_bL_cR_d=L_{ac}R_{db}$ | Composition of cells, the right multipliers in reverse order |
| $\langle s,t\rangle_{*}=\mathrm{Sc}(st^{*})$ | The Hermitian form of the module, definite |
| $(L_aR_b)^{\dagger}=L_{a^{*}}R_{b^{*}}$ | The adjoint of a cell is a cell |
| $\{\mathrm{Cl}^1,\mathrm{Cl}^1\}\subseteq\mathbb{B}$ | Two fermionic steps are bosonic |
| $X^{*}=\sigma(\alpha(X^{r}))$ | The star, Hermitian conjugation; even anti-involution of the superalgebra |
| $\bigl([a,b]_{\mathrm{gr}}\bigr)^{*}=-(-1)^{\lvert a\rvert\lvert b\rvert}[a^{*},b^{*}]_{\mathrm{gr}}$ | The star reverses a commutator, preserves an anticommutator |
| $(ab)^{*}=(-1)^{\lvert a\rvert\lvert b\rvert}b^{*}a^{*}$ | The Koszul-signed super-*; **not** the star of the corpus |
| $\{\mathcal{Q},\mathcal{Q}\}=2\mathcal{Q}^{2}=2H$, $\{\mathcal{Q},\mathcal{Q}^{*}\}=2H'$ | The square pairing and the star pairing of a supercharge; both even, the second Hermitian always and the first when $\mathcal{Q}$ is |
| $L_{\mathcal{Q}}=L_sL_u$, $L_{\mathcal{Q}}^{\dagger}=L_{\mathcal{Q}^{*}}$ | The operator of a supercharge and its adjoint |
| $\mathcal{Q}=su$, $\mathcal{Q}^{*}=-u s^{*}$, $\mathcal{Q}\mathcal{Q}^{*}=-q(u)ss^{*}$ | The supercharge in the module $\mathrm{Cl}^1=\mathbb{B}u$ |
| $\{\mathcal{Q},\mathcal{Q}^{*}\}=-q(u)(ss^{*}+s^{*}s)$ | Its pairing when $s^{*}s$ has no part of $u$-parity $-1$, in particular for an even $s$ of definite $u$-parity |
| $\langle su,tu\rangle_{*}=-q(u)\langle s,t\rangle_{*}$, $\langle s,tu\rangle_{*}=0$ | The Hermitian form on the odd slot |
| $(-1)^F=i\vec e_z\in\mathbb{M}_+$, $((-1)^F)^2=e_t$ | The one fermionic mode the algebra hosts natively |
| $\gamma_\mu$, $\gamma_5$ | The frame cells of *The Gamma Formulation*: letters for the cells, used in that section only |
| $\Gamma=-iR_{\vec e_z}^{\mathrm{pau}}$ | The chirality cell of the module; equal to the fifth frame cell in the frame |
| $\chi=i\tilde\Xi_{\mathrm{ad}}$, $\chi^2=e_t$ | The central grading; central, outside $\mathbb{B}_{\mathbb{R}}$, represented on the Dirac module by the fifth frame cell |
| $\tilde\nabla\tilde\Psi_R=m\tilde\Psi_L$, $\tilde\nabla^{\natural}\tilde\Psi_L=m\tilde\Psi_R$ | The one-sided Dirac equation, the chiral pair |
| $(i\partial/\partial t'+D_3)F-mi\overline{F}\vec e_z=0$ | The two-sided Dirac equation, the mass on the right |

## Further Reading

- Manfred Scheunert, *The Theory of Lie Superalgebras*, Lecture Notes in Mathematics 716 (Springer, 1979), for the graded bracket, the super-Jacobi identity and the structure theory.
- Julius Wess and Jonathan Bagger, *Supersymmetry and Supergravity* (Princeton University Press, 2nd ed. 1992), for the super-Poincaré algebra and the supercharge conventions.
- Bryce S. DeWitt, *Supermanifolds* (Cambridge University Press, 2nd ed. 1992), for the Grassmann envelope, the Berezin integral and the functorial view of the odd coordinates.
- Felix A. Berezin, *Introduction to Superanalysis* (Reidel, 1987), for the anticommuting coefficients and the algebra of the odd extension.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for the involutions of a Clifford algebra, the adjoint of an anti-automorphism and the $*$-unitary groups they define.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for the graded Clifford algebra, its even part and the parity of its elements.
