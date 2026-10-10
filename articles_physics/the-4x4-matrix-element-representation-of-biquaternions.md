# __The 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions__

## Introduction

The physical point comes first. The rotor group $\{\tilde{\Lambda} : N(\tilde{\Lambda}) = e_0\}$ acts on the material sector $\mathbb{M}_-$ by the rotor conjugation $\tilde{Q} \mapsto \tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^{*}$, and that conjugation is literally the product of the left copy of $\tilde{\Lambda}$ with the right copy of $\tilde{\Lambda}^{*}$ acting on the four-vector: in the regular representation the Lorentz transformation of a four-vector is a product of two multiplications in the algebra.

The **regular representation** of the biquaternion algebra is the algebra acting on itself on the left. Multiplication on the left by a fixed element is linear on the four-dimensional space $\mathbb{B}$, so in the basis $e_0, e_1, e_2, e_3$ it is a $4 \times 4$ complex matrix. This article constructs that matrix and its companion for multiplication on the right, proves that the two constructions are multiplicative, and reads off the consequences: the determinant is the **square** of the biquaternion norm and the trace is four times the scalar part; the regular module is the direct sum of two copies of the simple module, which in this corpus are the two **chiralities**; the centralizer of the left copy is the right copy; and the two copies together give the two-sided action by which a Lorentz transformation of a four-vector is written. The image of the left multiplication is written $M_4(\mathbb{C})_L$: the subspace of $M_4(\mathbb{C})$ of the regular matrices, of complex dimension $4$ inside the $16$ of the matrix algebra.

The conventions are those of *Conventions in the Biquaternion Universe* and of the two companion articles, and none is redefined. The basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$ and $e_1e_2 = e_3$; the scalar imaginary $i$ commutes with every unit; the conjugations are ${}^{\natural}$, $\bar{\cdot}$, ${}^{*} = {}^{\natural}\circ\bar{\cdot}$ and ${}^{\flat} = -{}^{*}$; the biquaternion norm is $N(\tilde{Q}) = \tilde{Q}\tilde{Q}^{\natural} = \sum_\mu Q_\mu^2$; the subspaces are $\mathbb{C}_{\mathbb{B}}$ (centre), $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$ (real), $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$ (informational) and $\mathbb{M}_-$ (material); the physical coordinates are $\tilde{Q} = ict\,e_0 + \mathbf{x}$ in $\mathbb{M}_-$ and $ct'\,e_0 + i\mathbf{x}'$ in $\mathbb{M}_+$, with $\mathbf{x} = xe_1+ye_2+ze_3$ and $\mathbf{x}' = x'e_1+y'e_2+z'e_3$; the $ict$ metric is $\eta = \mathrm{diag}(-1,+1,+1,+1)$ and the d'Alembertian is $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \partial_{ict}^2 + \Delta$.

## The Left Regular Matrix

The isomorphism is written $\mathsf{M}_4^{L}$. It converts a biquaternion into a $4 \times 4$ complex matrix,

$$
\mathsf{M}_4^{L} : \mathbb{B} \longrightarrow M_4(\mathbb{C}),
$$

and it is fixed by its values on the basis, the rest following by $\mathbb{C}$-linearity. The scalar imaginary $i$ is the complex unit of the coefficients and is central, so it maps to a scalar matrix; the quaternion units are assigned the matrices

$$
\mathsf{M}_4^{L}(e_0) = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}, \quad
\mathsf{M}_4^{L}(e_1) = \begin{pmatrix} 0 & -1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & -1 \\ 0 & 0 & 1 & 0 \end{pmatrix}, \quad
\mathsf{M}_4^{L}(e_2) = \begin{pmatrix} 0 & 0 & -1 & 0 \\ 0 & 0 & 0 & 1 \\ 1 & 0 & 0 & 0 \\ 0 & -1 & 0 & 0 \end{pmatrix}, \quad
\mathsf{M}_4^{L}(e_3) = \begin{pmatrix} 0 & 0 & 0 & -1 \\ 0 & 0 & -1 & 0 \\ 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 0 \end{pmatrix},
$$

with $\mathsf{M}_4^{L}(i) = i\,\mathsf{M}_4^{L}(e_0)$ on the central scalar $\mathbb{C}_{\mathbb{B}}$.

This is the assignment, taken as fixed for the whole series. A general biquaternion $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ with $Q_\mu \in \mathbb{C}$ therefore maps to

$$
\mathsf{M}_4^{L}(\tilde{Q}) = \begin{pmatrix}
Q_0 & -Q_1 & -Q_2 & -Q_3 \\
Q_1 & Q_0 & -Q_3 & Q_2 \\
Q_2 & Q_3 & Q_0 & -Q_1 \\
Q_3 & -Q_2 & Q_1 & Q_0
\end{pmatrix},
$$

the Cayley matrix of *Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions*. Each entry is a single coefficient of $\tilde{Q}$ carrying a sign, and **no entry is a sum of two or more coefficients**, because in this basis every product of basis elements is one basis element times a sign.

**Proof (the general matrix).** The columns are the products $\tilde{Q}e_m$ expressed in the basis. For $m = 0$ the image is $\tilde{Q}$ itself, giving the first column $(Q_0, Q_1, Q_2, Q_3)$. For $m = k \geq 1$ one uses $e_0e_k = e_k$ and $e_je_k = \epsilon^{ijk}e_i$ for $j \neq k$ with $\{i,j,k\} = \{1,2,3\}$, so that

$$
\tilde{Q}e_k = Q_0e_k + Q_ke_k^2 + \sum_{j \neq k} Q_je_je_k = Q_0e_k - Q_ke_0 + \sum_{j \neq k} \epsilon^{ijk}Q_je_i .
$$

Expanding with $e_1e_2 = e_3$, $e_2e_3 = e_1$, $e_3e_1 = e_2$ gives the displayed columns.

**The check.** The assignment is the right one because the four matrices multiply as the four units do. Squaring a vector image,

$$
\mathsf{M}_4^{L}(e_1)^2 = \begin{pmatrix} 0 & -1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & -1 \\ 0 & 0 & 1 & 0 \end{pmatrix}^2 = \begin{pmatrix} -1 & 0 & 0 & 0 \\ 0 & -1 & 0 & 0 \\ 0 & 0 & -1 & 0 \\ 0 & 0 & 0 & -1 \end{pmatrix} = -\mathsf{M}_4^{L}(e_0),
$$

and the same holds for $\mathsf{M}_4^{L}(e_2)$ and $\mathsf{M}_4^{L}(e_3)$; so $e_k^2 = -e_0$ is reproduced. Multiplying the first two,

$$
\mathsf{M}_4^{L}(e_1)\mathsf{M}_4^{L}(e_2) = \begin{pmatrix} 0 & -1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & -1 \\ 0 & 0 & 1 & 0 \end{pmatrix}\begin{pmatrix} 0 & 0 & -1 & 0 \\ 0 & 0 & 0 & 1 \\ 1 & 0 & 0 & 0 \\ 0 & -1 & 0 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 & 0 & -1 \\ 0 & 0 & -1 & 0 \\ 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 0 \end{pmatrix} = \mathsf{M}_4^{L}(e_3),
$$

and the other products give $\mathsf{M}_4^{L}(e_2)\mathsf{M}_4^{L}(e_3) = \mathsf{M}_4^{L}(e_1)$ and $\mathsf{M}_4^{L}(e_3)\mathsf{M}_4^{L}(e_1) = \mathsf{M}_4^{L}(e_2)$, reproducing $e_1e_2 = e_3$ with its cyclic companions; reversing the order of the factors reverses the sign of each product, reproducing $e_ie_j = -e_je_i$ for $i \neq j$. Those relations are the whole multiplication table of the units, so the correspondence of bases is an isomorphism of algebras and not a formal analogy. In particular the $m$-th column of $\mathsf{M}_4^{L}(\tilde{Q})$ is the coordinate column of the product $\tilde{Q}e_m$. Write $\operatorname{col}(\tilde{S})$ for the coordinate column of $\tilde{S}$; then the matrix acts on columns by $\mathsf{M}_4^{L}(\tilde{Q})\operatorname{col}(\tilde{S}) = \operatorname{col}(\tilde{Q}\tilde{S})$, which is the column convention of *The Four-Vector Element Representation of Biquaternions*, whose column of $\tilde{S}$ is written $S$.

**The four basis columns.** The matrices act on the columns $Q$ of *The Four-Vector Element Representation of Biquaternions*, whose four basis columns are

$$
E_0 = \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \end{pmatrix}, \qquad E_1 = \begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \end{pmatrix}, \qquad E_2 = \begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \end{pmatrix}, \qquad E_3 = \begin{pmatrix} 0 \\ 0 \\ 0 \\ 1 \end{pmatrix},
$$

so that a general column is $Q = \sum_\mu Q^\mu E_\mu$. The column $\mathsf{M}_4^{L}(e_\mu)E_\nu$ is the four-vector of the product $e_\mu e_\nu$, which is how the matrices are also read.

The four matrices are real and orthogonal. The columns of $\mathsf{M}_4^{L}(e_1)$, for instance, are the images $e_1e_0 = e_1$, $e_1e_1 = -e_0$, $e_1e_2 = e_3$ and $e_1e_3 = -e_2$, that is, $(0,1,0,0)$, $(-1,0,0,0)$, $(0,0,0,1)$ and $(0,0,-1,0)$, namely $E_1$, $-E_0$, $E_3$ and $-E_2$.

**Remark (the same four for one reason).** The matrix is $4 \times 4$ and the coefficient space of *The Four-Vector Element Representation of Biquaternions* has complex dimension four, for the same reason and not by coincidence: the algebra has complex dimension four and the regular representation is the algebra acting on itself, so the space and the index set of the matrix are the same object. In *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* the number $2$ appears both as the dimension of the simple module and as the size of the matrix algebra, for the parallel reason that the algebra is recovered as the whole algebra of **$\mathbb{C}$-linear** maps of that module; its $\mathbb{B}$-linear maps are only the scalars, so the qualifier is not idle.

**Example.** For $\tilde{Q} = (2+i)e_0 + (1-i)e_1 + 3e_2 + ie_3$, so that $(Q_0, Q_1, Q_2, Q_3) = (2+i, 1-i, 3, i)$, the regular matrix is

$$
\mathsf{M}_4^{L}(\tilde{Q}) = \begin{pmatrix}
2+i & -1+i & -3 & -i \\
1-i & 2+i & -i & 3 \\
3 & i & 2+i & -1+i \\
i & -3 & 1-i & 2+i
\end{pmatrix}.
$$

The column of $\tilde{R} = e_0 + e_1$, namely $R = (1,1,0,0)$, is carried by this matrix to the column $(1+2i, 3, 3+i, -3+i)$, which is the four-vector of the product $\tilde{Q}\tilde{R}$ computed by the component formula of *The Four-Vector Element Representation of Biquaternions*.

**A material four-vector.** For an element of $\mathbb{M}_-$, written in the conventions' real parameters as $\tilde{Q} = iq'_0e_0 + q_1e_1 + q_2e_2 + q_3e_3$ with $q'_0 = ct$ and $(q_1, q_2, q_3) = (x,y,z)$, the regular matrix keeps its shape with $Q_0 = iq'_0$ and $Q_k = q_k$, and it is the matrix form of a four-vector of relativistic physics:

$$
\mathsf{M}_4^{L}(\tilde{Q}) = \begin{pmatrix}
iq'_0 & -q_1 & -q_2 & -q_3 \\
q_1 & iq'_0 & -q_3 & q_2 \\
q_2 & q_3 & iq'_0 & -q_1 \\
q_3 & -q_2 & q_1 & iq'_0
\end{pmatrix}.
$$

Its diagonal is $iq'_0$, so its trace is $4iq'_0$, purely imaginary — the matrix of a material four-vector is **not** traceless over $\mathbb{C}$, which is a first sign that its natural trace is taken elsewhere. What is physically invariant is its determinant, treated below, and the fact that it is singular exactly on the light cone.

## The Left Regular Matrix Is Multiplicative

**Theorem (multiplicativity).** For all $\tilde{Q}, \tilde{R} \in \mathbb{B}$,

$$
\mathsf{M}_4^{L}(\tilde{Q})\,\mathsf{M}_4^{L}(\tilde{R}) = \mathsf{M}_4^{L}(\tilde{Q}\tilde{R}).
$$

Hence $\mathsf{M}_4^{L}$ is an algebra homomorphism, and the coefficient space is a left $\mathbb{B}$-module under it.

**Proof.** For every $\tilde{S}$, the column rule and associativity give

$$
\mathsf{M}_4^{L}(\tilde{Q})\,\mathsf{M}_4^{L}(\tilde{R})\operatorname{col}(\tilde{S}) = \mathsf{M}_4^{L}(\tilde{Q})\operatorname{col}(\tilde{R}\tilde{S}) = \operatorname{col}\bigl(\tilde{Q}(\tilde{R}\tilde{S})\bigr) = \operatorname{col}\bigl((\tilde{Q}\tilde{R})\tilde{S}\bigr) = \mathsf{M}_4^{L}(\tilde{Q}\tilde{R})\operatorname{col}(\tilde{S}) ,
$$

the first step being the column rule applied to $\tilde{R}$, the second the column rule applied to $\tilde{Q}$, and the third associativity; the columns $\operatorname{col}(\tilde{S})$ span $\mathbb{C}^4$, so the two matrices agree.

**Example (a concrete check).** For $\tilde{Q} = e_0 + e_1$ and $\tilde{R} = e_0 + e_2$ the product is $\tilde{Q}\tilde{R} = e_0 + e_1 + e_2 + e_3$ and the two matrices are

$$
\mathsf{M}_4^{L}(\tilde{Q}) = \begin{pmatrix} 1 & -1 & 0 & 0 \\ 1 & 1 & 0 & 0 \\ 0 & 0 & 1 & -1 \\ 0 & 0 & 1 & 1 \end{pmatrix},
\qquad
\mathsf{M}_4^{L}(\tilde{R}) = \begin{pmatrix} 1 & 0 & -1 & 0 \\ 0 & 1 & 0 & 1 \\ 1 & 0 & 1 & 0 \\ 0 & -1 & 0 & 1 \end{pmatrix}.
$$

Their product is the matrix of $\mathsf{M}_4^{L}(\tilde{Q}\tilde{R})$, whose first column is $(1,1,1,1)$. The reversed order gives $\mathsf{M}_4^{L}(\tilde{R})\mathsf{M}_4^{L}(\tilde{Q}) = \mathsf{M}_4^{L}(\tilde{R}\tilde{Q})$ with first column $(1,1,1,-1)$, so the two orders differ, exactly as $\tilde{Q}\tilde{R} \neq \tilde{R}\tilde{Q}$. Multiplicativity is what makes the regular matrix a *representation* and not merely a table of coefficients: it is the statement that the algebra multiplication and the matrix multiplication are the same operation in two languages.

## The Right Regular Matrix

The assignment is written $\mathsf{M}_4^{R}$. It converts a biquaternion into a $4 \times 4$ complex matrix,

$$
\mathsf{M}_4^{R} : \mathbb{B} \longrightarrow M_4(\mathbb{C}),
$$

and it is fixed by its values on the basis, the rest following by $\mathbb{C}$-linearity. The scalar imaginary $i$ is central, so it maps to a scalar matrix; the quaternion units are assigned the matrices

$$
\mathsf{M}_4^{R}(e_0) = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}, \quad
\mathsf{M}_4^{R}(e_1) = \begin{pmatrix} 0 & -1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & -1 & 0 \end{pmatrix}, \quad
\mathsf{M}_4^{R}(e_2) = \begin{pmatrix} 0 & 0 & -1 & 0 \\ 0 & 0 & 0 & -1 \\ 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \end{pmatrix}, \quad
\mathsf{M}_4^{R}(e_3) = \begin{pmatrix} 0 & 0 & 0 & -1 \\ 0 & 0 & 1 & 0 \\ 0 & -1 & 0 & 0 \\ 1 & 0 & 0 & 0 \end{pmatrix},
$$

with $\mathsf{M}_4^{R}(i) = i\,\mathsf{M}_4^{R}(e_0)$ on the central scalar $\mathbb{C}_{\mathbb{B}}$.

This is the assignment, taken as fixed for the whole series. A general biquaternion $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ with $Q_\mu \in \mathbb{C}$ therefore maps to

$$
\mathsf{M}_4^{R}(\tilde{Q}) = \begin{pmatrix}
Q_0 & -Q_1 & -Q_2 & -Q_3 \\
Q_1 & Q_0 & Q_3 & -Q_2 \\
Q_2 & -Q_3 & Q_0 & Q_1 \\
Q_3 & Q_2 & -Q_1 & Q_0
\end{pmatrix}.
$$

**Proof (the general matrix).** The columns are the images $e_m\tilde{Q}$, expanded as in the left case with the factors in the opposite order. Alternatively, since $e_ke_j = -e_je_k$ for $j \neq k$, the matrix is the transpose of the left matrix conjugated by the fixed sign matrix $D$ of the next section, $\mathsf{M}_4^{R}(\tilde{Q}) = D\,\mathsf{M}_4^{L}(\tilde{Q})^{\mathsf{T}}D$, and computing the four general products directly confirms the display.

**The check.** The assignment is the right one because the four matrices multiply as the four units do, with the order of the factors reversed. Squaring a vector image, $\mathsf{M}_4^{R}(e_k)^2 = -I_4$, so $e_k^2 = -e_0$ is reproduced; multiplying the first two,

$$
\mathsf{M}_4^{R}(e_1)\mathsf{M}_4^{R}(e_2) = \begin{pmatrix} 0 & -1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & -1 & 0 \end{pmatrix}\begin{pmatrix} 0 & 0 & -1 & 0 \\ 0 & 0 & 0 & -1 \\ 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 & 0 & 1 \\ 0 & 0 & -1 & 0 \\ 0 & 1 & 0 & 0 \\ -1 & 0 & 0 & 0 \end{pmatrix} = -\mathsf{M}_4^{R}(e_3),
$$

which is $\mathsf{M}_4^{R}(e_2e_1) = \mathsf{M}_4^{R}(-e_3)$ and reproduces $e_1e_2 = e_3$ through the reversal. The general rule is $\mathsf{M}_4^{R}(e_i)\mathsf{M}_4^{R}(e_j) = \mathsf{M}_4^{R}(e_je_i)$; reversing the order of the factors reverses the order of the units, so the correspondence is an anti-isomorphism of algebras.

**Theorem (the right regular matrix is anti-multiplicative).** For all $\tilde{Q}, \tilde{R} \in \mathbb{B}$,

$$
\mathsf{M}_4^{R}(\tilde{Q})\,\mathsf{M}_4^{R}(\tilde{R}) = \mathsf{M}_4^{R}(\tilde{R}\tilde{Q}).
$$

Hence the assignment $\tilde{Q} \mapsto \mathsf{M}_4^{R}(\tilde{Q})$ is an algebra **anti**-homomorphism, and the right regular matrices are the regular representation of the opposite algebra $\mathbb{B}^{\mathrm{op}}$, not a second representation of $\mathbb{B}$.

**Proof.** For every $\tilde{S}$, the column rule and associativity give

$$
\mathsf{M}_4^{R}(\tilde{Q})\,\mathsf{M}_4^{R}(\tilde{R})\operatorname{col}(\tilde{S}) = \mathsf{M}_4^{R}(\tilde{Q})\operatorname{col}(\tilde{S}\tilde{R}) = \operatorname{col}\bigl((\tilde{S}\tilde{R})\tilde{Q}\bigr) = \operatorname{col}\bigl(\tilde{S}(\tilde{R}\tilde{Q})\bigr) = \mathsf{M}_4^{R}(\tilde{R}\tilde{Q})\operatorname{col}(\tilde{S}) ,
$$

and the columns $\operatorname{col}(\tilde{S})$ span $\mathbb{C}^4$, so the two matrices agree.

**Remark (which side is which).** The two regular matrices are the two ways a non-commutative algebra multiplies its own basis. Since quaternion conjugation is an anti-automorphism, the composite $\tilde{Q} \mapsto \mathsf{M}_4^{L}(\tilde{Q}^{\natural})$ is anti-multiplicative; it is therefore the right regular matrix up to a fixed change of basis, and the next section exhibits that change of basis and shows that it is not the identity. The two matrices are different objects as soon as the algebra is non-commutative, and the corpus uses both: the **left** copy preserves each chirality, while the **right** copy is the only one that can carry a chirality from one ideal to the other, which is the structural reason the mass term of the biquaternionic Dirac equation is a right multiplication, as established in *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* and in *Conventions in the Biquaternion Universe*.

## Transposition and the Two Matrices

**Proposition (transposition is quaternion conjugation).** For every biquaternion $\tilde{Q}$,

$$
\mathsf{M}_4^{L}(\tilde{Q})^{\mathsf{T}} = \mathsf{M}_4^{L}(\tilde{Q}^{\natural}),
$$

where the transpose is taken in the basis $e_0, e_1, e_2, e_3$ fixed above.

**Proof.** Transposing the closed form of $\mathsf{M}_4^{L}(\tilde{Q})$ gives

$$
\mathsf{M}_4^{L}(\tilde{Q})^{\mathsf{T}} = \begin{pmatrix}
Q_0 & Q_1 & Q_2 & Q_3 \\
-Q_1 & Q_0 & Q_3 & -Q_2 \\
-Q_2 & -Q_3 & Q_0 & Q_1 \\
-Q_3 & Q_2 & -Q_1 & Q_0
\end{pmatrix},
$$

and replacing $Q_k$ by $-Q_k$ in the closed form of $\mathsf{M}_4^{L}$ reproduces this matrix.

**Remark (the false identity).** The right matrix is **not** the transpose of the left one,

$$
\mathsf{M}_4^{R}(\tilde{Q}) \neq \mathsf{M}_4^{L}(\tilde{Q})^{\mathsf{T}} \quad \text{in general},
$$

and the element $\tilde{Q} = e_1$ separates them:

$$
\mathsf{M}_4^{L}(e_1)^{\mathsf{T}} = \begin{pmatrix} 0 & 1 & 0 & 0 \\ -1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & -1 & 0 \end{pmatrix}, \qquad
\mathsf{M}_4^{R}(e_1) = \begin{pmatrix} 0 & -1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & -1 & 0 \end{pmatrix}.
$$

The two agree in the lower-right block, which mixes the two space directions $e_2$ and $e_3$, and differ by the sign of the upper-left block, which mixes the time direction $e_0$ with $e_1$.

The proposition above gives the reason: $\mathsf{M}_4^{L}(\tilde{Q})^{\mathsf{T}} = \mathsf{M}_4^{L}(\tilde{Q}^{\natural})$ is a **left** multiplication, so it can equal the right multiplication $\mathsf{M}_4^{R}(\tilde{Q})$ only when the two actions coincide on $\tilde{Q}$. Measured exactly, the equations $\mathsf{M}_4^{R}(\tilde{Q}) = \mathsf{M}_4^{L}(\tilde{Q})^{\mathsf{T}}$ are linear in the eight real coordinates of $\tilde{Q}$ and their solution space has real dimension two, spanned by $e_0$ and $ie_0$: the identity holds on the centre $\mathbb{C}_{\mathbb{B}} = \mathbb{C} e_0$ and nowhere else. Replacing $\tilde{Q}$ by $\tilde{Q}^{\natural}$ gives no second identity, since $\tilde{Q} \mapsto \tilde{Q}^{\natural}$ is a bijection of the algebra and the variant is the same equation with the element renamed.

**Theorem (the correct relation).** Let $D = \operatorname{diag}(-1,1,1,1)$, so that $D^2 = I$. Then for every biquaternion $\tilde{Q}$,

$$
\mathsf{M}_4^{R}(\tilde{Q}) = D\,\mathsf{M}_4^{L}(\tilde{Q})^{\mathsf{T}}\,D = D\,\mathsf{M}_4^{L}(\tilde{Q}^{\natural})\,D .
$$

**Proof.** Apply $D$ on the left and on the right to the transpose of the closed form of $\mathsf{M}_4^{L}(\tilde{Q})$. Left multiplication by $D$ negates the first row and right multiplication by $D$ negates the first column; the corner entry lies in both and is negated twice, hence unchanged. The result is the closed form of $\mathsf{M}_4^{R}(\tilde{Q})$. The second equality uses the transpose proposition.

**The physical reading of $D$.** The matrix $D = \operatorname{diag}(-1,1,1,1)$ is exactly the $ict$ metric $\eta = \operatorname{diag}(-1,+1,+1,+1)$ of *Conventions in the Biquaternion Universe*. The relation $\mathsf{M}_4^{R}(\tilde{Q}) = \eta\,\mathsf{M}_4^{L}(\tilde{Q})^{\mathsf{T}}\,\eta$ therefore says that the change of basis relating the two copies of the algebra is the **metric itself**, and it is the level-2 face of the same sign that puts $-c^2t^2 + \mathbf{x}^2$ on the four-position. Nothing else in the article uses the metric, so the appearance of $\eta$ here is not a coincidence of notation but the visible trace of the sign convention itself.

**The same relation read as an adjoint.** With the bilinear form $\langle u, v \rangle_\eta = u^{\mathsf{T}}\eta v$ on the columns, the theorem says that $\mathsf{M}_4^{R}(\tilde{Q})$ is the transpose of $\mathsf{M}_4^{L}(\tilde{Q})$ **with respect to $\eta$** and not with respect to the Euclidean form:

$$
\langle \mathsf{M}_4^{L}(\tilde{Q})R, S \rangle_\eta = \langle R, \mathsf{M}_4^{R}(\tilde{Q})S \rangle_\eta
$$

for all columns $R, S$. This is what the failure of the false identity above amounts to: a transpose is taken with respect to a form, the form of the coordinates as written is Euclidean, and the form the algebra preserves is indefinite. The identity $\mathsf{M}_4^{R}(\tilde{Q}) = \mathsf{M}_4^{L}(\tilde{Q})^{\mathsf{T}}$ is the adjoint statement with $\eta$ replaced by $I$; it holds for every $\tilde{Q}$ in the basis whose first vector is $ie_0$ rather than $e_0$, where the two forms coincide, and it fails in the basis of the units.

**Corollary (the difference vanishes exactly on the centre).** The difference $\mathsf{M}_4^{L}(\tilde{Q}) - \mathsf{M}_4^{R}(\tilde{Q})$ is the zero matrix if and only if $\tilde{Q} \in \mathbb{C}_{\mathbb{B}} = \mathbb{C} e_0$.

**Proof.** If $\tilde{Q} = \lambda e_0$ then $\mathsf{M}_4^{L}(\tilde{Q}) = \mathsf{M}_4^{R}(\tilde{Q}) = \lambda I$, since scalar multiplication is central. Conversely, comparing the two closed forms in the lower-right $3 \times 3$ block, the off-diagonal entries agree only when $Q_1 = Q_2 = Q_3 = 0$; then the element is scalar and the two matrices coincide. Comparing the closed forms directly is the whole proof and no module theory is needed.

**Remark (what left and right mean).** The $m$-th column of the difference $\mathsf{M}_4^{L}(\tilde{Q}) - \mathsf{M}_4^{R}(\tilde{Q})$ is the coordinate column of the commutator $[\tilde{Q}, e_m] = \tilde{Q}e_m - e_m\tilde{Q}$. The difference vanishes on the centre and nowhere else, which is the precise sense in which the two matrices differ because the algebra is non-commutative. On the material sector the commutator has a physical reading: for two four-vectors $\tilde{Q}, \tilde{R} \in \mathbb{M}_-$ with real time parameters $q'_0, r'_0$, the scalar component and the symmetric part $q'_0r_i + r'_0q_i$ cancel, leaving only the antisymmetric combination of the spatial parameters,

$$
\tilde{Q}\tilde{R} - \tilde{R}\tilde{Q} = 2 \sum_{i=1}^{3} \Big( \sum_{j,k=1}^{3} \epsilon^{ijk} q_j r_k \Big) e_i ,
$$

so the matrix $\mathsf{M}_4^{L}(\tilde{Q}) - \mathsf{M}_4^{R}(\tilde{Q})$ carries $\tilde{R}$ to the element of $\mathrm{Vect}(\mathbb{B})$ whose spatial part is twice $\mathbf{q} \times \mathbf{r}$.

## The Module Structure and the Two Chiralities

The regular module is reducible, and its reduction into minimal left ideals is the algebra's splitting into its two chiralities.

**Definition.** Let

$$
\tilde\Pi_1 = \tfrac{1}{2}(e_0 + ie_3), \qquad \tilde\Pi_2 = \tfrac{1}{2}(e_0 - ie_3).
$$

**Lemma (orthogonal idempotents).** The elements $\tilde\Pi_1$ and $\tilde\Pi_2$ satisfy

$$
\tilde\Pi_1^2 = \tilde\Pi_1, \qquad \tilde\Pi_2^2 = \tilde\Pi_2, \qquad \tilde\Pi_1\tilde\Pi_2 = \tilde\Pi_2\tilde\Pi_1 = 0, \qquad \tilde\Pi_1 + \tilde\Pi_2 = e_0,
$$

so that $\mathbb{B} = \mathbb{B}\tilde\Pi_1 \oplus \mathbb{B}\tilde\Pi_2$ as a direct sum of left ideals.

**Proof.** Because $i$ is central, $e_3^2 = -e_0$ and $i^2 = -1$, one computes $\tilde\Pi_1^2 = \tfrac14(e_0 + 2ie_3 + i^2e_3^2) = \tfrac14(e_0 + 2ie_3 + e_0) = \tilde\Pi_1$, and similarly $\tilde\Pi_2^2 = \tilde\Pi_2$; while $\tilde\Pi_1\tilde\Pi_2 = \tfrac14(e_0 - i^2e_3^2) = \tfrac14(e_0 - e_0) = 0$. The sum is $e_0$, and the two ideals meet only in $0$: an element lying in both satisfies $\tilde{Q} = \tilde{Q}\tilde\Pi_2 = 0$, because membership of $\mathbb{B}\tilde\Pi_2$ gives $\tilde{Q}\tilde\Pi_2 = \tilde{Q}$ while $\tilde\Pi_1\tilde\Pi_2 = 0$. The sum is therefore direct. Under the isomorphism $\Phi$ of *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* the two idempotents are the matrix units $\tilde\Pi_1 \mapsto E_{11}$ and $\tilde\Pi_2 \mapsto E_{22}$, and the two ideals are the two **columns** of the matrix algebra, which the corpus calls the two chiralities.

**Theorem (the left regular matrix is the sum of the two chiralities).** In the basis

$$
\tilde\Pi_1, \quad e_1\tilde\Pi_1, \quad \tilde\Pi_2, \quad e_1\tilde\Pi_2
$$

of $\mathbb{B}$, the left regular matrix of $\tilde{Q}$ is block diagonal,

$$
\mathsf{M}_4^{L}(\tilde{Q}) = \begin{pmatrix} A_+(\tilde{Q}) & 0 \\ 0 & A_-(\tilde{Q}) \end{pmatrix},
\qquad
A_+(\tilde{Q}) = \begin{pmatrix} Q_0 - iQ_3 & -Q_1 + iQ_2 \\ Q_1 + iQ_2 & Q_0 + iQ_3 \end{pmatrix},
$$

$$
A_-(\tilde{Q}) = \begin{pmatrix} Q_0 + iQ_3 & -Q_1 - iQ_2 \\ Q_1 - iQ_2 & Q_0 - iQ_3 \end{pmatrix},
$$

and each block has trace $2Q_0$ and determinant $N(\tilde{Q})$. Consequently each block is similar to the matrix $\Phi(\tilde{Q})$ of *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*, each block is a copy of the simple module $S$, and

$$
\mathsf{M}_4^{L} \cong S \oplus S
$$

as a left $\mathbb{B}$-module.

**Proof.** The two ideals are stable under $\mathsf{M}_4^{L}(\tilde{Q})$, because $\tilde{Q}(\tilde{S}\tilde\Pi_1) = (\tilde{Q}\tilde{S})\tilde\Pi_1$ for every $\tilde{S}$; hence the matrix is block diagonal in any basis adapted to the decomposition. The ideal $\mathbb{B}\tilde\Pi_1$ has the basis $\tilde\Pi_1, e_1\tilde\Pi_1$, since $e_2\tilde\Pi_1 = ie_1\tilde\Pi_1$ and $e_3\tilde\Pi_1 = -i\tilde\Pi_1$. Its multiplication by the units is read from

$$
e_2\tilde\Pi_1 = ie_1\tilde\Pi_1, \quad e_3\tilde\Pi_1 = -i\tilde\Pi_1, \qquad e_1(e_1\tilde\Pi_1) = -\tilde\Pi_1, \quad e_2(e_1\tilde\Pi_1) = i\tilde\Pi_1, \quad e_3(e_1\tilde\Pi_1) = ie_1\tilde\Pi_1,
$$

so in the basis $\tilde\Pi_1, e_1\tilde\Pi_1$ the three vector units act by the matrices $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, $\begin{pmatrix} 0 & i \\ i & 0 \end{pmatrix}$ and $\begin{pmatrix} -i & 0 \\ 0 & i \end{pmatrix}$, and carrying out the sum $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ gives $A_+$; the same computation on the basis $\tilde\Pi_2, e_1\tilde\Pi_2$ of $\mathbb{B}\tilde\Pi_2$ gives $A_-$. The trace of each block is $2Q_0$ by inspection and the determinant is

$$
\det A_+ = (Q_0 - iQ_3)(Q_0 + iQ_3) - (-Q_1 + iQ_2)(Q_1 + iQ_2) = Q_0^2 + Q_3^2 + Q_1^2 + Q_2^2 = N(\tilde{Q}),
$$

and likewise $\det A_- = N(\tilde{Q})$. For the similarity, with

$$
u_+ = e_0 + e_3, \qquad u_- = e_1 + e_2,
$$

one has

$$
\Phi(u_+) = \begin{pmatrix} 1-i & 0 \\ 0 & 1+i \end{pmatrix}, \qquad \Phi(u_-) = \begin{pmatrix} 0 & -1-i \\ 1-i & 0 \end{pmatrix},
$$

and

$$
A_+(\tilde{Q}) = \Phi(u_+)\,\Phi(\tilde{Q})\,\Phi(u_+)^{-1}, \qquad A_-(\tilde{Q}) = \Phi(u_-)\,\Phi(\tilde{Q})\,\Phi(u_-)^{-1}
$$

for every $\tilde{Q}$: both sides are $\mathbb{C}$-linear in $\tilde{Q}$, so it suffices to compare them on the four basis elements, where they agree. Both conjugating matrices are invertible, since $\det\Phi(u_+) = (1-i)(1+i) = 2 = \det\Phi(u_-)$. Each block therefore realizes the simple module $S$ of *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*, and the regular module is $S \oplus S$.

### The Characteristic Polynomial

**Corollary.** In the block basis above the regular matrix is block diagonal with the two blocks similar to $\Phi(\tilde{Q})$, so its characteristic polynomial is the square of that of the simple module,

$$
\chi_{\mathsf{M}_4^{L}(\tilde{Q})}(\lambda) = \bigl( \lambda^2 - 2Q_0\lambda + N(\tilde{Q}) \bigr)^2 .
$$

The square is the algebraic shadow of the factor $2$ between the dimensions of the regular module and the simple module, and it is why every eigenvalue of the simple module occurs with multiplicity at least two in the regular one. The eigenvalues themselves are the two roots of $\lambda^2 - 2Q_0\lambda + N(\tilde{Q})$, repeated; the general theory of the characteristic polynomial, of eigenvalues and of diagonalisation is the subject of *Eigenvalues and Diagonalisation* in the mathematics pages.

### Why Left Multiplication Cannot Couple the Chiralities

The block form is a statement about physics as much as about matrices. Left multiplication preserves each minimal left ideal, so no element of $\mathbb{B}$ acting on the left can carry a field in one chirality into the other: the block diagonal form *is* that statement. A term that couples the two chiralities has to act on the **right**, and the corpus's mass term does exactly that. In the matrix realization the element that performs it is

$$
\tilde{a}_{\mathrm{tr}} = \tfrac{1}{2}(ie_1 - e_2) \longmapsto E_{12},
$$

whose right action maps the first column onto the second — $E_{11} \mapsto E_{12}$ and $E_{21} \mapsto E_{22}$ — while annihilating the second, so that $\tilde\Pi_1\tilde{a}_{\mathrm{tr}} = \tilde{a}_{\mathrm{tr}}$ while $\tilde\Pi_2\tilde{a}_{\mathrm{tr}} = 0$, and the algebra product is nilpotent, $\tilde{a}_{\mathrm{tr}}^2 = 0$. The pair $\tilde{a}_{\mathrm{tr}}$, $\tilde{a}_{\mathrm{tr}}^{*} = \tfrac12(ie_1 + e_2)$ satisfies $\tilde{a}_{\mathrm{tr}}\tilde{a}_{\mathrm{tr}}^{*} = \tilde\Pi_1$ and $\tilde{a}_{\mathrm{tr}}^{*}\tilde{a}_{\mathrm{tr}} = \tilde\Pi_2$. In the notation of the spinor-module articles these are the truncated ladder elements $x$ and $y$. The consequence is recorded in *Conventions in the Biquaternion Universe*: the biquaternionic Dirac equation is linear and chirality-off-diagonal, $\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L$ and $\tilde{\nabla}^{\natural}\tilde{\Psi}_L = m\tilde{\Psi}_R$, and the Dirac field is carried by the spinor module and not by the whole algebra. The regular matrix is where one sees that this is forced by the algebra and not chosen: the left action has no off-diagonal blocks.

## The Determinant and the Trace

**Corollary (determinant and trace).** For every biquaternion $\tilde{Q}$,

$$
\det \mathsf{M}_4^{L}(\tilde{Q}) = N(\tilde{Q})^2, \qquad \operatorname{Tr}\mathsf{M}_4^{L}(\tilde{Q}) = 4Q_0 .
$$

The determinant of the regular matrix is the **square** of the biquaternion norm, and it is not the biquaternion norm.

**Proof.** In the block basis the matrix is block diagonal with blocks $A_+$ and $A_-$, so its determinant is $\det A_+\det A_- = N(\tilde{Q})^2$ and its trace is $\operatorname{Tr}A_+ + \operatorname{Tr}A_- = 2Q_0 + 2Q_0 = 4Q_0$. Both are invariant under the change of basis.

**Example.** For $\tilde{Q} = (2+i)e_0 + (1-i)e_1 + 3e_2 + ie_3$ one has $N(\tilde{Q}) = 11+2i$ and

$$
\det\mathsf{M}_4^{L}(\tilde{Q}) = (11+2i)^2 = 117 + 44i, \qquad \operatorname{Tr}\mathsf{M}_4^{L}(\tilde{Q}) = 4(2+i) = 8 + 4i,
$$

in agreement with the two blocks $A_+(\tilde{Q}) = \begin{pmatrix} 3+i & -1+4i \\ 1+2i & 1+i \end{pmatrix}$ and $A_-(\tilde{Q}) = \begin{pmatrix} 1+i & -1-2i \\ 1-4i & 3+i \end{pmatrix}$ on this element, each of trace $4+2i$ and determinant $11+2i$.

**For a material four-vector.** With $\tilde{Q} = iq'_0e_0 + \mathbf{q} \in \mathbb{M}_-$ the biquaternion norm is real, $N(\tilde{Q}) = -(q'_0)^2 + \mathbf{q}^2$, so

$$
\det\mathsf{M}_4^{L}(\tilde{Q}) = \bigl( -(q'_0)^2 + \mathbf{q}^2 \bigr)^2, \qquad \operatorname{Tr}\mathsf{M}_4^{L}(\tilde{Q}) = 4iq'_0 .
$$

For the four-position, with $q'_0 = ct$ and $\mathbf{q} = \mathbf{x}$, the determinant of the regular matrix is the **square of the interval**: for $ct = 2$ and $\mathbf{x} = (1, \tfrac12, \tfrac12)$ the interval is the rational number $-4 + 1 + \tfrac14 + \tfrac14 = -\tfrac52$, and the regular matrix has determinant $\tfrac{25}{4}$, real and positive. For the four-momentum the on-shell biquaternion norm is $-m^2c^2$, so the regular matrix has determinant $m^4c^4$.

**The regular matrix is singular exactly on the light cone.** Since $\det\mathsf{M}_4^{L}(\tilde{Q}) = N(\tilde{Q})^2$, the regular matrix of an element fails to be invertible exactly when $N(\tilde{Q}) = 0$, that is, exactly on the zero-divisor cone. For a material four-vector that is the light cone $-c^2t^2 + \mathbf{x}^2 = 0$; for the four-momentum it is the massless case $m = 0$. The physical statement and the algebraic one are the same: a four-vector is a zero divisor of the algebra exactly when it is null, and the determinant of the regular representation is the test. Moreover the determinant is a **square**, and the square has a physical reading: the four-vector is the direct sum of two chiral copies, and each copy carries one factor of the biquaternion norm.

**Remark (the determinant is not the biquaternion norm).** The simple module carries the biquaternion norm as its determinant, $\det\Phi(\tilde{Q}) = N(\tilde{Q})$, and the regular module is the direct sum of two copies of it, so its determinant is the product of two biquaternion norms. The square appears because the regular representation acts on a space of twice the dimension, and the factor $2$ is the number of chiralities. Squaring does not change the zero set, which is why the light-cone statement survives the doubling, but it does change the degree: an identity that holds for $N$ to the first power in the 2×2 article holds only for $N^2$ here.

## The Matrix of a Four-Vector

The general results above, read on the material sector, give the four-vector a $4 \times 4$ matrix of its own, and that matrix is the one multiplied into the columns in *The 4×4 Matrix Operator Representation $M_4(\mathbb{C})$ of Biquaternions*.

**Proposition.** For $\tilde{Q} = iq'_0e_0 + q_1e_1 + q_2e_2 + q_3e_3 \in \mathbb{M}_-$ with real components, the left regular matrix is the matrix displayed at the end of the first section, with

$$
\operatorname{Tr}\mathsf{M}_4^{L}(\tilde{Q}) = 4iq'_0, \qquad \det\mathsf{M}_4^{L}(\tilde{Q}) = \bigl( -(q'_0)^2 + (q_1)^2 + (q_2)^2 + (q_3)^2 \bigr)^2 .
$$

**Proof.** Substitute $Q_0 = iq'_0$ and $Q_k = q_k$ into the corollary of the preceding section.

**Four-vectors of physics.** Four cases are worth recording, with constants rather than with units.

| Four-vector | Components $(q'_0, \mathbf{q})$ | $\det\mathsf{M}_4^{L}$ | $\operatorname{Tr}\mathsf{M}_4^{L}$ |
|---|---|---|---|
| four-position | $(ct, \mathbf{x})$ | $( -c^2t^2 + \mathbf{x}^2 )^2$ | $4ict$ |
| four-velocity | $(\gamma c, \gamma\mathbf{v})$ | $c^4$ | $4i\gamma c$ |
| four-momentum, on shell | $(E/c, \mathbf{p})$ | $m^4c^4$ | $4iE/c$ |
| four-momentum, massless | $(E/c, \mathbf{p})$ | $0$ | $4iE/c$ |

The determinant of the four-velocity's regular matrix is the constant $c^4$, which is the matrix form of the statement that the four-velocity has constant biquaternion norm $-c^2$; the determinant is its square, and it is constant because the interval of a timelike world line is. The massless four-momentum has a singular regular matrix, and the massive one does not: the regular matrix detects the mass shell as the complement of the singular locus.

**The two-sided action on this matrix.** The rotor conjugation of the two-sided action below acts on the four-vector, and read as matrices it is the product of a left matrix and a right matrix with the four-vector in between; the four-vector's own regular matrix is not the object that is conjugated. The distinction matters in *The 4×4 Matrix Operator Representation $M_4(\mathbb{C})$ of Biquaternions*, where the field is a biquaternion and the derivative is a four-vector, and the two are multiplied on the two sides.

### The Gradient

The biquaternionic gradient $\tilde{\nabla} = e_0\partial_{ict} + e_1\partial_x + e_2\partial_y + e_3\partial_z$ has the shape of a material four-vector, and its regular matrix is the $4 \times 4$ matrix of first-order partial derivatives obtained by replacing the constants above by the corresponding derivatives:

$$
\mathsf{M}_4^{L}(\tilde{\nabla}) = \begin{pmatrix}
\partial_{ict} & -\partial_x & -\partial_y & -\partial_z \\
\partial_x & \partial_{ict} & -\partial_z & \partial_y \\
\partial_y & \partial_z & \partial_{ict} & -\partial_x \\
\partial_z & -\partial_y & \partial_x & \partial_{ict}
\end{pmatrix},
$$

with $\operatorname{Tr}\mathsf{M}_4^{L}(\tilde{\nabla}) = 4\partial_{ict}$. Its chiral block is the first-order matrix

$$
A_+(\tilde{\nabla}) = \begin{pmatrix} \partial_{ict} - i\partial_z & -\partial_x + i\partial_y \\ \partial_x + i\partial_y & \partial_{ict} + i\partial_z \end{pmatrix},
\qquad \det A_+(\tilde{\nabla}) = \Box ,
$$

the partial derivatives commuting. The determinant of the whole is the square,

$$
\det\mathsf{M}_4^{L}(\tilde{\nabla}) = \Box^2 ,
$$

because the two chiral blocks are similar and each carries one factor. This is the algebraic content of the square root: a first-order matrix acting on the spinor module has the second-order d'Alembertian as determinant, and the doubling of the regular module is where the two chiral copies of the first-order matrix come from. The conventions of the mass term are those of *Conventions in the Biquaternion Universe*, and the wave equations built on it are the subject of the wave-mechanics articles.

## Remarkable Subspaces

Each of the algebra's remarkable subspaces has its own simplified regular matrix, obtained by substituting that subspace's parametrisation into the general matrix of the first section. The parametrisations are those of *Conventions in the Biquaternion Universe*: the complex coefficients are $Q_\mu = q_\mu + iq'_\mu$ with $q_\mu, q'_\mu$ real, and the physical coordinates are $ct, \mathbf{x}$ on the material side and $ct', \mathbf{x}'$ on the informational one.

Each subspace is displayed as a three-step chain: the general matrix in the complex coefficients $Q_\mu$, the same matrix with that subspace's real parameters substituted, and the same matrix in the physical coordinates, under the one dictionary

$$
q_0 = ct', \quad q'_0 = ct, \quad q_1 = x, \quad q_2 = y, \quad q_3 = z, \quad q'_1 = x', \quad q'_2 = y', \quad q'_3 = z' ,
$$

the unprimed slot carrying the informational time $ct'$ and the material space $\mathbf{x}$, the primed slot the material time $ct$ and the informational space $\mathbf{x}'$.

**The centre subspace $\mathbb{C}_{\mathbb{B}}$.** One complex coefficient at the scalar slot, $Q_1 = Q_2 = Q_3 = 0$: the regular matrix is scalar, and the chain from the complex coefficient to its two real parameters to the two physical times is

$$
\mathsf{M}_4^{L}(\tilde{Q}) = Q_0\,I_4 = (q_0 + iq'_0)\,I_4 = (ct' + ict)\,I_4,
$$

with $Q_0 = q_0 + iq'_0$, $q_0 = ct'$ and $q'_0 = ct$. The invariants are the scalars of the same chain,

$$
\operatorname{Tr}\mathsf{M}_4^{L} = 4(ct' + ict), \qquad \det\mathsf{M}_4^{L} = (ct' + ict)^4 .
$$

It is the locus on which left and right multiplication coincide, which is what the corollary *the difference vanishes exactly on the centre* says on the remarkable subspaces: the centre is exactly where $\mathsf{M}_4^{L}(\tilde{Q}) = \mathsf{M}_4^{R}(\tilde{Q})$.

**The vector subspace $\mathrm{Vect}(\mathbb{B})$.** The scalar coefficient vanishes, $Q_0 = 0$, so the matrix is traceless, and the chain runs over the three complex spatial coefficients,

$$
\mathsf{M}_4^{L}(\tilde{Q}) = \begin{pmatrix} 0 & -Q_1 & -Q_2 & -Q_3 \\ Q_1 & 0 & -Q_3 & Q_2 \\ Q_2 & Q_3 & 0 & -Q_1 \\ Q_3 & -Q_2 & Q_1 & 0 \end{pmatrix}
= \begin{pmatrix} 0 & -(q_1+iq'_1) & -(q_2+iq'_2) & -(q_3+iq'_3) \\ q_1+iq'_1 & 0 & -(q_3+iq'_3) & q_2+iq'_2 \\ q_2+iq'_2 & q_3+iq'_3 & 0 & -(q_1+iq'_1) \\ q_3+iq'_3 & -(q_2+iq'_2) & q_1+iq'_1 & 0 \end{pmatrix}
= \begin{pmatrix} 0 & -(x+ix') & -(y+iy') & -(z+iz') \\ x+ix' & 0 & -(z+iz') & y+iy' \\ y+iy' & z+iz' & 0 & -(x+ix') \\ z+iz' & -(y+iy') & x+ix' & 0 \end{pmatrix},
$$

with $Q_k = q_k + iq'_k$, $q_k = x_k$ and $q'_k = x'_k$ real, and

$$
\operatorname{Tr}\mathsf{M}_4^{L} = 0, \qquad \det\mathsf{M}_4^{L} = \big( Q_1^2 + Q_2^2 + Q_3^2 \big)^2 = \big( (x+ix')^2 + (y+iy')^2 + (z+iz')^2 \big)^2 .$$

The matrix is traceless because the scalar part is, and it is singular exactly on the complex isotropic cone of the three spatial coefficients — the vector subspace is the derived subspace $[\mathbb{B}, \mathbb{B}]$ and contains the algebra's nilpotents.

**The quaternion subspace $\mathbb{H}_{\mathbb{B}}$.** All four coefficients real, $Q_\mu = q_\mu$, so the complex coefficients and their real parameters are the same four numbers and the chain is a rewriting into the physical names $q_0 = ct'$, $q_k = x_k$:

$$
\mathsf{M}_4^{L}(\tilde{Q}) = \begin{pmatrix} Q_0 & -Q_1 & -Q_2 & -Q_3 \\ Q_1 & Q_0 & -Q_3 & Q_2 \\ Q_2 & Q_3 & Q_0 & -Q_1 \\ Q_3 & -Q_2 & Q_1 & Q_0 \end{pmatrix}
= \begin{pmatrix} q_0 & -q_1 & -q_2 & -q_3 \\ q_1 & q_0 & -q_3 & q_2 \\ q_2 & q_3 & q_0 & -q_1 \\ q_3 & -q_2 & q_1 & q_0 \end{pmatrix}
= \begin{pmatrix} ct' & -x & -y & -z \\ x & ct' & -z & y \\ y & z & ct' & -x \\ z & -y & x & ct' \end{pmatrix},
$$

the real Cayley matrix, with $\operatorname{Tr}\mathsf{M}_4^{L} = 4ct'$ and $\det\mathsf{M}_4^{L} = \big( c^2(t')^2 + \mathbf{x}^2 \big)^2$.

Its entries are real and its determinant is the square of a sum of four squares, so it is invertible for every nonzero element: this is the real $4 \times 4$ left regular representation of the quaternions, and the absence of zero divisors in $\mathbb{H}$ is the invertibility of this matrix.

**The antiquaternion subspace $i\mathbb{H}_{\mathbb{B}}$.** All four coefficients purely imaginary, $Q_\mu = iq'_\mu$, so the matrix is $i$ times the quaternion subspace's and the chain is the quaternion one under the factor $i$:

$$
\mathsf{M}_4^{L}(\tilde{Q}) = \begin{pmatrix} Q_0 & -Q_1 & -Q_2 & -Q_3 \\ Q_1 & Q_0 & -Q_3 & Q_2 \\ Q_2 & Q_3 & Q_0 & -Q_1 \\ Q_3 & -Q_2 & Q_1 & Q_0 \end{pmatrix}
= i\begin{pmatrix} q'_0 & -q'_1 & -q'_2 & -q'_3 \\ q'_1 & q'_0 & -q'_3 & q'_2 \\ q'_2 & q'_3 & q'_0 & -q'_1 \\ q'_3 & -q'_2 & q'_1 & q'_0 \end{pmatrix}
= i\begin{pmatrix} ct & -x' & -y' & -z' \\ x' & ct & -z' & y' \\ y' & z' & ct & -x' \\ z' & -y' & x' & ct \end{pmatrix},
$$

with $q'_0 = ct$ and $q'_k = x'_k$ real, $\operatorname{Tr}\mathsf{M}_4^{L} = 4ict$ and $\det\mathsf{M}_4^{L} = \big( c^2t^2 + (\mathbf{x}')^2 \big)^2$. The assignment of the two times and the two spaces is the one the real sector does not take. The determinant is again the square of a sum of four squares, so this subspace too is a division algebra, a copy of $\mathbb{H}$.

**The informational subspace $\mathbb{M}_+$.** The scalar coefficient is real and the three spatial ones are purely imaginary, $Q_0 = q_0$ and $Q_k = iq'_k$: a real diagonal and a purely imaginary spatial block, reached by the same three-step chain,

$$
\mathsf{M}_4^{L}(\tilde{Q}) = \begin{pmatrix} Q_0 & -Q_1 & -Q_2 & -Q_3 \\ Q_1 & Q_0 & -Q_3 & Q_2 \\ Q_2 & Q_3 & Q_0 & -Q_1 \\ Q_3 & -Q_2 & Q_1 & Q_0 \end{pmatrix}
= \begin{pmatrix} q_0 & -iq'_1 & -iq'_2 & -iq'_3 \\ iq'_1 & q_0 & -iq'_3 & iq'_2 \\ iq'_2 & iq'_3 & q_0 & -iq'_1 \\ iq'_3 & -iq'_2 & iq'_1 & q_0 \end{pmatrix}
= \begin{pmatrix} ct' & -ix' & -iy' & -iz' \\ ix' & ct' & -iz' & iy' \\ iy' & iz' & ct' & -ix' \\ iz' & -iy' & ix' & ct' \end{pmatrix},
$$

with $q_0 = ct'$ and $q'_k = x'_k$ real, $\operatorname{Tr}\mathsf{M}_4^{L} = 4ct'$ and $\det\mathsf{M}_4^{L} = \big( c^2(t')^2 - (\mathbf{x}')^2 \big)^2$. It is the mirror of the material case, of signature $(1,3)$. It is **Hermitian**, and its determinant is the square of the informational interval, so it is singular exactly on the informational null cone $ct' = \pm|\mathbf{x}'|$.

**The material subspace $\mathbb{M}_-$.** The scalar coefficient is purely imaginary and the three spatial ones are real, $Q_0 = iq'_0$ and $Q_k = q_k$: a purely imaginary diagonal and a real spatial block, and the chain carries the material four-vector from the complex coefficients through their real parameters to the physical coordinates $ict, x, y, z$,

$$
\mathsf{M}_4^{L}(\tilde{Q}) = \begin{pmatrix} Q_0 & -Q_1 & -Q_2 & -Q_3 \\ Q_1 & Q_0 & -Q_3 & Q_2 \\ Q_2 & Q_3 & Q_0 & -Q_1 \\ Q_3 & -Q_2 & Q_1 & Q_0 \end{pmatrix}
= \begin{pmatrix} iq'_0 & -q_1 & -q_2 & -q_3 \\ q_1 & iq'_0 & -q_3 & q_2 \\ q_2 & q_3 & iq'_0 & -q_1 \\ q_3 & -q_2 & q_1 & iq'_0 \end{pmatrix}
= \begin{pmatrix} ict & -x & -y & -z \\ x & ict & -z & y \\ y & z & ict & -x \\ z & -y & x & ict \end{pmatrix},
$$

with $q'_0 = ct$ and $q_k = x_k$ real, $\operatorname{Tr}\mathsf{M}_4^{L} = 4ict$ and $\det\mathsf{M}_4^{L} = \big( -c^2t^2 + \mathbf{x}^2 \big)^2$. It is the matrix displayed in *The Matrix of a Four-Vector*. It is **anti-Hermitian**, and its determinant is the square of the Minkowski interval, so it is singular exactly on the light cone: a four-vector is a zero divisor of the algebra exactly when it is null.

**Why the informational sector is Hermitian and the material one anti-Hermitian.** The two displays are not a coincidence: the left regular representation is a $*$-homomorphism for Hermitian conjugation,

$$
\mathsf{M}_4^{L}(\tilde{Q})^{\dagger} = \mathsf{M}_4^{L}\big( \tilde{Q}^{*} \big),
$$

which follows from the transpose proposition $\mathsf{M}_4^{L}(\tilde{Q})^{\mathsf{T}} = \mathsf{M}_4^{L}(\tilde{Q}^{\natural})$ by conjugating every entry. The Hermitian elements therefore have Hermitian regular matrices and the anti-Hermitian elements anti-Hermitian ones — the same pair of statements that the $2 \times 2$ article reads on the simple module, here read on the four-vector.

## The Double Centralizer

**Theorem (the centralizer is the right copy).** The set of matrices commuting with every left regular matrix,

$$
\bigl\{ C \in M_4(\mathbb{C}) : C\,\mathsf{M}_4^{L}(\tilde{R}) = \mathsf{M}_4^{L}(\tilde{R})\,C \ \text{ for every } \tilde{R} \in \mathbb{B} \bigr\},
$$

is the image $\mathsf{M}_4^{R}(\mathbb{B})$, of complex dimension $4$.

**Proof.** The column rule for the left matrix reads $\mathsf{M}_4^{L}(\tilde{R})\operatorname{col}(\tilde{S}) = \operatorname{col}(\tilde{R}\tilde{S})$, and in particular $\mathsf{M}_4^{L}(\tilde{R})\operatorname{col}(e_0) = \operatorname{col}(\tilde{R})$. Let $C$ commute with every $\mathsf{M}_4^{L}(\tilde{R})$ and let $\tilde{Q}$ be the element whose column is $C\operatorname{col}(e_0)$. Then, for every $\tilde{R}$,

$$
C\operatorname{col}(\tilde{R}) = C\,\mathsf{M}_4^{L}(\tilde{R})\operatorname{col}(e_0) = \mathsf{M}_4^{L}(\tilde{R})\,C\operatorname{col}(e_0) = \operatorname{col}(\tilde{R}\tilde{Q}) = \mathsf{M}_4^{R}(\tilde{Q})\operatorname{col}(\tilde{R}),
$$

the last step being the column rule for the right matrix. The columns $\operatorname{col}(\tilde{R})$ span $\mathbb{C}^4$, so $C = \mathsf{M}_4^{R}(\tilde{Q})$ and the centralizer is contained in $\mathsf{M}_4^{R}(\mathbb{B})$. Conversely every $\mathsf{M}_4^{R}(\tilde{Q})$ commutes with every $\mathsf{M}_4^{L}(\tilde{R})$, because $(\tilde{R}\tilde{S})\tilde{Q} = \tilde{R}(\tilde{S}\tilde{Q})$ is associativity; hence the centralizer is exactly $\mathsf{M}_4^{R}(\mathbb{B})$. That copy has complex dimension $4$ because $\mathsf{M}_4^{R}$ is injective: $\mathsf{M}_4^{R}(\tilde{Q}) = 0$ forces its first column, which is the column of $\tilde{Q}$, to vanish. The dimension was also computed directly, as the null space of the $48 \times 16$ linear system that the three commutation conditions $M\mathsf{M}_4^{L}(e_k) = \mathsf{M}_4^{L}(e_k)M$, $k = 1,2,3$, impose on the entries of $M$; the null space is four-dimensional and is spanned by the four matrices $\mathsf{M}_4^{R}(e_\mu)$.

**Remark.** The theorem is the regular-module case of the double centralizer phenomenon. In physical terms it says that the matrices commuting with every left regular matrix are exactly the right regular matrices: the left copy is the algebra acting on its four-vector, and the right copy is the largest set of matrices that can be applied to the four-vector without disturbing that left action. The right copy is also the source of the chirality coupling, since it is the only copy with off-diagonal blocks in the chirality basis; the mass term and the centralizer are therefore the same fact seen from two sides.

## The Real Form

**Proposition (the real regular matrix).** Regarded over $\mathbb{R}$ in the real basis

$$
e_0, e_1, e_2, e_3, ie_0, ie_1, ie_2, ie_3
$$

of the eight-dimensional real space underlying $\mathbb{B}$, the left regular matrix becomes an $8 \times 8$ real matrix $\mathsf{M}_4^{L,\mathbb{R}}(\tilde{Q})$, with

$$
\det\mathsf{M}_4^{L,\mathbb{R}}(\tilde{Q}) = |N(\tilde{Q})|^4, \qquad \operatorname{Tr}\mathsf{M}_4^{L,\mathbb{R}}(\tilde{Q}) = 8\operatorname{Re}(Q_0).
$$

**Proof.** The real matrix is the realification of the complex matrix $\mathsf{M}_4^{L}(\tilde{Q})$, each complex entry being replaced by its real $2 \times 2$ block. A complex matrix with eigenvalues $\lambda_1, \ldots, \lambda_4$ has realification with eigenvalues $\lambda_1, \bar\lambda_1, \ldots, \lambda_4, \bar\lambda_4$, so its determinant is $|\lambda_1\cdots\lambda_4|^2 = |\det\mathsf{M}_4^{L}(\tilde{Q})|^2 = |N(\tilde{Q})^2|^2 = |N(\tilde{Q})|^4$ and its trace is $2\operatorname{Re}(\lambda_1 + \cdots + \lambda_4) = 2\operatorname{Re}(4Q_0) = 8\operatorname{Re}(Q_0)$.

**For a material four-vector.** With $\tilde{Q} \in \mathbb{M}_-$ the scalar part is $Q_0 = iq'_0$, whose real part vanishes, so

$$
\operatorname{Tr}\mathsf{M}_4^{L,\mathbb{R}}(\tilde{Q}) = 0, \qquad \det\mathsf{M}_4^{L,\mathbb{R}}(\tilde{Q}) = \bigl( -(q'_0)^2 + \mathbf{q}^2 \bigr)^4 ,
$$

the biquaternion norm being real on the material sector. The real regular matrix of a material four-vector is therefore **traceless**, and this is the sense in which the trace of a four-vector is zero: not over $\mathbb{C}$, where it is $4iq'_0$, but over the real eight-dimensional space, where the trace is twice the real part of the complex trace. The tracelessness is a property of the material sector alone, whose scalar part is purely imaginary; on the informational sector the scalar part is real and the real trace is $8q_0 = 8ct'$, generally nonzero. On the quaternion subalgebra $\mathbb{H}_{\mathbb{B}}$ and read on $\mathbb{H}_{\mathbb{B}}$ itself the construction is the $4 \times 4$ real regular representation of the quaternions.

## The Two-Sided Action

One geometric statement uses both copies at once, and it is the reason the regular matrix belongs to the physics corpus.

**Definition.** The **rotor group** of $\mathbb{B}$ is

$$
\{\tilde{\Lambda} \in \mathbb{B} : N(\tilde{\Lambda}) = e_0\} .
$$

It is a group, and under $\Phi$ it is the special linear group $SL(2,\mathbb{C})$, since $N(\tilde{\Lambda}) = \det\Phi(\tilde{\Lambda}) = 1$.

**Proposition (the two-sided action).** The map

$$
\tilde{Q} \longmapsto \tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^{*}
$$

is a group action of the rotor group on the material sector $\mathbb{M}_-$ and on the informational sector $\mathbb{M}_+$, and it preserves the biquaternion norm on each:

$$
N(\tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^{*}) = N(\tilde{Q}) .
$$

**Proof.** If $\tilde{Q}$ is anti-Hermitian then $(\tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^{*})^{*} = \tilde{\Lambda}\tilde{Q}^{*}\tilde{\Lambda}^{*} = -\tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^{*}$, so $\mathbb{M}_-$ is preserved; if $\tilde{Q}$ is Hermitian then $\tilde{Q}^{*} = \tilde{Q}$ and $\mathbb{M}_+$ is preserved. The biquaternion norm is multiplicative, so $N(\tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^{*}) = N(\tilde{\Lambda})N(\tilde{Q})N(\tilde{\Lambda}^{*})$, and $N(\tilde{\Lambda}) = e_0$ while $N(\tilde{\Lambda}^{*}) = N(\tilde{\Lambda})^{*} = e_0$. Composition holds because $\tilde{\Lambda}_1(\tilde{\Lambda}_2\tilde{Q}\tilde{\Lambda}_2^{*})\tilde{\Lambda}_1^{*} = (\tilde{\Lambda}_1\tilde{\Lambda}_2)\tilde{Q}(\tilde{\Lambda}_1\tilde{\Lambda}_2)^{*}$.

### The Lorentz Transformation as Left Times Right

**Corollary (the regular form of the rotor conjugation).** For every rotor $\tilde{\Lambda}$ and every four-vector $\tilde{Q}$,

$$
\tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^{*} = \mathsf{M}_4^{L}(\tilde{\Lambda})\,\mathsf{M}_4^{R}(\tilde{\Lambda}^{*})\,\tilde{Q},
$$

so the rotor conjugation is the left copy of $\tilde{\Lambda}$ composed with the right copy of $\tilde{\Lambda}^{*}$.

**Proof.** By definition $\mathsf{M}_4^{L}(\tilde{\Lambda})$ multiplies on the left and $\mathsf{M}_4^{R}(\tilde{\Lambda}^{*})$ on the right; applying the second to the four-vector and then the first gives $\tilde{\Lambda}(\tilde{Q}\tilde{\Lambda}^{*}) = \tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^{*}$ by associativity.

This is the statement promised in the introduction. A Lorentz transformation of a four-vector, in the biquaternion framework, is not primarily a matrix: it is a **two-sided multiplication**, one copy on each side, and the regular representation is the realization in which both copies are $4 \times 4$ matrices. The identity also shows why both regular representations are needed — the left one alone cannot produce the transformation, since the right factor is not central.

**The invariance of the interval.** Since $N$ is multiplicative and $N(\tilde{\Lambda}^{*}) = N(\tilde{\Lambda})^{*} = e_0$, the interval of a material four-vector is preserved by every rotor conjugation. The zero set is therefore invariant, and the causal classes of the framework are the orbits of the rotor group. This is the algebraic statement of the invariance of the interval, and it is what makes the rotor group the Lorentz group of the framework.

### Rotation Rotors and Boost Rotors

The rotors split into two families, distinguished by which conjugation fixes them.

**Rotation rotors** have real coefficients, so they lie in the real quaternion subalgebra $\mathbb{H}_{\mathbb{B}}$, and complex conjugation fixes them:

$$
\tilde{R}(\theta, \hat n) = \cos\tfrac{\theta}{2}\,e_0 + \sin\tfrac{\theta}{2}\,\hat n\cdot e, \qquad N(\tilde{R}) = \cos^2\tfrac{\theta}{2} + \sin^2\tfrac{\theta}{2} = e_0, \qquad \tilde{R}^{*} = \tilde{R}^{\natural} .
$$

Here $\hat n\cdot e = n_1e_1 + n_2e_2 + n_3e_3$ with $\hat n$ a real unit vector. Because $\tilde{R}^{*} = \tilde{R}^{\natural}$, the action is the quaternion conjugation $\tilde{Q}\mapsto\tilde{R}\tilde{Q}\tilde{R}^{\natural}$, which is the spatial rotation. Taking $\cos\tfrac{\theta}{2} = \tfrac35$ and $\sin\tfrac{\theta}{2} = \tfrac45$ about the axis $e_1$, so that $\cos\theta = -\tfrac{7}{25}$ and $\sin\theta = \tfrac{24}{25}$,

$$
e_2 \longmapsto \cos\theta\,e_2 + \sin\theta\,e_3 = -\tfrac{7}{25}e_2 + \tfrac{24}{25}e_3, \qquad e_3 \longmapsto -\sin\theta\,e_2 + \cos\theta\,e_3,
$$

while $e_1$ and the time direction $ict\,e_0$ are fixed. The rotor carries the **half** angle and the action the full angle, which is the familiar double-valuedness of the rotation group and the reason the rotor group is a double cover.

**Boost rotors** have a real scalar part and purely imaginary vector part, so they are Hermitian and complex conjugation negates their vector part:

$$
\tilde{B}(s, \hat n) = \cosh s\,e_0 + i\sinh s\,\hat n\cdot e, \qquad N(\tilde{B}) = \cosh^2 s - \sinh^2 s = e_0, \qquad \tilde{B}^{*} = \tilde{B} .
$$

Because $\tilde{B}^{*} = \tilde{B}$, the action is $\tilde{Q}\mapsto\tilde{B}\tilde{Q}\tilde{B}$, and it is a boost with **rapidity** $2s$. Taking $\cosh s = \tfrac53$ and $\sinh s = \tfrac43$, so that $\cosh 2s = \tfrac{41}{9}$ and $\sinh 2s = \tfrac{40}{9}$, a boost along $e_1$ acts on the four-position by

$$
ct \mapsto \cosh 2s\;ct - \sinh 2s\;x, \qquad x \mapsto \cosh 2s\;x - \sinh 2s\;ct, \qquad y \mapsto y, \quad z \mapsto z .
$$

The prime is deliberately not used for the transformed coordinates: in this corpus a prime marks an **informational** coordinate, so $ct'$ and $\mathbf{x}'$ are the informational time and space of the conventions stated above, and the transformed material pair needs no new symbols. For the event $(ct, x) = (2, 1)$ the image is $(\tfrac{14}{3}, -\tfrac{13}{3})$ in the same order, and the interval is preserved, $-\tfrac{196}{9} + \tfrac{169}{9} = -3 = -4 + 1$: a timelike displacement of interval $-3$ is carried to a timelike displacement of interval $-3$. The boost is a hyperbolic rotation, the parameter $s$ is the half-rapidity, and the appearance of the double angle is the same factor of two as in the rotation case, there called the double cover.

**Why the boosts are Hermitian and the rotations real.** The rotation rotors are the unit elements of the real sector $\mathbb{H}_{\mathbb{B}}$ and the boost rotors are the unit elements of the informational sector $\mathbb{M}_+$ whose scalar part is positive; together the two families generate the rotor group. The physical statement is that the two kinds of Lorentz transformation correspond to the two ways in which a unit-norm element can avoid the scalar imaginary: by having no $i$ at all, which is a rotation, or by carrying it in the vector part, which is a boost.

### The Double Cover

**Theorem (the double cover).** The two-sided action defines a surjective group homomorphism

$$
\mathrm{Ad} : SL(2,\mathbb{C}) \longrightarrow SO^+(1,3),
$$

onto the identity component $SO^+(1,3)$ of the orthogonal group of the interval, with kernel $\{e_0, -e_0\}$, central of order two.

**Proof.** A real-linear map of $\mathbb{M}_-$ preserving the quadratic form of signature $(3,1)$ is an element of $O(3,1)$; the action is continuous in $\tilde{\Lambda}$ and $SL(2,\mathbb{C})$ is connected, so the image is a connected subgroup of $O(3,1)$ and therefore lies in $SO^+(1,3)$. Surjectivity onto that component is the standard fact that $SL(2,\mathbb{C})$ is the double cover of the restricted Lorentz group, cited from the standard theory of the orthogonal groups. For the kernel, $\tilde{\Lambda}$ acts trivially precisely when $\tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^{*} = \tilde{Q}$ for every $\tilde{Q}$ in $\mathbb{M}_-$. Taking $\tilde{Q} = ie_0$ gives $\tilde{\Lambda}\tilde{\Lambda}^{*} = e_0$, that is, $\tilde{\Lambda}$ is unitary, and the condition then reads $\tilde{\Lambda}\tilde{Q} = \tilde{Q}\tilde{\Lambda}$ for every $\tilde{Q}$ in $\mathbb{M}_-$. The elements of $\mathbb{M}_-$ span $\mathbb{B}$ over $\mathbb{C}$, so $\tilde{\Lambda}$ commutes with every element of $\mathbb{B}$ and is therefore a central element $\lambda e_0$; the norm condition $N(\lambda e_0) = \lambda^2 = 1$ leaves $\lambda = \pm 1$. Both central elements act trivially and no other element does.

**The physical reading.** The rotor group is the covering group of the Lorentz group, the map $\mathrm{Ad}$ is two-to-one, and the two-element kernel is the statement that a physical Lorentz transformation corresponds to two rotors, $\tilde{\Lambda}$ and $-\tilde{\Lambda}$. The double cover is met in the spinor articles, where it is read on the module; here it is read as the two-sided action of the regular representation, that is, as the left copy composed with the right copy of the conjugate transpose. The corpus's account of the framework records that this rotor conjugation is the **only coupling** the framework supplies, and that it is kinematic: it is a symmetry of each of the two sectors and not a source, and no equation of motion for $\mathbb{M}_+$-valued fields is supplied with it.

## Physical Readings

The regular matrix reads as the algebra acting on itself, and its reading is a process: the Cayley matrix is left multiplication in coordinates, so the matrix is a transformation and not a state. Read on the two matrices, the left and the right regular matrices are the actions of the two ledgers, and the false transpose identity the article refutes is the warning that the two ledgers are not related by transposition. Read on the monoid, the multiplicativity $C_{\tilde P}C_{\tilde Q} = C_{\tilde P\tilde Q}$ is why a composition of processes is a product of matrices (*The Monoid of Acting Maps: the Process Is the Multiplication, the State Is the Idempotent*).

## Summary

The left regular matrix $\mathsf{M}_4^{L}(\tilde{Q})$ is the left multiplication of the algebra on itself written in the basis $e_0, e_1, e_2, e_3$, and it is the Cayley matrix of quaternion multiplication, each entry of which is a single coefficient of $\tilde{Q}$ carrying a sign and none of which is a sum of coefficients. It is multiplicative, its transpose is the left matrix of the quaternion conjugate, $\mathsf{M}_4^{L}(\tilde{Q})^{\mathsf{T}} = \mathsf{M}_4^{L}(\tilde{Q}^{\natural})$, its determinant is the square of the biquaternion norm, $\det\mathsf{M}_4^{L}(\tilde{Q}) = N(\tilde{Q})^2$, and its trace is $4Q_0$. The right regular matrix $\mathsf{M}_4^{R}(\tilde{Q})$, whose $m$-th column is the column of $e_m\tilde{Q}$, is anti-multiplicative and is the regular representation of the opposite algebra; the naive identity $\mathsf{M}_4^{R}(\tilde{Q}) = \mathsf{M}_4^{L}(\tilde{Q})^{\mathsf{T}}$ is false — and the variant with $\tilde{Q}^{\natural}$ is the same statement, since $\mathsf{M}_4^{L}(\tilde{Q}^{\natural})^{\mathsf{T}} = \mathsf{M}_4^{L}(\tilde{Q})$ — while what holds is $\mathsf{M}_4^{R}(\tilde{Q}) = D\mathsf{M}_4^{L}(\tilde{Q})^{\mathsf{T}}D = D\mathsf{M}_4^{L}(\tilde{Q}^{\natural})D$ with $D = \operatorname{diag}(-1,1,1,1) = \eta$, the $ict$ metric.

The regular module is $\mathbb{B} = \mathbb{B}\tilde\Pi_1 \oplus \mathbb{B}\tilde\Pi_2$ with $\tilde\Pi_{1,2} = \tfrac12(e_0 \pm ie_3)$, the two chiralities; in the adapted basis $\tilde\Pi_1, e_1\tilde\Pi_1, \tilde\Pi_2, e_1\tilde\Pi_2$ the regular matrix is block diagonal with blocks $A_+$, $A_-$, each similar to $\Phi(\tilde{Q})$ and each a copy of the simple module $S$. So $\mathsf{M}_4^{L} \cong S \oplus S$, the characteristic polynomial is $(\lambda^2 - 2Q_0\lambda + N)^2$, and left multiplication cannot couple the two chiralities — which is why the mass term is a right multiplication by $\tilde{a}_{\mathrm{tr}} = \tfrac12(ie_1 - e_2)$. The centralizer of $\mathsf{M}_4^{L}(\mathbb{B})$ is $\mathsf{M}_4^{R}(\mathbb{B})$, of complex dimension four; over $\mathbb{R}$ the regular matrix is $8 \times 8$ with determinant $|N|^4$ and trace $8\operatorname{Re}(Q_0)$, hence traceless on a material four-vector.

Read on the material sector, the regular matrix of a four-vector is the matrix displayed in the first section, with trace $4iq'_0$ and determinant the square of the interval; the four-position has determinant $(-c^2t^2 + \mathbf{x}^2)^2$, the four-velocity $c^4$, the on-shell four-momentum $m^4c^4$, and the massless four-momentum zero. The gradient's regular matrix is the first-order $4 \times 4$ matrix whose chiral block has determinant $\Box$ and whose determinant is $\Box^2$. Finally, the rotor group $\{\tilde{\Lambda} : N(\tilde{\Lambda}) = e_0\} \cong SL(2,\mathbb{C})$ acts on $\mathbb{M}_-$ and $\mathbb{M}_+$ by $\tilde{Q} \mapsto \tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^{*}$, which is $\mathsf{M}_4^{L}(\tilde{\Lambda})\mathsf{M}_4^{R}(\tilde{\Lambda}^{*})$ acting on the four-vector — the Lorentz transformation as left times right — preserving the interval, with rotation rotors the unit real quaternions, boost rotors the Hermitian unit elements, and the covering homomorphism $\mathrm{Ad}$ onto $SO^+(1,3)$ two-to-one with kernel $\{\pm e_0\}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $e_0, e_1, e_2, e_3$ | Algebra basis, $e_0 = 1$, $e_k^2 = -e_0$, $e_1e_2 = e_3$ |
| $i$ | Central scalar imaginary, $i^2 = -1$ |
| $\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu$ | Developed form, $Q_\mu \in \mathbb{C}$ |
| $Q^\mu = (Q^0, Q^1, Q^2, Q^3)$ | Four-vector; $Q^0 = Q_0$, $(Q^1,Q^2,Q^3) = (Q_1,Q_2,Q_3)$ |
| $\mathsf{M}_4^{L}(\tilde{Q})$ | Matrix of left multiplication, the Cayley matrix; a homomorphism |
| $\mathsf{M}_4^{R}(\tilde{Q})$ | Matrix of right multiplication; an anti-homomorphism, the regular representation of $\mathbb{B}^{\mathrm{op}}$ |
| $D = \operatorname{diag}(-1,1,1,1) = \eta$ | Fixed sign matrix; $\mathsf{M}_4^{R}(\tilde{Q}) = D\mathsf{M}_4^{L}(\tilde{Q})^{\mathsf{T}}D$; equals the $ict$ metric |
| $\epsilon^{ijk}$ | Levi-Civita symbol on the indices $1, 2, 3$ |
| $N(\tilde{Q}) = \sum_\mu Q_\mu^2$ | Biquaternion norm; $\det\mathsf{M}_4^{L} = N^2$, $\det\Phi = N$ |
| ${}^{\natural}, \bar{\cdot}, {}^{*} = {}^{\natural}\circ\bar{\cdot}, {}^{\flat} = -{}^{*}$ | Quaternion, complex, Hermitian, anti-Hermitian conjugation |
| $\mathbb{C}_{\mathbb{B}}$ | Centre, the scalar subspace $\mathbb{C} e_0$; locus where $\mathsf{M}_4^{L} = \mathsf{M}_4^{R}$ |
| $\mathbb{H}_{\mathbb{B}}, i\mathbb{H}_{\mathbb{B}}, \mathbb{M}_+, \mathbb{M}_-$ | Real sector, imaginary sector, informational sector, material sector |
| $\tilde\Pi_1 = \tfrac12(e_0 + ie_3)$, $\tilde\Pi_2 = \tfrac12(e_0 - ie_3)$ | Orthogonal idempotents, $\tilde\Pi_1 + \tilde\Pi_2 = e_0$, $\tilde\Pi_1\tilde\Pi_2 = 0$ |
| $\mathbb{B}\tilde\Pi_1$, $\mathbb{B}\tilde\Pi_2$ | The two minimal left ideals, i.e. the two chiralities; $\mathbb{B} = \mathbb{B}\tilde\Pi_1 \oplus \mathbb{B}\tilde\Pi_2$ |
| $A_+(\tilde{Q}), A_-(\tilde{Q})$ | The two $2 \times 2$ blocks of $\mathsf{M}_4^{L}$ in the adapted basis; $\operatorname{Tr} = 2Q_0$, $\det = N$ |
| $u_+ = e_0 + e_3$, $u_- = e_1 + e_2$ | Conjugating elements, $A_\pm(\tilde{Q}) = \Phi(u_\pm)\Phi(\tilde{Q})\Phi(u_\pm)^{-1}$ |
| $\tilde{a}_{\mathrm{tr}} = \tfrac12(ie_1 - e_2) \mapsto E_{12}$ | Truncated ladder element (the corpus's $x$); right multiplication carries $\mathbb{B}\tilde\Pi_1$ onto $\mathbb{B}\tilde\Pi_2$ |
| $S = \mathbb{C}^2$ | Simple left $\mathbb{B}$-module, the spinor module; $\mathsf{M}_4^{L} \cong S \oplus S$ |
| $\Phi(\tilde{Q})$ | The $2 \times 2$ matrix realization of *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* |
| $\{C : C\mathsf{M}_4^{L}(\tilde{R}) = \mathsf{M}_4^{L}(\tilde{R})C \ \forall \tilde{R}\} = \mathsf{M}_4^{R}(\mathbb{B})$ | The centralizer of the left copy in $M_4(\mathbb{C})$ is the right copy, of complex dimension $4$: the double centralizer statement |
| $\mathsf{M}_4^{L,\mathbb{R}}(\tilde{Q})$ | Real $8 \times 8$ regular matrix; $\det = |N|^4$, $\operatorname{Tr} = 8\operatorname{Re}(Q_0)$ |
| $q'_0, q_1, q_2, q_3$ | Real parameters of a material four-vector, $\tilde{Q} = iq'_0e_0 + q_1e_1 + q_2e_2 + q_3e_3$, $\mathbf{q} = q_1e_1+q_2e_2+q_3e_3$; $q'_0 = ct$, $(q_1,q_2,q_3) = (x,y,z)$; $\operatorname{Tr}\mathsf{M}_4^{L} = 4iq'_0$, $\det\mathsf{M}_4^{L} = (-(q'_0)^2 + \mathbf{q}^2)^2$ |
| $\mathsf{M}_4^{L,\mathbb{R}}(\tilde{Q})$ for $\tilde{Q} \in \mathbb{M}_-$ | Traceless real $8 \times 8$ matrix; determinant the fourth power of the interval |
| $\tilde{\nabla} = e_0\partial_{ict} + e_1\partial_x + e_2\partial_y + e_3\partial_z$ | Biquaternionic gradient; $\det A_+(\tilde{\nabla}) = \Box$, $\det\mathsf{M}_4^{L}(\tilde{\nabla}) = \Box^2$ |
| $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \partial_{ict}^2 + \Delta$ | d'Alembertian, series convention |
| $\eta = \operatorname{diag}(-1,+1,+1,+1)$ | $ict$ metric (level 2) |
| $\tilde{\Lambda}$, $N(\tilde{\Lambda}) = e_0$ | Rotor; the rotor group $\cong SL(2,\mathbb{C})$ |
| $\tilde{R}(\theta,\hat n)$, $\tilde{B}(s,\hat n)$ | Rotation rotor (real, $\tilde{R}^{*} = \tilde{R}^{\natural}$) and boost rotor (Hermitian, $\tilde{B}^{*} = \tilde{B}$) |
| $\mathrm{Ad} : SL(2,\mathbb{C}) \to SO^+(1,3)$ | Covering homomorphism, kernel $\{\pm e_0\}$ |
| $c$ | Speed of light in the medium, $c = 1/\sqrt{\epsilon\mu}$ |
| $ict$, $\mathbf{x}$; $ct'$, $i\mathbf{x}'$ | Material coordinate; informational coordinate |

## Further Reading

- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for the regular representation of an algebra and the structure of its centralizer.
- Charles W. Curtis and Irving Reiner, *Representation Theory of Finite Groups and Associative Algebras* (Interscience, 1962), for the regular module, its decomposition into minimal left ideals and the double centralizer theorem.
- Frank W. Anderson and Kent R. Fuller, *Rings and Categories of Modules*, 2nd edition (Springer, 1992), for the regular module as a left module over itself and the centralizer of the left copy.
- William Fulton and Joe Harris, *Representation Theory: A First Course*, Graduate Texts in Mathematics 129 (Springer, 1991), for the regular representation as the direct sum of the simple modules with multiplicity equal to their dimensions.
- John Voight, *Quaternion Algebras*, Graduate Texts in Mathematics 288 (Springer, 2021), for the regular representation of a quaternion algebra and its complexification.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the Cayley matrix of quaternion multiplication and its transpose.
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations*, 2nd edition (Springer, 2015), for the double cover $SL(2,\mathbb{C}) \to SO^+(1,3)$ and the two-to-one homomorphism onto the orthogonal group of a form.
- J. D. Jackson, *Classical Electrodynamics*, 3rd edition (Wiley, 1999), for the covariant four-vector formalism and the $ict$ convention.
